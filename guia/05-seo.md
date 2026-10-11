# SEO

> Última verificación: 2026-10-10 · [Volver al README](../README.md)

Visibilidad en buscadores. Las medidas se basan en la documentación de **Google Search Central**; otros buscadores pueden diferir. El SEO no es una obligación legal: es **buena práctica**, y por eso la dimensión «regiones» es universal.

<!-- INDICE -->
**Índice**

- [1. Presencia e indexación](#1-presencia-e-indexación)
  - [1.1 SEO-01: Registrar la web en Search Console](#11-seo-01-registrar-la-web-en-search-console)
  - [1.2 SEO-02: Solicitar a Google que indexe la web](#12-seo-02-solicitar-a-google-que-indexe-la-web)
  - [1.3 SEO-03: Generar sitemap.xml](#13-seo-03-generar-sitemapxml)
  - [1.4 SEO-04: Generar robots.txt](#14-seo-04-generar-robotstxt)
- [2. Contenido en resultados](#2-contenido-en-resultados)
  - [2.1 SEO-05: Títulos y descripciones personalizados](#21-seo-05-títulos-y-descripciones-personalizados)
- [3. Estructura y señales técnicas](#3-estructura-y-señales-técnicas)
  - [3.1 SEO-06: Canónicas y contenido duplicado](#31-seo-06-canónicas-y-contenido-duplicado)
  - [3.2 SEO-07: Redirecciones 301 y páginas 404](#32-seo-07-redirecciones-301-y-páginas-404)
  - [3.3 SEO-08: Compatibilidad móvil e indexación centrada en móviles](#33-seo-08-compatibilidad-móvil-e-indexación-centrada-en-móviles)
  - [3.4 SEO-09: Datos estructurados](#34-seo-09-datos-estructurados)
  - [3.5 SEO-10: hreflang para versiones por idioma o región](#35-seo-10-hreflang-para-versiones-por-idioma-o-región)
  - [3.6 SEO-11: Enlazado interno y arquitectura de la información](#36-seo-11-enlazado-interno-y-arquitectura-de-la-información)
- [4. Identidad y vista previa](#4-identidad-y-vista-previa)
  - [4.1 SEO-12: Favicon](#41-seo-12-favicon)
  - [4.2 SEO-13: Open Graph y vista previa al compartir](#42-seo-13-open-graph-y-vista-previa-al-compartir)
- [5. Medidas relacionadas en otras categorías](#5-medidas-relacionadas-en-otras-categorías)
<!-- /INDICE -->

## 1. Presencia e indexación

### 1.1 SEO-01: Registrar la web en Search Console

- **Prioridad:** Alta
- **Naturaleza:** Buena práctica
- **Sectores:** INF ● · TIE ● · SUS ◐ · UGC ● · MEN ◐
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ✅ Correcta

**De qué trata.** Search Console es un servicio **gratuito** de Google para vigilar la presencia del sitio en la Búsqueda: indexación, tráfico, errores, Core Web Vitals y alertas. **No es un requisito** para aparecer en Google.

**Qué hacer**

- Verificar la propiedad como **dominio** (DNS) para cubrir todos los subdominios y protocolos.
- Añadir al menos otro usuario con acceso para no depender de una sola persona.
- Revisar con regularidad los informes de indexación, experiencia de página y problemas de seguridad (ver [POST-02](09-post-lanzamiento.md#21-post-02-plan-de-revisiones-periódicas)).
- Si el sitio es una aplicación detrás de inicio de sesión, el valor se limita a la parte pública.

**Fuentes:** [Ayuda de Search Console](https://support.google.com/webmasters/answer/9128668)

### 1.2 SEO-02: Solicitar a Google que indexe la web

- **Prioridad:** Media
- **Naturaleza:** Buena práctica
- **Sectores:** INF ● · TIE ● · SUS ◐ · UGC ● · MEN ◐
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ✅ Correcta

**De qué trata.** Pedir el rastreo de URLs nuevas o modificadas. **No garantiza** inclusión ni posicionamiento: Google lo indica expresamente.

**Qué hacer**

- Para pocas URLs importantes, usa la herramienta de **inspección de URLs** y «Solicitar indexación».
- Para muchas URLs, envía un **sitemap** ([SEO-03](05-seo.md#13-seo-03-generar-sitemapxml)) y deja que Google las descubra.
- No reenvíes la misma URL repetidamente: tiene cuota y no acelera el rastreo.
- Espera desde días hasta semanas; si no se indexa, revisa la calidad del contenido y los bloqueos ([SEO-04](05-seo.md#14-seo-04-generar-robotstxt)).
- Si usas WordPress o Blogger, normalmente la plataforma ya notifica el contenido nuevo.

**Fuentes:** [Google: pedir un nuevo rastreo de tus URLs](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl)

### 1.3 SEO-03: Generar sitemap.xml

- **Prioridad:** Media
- **Naturaleza:** Buena práctica
- **Sectores:** INF ● · TIE ● · SUS ◐ · UGC ● · MEN ◐
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ✅ Correcta

**De qué trata.** Un sitemap facilita el descubrimiento de URLs, sobre todo en sitios grandes, nuevos o con mucho contenido multimedia. **No garantiza** que Google las rastree o indexe.

**Qué hacer**

- Incluir solo URLs **canónicas, indexables y con código 200**.
- Referenciarlo en `robots.txt` (`Sitemap: https://tudominio.com/sitemap.xml`) y enviarlo en Search Console.
- Mantenerlo actualizado automáticamente (muchos CMS lo generan).
- En sitios pequeños (unas 500 páginas o menos) y bien enlazados internamente puede no ser imprescindible, aunque rara vez perjudica.

**Fuentes:** [Google: visión general de los sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview)

### 1.4 SEO-04: Generar robots.txt

- **Prioridad:** Media
- **Naturaleza:** Buena práctica
- **Sectores:** INF ◐ · TIE ● · SUS ◐ · UGC ● · MEN ◐
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ✅ Correcta

**De qué trata.** `robots.txt` sirve para gestionar el **rastreo** (evitar sobrecargas o rastrear páginas poco útiles). **No es un mecanismo para ocultar páginas** del índice.

**Qué hacer**

- Usarlo solo si necesitas gestionar el rastreo de ciertas rutas (filtros infinitos, búsquedas internas, áreas privadas sin valor).
- Para **mantener una página fuera de Google**, usar `noindex` (meta o cabecera `X-Robots-Tag`) o protección con contraseña. Una página bloqueada en `robots.txt` puede aparecer igualmente, sin descripción, si otros sitios la enlazan.
- **No combinar** ambas cosas sobre la misma URL: si bloqueas el rastreo, Google no puede ver el `noindex`.
- No bloquear los recursos (CSS, JS, imágenes) que Google necesita para renderizar la página.
- No usarlo para proteger información sensible: es un archivo público.

**Fuentes:** [Google: introducción a robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro)

## 2. Contenido en resultados

### 2.1 SEO-05: Títulos y descripciones personalizados

- **Prioridad:** Alta (títulos) · Media (descripciones)
- **Naturaleza:** Buena práctica
- **Sectores:** INF ● · TIE ● · SUS ◐ · UGC ● · MEN ◐
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ✅ Correcta

**De qué trata.** Cada página importante debe tener un título claro, único y fiel al contenido. La descripción ayuda a presentar el resultado y atraer clics, pero Google **puede sustituirla** y no es una garantía de posicionamiento.

**Qué hacer**

- `<title>` único por página, descriptivo, con lo más relevante al principio y sin repetir el nombre del sitio de forma excesiva. Es además un requisito de accesibilidad ([WCAG 2.4.2](01-accesibilidad.md#38-wcag-242-titulado-de-páginas-a)).
- `<meta name="description">` única por página, resumen informativo y atractivo; no una lista de palabras clave.
- **No pierdas tiempo con `<meta name="keywords">`**: Google no la usa desde 2009.
- Un `<h1>` por página coherente con el título.
- Texto `alt` descriptivo en las imágenes ([WCAG 1.1.1](01-accesibilidad.md#21-wcag-111-contenido-no-textual-a)): ayuda a Google a entenderlas.

**Fuentes**

- [Google: fragmentos y metadescripciones](https://developers.google.com/search/docs/appearance/snippet)
- [Google: Google no usa la etiqueta meta keywords](https://developers.google.com/search/blog/2009/09/google-does-not-use-keywords-meta-tag)

## 3. Estructura y señales técnicas

### 3.1 SEO-06: Canónicas y contenido duplicado

- **Prioridad:** Media
- **Naturaleza:** Buena práctica
- **Sectores:** INF ● · TIE ● · SUS ◐ · UGC ● · MEN ◐
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ➕ Añadida

**De qué trata.** Cuando una misma página es accesible por varias URL (parámetros, `http`/`https`, con y sin `www`, filtros, versiones imprimibles), conviene indicar cuál es la representativa. Google lo decide también con otras señales; indicarlo ayuda, pero ningún método es obligatorio.

**Qué hacer**

- Usar **redirecciones permanentes** para los duplicados que retiras ([SEO-07](05-seo.md#32-seo-07-redirecciones-301-y-páginas-404)).
- Añadir `<link rel="canonical">` con URL **absoluta** y también en la propia página canónica (autorreferenciada). Para archivos como PDF se puede usar la cabecera HTTP.
- Incluir solo URL canónicas en el sitemap ([SEO-03](05-seo.md#13-seo-03-generar-sitemapxml)) y enlazar internamente a la canónica.
- **No** usar `robots.txt` ni `noindex` para elegir la canónica, y evitar señales contradictorias entre métodos.
- Con JavaScript, poner la canónica en el HTML de origen y que el script no la modifique.
- No usar `rel="canonical"` para variantes de idioma o región: para eso, [SEO-10](05-seo.md#35-seo-10-hreflang-para-versiones-por-idioma-o-región).

**Fuentes:** [Google: consolidar URL duplicadas](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)

### 3.2 SEO-07: Redirecciones 301 y páginas 404

- **Prioridad:** Alta (al migrar o cambiar URL) · Media (el resto del tiempo)
- **Naturaleza:** Buena práctica
- **Sectores:** INF ● · TIE ● · SUS ◐ · UGC ● · MEN ◐
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ➕ Añadida

**De qué trata.** Al mover, renombrar o eliminar contenido hay que conservar el valor de las URL antiguas y no dejar al usuario ante errores confusos.

**Qué hacer**

- **Traslado permanente:** redirección `301` o `308` desde cada URL antigua a su equivalente más cercano (1 a 1), preferiblemente en el servidor. Evita cadenas y bucles.
- **Traslado temporal:** `302`/`307`, que mantienen la URL original en resultados.
- No redirigir masivamente todo a la portada ni a una página no relacionada.
- Contenido eliminado sin equivalente: devolver un `404` o `410` real. Evita los *soft 404* (un `200` con un mensaje de «no encontrado»).
- Ofrecer una página 404 **útil**: mensaje claro y amable, el mismo diseño y navegación del sitio, enlaces a la portada y a contenido popular, buscador y una forma de informar de enlaces rotos. Y comprobar que devuelve **realmente** el código 404.
- Tras una migración, comprobar en Search Console la cobertura y los errores ([SEO-01](05-seo.md#11-seo-01-registrar-la-web-en-search-console)).

**Fuentes**

- [Google: redirecciones y Search](https://developers.google.com/search/docs/crawling-indexing/301-redirects)
- [Google: códigos de estado HTTP](https://developers.google.com/search/docs/crawling-indexing/http-network-errors)

### 3.3 SEO-08: Compatibilidad móvil e indexación centrada en móviles

- **Prioridad:** Alta
- **Naturaleza:** Buena práctica
- **Sectores:** INF ● · TIE ● · SUS ◐ · UGC ● · MEN ●
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ➕ Añadida

**De qué trata.** Google usa la **versión móvil** del contenido para indexar y posicionar. HTTPS es la base de seguridad ([SEG-01](08-seguridad-y-operacion.md#11-seg-01-https-y-cabeceras-de-seguridad)); la experiencia móvil debe formar parte de las pruebas.

**Qué hacer**

- Usar **diseño responsive** (mismo HTML y misma URL): es la opción recomendada.
- Garantizar que la versión móvil tiene el **mismo contenido principal**, el mismo `title` y descripción, los mismos datos estructurados y las mismas imágenes con su `alt`.
- No bloquear en `robots.txt` los recursos necesarios para renderizar ni cargar el contenido principal solo tras una interacción.
- Probar en dispositivos reales y con objetivos táctiles suficientes ([WCAG 2.5.8](01-accesibilidad.md#320-wcag-258-tamaño-del-objetivo-mínimo-aa)).

**Fuentes:** [Google: indexación centrada en móviles](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing)

### 3.4 SEO-09: Datos estructurados

- **Prioridad:** Media
- **Naturaleza:** Buena práctica
- **Sectores:** INF ◐ · TIE ● · SUS ◐ · UGC ◐ · MEN ◐
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ➕ Añadida

**De qué trata.** Marcado estandarizado que describe el contenido de la página (producto, artículo, receta, evento, organización…). Puede dar lugar a **resultados enriquecidos**, pero **no los garantiza**.

**Qué hacer**

- Preferir **JSON-LD**.
- Marcar solo contenido que sea **visible** para el usuario y refleje la realidad; no crear páginas vacías para alojar datos.
- Incluir las propiedades obligatorias del tipo; es mejor lo completo y exacto que mucho incompleto.
- Validar con la prueba de resultados enriquecidos y revisar los informes de Search Console tras publicar.
- No marcar reseñas que no sean reales ([COM-07](03-consumo-y-comercio.md#23-com-07-eliminar-reseñas-falsas)).

**Fuentes:** [Google: introducción a los datos estructurados](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)

### 3.5 SEO-10: hreflang para versiones por idioma o región

- **Prioridad:** Media (solo si hay versiones lingüísticas o regionales)
- **Naturaleza:** Buena práctica
- **Sectores:** INF ◐ · TIE ◐ · SUS ◐ · UGC ◐ · MEN ◐
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ➕ Añadida

**De qué trata.** Indicar a Google qué versión mostrar según el idioma o la región del usuario. Sin versiones alternativas, no hace falta.

**Qué hacer**

- Elegir **un** método: etiquetas `<link>` en el HTML, cabeceras HTTP (útil para PDF) o sitemap.
- Cada versión debe listarse a sí misma y a todas las demás, con enlaces **recíprocos**; si falta el enlace de vuelta, Google lo ignora.
- URL completas, con protocolo. Código de idioma (ISO 639-1), con región opcional (ISO 3166-1 Alpha 2): `es-ES`, `en-GB`. Una región sola no es válida.
- Añadir `x-default` para la página de respaldo (por ejemplo, un selector de país).

**Fuentes:** [Google: versiones localizadas (hreflang)](https://developers.google.com/search/docs/specialty/international/localized-versions)

### 3.6 SEO-11: Enlazado interno y arquitectura de la información

- **Prioridad:** Media
- **Naturaleza:** Buena práctica
- **Sectores:** INF ● · TIE ● · SUS ◐ · UGC ● · MEN ◐
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ➕ Añadida

**De qué trata.** Los enlaces ayudan a Google a descubrir páginas y a entender su relevancia, y ayudan a las personas a orientarse. Es práctica de usabilidad, de rastreo y de accesibilidad.

**Qué hacer**

- Enlaces rastreables: elemento `<a>` con `href` real; no depender de `onclick` ni de enlaces solo de JavaScript.
- Texto de enlace **descriptivo** (nada de «pulsa aquí»): lo exige también [WCAG 2.4.4](01-accesibilidad.md#310-wcag-244-propósito-de-los-enlaces-en-contexto-a).
- Que cada página importante tenga al menos un enlace desde otra, sin páginas huérfanas, y una jerarquía clara.
- Imágenes que son enlaces: `alt` descriptivo.
- En enlaces externos, `rel="sponsored"` para pagados y `rel="ugc"` para los enviados por usuarios.

**Fuentes:** [Google: hacer enlaces rastreables](https://developers.google.com/search/docs/crawling-indexing/links-crawlable)

## 4. Identidad y vista previa

### 4.1 SEO-12: Favicon

- **Prioridad:** Media
- **Naturaleza:** Buena práctica
- **Sectores:** INF ● · TIE ● · SUS ● · UGC ● · MEN ●
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ✅ Correcta

**De qué trata.** El icono que aparece en pestañas, marcadores y resultados de búsqueda. Un set razonable es pequeño: no hace falta incluir todos los formatos y tamaños «por si acaso».

**Qué hacer**

- Declarar `<link rel="icon" href="...">` en el `<head>` de la página principal.
- Que el archivo sea **cuadrado** (1:1). Google acepta formatos como ICO, PNG, GIF o JPEG, exige al menos 8 × 8 px y **recomienda más de 48 × 48 px** para que se vea bien en los resultados.
- Un favicon **por host**: no se admite uno distinto para un subdirectorio. Mantén la URL estable y que represente visualmente la marca.
- **No bloquear** el archivo del favicon ni la portada en `robots.txt` ([SEO-04](05-seo.md#14-seo-04-generar-robotstxt)).
- Para instalación como app, declarar en el manifiesto iconos de 192 y 512 px, y un `apple-touch-icon` si te interesa iOS.
- Diseñarlo primero para 16 a 32 px; si el logotipo no se reconoce a ese tamaño, crear una variante simplificada.

**Matiz.** Google no garantiza que el favicon se muestre aunque cumplas los requisitos, y puede tardar de días a semanas.

**Fuentes**

- [Google: favicon en los resultados de búsqueda](https://developers.google.com/search/docs/appearance/favicon-in-search)
- [web.dev: añadir un manifiesto de aplicación web](https://web.dev/articles/add-manifest)

### 4.2 SEO-13: Open Graph y vista previa al compartir

- **Prioridad:** Media
- **Naturaleza:** Buena práctica
- **Sectores:** INF ● · TIE ● · SUS ◐ · UGC ● · MEN ◐
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ✅ Correcta

**De qué trata.** Las etiquetas Open Graph controlan el título, la descripción y la imagen que muestran redes sociales y apps de mensajería al compartir un enlace. No es imprescindible en todas las páginas, pero es una buena inversión en artículos, productos, campañas y páginas de captación.

**Qué hacer**

- Incluir las cuatro propiedades básicas: `og:title`, `og:type`, `og:image` y `og:url` (URL canónica; ver [SEO-06](05-seo.md#31-seo-06-canónicas-y-contenido-duplicado)). Añadir `og:description`, `og:site_name` y `og:locale` (`es_ES`).
- Usar **URL absolutas** y una imagen **por página** relevante: 1200 × 630 px (relación 1,91:1) es la referencia de Meta para la mejor visualización; por debajo de 600 × 315 px la vista previa es pequeña. Peso máximo de 8 MB.
- Indicar `og:image:width` y `og:image:height` y un `og:image:alt` descriptivo.
- Evitar imágenes genéricas reutilizadas, con demasiado texto o enormes que ralenticen la generación de la vista previa.
- Las imágenes se **cachean por URL**: para actualizarla, usa una URL nueva y vuelve a procesar el enlace en el depurador de la plataforma.
- Como complemento, etiquetas `twitter:card` para X.

**Fuentes**

- [Open Graph protocol](https://ogp.me/)
- [Meta: imágenes en enlaces compartidos](https://developers.facebook.com/docs/sharing/webmasters/images)

## 5. Medidas relacionadas en otras categorías

- [REN-02](06-rendimiento.md#12-ren-02-revisar-core-web-vitals): Core Web Vitals (señal de experiencia que Google usa en sus sistemas de clasificación).
- [REN-03](06-rendimiento.md#21-ren-03-comprimir-imágenes-y-usar-formatos-modernos): imágenes optimizadas.
- [POST-02](09-post-lanzamiento.md#21-post-02-plan-de-revisiones-periódicas): plan de revisiones periódicas (Search Console).
- [SEG-01](08-seguridad-y-operacion.md#11-seg-01-https-y-cabeceras-de-seguridad): HTTPS, base de seguridad que Google también prefiere para la URL canónica.
