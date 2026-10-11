# Post-lanzamiento y mantenimiento

> Última verificación: 2026-10-10 · [Volver al README](../README.md)

Lo que se hace **después** de publicar: comprobar que todo funciona de verdad y repetir las revisiones que caducan. Casi todas las medidas de esta categoría son recurrentes; las que ya se describen en otras categorías se enlazan en el calendario en lugar de repetirse. La parte técnica de seguridad, copias y monitorización está en [Seguridad y operación](08-seguridad-y-operacion.md).

<!-- INDICE -->
**Índice**

- [1. Verificación tras la publicación](#1-verificación-tras-la-publicación)
  - [1.1 POST-01: Testear formularios](#11-post-01-testear-formularios)
- [2. Mantenimiento recurrente](#2-mantenimiento-recurrente)
  - [2.1 POST-02: Plan de revisiones periódicas](#21-post-02-plan-de-revisiones-periódicas)
  - [2.2 POST-03: Revisión de enlaces rotos y calidad del contenido](#22-post-03-revisión-de-enlaces-rotos-y-calidad-del-contenido)
<!-- /INDICE -->

## 1. Verificación tras la publicación

### 1.1 POST-01: Testear formularios

- **Prioridad:** Alta
- **Naturaleza:** Buena práctica
- **Sectores:** INF ● · TIE ● · SUS ● · UGC ● · MEN ●
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ✅ Correcta

**De qué trata.** Probar los formularios con el mismo cuidado que el resto de la funcionalidad: validaciones, errores comprensibles, teclado, móvil, campos obligatorios, estados de carga y **envío real**. En formularios con datos personales, además, que la información de privacidad aparezca **en el momento de recogida** y que las casillas funcionen como se espera.

**Qué hacer**

- **Funcional:** envío de extremo a extremo (llega el correo o el registro; no cae en spam), valores límite, campos vacíos, caracteres especiales, doble envío, pérdida de conexión.
- **Validación y errores:** mensajes específicos asociados al campo, sugerencias de corrección y foco en el primer error ([WCAG 3.3.1](01-accesibilidad.md#48-wcag-331-identificación-de-errores-a), [WCAG 3.3.3](01-accesibilidad.md#410-wcag-333-sugerencias-ante-errores-aa)).
- **Accesibilidad:** operables solo con teclado, etiquetas visibles ([WCAG 3.3.2](01-accesibilidad.md#49-wcag-332-etiquetas-o-instrucciones-a)), `autocomplete` correcto ([WCAG 1.3.5](01-accesibilidad.md#211-wcag-135-identificar-el-propósito-de-la-entrada-aa)), estados de envío anunciados ([WCAG 4.1.3](01-accesibilidad.md#52-wcag-413-mensajes-de-estado-aa)), autenticación sin pruebas cognitivas ([WCAG 3.3.8](01-accesibilidad.md#413-wcag-338-autenticación-accesible-mínimo-aa)).
- **Móvil:** tipos de teclado correctos (`type="email"`, `inputmode`), objetivos táctiles suficientes ([WCAG 2.5.8](01-accesibilidad.md#320-wcag-258-tamaño-del-objetivo-mínimo-aa)).
- **Privacidad:** enlace a la política de privacidad en el formulario ([PRIV-02](02-privacidad-cookies-y-comunicaciones.md#21-priv-02-política-de-privacidad)), casillas sin premarcar y separadas por finalidad ([PRIV-04](02-privacidad-cookies-y-comunicaciones.md#23-priv-04-comprobar-los-formularios-de-consentimiento)), sin campos innecesarios ([PRIV-03](02-privacidad-cookies-y-comunicaciones.md#22-priv-03-no-recopilar-datos-innecesarios)) y registro del consentimiento.
- **Pagos:** probar en el entorno de pruebas del proveedor y verificar que el botón indica la obligación de pago ([COM-03](03-consumo-y-comercio.md#13-com-03-renovación-y-cobros-recurrentes-antes-del-pago)).
- Repetir tras cada cambio de plantilla, de proveedor de envío o de política de cookies.

## 2. Mantenimiento recurrente

### 2.1 POST-02: Plan de revisiones periódicas

- **Prioridad:** Alta
- **Naturaleza:** Buena práctica
- **Sectores:** INF ● · TIE ● · SUS ● · UGC ● · MEN ●
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ➕ Añadida

**De qué trata.** Muchas de las medidas del repositorio no se hacen una sola vez: se desvían con el tiempo (un script nuevo, un proveedor distinto, una norma modificada). Este calendario agrupa las revisiones recurrentes de medidas que ya están descritas en otras categorías. Es una síntesis, no una medida de tus listas originales, y las frecuencias son una propuesta orientativa que debes ajustar a tu riesgo y tráfico.

| Cuándo | Qué revisar | Medidas |
|---|---|---|
| **En cada publicación o despliegue** | Formularios y flujos críticos; accesibilidad básica con teclado; Core Web Vitals de laboratorio y presupuesto; que no aparezcan scripts nuevos antes del consentimiento; redirecciones al cambiar URL | [POST-01](09-post-lanzamiento.md#11-post-01-testear-formularios), [WCAG 2.1.1](01-accesibilidad.md#31-wcag-211-teclado-a), [REN-01](06-rendimiento.md#11-ren-01-medir-con-pagespeed-insights), [REN-06](06-rendimiento.md#33-ren-06-presupuesto-de-rendimiento-y-monitorización-con-datos-reales), [PRIV-08](02-privacidad-cookies-y-comunicaciones.md#33-priv-08-auditar-sdks-y-servicios-de-terceros), [SEO-07](05-seo.md#32-seo-07-redirecciones-301-y-páginas-404) |
| **Semanal o continuo** | Alertas de disponibilidad y errores; actualizaciones de seguridad | [SEG-05](08-seguridad-y-operacion.md#22-seg-05-disponibilidad-errores-y-registros), [SEG-03](08-seguridad-y-operacion.md#13-seg-03-actualizaciones-y-análisis-de-vulnerabilidades) |
| **Mensual** | Search Console (indexación, errores, enlaces, experiencia de página); datos de campo de Core Web Vitals; sitemap y robots; enlaces rotos | [SEO-01](05-seo.md#11-seo-01-registrar-la-web-en-search-console), [SEO-03](05-seo.md#13-seo-03-generar-sitemapxml), [SEO-04](05-seo.md#14-seo-04-generar-robotstxt), [REN-02](06-rendimiento.md#12-ren-02-revisar-core-web-vitals), [POST-03](09-post-lanzamiento.md#22-post-03-revisión-de-enlaces-rotos-y-calidad-del-contenido) |
| **Trimestral** | Escaneo de cookies y terceros frente a la política de cookies y al banner; revisión de proveedores y contratos; accesibilidad en plantillas clave y en PDF y terceros; cabeceras de seguridad; revisión de accesos y MFA; prueba de restauración de copias; consultas lentas e índices de la base de datos | [PRIV-06](02-privacidad-cookies-y-comunicaciones.md#31-priv-06-política-de-cookies), [PRIV-07](02-privacidad-cookies-y-comunicaciones.md#32-priv-07-banner-de-consentimiento-de-cookies), [PRIV-08](02-privacidad-cookies-y-comunicaciones.md#33-priv-08-auditar-sdks-y-servicios-de-terceros), [ACC-01](01-accesibilidad.md#11-acc-01-obligaciones-legales-de-accesibilidad), [ACC-03](01-accesibilidad.md#61-acc-03-documentos-descargables-y-contenido-de-terceros), [SEG-01](08-seguridad-y-operacion.md#11-seg-01-https-y-cabeceras-de-seguridad), [SEG-02](08-seguridad-y-operacion.md#12-seg-02-secretos-accesos-y-autenticación-multifactor), [SEG-04](08-seguridad-y-operacion.md#21-seg-04-copias-de-seguridad-y-restauración-probada), [REN-08](06-rendimiento.md#41-ren-08-índices-en-la-base-de-datos), [REN-09](06-rendimiento.md#42-ren-09-evitar-consultas-n1) |
| **Semestral** | Comparar política de privacidad y registro de tratamientos con el tratamiento real; revisar términos, reembolsos, precios mostrados, reseñas y afirmaciones comerciales; información de resolución de litigios | [PRIV-02](02-privacidad-cookies-y-comunicaciones.md#21-priv-02-política-de-privacidad), [PRIV-17](02-privacidad-cookies-y-comunicaciones.md#61-priv-17-registro-de-tratamientos-eipd-y-delegado-de-protección-de-datos), [COM-02](03-consumo-y-comercio.md#12-com-02-términos-y-condiciones-del-servicio), [COM-04](03-consumo-y-comercio.md#14-com-04-política-de-reembolsos-y-desistimiento), [COM-05](03-consumo-y-comercio.md#21-com-05-eliminar-gastos-ocultos), [COM-07](03-consumo-y-comercio.md#23-com-07-eliminar-reseñas-falsas), [COM-08](03-consumo-y-comercio.md#24-com-08-eliminar-afirmaciones-sin-fundamento), [COM-09](03-consumo-y-comercio.md#31-com-09-resolución-de-litigios-adr-y-retirada-del-enlace-a-la-plataforma-odr) |
| **Anual** | Datos del negocio; licencias de fuentes, imágenes, datos y dependencias; procedimiento de derechos y supresión; simulacro de brecha; declaración de accesibilidad; revisión de jurisdicciones | [COM-01](03-consumo-y-comercio.md#11-com-01-datos-del-negocio-en-la-web), [PI-01](04-propiedad-intelectual-y-contenido.md#11-pi-01-licenciar-fuentes-e-imágenes), [PRIV-05](02-privacidad-cookies-y-comunicaciones.md#24-priv-05-proceso-de-eliminación-de-datos-y-ejercicio-de-derechos), [PRIV-18](02-privacidad-cookies-y-comunicaciones.md#62-priv-18-brechas-de-seguridad-e-incidentes), [ACC-02](01-accesibilidad.md#12-acc-02-declaración-de-accesibilidad-y-canal-para-comunicar-barreras), [PRIV-01](02-privacidad-cookies-y-comunicaciones.md#11-priv-01-determinar-qué-jurisdicciones-te-aplican) |
| **Cada 3 años** | Renovar el registro del agente DMCA (caduca a los 3 años; 6 $) | [PI-02](04-propiedad-intelectual-y-contenido.md#12-pi-02-usuarios-que-suben-contenido-avisos-de-infracción-y-agente-dmca) |
| **Ante cualquier cambio** | Nueva herramienta, nuevo proveedor, nueva finalidad o nuevo mercado: actualizar privacidad, cookies, inventario de terceros, registro de tratamientos y consentimientos | [PRIV-02](02-privacidad-cookies-y-comunicaciones.md#21-priv-02-política-de-privacidad), [PRIV-06](02-privacidad-cookies-y-comunicaciones.md#31-priv-06-política-de-cookies), [PRIV-08](02-privacidad-cookies-y-comunicaciones.md#33-priv-08-auditar-sdks-y-servicios-de-terceros), [PRIV-17](02-privacidad-cookies-y-comunicaciones.md#61-priv-17-registro-de-tratamientos-eipd-y-delegado-de-protección-de-datos) |
| **Cuando cambie una norma** | Revisar las fichas afectadas; la lista de cambios pendientes está en [Correcciones y verificación](11-correcciones-y-verificacion.md) | Todas las de privacidad, consumo y accesibilidad |

### 2.2 POST-03: Revisión de enlaces rotos y calidad del contenido

- **Prioridad:** Media
- **Naturaleza:** Buena práctica
- **Sectores:** INF ● · TIE ● · SUS ◐ · UGC ● · MEN ◐
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ➕ Añadida

**De qué trata.** Con el tiempo, los enlaces dejan de funcionar, los datos se quedan obsoletos y los textos legales dejan de reflejar lo que hace el sitio. No es una obligación legal general, pero afecta a la confianza, a la usabilidad y al SEO.

**Qué hacer**

- Revisar enlaces internos y externos rotos con una herramienta de rastreo o los informes de Search Console ([SEO-01](05-seo.md#11-seo-01-registrar-la-web-en-search-console)); corregirlos o redirigirlos ([SEO-07](05-seo.md#32-seo-07-redirecciones-301-y-páginas-404)).
- Comprobar que los datos con vencimiento (precios, plazos, horarios, datos de contacto, textos legales) siguen vigentes; anotar la fecha de la última revisión en los documentos legales.
- Eliminar o actualizar contenido obsoleto y consolidar páginas duplicadas ([SEO-06](05-seo.md#31-seo-06-canónicas-y-contenido-duplicado)).
- Revisar que las imágenes tienen `alt` y que los PDF publicados siguen siendo accesibles ([ACC-03](01-accesibilidad.md#61-acc-03-documentos-descargables-y-contenido-de-terceros)).
