"""Verifica los feeds de opml/*.opml con peticiones HTTP reales.

Uso:  python tools/verificar.py
Comprueba cada xmlUrl (cabecera de navegador, siguiendo redirecciones):
  - HTTP 200
  - Cuerpo con XML valido y al menos un articulo (<item> o <entry>)
Sale con codigo 1 si algun feed falla.
Solo libreria estandar.
"""
import gzip
import sys
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from pathlib import Path

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
TIMEOUT = 25


def feeds_de_opml(ruta):
    arbol = ET.parse(ruta)
    vistos = []
    for nodo in arbol.getroot().iter("outline"):
        url = (nodo.get("xmlUrl") or "").strip()
        if url:
            vistos.append((nodo.get("text") or "?", url))
    return vistos


def comprobar(nombre, url):
    peticion = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(peticion, timeout=TIMEOUT) as resp:
            if resp.status != 200:
                return False, f"HTTP {resp.status}"
            crudo = resp.read(2_000_000)
            if crudo[:2] == b"\x1f\x8b":  # gzip sin descomprimir por urllib
                crudo = gzip.decompress(crudo)
            cuerpo = crudo.decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return False, f"HTTP {e.code}"
    except Exception as e:  # timeout, DNS, SSL...
        return False, type(e).__name__
    if "<item" in cuerpo or "<entry" in cuerpo:
        n = cuerpo.count("<item") + cuerpo.count("<entry")
        return True, f"OK ({n} articulos)"
    if "<rss" in cuerpo or "<feed" in cuerpo or "<rdf" in cuerpo.lower():
        return False, "XML sin articulos (0 items)"
    return False, "no es XML (HTML u otro)"


def main():
    raiz = Path(__file__).resolve().parent.parent
    archivos = sorted((raiz / "opml").glob("*.opml"))
    if not archivos:
        print("No hay archivos OPML en opml/.")
        return 1
    feeds = {}
    for archivo in archivos:
        for nombre, url in feeds_de_opml(archivo):
            feeds.setdefault(url, nombre)
    print(f"{len(feeds)} feeds unicos en {len(archivos)} archivos OPML.\n")
    fallos = 0
    for i, (url, nombre) in enumerate(sorted(feeds.items()), 1):
        ok, detalle = comprobar(nombre, url)
        marca = "OK  " if ok else "FALLO"
        if not ok:
            fallos += 1
        print(f"[{i:02d}/{len(feeds)}] {marca} {nombre}\n         {url}\n         {detalle}")
    print(f"\nResultado: {len(feeds) - fallos}/{len(feeds)} OK, {fallos} fallos.")
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
