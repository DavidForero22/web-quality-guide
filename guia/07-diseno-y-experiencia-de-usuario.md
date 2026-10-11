# Diseño y experiencia de usuario

> Última verificación: 2026-10-11 · [Volver al README](../README.md)

Decisiones de diseño de interfaz que mejoran la comprensión, la conversión y la consistencia. No son obligaciones legales: son **buenas prácticas** y muchas dependen del tipo de web, por eso cada ficha indica cuándo aplicarla y cuándo no. La dimensión «regiones» es universal.

Dos medidas de este ámbito no tienen ficha propia porque ya estaban cubiertas: los **estados de error de formulario** (ver [WCAG 3.3.1](01-accesibilidad.md#48-wcag-331-identificación-de-errores-a) y [WCAG 3.3.3](01-accesibilidad.md#410-wcag-333-sugerencias-ante-errores-aa)) y la **página 404** (ver [SEO-07](05-seo.md#32-seo-07-redirecciones-301-y-páginas-404)).

<!-- INDICE -->
**Índice**

- [1. Claridad y consistencia](#1-claridad-y-consistencia)
  - [1.1 UX-01: Acción principal clara y reducción de opciones](#11-ux-01-acción-principal-clara-y-reducción-de-opciones)
  - [1.2 UX-02: Design tokens](#12-ux-02-design-tokens)
- [2. Estados y conversión](#2-estados-y-conversión)
  - [2.1 UX-03: Estados de carga: skeletons, spinners y barras de progreso](#21-ux-03-estados-de-carga-skeletons-spinners-y-barras-de-progreso)
  - [2.2 UX-04: Página de confirmación tras una conversión](#22-ux-04-página-de-confirmación-tras-una-conversión)
<!-- /INDICE -->

## 1. Claridad y consistencia

### 1.1 UX-01: Acción principal clara y reducción de opciones

- **Prioridad:** Media
- **Naturaleza:** Buena práctica
- **Sectores:** INF ◐ · TIE ● · SUS ● · UGC ◐ · MEN ◐
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ⚠️ Matizada

**De qué trata.** Que cada página tenga una acción principal evidente y que las alternativas equivalentes o ambiguas no compitan con ella. Fusiona dos puntos del listado: «no violar la ley de Hick» y «CTA above the fold».

**Qué hacer**

- Identificar **una acción principal por página** y darle prominencia visual; las secundarias se presentan como alternativas subordinadas (botón secundario, enlace).
- Redactar el CTA con un texto **específico** («Solicitar presupuesto», «Reservar mesa»), no genérico («Enviar», «Aceptar»).
- **Agrupar o eliminar opciones equivalentes**: una página de contacto con seis canales del mismo peso genera indecisión; destaca uno y agrupa el resto.
- En catálogos, comparadores o herramientas profesionales, muchas opciones pueden ser necesarias: aporta filtros, búsqueda, categorías y jerarquía en lugar de eliminar contenido.
- Colocar las llamadas a la acción prioritarias donde se vean sin desplazarse **cuando la página tenga una acción principal** (landing, producto, formulario de conversión).

**Matices**

- La ley de Hick-Hyman describe que el tiempo de decisión crece con el número de alternativas; es un principio de apoyo, **no una regla para reducir siempre todo a una opción**.
- *Above the fold* no es un dogma. En el estudio de seguimiento ocular de NN/g (2018), los usuarios dedicaron alrededor del 57 % del tiempo de visualización a lo que queda sobre el pliegue y cerca del 74 % a las dos primeras pantallas: el contenido prioritario debe estar arriba, pero los usuarios sí se desplazan. Una página informativa puede necesitar contexto antes del CTA, y «sobre el pliegue» varía según el dispositivo.
- Prominencia no es manipulación: no hagas invisible la opción de rechazar ni uses *confirmshaming* ([COM-06](03-consumo-y-comercio.md#22-com-06-eliminar-patrones-oscuros); en el banner de cookies, aceptar y rechazar deben ser comparables, [PRIV-07](02-privacidad-cookies-y-comunicaciones.md#32-priv-07-banner-de-consentimiento-de-cookies)).
- El CTA debe tener un nombre accesible que contenga su texto visible ([WCAG 2.5.3](01-accesibilidad.md#317-wcag-253-etiqueta-en-el-nombre-a)) y un tamaño de objetivo suficiente ([WCAG 2.5.8](01-accesibilidad.md#320-wcag-258-tamaño-del-objetivo-mínimo-aa)).

**Fuentes**

- [NN/g: Scrolling and Attention](https://www.nngroup.com/articles/scrolling-and-attention/)
- [Laws of UX: Hick's Law](https://lawsofux.com/hicks-law/) (fuente secundaria; no se pudo abrir el artículo de NN/g)

### 1.2 UX-02: Design tokens

- **Prioridad:** Media (Baja en una landing sencilla)
- **Naturaleza:** Buena práctica
- **Sectores:** INF ◐ · TIE ● · SUS ● · UGC ◐ · MEN ◐
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ✅ Correcta

**De qué trata.** Los *design tokens* son valores con nombre (color, tipografía, espaciado, radios, sombras, puntos de ruptura) que funcionan como fuente única de verdad entre diseño y código. Reducen inconsistencias y hacen baratos los cambios globales (temas, modo oscuro, varias marcas).

**Qué hacer**

- No hace falta un sistema enorme desde el primer día: para un sitio pequeño bastan **variables CSS** (`--color-action`, `--space-md`, `--radius-card`).
- Usar nombres **semánticos** (qué hacen) y no de implementación (cómo se ven): `--color-action`, no `--azul-claro-2`.
- Separar tokens primitivos (la paleta) de tokens semánticos (el uso) para poder cambiar de tema sin tocar los componentes.
- Validar los pares de color de los tokens contra el contraste mínimo ([WCAG 1.4.3](01-accesibilidad.md#214-wcag-143-contraste-mínimo-aa), [WCAG 1.4.11](01-accesibilidad.md#218-wcag-1411-contraste-no-textual-aa)) una vez, en el token, en lugar de en cada componente.
- Si el proyecto tiene varios equipos o plataformas, adoptar el formato estándar del *Design Tokens Community Group* para intercambiarlos entre herramientas.

**Matiz.** La versión 2025.10 del formato es la primera estable, pero es un informe final del grupo comunitario, **no un estándar del W3C**.

**Fuentes**

- [W3C DTCG: la especificación alcanza su primera versión estable](https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/)
- [Design Tokens Format Module 2025.10](https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/)
- [MDN: propiedades personalizadas de CSS](https://developer.mozilla.org/docs/Web/CSS/Using_CSS_custom_properties)

## 2. Estados y conversión

### 2.1 UX-03: Estados de carga: skeletons, spinners y barras de progreso

- **Prioridad:** Baja (contextual)
- **Naturaleza:** Buena práctica
- **Sectores:** INF ◐ · TIE ◐ · SUS ● · UGC ◐ · MEN ◐
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ⚠️ Matizada

**De qué trata.** Elegir el indicador de espera adecuado según la duración y la estructura de lo que se carga. Un *skeleton* (marcador con la forma de la página) puede reducir la espera percibida, pero **complementa y no sustituye** a optimizar el rendimiento.

**Qué hacer**

| Situación | Indicador recomendado (NN/g) |
|---|---|
| Carga inferior a 1 s | Ninguno |
| Un módulo concreto, de unos 2 a 10 s (vídeo, tarjeta de un panel) | Spinner local |
| Página completa de menos de 10 s con estructura predecible (listados, paneles, artículos) | Skeleton |
| Más de 10 s, subidas o conversiones de archivo | Barra de progreso |

- Que el skeleton **represente fielmente** el contenido que llegará y conserve sus dimensiones: así evitas saltos de diseño ([REN-02](06-rendimiento.md#12-ren-02-revisar-core-web-vitals)). Prefiere el skeleton estático; la animación (*shimmer*) puede distraer y plantear problemas de accesibilidad.
- Respetar `prefers-reduced-motion` y poder pausar el movimiento que dure más de 5 s ([WCAG 2.2.2](01-accesibilidad.md#35-wcag-222-pausar-detener-ocultar-a)).
- Anunciar el estado de carga a las tecnologías de apoyo (`aria-busy`, `role="status"`) sin mover el foco ([WCAG 4.1.3](01-accesibilidad.md#52-wcag-413-mensajes-de-estado-aa)).
- Evitar el esqueleto de «marco» (solo cabecera y pie): aporta poca información sobre la estructura.

**Matiz.** La evidencia sobre skeletons no es unánime y NN/g los presenta como «una herramienta adicional». Para una carga breve o un elemento pequeño, un spinner local es más simple.

**Fuentes:** [NN/g: Skeleton Screens 101](https://www.nngroup.com/articles/skeleton-screens/)

### 2.2 UX-04: Página de confirmación tras una conversión

- **Prioridad:** Media
- **Naturaleza:** Buena práctica
- **Sectores:** INF ◐ · TIE ● · SUS ● · UGC ◐ · MEN ◐
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ✅ Correcta

**De qué trata.** Tras una compra, alta, solicitud, descarga o envío de formulario relevante, una página de agradecimiento confirma qué ocurrió y qué pasa después. Reduce la ansiedad, evita envíos duplicados y permite medir la conversión de forma fiable con una URL propia.

**Qué hacer**

- Confirmar **qué se ha enviado**, **qué ocurre a continuación** y **cuándo** habrá respuesta.
- Usar **una URL distinta por tipo de conversión** (compra, solicitud, alta, descarga) y redirigir tras el envío para que recargar no repita el formulario.
- Ofrecer **un único siguiente paso** relevante; no convertir la página en un catálogo de ventas cruzadas.
- **No incluir datos personales en la URL ni en sus parámetros** (correo, nombre, teléfono): Google Analytics lo prohíbe en su política de datos personales y se suma al riesgo de privacidad ([PRIV-03](02-privacidad-cookies-y-comunicaciones.md#22-priv-03-no-recopilar-datos-innecesarios)).
- Cargar las etiquetas de medición de la conversión solo con consentimiento ([PRIV-07](02-privacidad-cookies-y-comunicaciones.md#32-priv-07-banner-de-consentimiento-de-cookies)).
- En compras, enviar además la **confirmación del contrato** en un soporte duradero (por ejemplo, correo), conforme a la Directiva 2011/83 (art. 8.7; verifica la transposición).
- Accesibilidad: un `<title>` y un encabezado descriptivos ([WCAG 2.4.2](01-accesibilidad.md#38-wcag-242-titulado-de-páginas-a)); si la confirmación aparece sin recargar la página, anunciarla ([WCAG 4.1.3](01-accesibilidad.md#52-wcag-413-mensajes-de-estado-aa)).

**Fuentes**

- [Google Analytics: evitar enviar datos personales (PII)](https://support.google.com/analytics/answer/6366371)
- [Directiva 2011/83/UE](https://eur-lex.europa.eu/eli/dir/2011/83/oj)
