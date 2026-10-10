# Post-lanzamiento y mantenimiento

> Última verificación: 2026-10-10 · [Volver al README](../README.md)

Lo que se hace **después** de publicar: comprobar que todo funciona de verdad, repetir las revisiones que caducan y vigilar los cambios normativos. Casi todas las medidas de esta categoría son recurrentes; las medidas que ya se describen en otras categorías se enlazan en el calendario en lugar de repetirse.

<!-- INDICE -->
**Índice**

- [1. Verificación tras la publicación](#1-verificación-tras-la-publicación)
  - [1.1 POST-01: Testear formularios](#11-post-01-testear-formularios)
- [2. Mantenimiento recurrente](#2-mantenimiento-recurrente)
  - [2.1 POST-02: Plan de revisiones periódicas](#21-post-02-plan-de-revisiones-periódicas)
- [3. Posibles lagunas](#3-posibles-lagunas)
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

**De qué trata.** Muchas de las medidas del repositorio no se hacen una sola vez: se desvían con el tiempo (un script nuevo, un proveedor distinto, una norma modificada). Este calendario agrupa las revisiones recurrentes de medidas que ya están descritas en otras categorías. No es una medida de tus listas originales: es una síntesis, y las frecuencias son una propuesta orientativa que debes ajustar a tu riesgo y tráfico.

| Cuándo | Qué revisar | Medidas |
|---|---|---|
| **En cada publicación o despliegue** | Formularios y flujos críticos; accesibilidad básica con teclado; Core Web Vitals de laboratorio; que no aparezcan scripts nuevos antes del consentimiento | [POST-01](07-post-lanzamiento.md#11-post-01-testear-formularios), [WCAG 2.1.1](01-accesibilidad.md#31-wcag-211-teclado-a), [REN-01](06-rendimiento.md#11-ren-01-medir-con-pagespeed-insights), [PRIV-08](02-privacidad-cookies-y-comunicaciones.md#33-priv-08-auditar-sdks-y-servicios-de-terceros) |
| **Mensual** | Search Console (indexación, errores, enlaces, experiencia de página); datos de campo de Core Web Vitals; sitemap y robots | [SEO-01](05-seo.md#11-seo-01-registrar-la-web-en-search-console), [SEO-03](05-seo.md#13-seo-03-generar-sitemapxml), [SEO-04](05-seo.md#14-seo-04-generar-robotstxt), [REN-02](06-rendimiento.md#12-ren-02-revisar-core-web-vitals) |
| **Trimestral** | Escaneo de cookies y terceros frente a la política de cookies y al banner; revisión de proveedores y contratos; prueba completa de accesibilidad en plantillas clave; revisión de imágenes y rendimiento | [PRIV-06](02-privacidad-cookies-y-comunicaciones.md#31-priv-06-política-de-cookies), [PRIV-07](02-privacidad-cookies-y-comunicaciones.md#32-priv-07-banner-de-consentimiento-de-cookies), [PRIV-08](02-privacidad-cookies-y-comunicaciones.md#33-priv-08-auditar-sdks-y-servicios-de-terceros), [ACC-01](01-accesibilidad.md#11-acc-01-obligaciones-legales-de-accesibilidad), [REN-03](06-rendimiento.md#21-ren-03-comprimir-imágenes-y-usar-formatos-modernos) |
| **Semestral** | Comparar política de privacidad con el tratamiento real; revisar términos, reembolsos y precios mostrados; reseñas y afirmaciones comerciales | [PRIV-02](02-privacidad-cookies-y-comunicaciones.md#21-priv-02-política-de-privacidad), [COM-02](03-consumo-y-comercio.md#12-com-02-términos-y-condiciones-del-servicio), [COM-04](03-consumo-y-comercio.md#14-com-04-política-de-reembolsos-y-desistimiento), [COM-05](03-consumo-y-comercio.md#21-com-05-eliminar-gastos-ocultos), [COM-07](03-consumo-y-comercio.md#23-com-07-eliminar-reseñas-falsas), [COM-08](03-consumo-y-comercio.md#24-com-08-eliminar-afirmaciones-sin-fundamento) |
| **Anual** | Datos del negocio; licencias de fuentes, imágenes y dependencias; procedimiento de derechos y supresión; revisión de jurisdicciones | [COM-01](03-consumo-y-comercio.md#11-com-01-datos-del-negocio-en-la-web), [PI-01](04-propiedad-intelectual-y-contenido.md#11-pi-01-licenciar-fuentes-e-imágenes), [PRIV-05](02-privacidad-cookies-y-comunicaciones.md#24-priv-05-proceso-de-eliminación-de-datos-y-ejercicio-de-derechos), [PRIV-01](02-privacidad-cookies-y-comunicaciones.md#11-priv-01-determinar-qué-jurisdicciones-te-aplican) |
| **Cada 3 años** | Renovar el registro del agente DMCA (caduca a los 3 años; $6) | [PI-02](04-propiedad-intelectual-y-contenido.md#12-pi-02-usuarios-que-suben-contenido-avisos-de-infracción-y-agente-dmca) |
| **Ante cualquier cambio** | Nueva herramienta, nuevo proveedor, nueva finalidad o nuevo mercado: actualizar privacidad, cookies, inventario de terceros y consentimientos | [PRIV-02](02-privacidad-cookies-y-comunicaciones.md#21-priv-02-política-de-privacidad), [PRIV-06](02-privacidad-cookies-y-comunicaciones.md#31-priv-06-política-de-cookies), [PRIV-08](02-privacidad-cookies-y-comunicaciones.md#33-priv-08-auditar-sdks-y-servicios-de-terceros) |
| **Cuando cambie una norma** | Revisar las fichas afectadas; la lista de cambios pendientes está en [Correcciones y verificación](09-correcciones-y-verificacion.md) | Todas las de privacidad, consumo y accesibilidad |

## 3. Posibles lagunas

Medidas relevantes que **no estaban en tus listas** y no se han desarrollado:

- Copias de seguridad y prueba de restauración.
- Monitorización de disponibilidad y alertas de errores (registros, informes de CSP).
- Actualización de dependencias, CMS y complementos; análisis de vulnerabilidades.
- Seguridad del sitio: HTTPS, cabeceras de seguridad, gestión de secretos, autenticación en doble factor.
- Plan de respuesta a incidentes y a brechas de datos.
- Revisión de enlaces rotos y de la calidad del contenido.
