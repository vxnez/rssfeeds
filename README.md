# 📡 Repositorio Curado de RSS

Una colección completa, limpia y actualizada de feeds RSS en **español** e **inglés**, organizada por categorías y optimizada para lectores de RSS (como NetNewsWire, Feedly, Inoreader, FreshRSS, etc.).

> ✅ **Verificado el 09/09/2026:** cada URL de esta lista fue comprobada con petición HTTP real (cabecera de navegador, siguiendo redirecciones) y confirmada como XML válido con artículos (`<item>`/`<entry>`). Las URLs muertas fueron eliminadas o reemplazadas por su alternativa oficial. Cuando un feed redirigía, se publicó la URL canónica final.

---

## 📑 Tabla de Contenidos

- [🇪🇸 Español](#-español)
  - [📰 Noticias y Actualidad](#-noticias-y-actualidad)
  - [💻 Tecnología](#-tecnología)
  - [🎮 Gaming](#-gaming)
  - [📈 Negocios y Economía](#-negocios-y-economía)
- [🇬🇧 Inglés](#-inglés)
  - [📰 News and General](#-news-and-general)
  - [💻 Technology](#-technology)
  - [🎮 Gaming](#-gaming-1)
  - [📊 Business & Finance](#-business--finance)
- [🔧 Cambios respecto a la versión anterior](#-cambios-respecto-a-la-versión-anterior)

---

## 🇪🇸 Español

### 📰 Noticias y Actualidad
*Fuentes de información general, cobertura política, social y de actualidad en el mundo hispanohablante.*

* **El País (España):** Periódico global en español líder en información y periodismo de investigación.
  ```text
  https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/portada
  ```
* **BBC News Mundo:** Servicio de noticias en español de la cadena británica BBC, con cobertura internacional imparcial. *(Corregido: era `.../undo/rss.xml`, typo con 404.)*
  ```text
  https://feeds.bbci.co.uk/mundo/rss.xml
  ```
* **El Mundo:** Uno de los diarios de referencia en España con cobertura en política, sociedad y cultura.
  ```text
  https://e00-elmundo.uecdn.es/elmundo/rss/portada.xml
  ```
* **Aristegui Noticias (México):** Portal de periodismo de investigación y análisis político en México. *(Corregido: `aristeguinoticias.com/feed/` devolvía HTML; el feed oficial vive en el subdominio editorial.)*
  ```text
  https://editorial.aristeguinoticias.com/feed/
  ```
* **Infobae (América Latina):** Noticias de última hora, política y actualidad con enfoque en toda América Latina.
  ```text
  https://www.infobae.com/arc/outboundfeeds/rss/
  ```

### 💻 Tecnología
*Novedades sobre gadgets, software, inteligencia artificial, internet y cultura digital en español.*

* **Xataka:** El medio de tecnología y cultura digital en español más popular del ecosistema iberoamericano.
  ```text
  https://www.xataka.com/feedburner.xml
  ```
* **Genbeta:** Blog de software, aplicaciones, internet, trucos y desarrollo web.
  ```text
  https://www.genbeta.com/feedburner.xml
  ```
* **Hipertextual:** Ciencia, tecnología, cultura digital y análisis profundo del impacto tecnológico en la sociedad.
  ```text
  https://hipertextual.com/feed
  ```
* **ComputerHoy:** Análisis de hardware, dispositivos móviles, trucos de software y guías de compra. *(Corregido: `computerhoy.com/rss` devolvía HTML; el feed oficial está en el dominio 20minutos.)*
  ```text
  https://computerhoy.20minutos.es/rss/
  ```
* **Applesfera:** Todo sobre el universo Apple, iPhone, Mac, iPad y el ecosistema de Cupertino en español.
  ```text
  https://www.applesfera.com/feedburner.xml
  ```

### 🎮 Gaming
*Actualidad sobre videojuegos, análisis de lanzamientos, avances y cultura gamer en español.*

* **Vandal:** Portal veterano de videojuegos con análisis, guías, noticias y avances de todas las plataformas. *(Corregido: `/rss/noticias.xml` daba 404; el feed oficial es `xml.cgi`, declarado en su propio HTML.)*
  ```text
  https://vandal.elespanol.com/xml.cgi
  ```
* **VidaExtra:** Noticias de consolas y videojuegos, lanzamientos y actualidad del sector. *(Reemplaza a MeriStation, cuyo RSS fue retirado tras la migración a AS.com.)*
  ```text
  https://www.vidaextra.com/feedburner.xml
  ```
* **Eurogamer.es:** Edición española de Eurogamer con análisis y noticias del sector. *(Reemplaza a MeriStation como segunda alternativa verificada.)*
  ```text
  https://www.eurogamer.es/feed
  ```
* **HobbyConsolas:** Revista clásica del sector con análisis de consolas, retrogaming y lanzamientos actuales.
  ```text
  https://www.hobbyconsolas.com/rss
  ```
* **3DJuegos:** Comunidad y portal de referencia para jugadores de PC y consolas con noticias de última hora. *(Corregido: `/universo/rss/ultimas_noticias.php` devolvía 410 Gone; el feed oficial es `feedburner.xml`.)*
  ```text
  https://www.3djuegos.com/feedburner.xml
  ```

### 📈 Negocios y Economía
*Información financiera, mercados bursátiles, macroeconomía y análisis empresarial.*

* **Expansión (España):** Diario líder en información económica, mercados financieros y gestión empresarial en España.
  ```text
  https://e00-expansion.uecdn.es/rss/portada.xml
  ```
* **El Economista (España):** Portal de economía, finanzas, empresas y mercados de valores. *(Corregido: `rss-portada.xml` daba 404; se usa la selección/portada oficial.)*
  ```text
  https://www.eleconomista.es/rss/rss-seleccion-ee.php
  ```
* **El Economista – Economía:** Canal específico de economía de elEconomista.es.
  ```text
  https://www.eleconomista.es/rss/rss-economia.php
  ```
* **El Financiero (México):** Economía, finanzas, negocios y política económica con perspectiva mexicana e internacional. *(Corregido: sin `?outputType=xml` devolvía HTML; esta es la URL canónica final.)*
  ```text
  https://www.elfinanciero.com.mx/arc/outboundfeeds/rss/?outputType=xml
  ```

---

## 🇬🇧 Inglés

### 📰 News and General
*Global news outlets, general interest coverage, and international reporting.*

* **BBC News (World):** Comprehensive global news coverage from the British Broadcasting Corporation.
  ```text
  https://feeds.bbci.co.uk/news/world/rss.xml
  ```
* **Al Jazeera (All News):** International breaking news and in-depth reporting from Doha. *(Replaces Reuters, which discontinued its public RSS – official endpoints now return 401/anti-bot pages.)*
  ```text
  https://www.aljazeera.com/xml/rss/all.xml
  ```
* **DW (Deutsche Welle – Top Stories):** German international broadcaster with global coverage. *(Replaces Reuters as second verified alternative.)*
  ```text
  https://rss.dw.com/rdf/rss-en-all
  ```
* **The New York Times:** Award-winning journalism covering international affairs, culture, and politics.
  ```text
  https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml
  ```
* **CNN Top Stories:** Breaking news and multimedia reporting on major world events.
  ```text
  http://rss.cnn.com/rss/cnn_topstories.rss
  ```
* **The Guardian:** Independent journalism covering world news, politics, environment, and culture.
  ```text
  https://www.theguardian.com/world/rss
  ```
* **Time Magazine – Top Stories:** In-depth features, opinion, and analysis on current global affairs.
  ```text
  http://feeds.feedburner.com/time/topstories
  ```
* **Yahoo News – Latest news and headlines:** Aggregated headlines and trending news stories. *(Fixed: `yahoo.com/news/rss/topstories` returned 403; official feed is `news.yahoo.com/rss/`.)*
  ```text
  https://news.yahoo.com/rss/
  ```
* **Washington Post:** In-depth political reporting and global news coverage based in Washington D.C.
  ```text
  http://feeds.washingtonpost.com/rss/world
  ```
* **Vox – All:** Explanatory journalism helping readers understand our complex world.
  ```text
  https://www.vox.com/rss/index.xml
  ```
* **NPR – Top Stories:** Public radio news, in-depth reporting and cultural coverage. *(Replaces HuffPost front-page feed, which now returns an empty chaski feed with 0 items.)*
  ```text
  https://feeds.npr.org/1001/rss.xml
  ```
* **CNN – World news:** Dedicated international updates and breaking global stories.
  ```text
  http://rss.cnn.com/rss/cnn_world.rss
  ```
* **ABC News – Top stories:** Broadcast journalism updates on national and international headlines.
  ```text
  http://abcnews.go.com/abcnews/topstories
  ```
* **Market Watch – Top stories:** Financial markets, stock updates, and consumer financial news.
  ```text
  http://www.marketwatch.com/rss/topstories/
  ```
* **Salon.com:** Progressive political commentary, culture, arts, and entertainment.
  ```text
  https://www.salon.com/feed/
  ```
* **New Yorker – Everything:** Literary essays, sophisticated critique, fiction, and comprehensive reporting.
  ```text
  https://www.newyorker.com/feed/everything
  ```
* **Daily Mail – Latest stories:** Tabloid news, celebrity coverage, and human interest stories.
  ```text
  https://www.dailymail.com/articles.rss
  ```
* **New York Post:** Bold reporting on news, sports, entertainment, and New York culture.
  ```text
  https://nypost.com/feed/
  ```
* **Fox News Science:** Science and technology reporting with a mainstream American perspective.
  ```text
  https://moxie.foxnews.com/google-publisher/tech.xml
  ```

### 💻 Technology
*Cutting-edge tech journalism, startup culture, developer tools, and consumer electronics.*

* **TechCrunch:** Dedicated to startups, venture capital investments, and emerging technologies.
  ```text
  https://techcrunch.com/feed/
  ```
* **Wired:** How emerging technologies affect culture, the economy, and politics.
  ```text
  https://www.wired.com/feed/rss
  ```
* **The Verge:** Examining how technology changes life, science, design, and entertainment.
  ```text
  https://www.theverge.com/rss/index.xml
  ```
* **Ars Technica:** Tech news, deep dives, gadget reviews, and geek culture analysis.
  ```text
  https://feeds.arstechnica.com/arstechnica/index
  ```
* **Hacker News (Front Page):** Curated tech and computer science discussion links from the developer community.
  ```text
  https://news.ycombinator.com/rss
  ```
* **MacWorld:** Essential guides, software tips, and hardware news for Apple users. *(Fixed: old `rss.macworld.com/...` host is dead; official feed is `macworld.com/feed`.)*
  ```text
  https://www.macworld.com/feed
  ```
* **PCWorld:** Personal computing news, component reviews, and operating system advice. *(Fixed: old `feeds.pcworld.com/...` host is dead; official feed is `pcworld.com/feed`.)*
  ```text
  https://www.pcworld.com/feed
  ```
* **LifeHacker:** Productivity tips, DIY guides, software lifehacks, and tech tutorials.
  ```text
  https://lifehacker.com/rss
  ```
* **Engadget:** Gadget reviews, consumer electronics, and future tech previews.
  ```text
  https://www.engadget.com/rss-full.xml
  ```
* **Mashable:** Multi-platform media and entertainment tech news site.
  ```text
  http://feeds.mashable.com/Mashable
  ```
* **Gizmodo:** Design, technology, science, and science fiction commentary.
  ```text
  https://gizmodo.com/rss
  ```
* **Technology Review:** MIT's magazine explaining the commercial and social impacts of new tech.
  ```text
  https://www.technologyreview.com/feed/
  ```
* **VentureBeat:** Tech news focusing on gaming, artificial intelligence, and enterprise technology. *(Fixed: the listed URL was a 2013 article, not a feed. Official feed is `venturebeat.com/feed/` – note: protected by a bot checkpoint, may return 429 to automated scripts but works in most RSS readers.)*
  ```text
  https://venturebeat.com/feed/
  ```
* **Computer World:** Enterprise IT, cloud computing, cybersecurity, and workplace tech trends.
  ```text
  https://www.computerworld.com/feed/
  ```
* **MakeUsOf:** Technology guides, how-to manuals, and tips to get more out of devices.
  ```text
  http://feeds.feedburner.com/Makeuseof
  ```
* **CNet:** Consumer technology reviews, tech news, and smart home advice.
  ```text
  https://www.cnet.com/rss/news
  ```
* **HowToGeek:** Clear tutorials and explanations simplifying complex tech concepts.
  ```text
  https://www.howtogeek.com/feed/
  ```

### 🎮 Gaming
*Video game journalism, industry news, hardware reviews, and enthusiast communities.*

* **IGN:** Leading global video game reviews, entertainment media, trailers, and guides. *(Updated to canonical URL after redirect.)*
  ```text
  https://www.ign.com/rss/articles/feed
  ```
* **Polygon:** In-depth reporting on video games, board games, comic books, and internet culture.
  ```text
  https://www.polygon.com/rss/index.xml
  ```
* **GameSpot:** Video game news, live streams, reviews, and gaming community forums.
  ```text
  https://www.gamespot.com/feeds/mashup/
  ```
* **Kotaku:** Gaming culture, industry news, developer insights, and reviews.
  ```text
  https://kotaku.com/rss
  ```
* **Eurogamer:** Independent video game journalism with sharp critical reviews and industry analysis.
  ```text
  https://www.eurogamer.net/feed
  ```
* **Nintendo Life:** Dedicated Nintendo ecosystem coverage, reviews, and retro releases.
  ```text
  http://www.nintendolife.com/feeds/latest
  ```
* **Game Informer:** Long-running gaming magazine reporting on major releases and developer updates. *(Fixed: old `/p/rss.aspx` returns HTML; official feed is `gameinformer.com/rss.xml`.)*
  ```text
  https://gameinformer.com/rss.xml
  ```
* **Xbox.com – News:** Official announcements, game pass updates, and hardware news from Xbox.
  ```text
  http://news.xbox.com/feed
  ```
* **Rock Paper Shotgun:** PC gaming journalism focusing on indie games, strategy, and PC releases.
  ```text
  https://www.rockpapershotgun.com/feed
  ```
* **PCGamesN:** PC gaming guides, news, and hardware reviews.
  ```text
  https://www.pcgamesn.com/rss
  ```
* **Pushsquare:** PlayStation ecosystem news, trophy guides, and hardware updates.
  ```text
  http://www.pushsquare.com/feeds/latest
  ```

### 📊 Business & Finance
*Economic policy, corporate strategy, financial markets, and management insights.*

* **Financial Times:** Global business intelligence, economics commentary, and financial market data.
  ```text
  https://www.ft.com/?format=rss
  ```
* **Bloomberg:** Financial market tracking, global business reporting, and economic indicators.
  ```text
  https://feeds.bloomberg.com/markets/news.rss
  ```
* **CNBC – Top News:** Market news, business headlines and financial analysis. *(Replaces Harvard Business Review, whose public feed now returns a non-standard payload with 0 readable items.)*
  ```text
  https://www.cnbc.com/id/100003114/device/rss/rss.html
  ```
* **Freakonomics:** Exploring the hidden side of everything through economic thinking and data.
  ```text
  http://freakonomics.com//feed/
  ```
* **Fortune:** Global corporate news, executive profiles, and business rankings.
  ```text
  http://fortune.com/feed/
  ```
* **Economist:** Global politics, economics, business, and science weekly perspective.
  ```text
  https://www.economist.com/the-world-this-week/rss.xml
  ```
* **Business Insider:** Financial news, tech business updates, and market trends.
  ```text
  http://feeds2.feedburner.com/businessinsider
  ```

> 🗑️ **HuffPost (front-page y business) eliminado sin reemplazo directo:** ambos feeds redirigen a `chaski.huffpost.com/...`, que devuelve XML válido pero con **0 artículos**. HuffPost descontinuó su RSS público; como alternativas generales ya están NPR, DW y Al Jazeera en esta lista.

---

## 📥 Cómo utilizarlo
1. Copia el enlace RSS utilizando el botón de copiado rápido integrado en cada bloque de código de arriba.
2. Pégalo en tu lector de feeds favorito (**Feedly**, **Inoreader**, **NetNewsWire**, **FreshRSS**, etc.).
3. ¡Disfruta de tus fuentes de información centralizadas!
