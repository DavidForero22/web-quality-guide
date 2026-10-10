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
- [3. Posibles lagunas](#3-posibles-lagunas)
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
- Repetir tras cada cambio relevante y de forma periódica ([POST-02](07-post-lanzamiento.md#21-post-02-plan-de-revisiones-periódicas)).

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

## 3. Posibles lagunas

Medidas relevantes que **no estaban en tus listas** y no se han desarrollado:

- Caché HTTP, CDN y compresión (Brotli/gzip) de recursos.
- Estrategia de carga de fuentes web y de JavaScript de terceros.
- Presupuestos de rendimiento y monitorización continua (datos de usuarios reales).
- Optimización de vídeo y de recursos incrustados.
