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
- [3. Medidas relacionadas en otras categorías](#3-medidas-relacionadas-en-otras-categorías)
- [4. Posibles lagunas](#4-posibles-lagunas)
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
- Revisar con regularidad los informes de indexación, experiencia de página y problemas de seguridad (ver [POST-02](07-post-lanzamiento.md#21-post-02-plan-de-revisiones-periódicas)).
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

## 3. Medidas relacionadas en otras categorías

- [REN-02](06-rendimiento.md#12-ren-02-revisar-core-web-vitals): Core Web Vitals (señal de experiencia que Google usa en sus sistemas de clasificación).
- [REN-03](06-rendimiento.md#21-ren-03-comprimir-imágenes-y-usar-formatos-modernos): imágenes optimizadas.
- [POST-02](07-post-lanzamiento.md#21-post-02-plan-de-revisiones-periódicas): plan de revisiones periódicas (Search Console).

## 4. Posibles lagunas

Medidas relevantes que **no estaban en tus listas** y no se han desarrollado:

- URL canónicas y gestión de contenido duplicado.
- Redirecciones 301 y gestión de páginas 404 al migrar o reestructurar.
- HTTPS en todo el sitio y compatibilidad móvil.
- Datos estructurados (schema.org) para resultados enriquecidos.
- `hreflang` en sitios multilingües.
- Enlazado interno y arquitectura de la información.
