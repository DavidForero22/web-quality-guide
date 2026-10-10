# Rendimiento

> Última verificación: 2026-10-10 · [Volver al README](../README.md)

Velocidad de carga, respuesta y estabilidad visual. Es buena práctica de experiencia de usuario y una señal que Google tiene en cuenta; no es una obligación legal.

<!-- INDICE -->
**Índice**

- [1. Medición](#1-medición)
  - [1.1 REN-01: Medir con PageSpeed Insights](#11-ren-01-medir-con-pagespeed-insights)
  - [1.2 REN-02: Revisar Core Web Vitals](#12-ren-02-revisar-core-web-vitals)
- [2. Recursos](#2-recursos)
  - [2.1 REN-03: Comprimir imágenes y usar formatos modernos](#21-ren-03-comprimir-imágenes-y-usar-formatos-modernos)
- [3. Entrega y carga](#3-entrega-y-carga)
  - [3.1 REN-04: Caché HTTP, CDN y compresión](#31-ren-04-caché-http-cdn-y-compresión)
  - [3.2 REN-05: Fuentes web y JavaScript de terceros](#32-ren-05-fuentes-web-y-javascript-de-terceros)
  - [3.3 REN-06: Presupuesto de rendimiento y monitorización con datos reales](#33-ren-06-presupuesto-de-rendimiento-y-monitorización-con-datos-reales)
  - [3.4 REN-07: Vídeo y contenido incrustado](#34-ren-07-vídeo-y-contenido-incrustado)
<!-- /INDICE -->

## 1. Medición

### 1.1 REN-01: Medir con PageSpeed Insights

- **Prioridad:** Alta
- **Naturaleza:** Buena práctica
- **Sectores:** INF ● · TIE ● · SUS ● · UGC ● · MEN ●
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ✅ Correcta

**De qué trata.** PageSpeed Insights combina **datos de laboratorio** (Lighthouse, una carga simulada con dispositivo y red fijos) con **datos de campo** (usuarios reales de Chrome durante los últimos 28 días, percentil 75). Es un diagnóstico útil, **no una tarea que se hace una vez**.

**Qué hacer**

- Usar los **datos de campo** para saber si la experiencia real es buena (Core Web Vitals) y los **de laboratorio** para depurar problemas concretos.
- Medir móvil y escritorio por separado, y las plantillas clave (portada, listado, ficha, carrito, artículo), no solo la portada.
- Esperar variabilidad entre ejecuciones de laboratorio: es normal.
- **No perseguir una puntuación perfecta** a costa de la experiencia o de funcionalidad: la nota de 0 a 100 es un indicador, no el objetivo.
- Repetir tras cada cambio relevante y de forma periódica ([POST-02](08-post-lanzamiento.md#21-post-02-plan-de-revisiones-periódicas)).

**Matiz.** Si la URL no tiene suficientes datos de campo, PSI recurre a datos del origen o no muestra datos reales; en sitios nuevos o con poco tráfico, vale más el laboratorio.

**Fuentes:** [Google: acerca de PageSpeed Insights](https://developers.google.com/speed/docs/insights/v5/about)

### 1.2 REN-02: Revisar Core Web Vitals

- **Prioridad:** Alta
- **Naturaleza:** Buena práctica
- **Sectores:** INF ● · TIE ● · SUS ● · UGC ● · MEN ●
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ✅ Correcta

**De qué trata.** Tres métricas que identifican carga lenta, mala respuesta e inestabilidad visual. Una página «aprueba» si cumple las tres en el **percentil 75** de las cargas, medidas por separado en móvil y escritorio.

| Métrica | Qué mide | Objetivo (bueno) |
|---|---|---|
| **LCP** (*Largest Contentful Paint*) | Carga del contenido principal | ≤ 2,5 s |
| **INP** (*Interaction to Next Paint*) | Capacidad de respuesta a la interacción | ≤ 200 ms |
| **CLS** (*Cumulative Layout Shift*) | Estabilidad visual | ≤ 0,1 |

**Qué hacer**

- **LCP:** optimizar la imagen o bloque principal (tamaño, formato, prioridad de carga), reducir el tiempo de respuesta del servidor y los recursos que bloquean el renderizado.
- **INP:** reducir y trocear JavaScript de larga duración, retrasar scripts de terceros.
- **CLS:** declarar `width` y `height` (o `aspect-ratio`) en imágenes y vídeos, reservar espacio para anuncios y banners, evitar insertar contenido sobre el existente.
- Medir con datos de campo (Search Console, PSI) además de laboratorio.

**Matices**

- **INP sustituyó a FID** como Core Web Vital estable en 2024.
- Google las usa en sus sistemas de clasificación como parte de la experiencia de página, pero **aprobarlas no garantiza posiciones altas**: el contenido relevante y útil pesa más.

**Fuentes**

- [web.dev: Core Web Vitals](https://web.dev/articles/vitals)
- [Google: Core Web Vitals y la Búsqueda](https://developers.google.com/search/docs/appearance/core-web-vitals)

## 2. Recursos

### 2.1 REN-03: Comprimir imágenes y usar formatos modernos

- **Prioridad:** Alta
- **Naturaleza:** Buena práctica
- **Sectores:** INF ● · TIE ● · SUS ◐ · UGC ● · MEN ●
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ✅ Correcta

**De qué trata.** Reducir los bytes servidos acelera la carga y suele mejorar el LCP. **WebP no es obligatorio**: el objetivo es servir imágenes del tamaño adecuado a cada pantalla, comprimidas y sin pérdida visible.

**Qué hacer**

- Servir imágenes **responsivas** con `srcset` y `sizes`, para no enviar a un móvil la imagen de escritorio.
- Considerar formatos modernos (**WebP**, **AVIF**) con `<picture>` y un respaldo en JPEG/PNG según tu público y flujo técnico.
- Indicar `width` y `height` para evitar saltos de diseño ([REN-02](06-rendimiento.md#12-ren-02-revisar-core-web-vitals)).
- Carga diferida (`loading="lazy"`) para imágenes fuera de pantalla; **no** para la imagen principal (LCP).
- Mantener un `alt` útil en cada imagen ([WCAG 1.1.1](01-accesibilidad.md#21-wcag-111-contenido-no-textual-a)).
- Preferir SVG para iconos y logotipos.

**Fuentes:** [web.dev: sirve imágenes responsivas](https://web.dev/articles/serve-responsive-images)

## 3. Entrega y carga

### 3.1 REN-04: Caché HTTP, CDN y compresión

- **Prioridad:** Alta
- **Naturaleza:** Buena práctica
- **Sectores:** INF ● · TIE ● · SUS ● · UGC ● · MEN ●
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ➕ Añadida

**De qué trata.** Evitar descargas innecesarias y reducir el tamaño de lo que se descarga. Suelen mejorar la carga sobre todo en sitios con audiencia distribuida o recursos pesados.

**Qué hacer**

- **Recursos con nombre versionado** (con *hash*): `Cache-Control: max-age=31536000` (y `immutable` si procede).
- **HTML y recursos sin versionar:** `no-cache` con validación `ETag`, para que el servidor responda `304 Not Modified` si no ha cambiado. Declara siempre `Cache-Control`; no dejes que el navegador lo estime.
- **Compresión de texto** (HTML, CSS, JS, SVG): preferir **Brotli** a gzip; no comprimir imágenes ya comprimidas ni archivos muy pequeños. Minificar en la compilación.
- **CDN** para recursos estáticos y, si procede, para HTML cacheable; ten cuidado con lo personalizado y con los datos personales en caché.
- Comprobar en la pestaña Red de DevTools el tamaño transferido frente al real.

**Fuentes**

- [web.dev: caché HTTP](https://web.dev/articles/http-cache)
- [web.dev: optimiza la codificación y el tamaño de transferencia](https://web.dev/articles/optimizing-content-efficiency-optimize-encoding-and-transfer)

### 3.2 REN-05: Fuentes web y JavaScript de terceros

- **Prioridad:** Media
- **Naturaleza:** Buena práctica
- **Sectores:** INF ● · TIE ● · SUS ● · UGC ● · MEN ●
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ➕ Añadida

**De qué trata.** Controlar la carga de fuentes y de scripts externos para evitar bloqueos, saltos de diseño y dependencias innecesarias. Cada tercero que cargas es además un riesgo de privacidad ([PRIV-08](02-privacidad-cookies-y-comunicaciones.md#33-priv-08-auditar-sdks-y-servicios-de-terceros)).

**Qué hacer**

- **Fuentes:** usar WOFF2, subconjuntos (`unicode-range`) y las fuentes imprescindibles; fuentes del sistema o variables cuando sea posible. `font-display` según el caso (`optional` para el cuerpo, `swap` para marca). Precarga con moderación. SVG mejor que fuentes de iconos.
- **Autoalojar** fuentes solo mejora el rendimiento si usas CDN y HTTP/2: mídelo. Tiene además ventajas de privacidad ([PRIV-09](02-privacidad-cookies-y-comunicaciones.md#34-priv-09-cargar-las-fuentes-de-google-desde-tu-propio-servidor)).
- **JavaScript de terceros:** identificarlos con Lighthouse («Third-party usage») y bloqueando peticiones en DevTools para medir su coste; cargar con `async`/`defer`, retrasar los no críticos y eliminar los que no aporten.
- Evitar que los scripts de terceros se carguen antes del consentimiento ([PRIV-07](02-privacidad-cookies-y-comunicaciones.md#32-priv-07-banner-de-consentimiento-de-cookies)).

**Fuentes**

- [web.dev: buenas prácticas con fuentes](https://web.dev/articles/font-best-practices)
- [web.dev: identificar JavaScript de terceros lento](https://web.dev/articles/identify-slow-third-party-javascript)

### 3.3 REN-06: Presupuesto de rendimiento y monitorización con datos reales

- **Prioridad:** Media
- **Naturaleza:** Buena práctica
- **Sectores:** INF ◐ · TIE ● · SUS ● · UGC ● · MEN ◐
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ➕ Añadida

**De qué trata.** Fijar límites y medir con usuarios reales para que el rendimiento no se degrade con cada cambio. Es proporcional al tráfico y al presupuesto: un sitio pequeño necesita poco.

**Qué hacer**

- Definir un **presupuesto** con tres tipos de límite: cantidad (peso de imágenes y scripts, número de fuentes), hitos (LCP, INP, CLS; [REN-02](06-rendimiento.md#12-ren-02-revisar-core-web-vitals)) y reglas (puntuación de Lighthouse).
- Presupuestos distintos por tipo de página (portada, ficha, artículo).
- Aplicarlos en el proceso de compilación (p. ej., Lighthouse CI) y actuar cuando se superen: optimizar, retirar o no añadir.
- Medir **datos de campo** continuamente (Search Console, PageSpeed Insights o la biblioteca `web-vitals`) y no solo de laboratorio ([REN-01](06-rendimiento.md#11-ren-01-medir-con-pagespeed-insights)).
- Referencia del artículo de web.dev: menos de 170 KB de recursos críticos comprimidos y TTI inferior a 5 s en un dispositivo de gama media con red lenta. Ajústalo a tu público.

**Fuentes:** [web.dev: presupuestos de rendimiento](https://web.dev/articles/performance-budgets-101)

### 3.4 REN-07: Vídeo y contenido incrustado

- **Prioridad:** Media (si forman parte importante de la experiencia)
- **Naturaleza:** Buena práctica
- **Sectores:** INF ◐ · TIE ◐ · SUS ◐ · UGC ◐ · MEN ◐
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ➕ Añadida

**De qué trata.** El vídeo y los `iframe` (mapas, reproductores, redes sociales) son de los recursos más pesados. Si no son esenciales, bastan la carga diferida o alternativas ligeras.

**Qué hacer**

- `preload="none"` y `poster` en vídeos que no se reproducen al instante; carga diferida (`loading="lazy"`) fuera de pantalla. **No** diferir el elemento que es el LCP.
- **Evitar el autoplay** salvo que sea silencioso y breve; si hay audio automático, debe poder pausarse ([WCAG 1.4.2](01-accesibilidad.md#213-wcag-142-control-del-audio-a), [WCAG 2.2.2](01-accesibilidad.md#35-wcag-222-pausar-detener-ocultar-a)).
- `loading="lazy"` en los `iframe` de contenido incrustado; cargar el embed real solo al interactuar (imagen previa) cuando sea posible.
- Subtítulos y alternativas de texto ([WCAG 1.2.2](01-accesibilidad.md#23-wcag-122-subtítulos-pregrabado-a)).

**Fuentes:** [web.dev: carga diferida de vídeo](https://web.dev/articles/lazy-loading-video)
