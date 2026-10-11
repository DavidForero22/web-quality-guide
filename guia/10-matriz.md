# Matriz de prioridad, sector y región

> Archivo **generado automáticamente** por `herramientas/actualizar-indices.py`. No lo edites a mano: cambia las fichas de cada medida y vuelve a ejecutar el script. · [Volver al README](../README.md)

Vista transversal de todas las medidas para decidir qué hacer según tu proyecto.

<!-- INDICE -->
**Índice**

- [1. Leyenda](#1-leyenda)
- [2. Matriz de medidas](#2-matriz-de-medidas)
- [3. Criterios WCAG 2.2 A y AA](#3-criterios-wcag-22-a-y-aa)
- [4. Vista por sector](#4-vista-por-sector)
  - [4.1 Informativo, educativo o blog (`INF`)](#41-informativo-educativo-o-blog-inf)
  - [4.2 Tienda online (`TIE`)](#42-tienda-online-tie)
  - [4.3 Suscripción o SaaS (`SUS`)](#43-suscripción-o-saas-sus)
  - [4.4 Contenido de usuarios (`UGC`)](#44-contenido-de-usuarios-ugc)
  - [4.5 Servicios para menores (`MEN`)](#45-servicios-para-menores-men)
- [5. Vista por región](#5-vista-por-región)
  - [5.1 UE y España (`UE/ES`)](#51-ue-y-españa-uees)
  - [5.2 EE. UU. (`EE. UU.`)](#52-ee-uu-ee-uu)
  - [5.3 Reino Unido (`UK`)](#53-reino-unido-uk)
  - [5.4 Latinoamérica (`LATAM`)](#54-latinoamérica-latam)
<!-- /INDICE -->

## 1. Leyenda

| Sectores | |
|---|---|
| `INF` | Informativo, educativo o blog |
| `TIE` | Tienda online |
| `SUS` | Suscripción o SaaS |
| `UGC` | Contenido de usuarios |
| `MEN` | Servicios para menores |

| Regiones | |
|---|---|
| `UE/ES` | UE y España |
| `EE. UU.` | EE. UU. |
| `UK` | Reino Unido |
| `LATAM` | Latinoamérica |

| Símbolo | En un sector | En una región |
|---|---|---|
| ● | Aplica / prioritaria | Obligación directa o más estricta |
| ◐ | Según condiciones | Con matices o por otra norma |
| ○ | No suele aplicar | Sin equivalente relevante |

## 2. Matriz de medidas

Todas las medidas excepto los criterios WCAG (ver la sección siguiente).

| Medida | Prioridad | Naturaleza | INF | TIE | SUS | UGC | MEN | UE/ES | EE. UU. | UK | LATAM |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [ACC-01](01-accesibilidad.md#11-acc-01-obligaciones-legales-de-accesibilidad): Obligaciones legales de accesibilidad | Alta | Obligación legal condicionada | ◐ | ● | ● | ◐ | ◐ | ● | ◐ | ◐ | ◐ |
| [ACC-02](01-accesibilidad.md#12-acc-02-declaración-de-accesibilidad-y-canal-para-comunicar-barreras): Declaración de accesibilidad y canal para comunicar barreras | Media | Obligación legal condicionada | ◐ | ◐ | ◐ | ○ | ◐ | ● | ◐ | ◐ | ○ |
| [ACC-03](01-accesibilidad.md#61-acc-03-documentos-descargables-y-contenido-de-terceros): Documentos descargables y contenido de terceros | Media | Obligación legal condicionada | ● | ◐ | ◐ | ◐ | ◐ | ● | ◐ | ◐ | ◐ |
| [PRIV-01](02-privacidad-cookies-y-comunicaciones.md#11-priv-01-determinar-qué-jurisdicciones-te-aplican): Determinar qué jurisdicciones te aplican | Alta | Obligación legal | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| [PRIV-02](02-privacidad-cookies-y-comunicaciones.md#21-priv-02-política-de-privacidad): Política de privacidad | Alta | Obligación legal | ◐ | ● | ● | ● | ● | ● | ◐ | ● | ● |
| [PRIV-03](02-privacidad-cookies-y-comunicaciones.md#22-priv-03-no-recopilar-datos-innecesarios): No recopilar datos innecesarios | Alta | Obligación legal | ● | ● | ● | ● | ● | ● | ◐ | ● | ● |
| [PRIV-04](02-privacidad-cookies-y-comunicaciones.md#23-priv-04-comprobar-los-formularios-de-consentimiento): Comprobar los formularios de consentimiento | Alta | Obligación legal condicionada | ◐ | ● | ● | ● | ● | ● | ◐ | ● | ● |
| [PRIV-05](02-privacidad-cookies-y-comunicaciones.md#24-priv-05-proceso-de-eliminación-de-datos-y-ejercicio-de-derechos): Proceso de eliminación de datos y ejercicio de derechos | Alta | Obligación legal | ◐ | ● | ● | ● | ● | ● | ◐ | ● | ● |
| [PRIV-06](02-privacidad-cookies-y-comunicaciones.md#31-priv-06-política-de-cookies): Política de cookies | Alta | Obligación legal condicionada | ● | ● | ● | ● | ● | ● | ○ | ● | ◐ |
| [PRIV-07](02-privacidad-cookies-y-comunicaciones.md#32-priv-07-banner-de-consentimiento-de-cookies): Banner de consentimiento de cookies | Alta | Obligación legal condicionada | ● | ● | ● | ● | ● | ● | ◐ | ● | ◐ |
| [PRIV-08](02-privacidad-cookies-y-comunicaciones.md#33-priv-08-auditar-sdks-y-servicios-de-terceros): Auditar SDKs y servicios de terceros | Alta | Obligación legal | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| [PRIV-09](02-privacidad-cookies-y-comunicaciones.md#34-priv-09-cargar-las-fuentes-de-google-desde-tu-propio-servidor): Cargar las fuentes de Google desde tu propio servidor | Media | Buena práctica | ● | ● | ● | ● | ● | ● | ○ | ◐ | ○ |
| [PRIV-10](02-privacidad-cookies-y-comunicaciones.md#35-priv-10-grabación-de-sesiones-session-replay): Grabación de sesiones (session replay) | Alta | Obligación legal condicionada | ◐ | ● | ● | ◐ | ● | ● | ● | ● | ◐ |
| [PRIV-11](02-privacidad-cookies-y-comunicaciones.md#36-priv-11-microsoft-clarity): Microsoft Clarity | Baja | Opcional | ◐ | ◐ | ◐ | ◐ | ○ | ● | ◐ | ● | ◐ |
| [PRIV-12](02-privacidad-cookies-y-comunicaciones.md#37-priv-12-meta-pixel): Meta Pixel | Baja | Opcional | ○ | ◐ | ◐ | ○ | ○ | ● | ◐ | ● | ◐ |
| [PRIV-13](02-privacidad-cookies-y-comunicaciones.md#41-priv-13-no-pedir-la-edad-a-los-usuarios): No pedir la edad a los usuarios | Media | Buena práctica | ◐ | ◐ | ◐ | ● | ● | ● | ● | ● | ● |
| [PRIV-14](02-privacidad-cookies-y-comunicaciones.md#42-priv-14-consentimiento-para-datos-de-menores): Consentimiento para datos de menores | Alta | Obligación legal condicionada | ○ | ○ | ◐ | ◐ | ● | ● | ● | ● | ● |
| [PRIV-15](02-privacidad-cookies-y-comunicaciones.md#51-priv-15-autorización-previa-y-enlace-de-baja-en-el-correo-comercial): Autorización previa y enlace de baja en el correo comercial | Alta | Obligación legal | ◐ | ● | ● | ◐ | ◐ | ● | ◐ | ● | ◐ |
| [PRIV-16](02-privacidad-cookies-y-comunicaciones.md#52-priv-16-cumplimiento-de-can-spam-y-su-multa-por-correo): Cumplimiento de CAN-SPAM y su multa por correo | Media | Obligación legal condicionada | ◐ | ● | ● | ◐ | ◐ | ○ | ● | ○ | ○ |
| [PRIV-17](02-privacidad-cookies-y-comunicaciones.md#61-priv-17-registro-de-tratamientos-eipd-y-delegado-de-protección-de-datos): Registro de tratamientos, EIPD y delegado de protección de datos | Alta | Obligación legal | ◐ | ● | ● | ● | ● | ● | ○ | ● | ◐ |
| [PRIV-18](02-privacidad-cookies-y-comunicaciones.md#62-priv-18-brechas-de-seguridad-e-incidentes): Brechas de seguridad e incidentes | Alta | Obligación legal | ◐ | ● | ● | ● | ● | ● | ● | ● | ● |
| [COM-01](03-consumo-y-comercio.md#11-com-01-datos-del-negocio-en-la-web): Datos del negocio en la web | Alta | Obligación legal | ◐ | ● | ● | ● | ◐ | ● | ○ | ● | ◐ |
| [COM-02](03-consumo-y-comercio.md#12-com-02-términos-y-condiciones-del-servicio): Términos y condiciones del servicio | Alta | Obligación legal condicionada | ○ | ● | ● | ● | ◐ | ● | ◐ | ● | ◐ |
| [COM-03](03-consumo-y-comercio.md#13-com-03-renovación-y-cobros-recurrentes-antes-del-pago): Renovación y cobros recurrentes antes del pago | Alta | Obligación legal | ○ | ◐ | ● | ◐ | ◐ | ● | ● | ● | ◐ |
| [COM-04](03-consumo-y-comercio.md#14-com-04-política-de-reembolsos-y-desistimiento): Política de reembolsos y desistimiento | Alta | Obligación legal | ○ | ● | ● | ◐ | ◐ | ● | ◐ | ● | ● |
| [COM-05](03-consumo-y-comercio.md#21-com-05-eliminar-gastos-ocultos): Eliminar gastos ocultos | Alta | Obligación legal | ○ | ● | ● | ◐ | ◐ | ● | ◐ | ● | ● |
| [COM-06](03-consumo-y-comercio.md#22-com-06-eliminar-patrones-oscuros): Eliminar patrones oscuros | Alta | Obligación legal | ◐ | ● | ● | ● | ● | ● | ◐ | ● | ◐ |
| [COM-07](03-consumo-y-comercio.md#23-com-07-eliminar-reseñas-falsas): Eliminar reseñas falsas | Alta | Obligación legal | ◐ | ● | ◐ | ● | ○ | ● | ● | ● | ◐ |
| [COM-08](03-consumo-y-comercio.md#24-com-08-eliminar-afirmaciones-sin-fundamento): Eliminar afirmaciones sin fundamento | Alta | Obligación legal | ◐ | ● | ● | ○ | ◐ | ● | ● | ● | ● |
| [COM-09](03-consumo-y-comercio.md#31-com-09-resolución-de-litigios-adr-y-retirada-del-enlace-a-la-plataforma-odr): Resolución de litigios (ADR) y retirada del enlace a la plataforma ODR | Media | Obligación legal condicionada | ○ | ● | ● | ◐ | ◐ | ● | ○ | ◐ | ○ |
| [COM-10](03-consumo-y-comercio.md#32-com-10-contenido-y-servicios-digitales-conformidad-y-actualizaciones): Contenido y servicios digitales: conformidad y actualizaciones | Alta | Obligación legal | ○ | ◐ | ● | ◐ | ◐ | ● | ○ | ● | ◐ |
| [PI-01](04-propiedad-intelectual-y-contenido.md#11-pi-01-licenciar-fuentes-e-imágenes): Licenciar fuentes e imágenes | Alta | Obligación legal | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| [PI-02](04-propiedad-intelectual-y-contenido.md#12-pi-02-usuarios-que-suben-contenido-avisos-de-infracción-y-agente-dmca): Usuarios que suben contenido: avisos de infracción y agente DMCA | Media | Obligación legal condicionada | ○ | ◐ | ◐ | ● | ◐ | ● | ● | ● | ◐ |
| [PI-03](04-propiedad-intelectual-y-contenido.md#21-pi-03-política-de-uso-aceptable-y-moderación-de-contenido): Política de uso aceptable y moderación de contenido | Alta | Obligación legal condicionada | ◐ | ◐ | ◐ | ● | ◐ | ● | ◐ | ● | ◐ |
| [PI-04](04-propiedad-intelectual-y-contenido.md#22-pi-04-derechos-de-imagen-de-las-personas): Derechos de imagen de las personas | Alta | Obligación legal | ◐ | ◐ | ○ | ● | ● | ● | ◐ | ◐ | ◐ |
| [SEO-01](05-seo.md#11-seo-01-registrar-la-web-en-search-console): Registrar la web en Search Console | Alta | Buena práctica | ● | ● | ◐ | ● | ◐ | ● | ● | ● | ● |
| [SEO-02](05-seo.md#12-seo-02-solicitar-a-google-que-indexe-la-web): Solicitar a Google que indexe la web | Media | Buena práctica | ● | ● | ◐ | ● | ◐ | ● | ● | ● | ● |
| [SEO-03](05-seo.md#13-seo-03-generar-sitemapxml): Generar sitemap.xml | Media | Buena práctica | ● | ● | ◐ | ● | ◐ | ● | ● | ● | ● |
| [SEO-04](05-seo.md#14-seo-04-generar-robotstxt): Generar robots.txt | Media | Buena práctica | ◐ | ● | ◐ | ● | ◐ | ● | ● | ● | ● |
| [SEO-05](05-seo.md#21-seo-05-títulos-y-descripciones-personalizados): Títulos y descripciones personalizados | Alta | Buena práctica | ● | ● | ◐ | ● | ◐ | ● | ● | ● | ● |
| [SEO-06](05-seo.md#31-seo-06-canónicas-y-contenido-duplicado): Canónicas y contenido duplicado | Media | Buena práctica | ● | ● | ◐ | ● | ◐ | ● | ● | ● | ● |
| [SEO-07](05-seo.md#32-seo-07-redirecciones-301-y-páginas-404): Redirecciones 301 y páginas 404 | Alta | Buena práctica | ● | ● | ◐ | ● | ◐ | ● | ● | ● | ● |
| [SEO-08](05-seo.md#33-seo-08-compatibilidad-móvil-e-indexación-centrada-en-móviles): Compatibilidad móvil e indexación centrada en móviles | Alta | Buena práctica | ● | ● | ◐ | ● | ● | ● | ● | ● | ● |
| [SEO-09](05-seo.md#34-seo-09-datos-estructurados): Datos estructurados | Media | Buena práctica | ◐ | ● | ◐ | ◐ | ◐ | ● | ● | ● | ● |
| [SEO-10](05-seo.md#35-seo-10-hreflang-para-versiones-por-idioma-o-región): hreflang para versiones por idioma o región | Media | Buena práctica | ◐ | ◐ | ◐ | ◐ | ◐ | ● | ● | ● | ● |
| [SEO-11](05-seo.md#36-seo-11-enlazado-interno-y-arquitectura-de-la-información): Enlazado interno y arquitectura de la información | Media | Buena práctica | ● | ● | ◐ | ● | ◐ | ● | ● | ● | ● |
| [SEO-12](05-seo.md#41-seo-12-favicon): Favicon | Media | Buena práctica | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| [SEO-13](05-seo.md#42-seo-13-open-graph-y-vista-previa-al-compartir): Open Graph y vista previa al compartir | Media | Buena práctica | ● | ● | ◐ | ● | ◐ | ● | ● | ● | ● |
| [REN-01](06-rendimiento.md#11-ren-01-medir-con-pagespeed-insights): Medir con PageSpeed Insights | Alta | Buena práctica | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| [REN-02](06-rendimiento.md#12-ren-02-revisar-core-web-vitals): Revisar Core Web Vitals | Alta | Buena práctica | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| [REN-03](06-rendimiento.md#21-ren-03-comprimir-imágenes-y-usar-formatos-modernos): Comprimir imágenes y usar formatos modernos | Alta | Buena práctica | ● | ● | ◐ | ● | ● | ● | ● | ● | ● |
| [REN-04](06-rendimiento.md#31-ren-04-caché-http-cdn-y-compresión): Caché HTTP, CDN y compresión | Alta | Buena práctica | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| [REN-05](06-rendimiento.md#32-ren-05-fuentes-web-y-javascript-de-terceros): Fuentes web y JavaScript de terceros | Media | Buena práctica | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| [REN-06](06-rendimiento.md#33-ren-06-presupuesto-de-rendimiento-y-monitorización-con-datos-reales): Presupuesto de rendimiento y monitorización con datos reales | Media | Buena práctica | ◐ | ● | ● | ● | ◐ | ● | ● | ● | ● |
| [REN-07](06-rendimiento.md#34-ren-07-vídeo-y-contenido-incrustado): Vídeo y contenido incrustado | Media | Buena práctica | ◐ | ◐ | ◐ | ◐ | ◐ | ● | ● | ● | ● |
| [REN-08](06-rendimiento.md#41-ren-08-índices-en-la-base-de-datos): Índices en la base de datos | Alta | Buena práctica | ◐ | ● | ● | ● | ◐ | ● | ● | ● | ● |
| [REN-09](06-rendimiento.md#42-ren-09-evitar-consultas-n1): Evitar consultas N+1 | Alta | Buena práctica | ◐ | ● | ● | ● | ◐ | ● | ● | ● | ● |
| [UX-01](07-diseno-y-experiencia-de-usuario.md#11-ux-01-acción-principal-clara-y-reducción-de-opciones): Acción principal clara y reducción de opciones | Media | Buena práctica | ◐ | ● | ● | ◐ | ◐ | ● | ● | ● | ● |
| [UX-02](07-diseno-y-experiencia-de-usuario.md#12-ux-02-design-tokens): Design tokens | Media | Buena práctica | ◐ | ● | ● | ◐ | ◐ | ● | ● | ● | ● |
| [UX-03](07-diseno-y-experiencia-de-usuario.md#21-ux-03-estados-de-carga-skeletons-spinners-y-barras-de-progreso): Estados de carga: skeletons, spinners y barras de progreso | Baja | Buena práctica | ◐ | ◐ | ● | ◐ | ◐ | ● | ● | ● | ● |
| [UX-04](07-diseno-y-experiencia-de-usuario.md#22-ux-04-página-de-confirmación-tras-una-conversión): Página de confirmación tras una conversión | Media | Buena práctica | ◐ | ● | ● | ◐ | ◐ | ● | ● | ● | ● |
| [SEG-01](08-seguridad-y-operacion.md#11-seg-01-https-y-cabeceras-de-seguridad): HTTPS y cabeceras de seguridad | Alta | Obligación legal condicionada | ● | ● | ● | ● | ● | ● | ◐ | ● | ● |
| [SEG-02](08-seguridad-y-operacion.md#12-seg-02-secretos-accesos-y-autenticación-multifactor): Secretos, accesos y autenticación multifactor | Alta | Buena práctica | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| [SEG-03](08-seguridad-y-operacion.md#13-seg-03-actualizaciones-y-análisis-de-vulnerabilidades): Actualizaciones y análisis de vulnerabilidades | Alta | Buena práctica | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| [SEG-04](08-seguridad-y-operacion.md#21-seg-04-copias-de-seguridad-y-restauración-probada): Copias de seguridad y restauración probada | Alta | Buena práctica | ◐ | ● | ● | ● | ● | ● | ● | ● | ● |
| [SEG-05](08-seguridad-y-operacion.md#22-seg-05-disponibilidad-errores-y-registros): Disponibilidad, errores y registros | Media | Buena práctica | ◐ | ● | ● | ● | ◐ | ● | ● | ● | ● |
| [POST-01](09-post-lanzamiento.md#11-post-01-testear-formularios): Testear formularios | Alta | Buena práctica | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| [POST-02](09-post-lanzamiento.md#21-post-02-plan-de-revisiones-periódicas): Plan de revisiones periódicas | Alta | Buena práctica | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| [POST-03](09-post-lanzamiento.md#22-post-03-revisión-de-enlaces-rotos-y-calidad-del-contenido): Revisión de enlaces rotos y calidad del contenido | Media | Buena práctica | ● | ● | ◐ | ● | ◐ | ● | ● | ● | ● |

## 3. Criterios WCAG 2.2 A y AA

Los 55 criterios comparten sector y región con [ACC-01](01-accesibilidad.md#11-acc-01-obligaciones-legales-de-accesibilidad): obligación directa en la UE para los servicios cubiertos, y referencia técnica habitual en EE. UU., Reino Unido y Latinoamérica. Lo que cambia entre criterios es la prioridad y la condición «aplica si».

- **Prioridad Alta (26):** [WCAG 1.1.1](01-accesibilidad.md#21-wcag-111-contenido-no-textual-a), [WCAG 1.2.2](01-accesibilidad.md#23-wcag-122-subtítulos-pregrabado-a), [WCAG 1.3.1](01-accesibilidad.md#27-wcag-131-información-y-relaciones-a), [WCAG 1.3.2](01-accesibilidad.md#28-wcag-132-secuencia-significativa-a), [WCAG 1.4.1](01-accesibilidad.md#212-wcag-141-uso-del-color-a), [WCAG 1.4.3](01-accesibilidad.md#214-wcag-143-contraste-mínimo-aa), [WCAG 1.4.4](01-accesibilidad.md#215-wcag-144-cambio-de-tamaño-del-texto-aa), [WCAG 1.4.10](01-accesibilidad.md#217-wcag-1410-reflujo-aa), [WCAG 1.4.11](01-accesibilidad.md#218-wcag-1411-contraste-no-textual-aa), [WCAG 2.1.1](01-accesibilidad.md#31-wcag-211-teclado-a), [WCAG 2.1.2](01-accesibilidad.md#32-wcag-212-sin-trampas-para-el-foco-del-teclado-a), [WCAG 2.3.1](01-accesibilidad.md#36-wcag-231-umbral-de-tres-destellos-o-menos-a), [WCAG 2.4.1](01-accesibilidad.md#37-wcag-241-evitar-bloques-a), [WCAG 2.4.2](01-accesibilidad.md#38-wcag-242-titulado-de-páginas-a), [WCAG 2.4.3](01-accesibilidad.md#39-wcag-243-orden-del-foco-a), [WCAG 2.4.4](01-accesibilidad.md#310-wcag-244-propósito-de-los-enlaces-en-contexto-a), [WCAG 2.4.7](01-accesibilidad.md#313-wcag-247-foco-visible-aa), [WCAG 2.4.11](01-accesibilidad.md#314-wcag-2411-foco-no-oculto-mínimo-aa), [WCAG 2.5.8](01-accesibilidad.md#320-wcag-258-tamaño-del-objetivo-mínimo-aa), [WCAG 3.1.1](01-accesibilidad.md#41-wcag-311-idioma-de-la-página-a), [WCAG 3.2.1](01-accesibilidad.md#43-wcag-321-al-recibir-el-foco-a), [WCAG 3.2.2](01-accesibilidad.md#44-wcag-322-al-recibir-entradas-a), [WCAG 3.3.1](01-accesibilidad.md#48-wcag-331-identificación-de-errores-a), [WCAG 3.3.2](01-accesibilidad.md#49-wcag-332-etiquetas-o-instrucciones-a), [WCAG 3.3.8](01-accesibilidad.md#413-wcag-338-autenticación-accesible-mínimo-aa), [WCAG 4.1.2](01-accesibilidad.md#51-wcag-412-nombre-función-valor-a)
- **Prioridad Media (29):** [WCAG 1.2.1](01-accesibilidad.md#22-wcag-121-solo-audio-y-solo-vídeo-pregrabado-a), [WCAG 1.2.3](01-accesibilidad.md#24-wcag-123-audiodescripción-o-alternativa-para-medios-pregrabado-a), [WCAG 1.2.4](01-accesibilidad.md#25-wcag-124-subtítulos-en-directo-aa), [WCAG 1.2.5](01-accesibilidad.md#26-wcag-125-audiodescripción-pregrabado-aa), [WCAG 1.3.3](01-accesibilidad.md#29-wcag-133-características-sensoriales-a), [WCAG 1.3.4](01-accesibilidad.md#210-wcag-134-orientación-aa), [WCAG 1.3.5](01-accesibilidad.md#211-wcag-135-identificar-el-propósito-de-la-entrada-aa), [WCAG 1.4.2](01-accesibilidad.md#213-wcag-142-control-del-audio-a), [WCAG 1.4.5](01-accesibilidad.md#216-wcag-145-imágenes-de-texto-aa), [WCAG 1.4.12](01-accesibilidad.md#219-wcag-1412-espaciado-del-texto-aa), [WCAG 1.4.13](01-accesibilidad.md#220-wcag-1413-contenido-al-pasar-el-puntero-o-recibir-foco-aa), [WCAG 2.1.4](01-accesibilidad.md#33-wcag-214-atajos-de-teclado-de-un-solo-carácter-a), [WCAG 2.2.1](01-accesibilidad.md#34-wcag-221-tiempo-ajustable-a), [WCAG 2.2.2](01-accesibilidad.md#35-wcag-222-pausar-detener-ocultar-a), [WCAG 2.4.5](01-accesibilidad.md#311-wcag-245-múltiples-vías-aa), [WCAG 2.4.6](01-accesibilidad.md#312-wcag-246-encabezados-y-etiquetas-aa), [WCAG 2.5.1](01-accesibilidad.md#315-wcag-251-gestos-del-puntero-a), [WCAG 2.5.2](01-accesibilidad.md#316-wcag-252-cancelación-del-puntero-a), [WCAG 2.5.3](01-accesibilidad.md#317-wcag-253-etiqueta-en-el-nombre-a), [WCAG 2.5.4](01-accesibilidad.md#318-wcag-254-activación-por-movimiento-a), [WCAG 2.5.7](01-accesibilidad.md#319-wcag-257-movimientos-de-arrastre-aa), [WCAG 3.1.2](01-accesibilidad.md#42-wcag-312-idioma-de-las-partes-aa), [WCAG 3.2.3](01-accesibilidad.md#45-wcag-323-navegación-coherente-aa), [WCAG 3.2.4](01-accesibilidad.md#46-wcag-324-identificación-coherente-aa), [WCAG 3.2.6](01-accesibilidad.md#47-wcag-326-ayuda-coherente-a), [WCAG 3.3.3](01-accesibilidad.md#410-wcag-333-sugerencias-ante-errores-aa), [WCAG 3.3.4](01-accesibilidad.md#411-wcag-334-prevención-de-errores-legales-financieros-o-de-datos-aa), [WCAG 3.3.7](01-accesibilidad.md#412-wcag-337-entrada-redundante-a), [WCAG 4.1.3](01-accesibilidad.md#52-wcag-413-mensajes-de-estado-aa)

## 4. Vista por sector

Para cada sector, las medidas que aplican (●) agrupadas por prioridad y las que dependen de condiciones (◐). Los criterios WCAG se añaden a todos los sectores con servicios online.

### 4.1 Informativo, educativo o blog (`INF`)

**Aplican (●)**

- **Prioridad Alta**
  - [PRIV-01](02-privacidad-cookies-y-comunicaciones.md#11-priv-01-determinar-qué-jurisdicciones-te-aplican): Determinar qué jurisdicciones te aplican
  - [PRIV-03](02-privacidad-cookies-y-comunicaciones.md#22-priv-03-no-recopilar-datos-innecesarios): No recopilar datos innecesarios
  - [PRIV-06](02-privacidad-cookies-y-comunicaciones.md#31-priv-06-política-de-cookies): Política de cookies
  - [PRIV-07](02-privacidad-cookies-y-comunicaciones.md#32-priv-07-banner-de-consentimiento-de-cookies): Banner de consentimiento de cookies
  - [PRIV-08](02-privacidad-cookies-y-comunicaciones.md#33-priv-08-auditar-sdks-y-servicios-de-terceros): Auditar SDKs y servicios de terceros
  - [PI-01](04-propiedad-intelectual-y-contenido.md#11-pi-01-licenciar-fuentes-e-imágenes): Licenciar fuentes e imágenes
  - [SEO-01](05-seo.md#11-seo-01-registrar-la-web-en-search-console): Registrar la web en Search Console
  - [SEO-05](05-seo.md#21-seo-05-títulos-y-descripciones-personalizados): Títulos y descripciones personalizados
  - [SEO-07](05-seo.md#32-seo-07-redirecciones-301-y-páginas-404): Redirecciones 301 y páginas 404
  - [SEO-08](05-seo.md#33-seo-08-compatibilidad-móvil-e-indexación-centrada-en-móviles): Compatibilidad móvil e indexación centrada en móviles
  - [REN-01](06-rendimiento.md#11-ren-01-medir-con-pagespeed-insights): Medir con PageSpeed Insights
  - [REN-02](06-rendimiento.md#12-ren-02-revisar-core-web-vitals): Revisar Core Web Vitals
  - [REN-03](06-rendimiento.md#21-ren-03-comprimir-imágenes-y-usar-formatos-modernos): Comprimir imágenes y usar formatos modernos
  - [REN-04](06-rendimiento.md#31-ren-04-caché-http-cdn-y-compresión): Caché HTTP, CDN y compresión
  - [SEG-01](08-seguridad-y-operacion.md#11-seg-01-https-y-cabeceras-de-seguridad): HTTPS y cabeceras de seguridad
  - [SEG-02](08-seguridad-y-operacion.md#12-seg-02-secretos-accesos-y-autenticación-multifactor): Secretos, accesos y autenticación multifactor
  - [SEG-03](08-seguridad-y-operacion.md#13-seg-03-actualizaciones-y-análisis-de-vulnerabilidades): Actualizaciones y análisis de vulnerabilidades
  - [POST-01](09-post-lanzamiento.md#11-post-01-testear-formularios): Testear formularios
  - [POST-02](09-post-lanzamiento.md#21-post-02-plan-de-revisiones-periódicas): Plan de revisiones periódicas
- **Prioridad Media**
  - [ACC-03](01-accesibilidad.md#61-acc-03-documentos-descargables-y-contenido-de-terceros): Documentos descargables y contenido de terceros
  - [PRIV-09](02-privacidad-cookies-y-comunicaciones.md#34-priv-09-cargar-las-fuentes-de-google-desde-tu-propio-servidor): Cargar las fuentes de Google desde tu propio servidor
  - [SEO-02](05-seo.md#12-seo-02-solicitar-a-google-que-indexe-la-web): Solicitar a Google que indexe la web
  - [SEO-03](05-seo.md#13-seo-03-generar-sitemapxml): Generar sitemap.xml
  - [SEO-06](05-seo.md#31-seo-06-canónicas-y-contenido-duplicado): Canónicas y contenido duplicado
  - [SEO-11](05-seo.md#36-seo-11-enlazado-interno-y-arquitectura-de-la-información): Enlazado interno y arquitectura de la información
  - [SEO-12](05-seo.md#41-seo-12-favicon): Favicon
  - [SEO-13](05-seo.md#42-seo-13-open-graph-y-vista-previa-al-compartir): Open Graph y vista previa al compartir
  - [REN-05](06-rendimiento.md#32-ren-05-fuentes-web-y-javascript-de-terceros): Fuentes web y JavaScript de terceros
  - [POST-03](09-post-lanzamiento.md#22-post-03-revisión-de-enlaces-rotos-y-calidad-del-contenido): Revisión de enlaces rotos y calidad del contenido

**Según condiciones (◐)**

- [ACC-01](01-accesibilidad.md#11-acc-01-obligaciones-legales-de-accesibilidad): Obligaciones legales de accesibilidad
- [ACC-02](01-accesibilidad.md#12-acc-02-declaración-de-accesibilidad-y-canal-para-comunicar-barreras): Declaración de accesibilidad y canal para comunicar barreras
- [PRIV-02](02-privacidad-cookies-y-comunicaciones.md#21-priv-02-política-de-privacidad): Política de privacidad
- [PRIV-04](02-privacidad-cookies-y-comunicaciones.md#23-priv-04-comprobar-los-formularios-de-consentimiento): Comprobar los formularios de consentimiento
- [PRIV-05](02-privacidad-cookies-y-comunicaciones.md#24-priv-05-proceso-de-eliminación-de-datos-y-ejercicio-de-derechos): Proceso de eliminación de datos y ejercicio de derechos
- [PRIV-10](02-privacidad-cookies-y-comunicaciones.md#35-priv-10-grabación-de-sesiones-session-replay): Grabación de sesiones (session replay)
- [PRIV-11](02-privacidad-cookies-y-comunicaciones.md#36-priv-11-microsoft-clarity): Microsoft Clarity
- [PRIV-13](02-privacidad-cookies-y-comunicaciones.md#41-priv-13-no-pedir-la-edad-a-los-usuarios): No pedir la edad a los usuarios
- [PRIV-15](02-privacidad-cookies-y-comunicaciones.md#51-priv-15-autorización-previa-y-enlace-de-baja-en-el-correo-comercial): Autorización previa y enlace de baja en el correo comercial
- [PRIV-16](02-privacidad-cookies-y-comunicaciones.md#52-priv-16-cumplimiento-de-can-spam-y-su-multa-por-correo): Cumplimiento de CAN-SPAM y su multa por correo
- [PRIV-17](02-privacidad-cookies-y-comunicaciones.md#61-priv-17-registro-de-tratamientos-eipd-y-delegado-de-protección-de-datos): Registro de tratamientos, EIPD y delegado de protección de datos
- [PRIV-18](02-privacidad-cookies-y-comunicaciones.md#62-priv-18-brechas-de-seguridad-e-incidentes): Brechas de seguridad e incidentes
- [COM-01](03-consumo-y-comercio.md#11-com-01-datos-del-negocio-en-la-web): Datos del negocio en la web
- [COM-06](03-consumo-y-comercio.md#22-com-06-eliminar-patrones-oscuros): Eliminar patrones oscuros
- [COM-07](03-consumo-y-comercio.md#23-com-07-eliminar-reseñas-falsas): Eliminar reseñas falsas
- [COM-08](03-consumo-y-comercio.md#24-com-08-eliminar-afirmaciones-sin-fundamento): Eliminar afirmaciones sin fundamento
- [PI-03](04-propiedad-intelectual-y-contenido.md#21-pi-03-política-de-uso-aceptable-y-moderación-de-contenido): Política de uso aceptable y moderación de contenido
- [PI-04](04-propiedad-intelectual-y-contenido.md#22-pi-04-derechos-de-imagen-de-las-personas): Derechos de imagen de las personas
- [SEO-04](05-seo.md#14-seo-04-generar-robotstxt): Generar robots.txt
- [SEO-09](05-seo.md#34-seo-09-datos-estructurados): Datos estructurados
- [SEO-10](05-seo.md#35-seo-10-hreflang-para-versiones-por-idioma-o-región): hreflang para versiones por idioma o región
- [REN-06](06-rendimiento.md#33-ren-06-presupuesto-de-rendimiento-y-monitorización-con-datos-reales): Presupuesto de rendimiento y monitorización con datos reales
- [REN-07](06-rendimiento.md#34-ren-07-vídeo-y-contenido-incrustado): Vídeo y contenido incrustado
- [REN-08](06-rendimiento.md#41-ren-08-índices-en-la-base-de-datos): Índices en la base de datos
- [REN-09](06-rendimiento.md#42-ren-09-evitar-consultas-n1): Evitar consultas N+1
- [UX-01](07-diseno-y-experiencia-de-usuario.md#11-ux-01-acción-principal-clara-y-reducción-de-opciones): Acción principal clara y reducción de opciones
- [UX-02](07-diseno-y-experiencia-de-usuario.md#12-ux-02-design-tokens): Design tokens
- [UX-03](07-diseno-y-experiencia-de-usuario.md#21-ux-03-estados-de-carga-skeletons-spinners-y-barras-de-progreso): Estados de carga: skeletons, spinners y barras de progreso
- [UX-04](07-diseno-y-experiencia-de-usuario.md#22-ux-04-página-de-confirmación-tras-una-conversión): Página de confirmación tras una conversión
- [SEG-04](08-seguridad-y-operacion.md#21-seg-04-copias-de-seguridad-y-restauración-probada): Copias de seguridad y restauración probada
- [SEG-05](08-seguridad-y-operacion.md#22-seg-05-disponibilidad-errores-y-registros): Disponibilidad, errores y registros

### 4.2 Tienda online (`TIE`)

**Aplican (●)**

- **Prioridad Alta**
  - [ACC-01](01-accesibilidad.md#11-acc-01-obligaciones-legales-de-accesibilidad): Obligaciones legales de accesibilidad
  - [PRIV-01](02-privacidad-cookies-y-comunicaciones.md#11-priv-01-determinar-qué-jurisdicciones-te-aplican): Determinar qué jurisdicciones te aplican
  - [PRIV-02](02-privacidad-cookies-y-comunicaciones.md#21-priv-02-política-de-privacidad): Política de privacidad
  - [PRIV-03](02-privacidad-cookies-y-comunicaciones.md#22-priv-03-no-recopilar-datos-innecesarios): No recopilar datos innecesarios
  - [PRIV-04](02-privacidad-cookies-y-comunicaciones.md#23-priv-04-comprobar-los-formularios-de-consentimiento): Comprobar los formularios de consentimiento
  - [PRIV-05](02-privacidad-cookies-y-comunicaciones.md#24-priv-05-proceso-de-eliminación-de-datos-y-ejercicio-de-derechos): Proceso de eliminación de datos y ejercicio de derechos
  - [PRIV-06](02-privacidad-cookies-y-comunicaciones.md#31-priv-06-política-de-cookies): Política de cookies
  - [PRIV-07](02-privacidad-cookies-y-comunicaciones.md#32-priv-07-banner-de-consentimiento-de-cookies): Banner de consentimiento de cookies
  - [PRIV-08](02-privacidad-cookies-y-comunicaciones.md#33-priv-08-auditar-sdks-y-servicios-de-terceros): Auditar SDKs y servicios de terceros
  - [PRIV-10](02-privacidad-cookies-y-comunicaciones.md#35-priv-10-grabación-de-sesiones-session-replay): Grabación de sesiones (session replay)
  - [PRIV-15](02-privacidad-cookies-y-comunicaciones.md#51-priv-15-autorización-previa-y-enlace-de-baja-en-el-correo-comercial): Autorización previa y enlace de baja en el correo comercial
  - [PRIV-17](02-privacidad-cookies-y-comunicaciones.md#61-priv-17-registro-de-tratamientos-eipd-y-delegado-de-protección-de-datos): Registro de tratamientos, EIPD y delegado de protección de datos
  - [PRIV-18](02-privacidad-cookies-y-comunicaciones.md#62-priv-18-brechas-de-seguridad-e-incidentes): Brechas de seguridad e incidentes
  - [COM-01](03-consumo-y-comercio.md#11-com-01-datos-del-negocio-en-la-web): Datos del negocio en la web
  - [COM-02](03-consumo-y-comercio.md#12-com-02-términos-y-condiciones-del-servicio): Términos y condiciones del servicio
  - [COM-04](03-consumo-y-comercio.md#14-com-04-política-de-reembolsos-y-desistimiento): Política de reembolsos y desistimiento
  - [COM-05](03-consumo-y-comercio.md#21-com-05-eliminar-gastos-ocultos): Eliminar gastos ocultos
  - [COM-06](03-consumo-y-comercio.md#22-com-06-eliminar-patrones-oscuros): Eliminar patrones oscuros
  - [COM-07](03-consumo-y-comercio.md#23-com-07-eliminar-reseñas-falsas): Eliminar reseñas falsas
  - [COM-08](03-consumo-y-comercio.md#24-com-08-eliminar-afirmaciones-sin-fundamento): Eliminar afirmaciones sin fundamento
  - [PI-01](04-propiedad-intelectual-y-contenido.md#11-pi-01-licenciar-fuentes-e-imágenes): Licenciar fuentes e imágenes
  - [SEO-01](05-seo.md#11-seo-01-registrar-la-web-en-search-console): Registrar la web en Search Console
  - [SEO-05](05-seo.md#21-seo-05-títulos-y-descripciones-personalizados): Títulos y descripciones personalizados
  - [SEO-07](05-seo.md#32-seo-07-redirecciones-301-y-páginas-404): Redirecciones 301 y páginas 404
  - [SEO-08](05-seo.md#33-seo-08-compatibilidad-móvil-e-indexación-centrada-en-móviles): Compatibilidad móvil e indexación centrada en móviles
  - [REN-01](06-rendimiento.md#11-ren-01-medir-con-pagespeed-insights): Medir con PageSpeed Insights
  - [REN-02](06-rendimiento.md#12-ren-02-revisar-core-web-vitals): Revisar Core Web Vitals
  - [REN-03](06-rendimiento.md#21-ren-03-comprimir-imágenes-y-usar-formatos-modernos): Comprimir imágenes y usar formatos modernos
  - [REN-04](06-rendimiento.md#31-ren-04-caché-http-cdn-y-compresión): Caché HTTP, CDN y compresión
  - [REN-08](06-rendimiento.md#41-ren-08-índices-en-la-base-de-datos): Índices en la base de datos
  - [REN-09](06-rendimiento.md#42-ren-09-evitar-consultas-n1): Evitar consultas N+1
  - [SEG-01](08-seguridad-y-operacion.md#11-seg-01-https-y-cabeceras-de-seguridad): HTTPS y cabeceras de seguridad
  - [SEG-02](08-seguridad-y-operacion.md#12-seg-02-secretos-accesos-y-autenticación-multifactor): Secretos, accesos y autenticación multifactor
  - [SEG-03](08-seguridad-y-operacion.md#13-seg-03-actualizaciones-y-análisis-de-vulnerabilidades): Actualizaciones y análisis de vulnerabilidades
  - [SEG-04](08-seguridad-y-operacion.md#21-seg-04-copias-de-seguridad-y-restauración-probada): Copias de seguridad y restauración probada
  - [POST-01](09-post-lanzamiento.md#11-post-01-testear-formularios): Testear formularios
  - [POST-02](09-post-lanzamiento.md#21-post-02-plan-de-revisiones-periódicas): Plan de revisiones periódicas
- **Prioridad Media**
  - [PRIV-09](02-privacidad-cookies-y-comunicaciones.md#34-priv-09-cargar-las-fuentes-de-google-desde-tu-propio-servidor): Cargar las fuentes de Google desde tu propio servidor
  - [PRIV-16](02-privacidad-cookies-y-comunicaciones.md#52-priv-16-cumplimiento-de-can-spam-y-su-multa-por-correo): Cumplimiento de CAN-SPAM y su multa por correo
  - [COM-09](03-consumo-y-comercio.md#31-com-09-resolución-de-litigios-adr-y-retirada-del-enlace-a-la-plataforma-odr): Resolución de litigios (ADR) y retirada del enlace a la plataforma ODR
  - [SEO-02](05-seo.md#12-seo-02-solicitar-a-google-que-indexe-la-web): Solicitar a Google que indexe la web
  - [SEO-03](05-seo.md#13-seo-03-generar-sitemapxml): Generar sitemap.xml
  - [SEO-04](05-seo.md#14-seo-04-generar-robotstxt): Generar robots.txt
  - [SEO-06](05-seo.md#31-seo-06-canónicas-y-contenido-duplicado): Canónicas y contenido duplicado
  - [SEO-09](05-seo.md#34-seo-09-datos-estructurados): Datos estructurados
  - [SEO-11](05-seo.md#36-seo-11-enlazado-interno-y-arquitectura-de-la-información): Enlazado interno y arquitectura de la información
  - [SEO-12](05-seo.md#41-seo-12-favicon): Favicon
  - [SEO-13](05-seo.md#42-seo-13-open-graph-y-vista-previa-al-compartir): Open Graph y vista previa al compartir
  - [REN-05](06-rendimiento.md#32-ren-05-fuentes-web-y-javascript-de-terceros): Fuentes web y JavaScript de terceros
  - [REN-06](06-rendimiento.md#33-ren-06-presupuesto-de-rendimiento-y-monitorización-con-datos-reales): Presupuesto de rendimiento y monitorización con datos reales
  - [UX-01](07-diseno-y-experiencia-de-usuario.md#11-ux-01-acción-principal-clara-y-reducción-de-opciones): Acción principal clara y reducción de opciones
  - [UX-02](07-diseno-y-experiencia-de-usuario.md#12-ux-02-design-tokens): Design tokens
  - [UX-04](07-diseno-y-experiencia-de-usuario.md#22-ux-04-página-de-confirmación-tras-una-conversión): Página de confirmación tras una conversión
  - [SEG-05](08-seguridad-y-operacion.md#22-seg-05-disponibilidad-errores-y-registros): Disponibilidad, errores y registros
  - [POST-03](09-post-lanzamiento.md#22-post-03-revisión-de-enlaces-rotos-y-calidad-del-contenido): Revisión de enlaces rotos y calidad del contenido

**Según condiciones (◐)**

- [ACC-02](01-accesibilidad.md#12-acc-02-declaración-de-accesibilidad-y-canal-para-comunicar-barreras): Declaración de accesibilidad y canal para comunicar barreras
- [ACC-03](01-accesibilidad.md#61-acc-03-documentos-descargables-y-contenido-de-terceros): Documentos descargables y contenido de terceros
- [PRIV-11](02-privacidad-cookies-y-comunicaciones.md#36-priv-11-microsoft-clarity): Microsoft Clarity
- [PRIV-12](02-privacidad-cookies-y-comunicaciones.md#37-priv-12-meta-pixel): Meta Pixel
- [PRIV-13](02-privacidad-cookies-y-comunicaciones.md#41-priv-13-no-pedir-la-edad-a-los-usuarios): No pedir la edad a los usuarios
- [COM-03](03-consumo-y-comercio.md#13-com-03-renovación-y-cobros-recurrentes-antes-del-pago): Renovación y cobros recurrentes antes del pago
- [COM-10](03-consumo-y-comercio.md#32-com-10-contenido-y-servicios-digitales-conformidad-y-actualizaciones): Contenido y servicios digitales: conformidad y actualizaciones
- [PI-02](04-propiedad-intelectual-y-contenido.md#12-pi-02-usuarios-que-suben-contenido-avisos-de-infracción-y-agente-dmca): Usuarios que suben contenido: avisos de infracción y agente DMCA
- [PI-03](04-propiedad-intelectual-y-contenido.md#21-pi-03-política-de-uso-aceptable-y-moderación-de-contenido): Política de uso aceptable y moderación de contenido
- [PI-04](04-propiedad-intelectual-y-contenido.md#22-pi-04-derechos-de-imagen-de-las-personas): Derechos de imagen de las personas
- [SEO-10](05-seo.md#35-seo-10-hreflang-para-versiones-por-idioma-o-región): hreflang para versiones por idioma o región
- [REN-07](06-rendimiento.md#34-ren-07-vídeo-y-contenido-incrustado): Vídeo y contenido incrustado
- [UX-03](07-diseno-y-experiencia-de-usuario.md#21-ux-03-estados-de-carga-skeletons-spinners-y-barras-de-progreso): Estados de carga: skeletons, spinners y barras de progreso

### 4.3 Suscripción o SaaS (`SUS`)

**Aplican (●)**

- **Prioridad Alta**
  - [ACC-01](01-accesibilidad.md#11-acc-01-obligaciones-legales-de-accesibilidad): Obligaciones legales de accesibilidad
  - [PRIV-01](02-privacidad-cookies-y-comunicaciones.md#11-priv-01-determinar-qué-jurisdicciones-te-aplican): Determinar qué jurisdicciones te aplican
  - [PRIV-02](02-privacidad-cookies-y-comunicaciones.md#21-priv-02-política-de-privacidad): Política de privacidad
  - [PRIV-03](02-privacidad-cookies-y-comunicaciones.md#22-priv-03-no-recopilar-datos-innecesarios): No recopilar datos innecesarios
  - [PRIV-04](02-privacidad-cookies-y-comunicaciones.md#23-priv-04-comprobar-los-formularios-de-consentimiento): Comprobar los formularios de consentimiento
  - [PRIV-05](02-privacidad-cookies-y-comunicaciones.md#24-priv-05-proceso-de-eliminación-de-datos-y-ejercicio-de-derechos): Proceso de eliminación de datos y ejercicio de derechos
  - [PRIV-06](02-privacidad-cookies-y-comunicaciones.md#31-priv-06-política-de-cookies): Política de cookies
  - [PRIV-07](02-privacidad-cookies-y-comunicaciones.md#32-priv-07-banner-de-consentimiento-de-cookies): Banner de consentimiento de cookies
  - [PRIV-08](02-privacidad-cookies-y-comunicaciones.md#33-priv-08-auditar-sdks-y-servicios-de-terceros): Auditar SDKs y servicios de terceros
  - [PRIV-10](02-privacidad-cookies-y-comunicaciones.md#35-priv-10-grabación-de-sesiones-session-replay): Grabación de sesiones (session replay)
  - [PRIV-15](02-privacidad-cookies-y-comunicaciones.md#51-priv-15-autorización-previa-y-enlace-de-baja-en-el-correo-comercial): Autorización previa y enlace de baja en el correo comercial
  - [PRIV-17](02-privacidad-cookies-y-comunicaciones.md#61-priv-17-registro-de-tratamientos-eipd-y-delegado-de-protección-de-datos): Registro de tratamientos, EIPD y delegado de protección de datos
  - [PRIV-18](02-privacidad-cookies-y-comunicaciones.md#62-priv-18-brechas-de-seguridad-e-incidentes): Brechas de seguridad e incidentes
  - [COM-01](03-consumo-y-comercio.md#11-com-01-datos-del-negocio-en-la-web): Datos del negocio en la web
  - [COM-02](03-consumo-y-comercio.md#12-com-02-términos-y-condiciones-del-servicio): Términos y condiciones del servicio
  - [COM-03](03-consumo-y-comercio.md#13-com-03-renovación-y-cobros-recurrentes-antes-del-pago): Renovación y cobros recurrentes antes del pago
  - [COM-04](03-consumo-y-comercio.md#14-com-04-política-de-reembolsos-y-desistimiento): Política de reembolsos y desistimiento
  - [COM-05](03-consumo-y-comercio.md#21-com-05-eliminar-gastos-ocultos): Eliminar gastos ocultos
  - [COM-06](03-consumo-y-comercio.md#22-com-06-eliminar-patrones-oscuros): Eliminar patrones oscuros
  - [COM-08](03-consumo-y-comercio.md#24-com-08-eliminar-afirmaciones-sin-fundamento): Eliminar afirmaciones sin fundamento
  - [COM-10](03-consumo-y-comercio.md#32-com-10-contenido-y-servicios-digitales-conformidad-y-actualizaciones): Contenido y servicios digitales: conformidad y actualizaciones
  - [PI-01](04-propiedad-intelectual-y-contenido.md#11-pi-01-licenciar-fuentes-e-imágenes): Licenciar fuentes e imágenes
  - [REN-01](06-rendimiento.md#11-ren-01-medir-con-pagespeed-insights): Medir con PageSpeed Insights
  - [REN-02](06-rendimiento.md#12-ren-02-revisar-core-web-vitals): Revisar Core Web Vitals
  - [REN-04](06-rendimiento.md#31-ren-04-caché-http-cdn-y-compresión): Caché HTTP, CDN y compresión
  - [REN-08](06-rendimiento.md#41-ren-08-índices-en-la-base-de-datos): Índices en la base de datos
  - [REN-09](06-rendimiento.md#42-ren-09-evitar-consultas-n1): Evitar consultas N+1
  - [SEG-01](08-seguridad-y-operacion.md#11-seg-01-https-y-cabeceras-de-seguridad): HTTPS y cabeceras de seguridad
  - [SEG-02](08-seguridad-y-operacion.md#12-seg-02-secretos-accesos-y-autenticación-multifactor): Secretos, accesos y autenticación multifactor
  - [SEG-03](08-seguridad-y-operacion.md#13-seg-03-actualizaciones-y-análisis-de-vulnerabilidades): Actualizaciones y análisis de vulnerabilidades
  - [SEG-04](08-seguridad-y-operacion.md#21-seg-04-copias-de-seguridad-y-restauración-probada): Copias de seguridad y restauración probada
  - [POST-01](09-post-lanzamiento.md#11-post-01-testear-formularios): Testear formularios
  - [POST-02](09-post-lanzamiento.md#21-post-02-plan-de-revisiones-periódicas): Plan de revisiones periódicas
- **Prioridad Media**
  - [PRIV-09](02-privacidad-cookies-y-comunicaciones.md#34-priv-09-cargar-las-fuentes-de-google-desde-tu-propio-servidor): Cargar las fuentes de Google desde tu propio servidor
  - [PRIV-16](02-privacidad-cookies-y-comunicaciones.md#52-priv-16-cumplimiento-de-can-spam-y-su-multa-por-correo): Cumplimiento de CAN-SPAM y su multa por correo
  - [COM-09](03-consumo-y-comercio.md#31-com-09-resolución-de-litigios-adr-y-retirada-del-enlace-a-la-plataforma-odr): Resolución de litigios (ADR) y retirada del enlace a la plataforma ODR
  - [SEO-12](05-seo.md#41-seo-12-favicon): Favicon
  - [REN-05](06-rendimiento.md#32-ren-05-fuentes-web-y-javascript-de-terceros): Fuentes web y JavaScript de terceros
  - [REN-06](06-rendimiento.md#33-ren-06-presupuesto-de-rendimiento-y-monitorización-con-datos-reales): Presupuesto de rendimiento y monitorización con datos reales
  - [UX-01](07-diseno-y-experiencia-de-usuario.md#11-ux-01-acción-principal-clara-y-reducción-de-opciones): Acción principal clara y reducción de opciones
  - [UX-02](07-diseno-y-experiencia-de-usuario.md#12-ux-02-design-tokens): Design tokens
  - [UX-04](07-diseno-y-experiencia-de-usuario.md#22-ux-04-página-de-confirmación-tras-una-conversión): Página de confirmación tras una conversión
  - [SEG-05](08-seguridad-y-operacion.md#22-seg-05-disponibilidad-errores-y-registros): Disponibilidad, errores y registros
- **Prioridad Baja**
  - [UX-03](07-diseno-y-experiencia-de-usuario.md#21-ux-03-estados-de-carga-skeletons-spinners-y-barras-de-progreso): Estados de carga: skeletons, spinners y barras de progreso

**Según condiciones (◐)**

- [ACC-02](01-accesibilidad.md#12-acc-02-declaración-de-accesibilidad-y-canal-para-comunicar-barreras): Declaración de accesibilidad y canal para comunicar barreras
- [ACC-03](01-accesibilidad.md#61-acc-03-documentos-descargables-y-contenido-de-terceros): Documentos descargables y contenido de terceros
- [PRIV-11](02-privacidad-cookies-y-comunicaciones.md#36-priv-11-microsoft-clarity): Microsoft Clarity
- [PRIV-12](02-privacidad-cookies-y-comunicaciones.md#37-priv-12-meta-pixel): Meta Pixel
- [PRIV-13](02-privacidad-cookies-y-comunicaciones.md#41-priv-13-no-pedir-la-edad-a-los-usuarios): No pedir la edad a los usuarios
- [PRIV-14](02-privacidad-cookies-y-comunicaciones.md#42-priv-14-consentimiento-para-datos-de-menores): Consentimiento para datos de menores
- [COM-07](03-consumo-y-comercio.md#23-com-07-eliminar-reseñas-falsas): Eliminar reseñas falsas
- [PI-02](04-propiedad-intelectual-y-contenido.md#12-pi-02-usuarios-que-suben-contenido-avisos-de-infracción-y-agente-dmca): Usuarios que suben contenido: avisos de infracción y agente DMCA
- [PI-03](04-propiedad-intelectual-y-contenido.md#21-pi-03-política-de-uso-aceptable-y-moderación-de-contenido): Política de uso aceptable y moderación de contenido
- [SEO-01](05-seo.md#11-seo-01-registrar-la-web-en-search-console): Registrar la web en Search Console
- [SEO-02](05-seo.md#12-seo-02-solicitar-a-google-que-indexe-la-web): Solicitar a Google que indexe la web
- [SEO-03](05-seo.md#13-seo-03-generar-sitemapxml): Generar sitemap.xml
- [SEO-04](05-seo.md#14-seo-04-generar-robotstxt): Generar robots.txt
- [SEO-05](05-seo.md#21-seo-05-títulos-y-descripciones-personalizados): Títulos y descripciones personalizados
- [SEO-06](05-seo.md#31-seo-06-canónicas-y-contenido-duplicado): Canónicas y contenido duplicado
- [SEO-07](05-seo.md#32-seo-07-redirecciones-301-y-páginas-404): Redirecciones 301 y páginas 404
- [SEO-08](05-seo.md#33-seo-08-compatibilidad-móvil-e-indexación-centrada-en-móviles): Compatibilidad móvil e indexación centrada en móviles
- [SEO-09](05-seo.md#34-seo-09-datos-estructurados): Datos estructurados
- [SEO-10](05-seo.md#35-seo-10-hreflang-para-versiones-por-idioma-o-región): hreflang para versiones por idioma o región
- [SEO-11](05-seo.md#36-seo-11-enlazado-interno-y-arquitectura-de-la-información): Enlazado interno y arquitectura de la información
- [SEO-13](05-seo.md#42-seo-13-open-graph-y-vista-previa-al-compartir): Open Graph y vista previa al compartir
- [REN-03](06-rendimiento.md#21-ren-03-comprimir-imágenes-y-usar-formatos-modernos): Comprimir imágenes y usar formatos modernos
- [REN-07](06-rendimiento.md#34-ren-07-vídeo-y-contenido-incrustado): Vídeo y contenido incrustado
- [POST-03](09-post-lanzamiento.md#22-post-03-revisión-de-enlaces-rotos-y-calidad-del-contenido): Revisión de enlaces rotos y calidad del contenido

### 4.4 Contenido de usuarios (`UGC`)

**Aplican (●)**

- **Prioridad Alta**
  - [PRIV-01](02-privacidad-cookies-y-comunicaciones.md#11-priv-01-determinar-qué-jurisdicciones-te-aplican): Determinar qué jurisdicciones te aplican
  - [PRIV-02](02-privacidad-cookies-y-comunicaciones.md#21-priv-02-política-de-privacidad): Política de privacidad
  - [PRIV-03](02-privacidad-cookies-y-comunicaciones.md#22-priv-03-no-recopilar-datos-innecesarios): No recopilar datos innecesarios
  - [PRIV-04](02-privacidad-cookies-y-comunicaciones.md#23-priv-04-comprobar-los-formularios-de-consentimiento): Comprobar los formularios de consentimiento
  - [PRIV-05](02-privacidad-cookies-y-comunicaciones.md#24-priv-05-proceso-de-eliminación-de-datos-y-ejercicio-de-derechos): Proceso de eliminación de datos y ejercicio de derechos
  - [PRIV-06](02-privacidad-cookies-y-comunicaciones.md#31-priv-06-política-de-cookies): Política de cookies
  - [PRIV-07](02-privacidad-cookies-y-comunicaciones.md#32-priv-07-banner-de-consentimiento-de-cookies): Banner de consentimiento de cookies
  - [PRIV-08](02-privacidad-cookies-y-comunicaciones.md#33-priv-08-auditar-sdks-y-servicios-de-terceros): Auditar SDKs y servicios de terceros
  - [PRIV-17](02-privacidad-cookies-y-comunicaciones.md#61-priv-17-registro-de-tratamientos-eipd-y-delegado-de-protección-de-datos): Registro de tratamientos, EIPD y delegado de protección de datos
  - [PRIV-18](02-privacidad-cookies-y-comunicaciones.md#62-priv-18-brechas-de-seguridad-e-incidentes): Brechas de seguridad e incidentes
  - [COM-01](03-consumo-y-comercio.md#11-com-01-datos-del-negocio-en-la-web): Datos del negocio en la web
  - [COM-02](03-consumo-y-comercio.md#12-com-02-términos-y-condiciones-del-servicio): Términos y condiciones del servicio
  - [COM-06](03-consumo-y-comercio.md#22-com-06-eliminar-patrones-oscuros): Eliminar patrones oscuros
  - [COM-07](03-consumo-y-comercio.md#23-com-07-eliminar-reseñas-falsas): Eliminar reseñas falsas
  - [PI-01](04-propiedad-intelectual-y-contenido.md#11-pi-01-licenciar-fuentes-e-imágenes): Licenciar fuentes e imágenes
  - [PI-03](04-propiedad-intelectual-y-contenido.md#21-pi-03-política-de-uso-aceptable-y-moderación-de-contenido): Política de uso aceptable y moderación de contenido
  - [PI-04](04-propiedad-intelectual-y-contenido.md#22-pi-04-derechos-de-imagen-de-las-personas): Derechos de imagen de las personas
  - [SEO-01](05-seo.md#11-seo-01-registrar-la-web-en-search-console): Registrar la web en Search Console
  - [SEO-05](05-seo.md#21-seo-05-títulos-y-descripciones-personalizados): Títulos y descripciones personalizados
  - [SEO-07](05-seo.md#32-seo-07-redirecciones-301-y-páginas-404): Redirecciones 301 y páginas 404
  - [SEO-08](05-seo.md#33-seo-08-compatibilidad-móvil-e-indexación-centrada-en-móviles): Compatibilidad móvil e indexación centrada en móviles
  - [REN-01](06-rendimiento.md#11-ren-01-medir-con-pagespeed-insights): Medir con PageSpeed Insights
  - [REN-02](06-rendimiento.md#12-ren-02-revisar-core-web-vitals): Revisar Core Web Vitals
  - [REN-03](06-rendimiento.md#21-ren-03-comprimir-imágenes-y-usar-formatos-modernos): Comprimir imágenes y usar formatos modernos
  - [REN-04](06-rendimiento.md#31-ren-04-caché-http-cdn-y-compresión): Caché HTTP, CDN y compresión
  - [REN-08](06-rendimiento.md#41-ren-08-índices-en-la-base-de-datos): Índices en la base de datos
  - [REN-09](06-rendimiento.md#42-ren-09-evitar-consultas-n1): Evitar consultas N+1
  - [SEG-01](08-seguridad-y-operacion.md#11-seg-01-https-y-cabeceras-de-seguridad): HTTPS y cabeceras de seguridad
  - [SEG-02](08-seguridad-y-operacion.md#12-seg-02-secretos-accesos-y-autenticación-multifactor): Secretos, accesos y autenticación multifactor
  - [SEG-03](08-seguridad-y-operacion.md#13-seg-03-actualizaciones-y-análisis-de-vulnerabilidades): Actualizaciones y análisis de vulnerabilidades
  - [SEG-04](08-seguridad-y-operacion.md#21-seg-04-copias-de-seguridad-y-restauración-probada): Copias de seguridad y restauración probada
  - [POST-01](09-post-lanzamiento.md#11-post-01-testear-formularios): Testear formularios
  - [POST-02](09-post-lanzamiento.md#21-post-02-plan-de-revisiones-periódicas): Plan de revisiones periódicas
- **Prioridad Media**
  - [PRIV-09](02-privacidad-cookies-y-comunicaciones.md#34-priv-09-cargar-las-fuentes-de-google-desde-tu-propio-servidor): Cargar las fuentes de Google desde tu propio servidor
  - [PRIV-13](02-privacidad-cookies-y-comunicaciones.md#41-priv-13-no-pedir-la-edad-a-los-usuarios): No pedir la edad a los usuarios
  - [PI-02](04-propiedad-intelectual-y-contenido.md#12-pi-02-usuarios-que-suben-contenido-avisos-de-infracción-y-agente-dmca): Usuarios que suben contenido: avisos de infracción y agente DMCA
  - [SEO-02](05-seo.md#12-seo-02-solicitar-a-google-que-indexe-la-web): Solicitar a Google que indexe la web
  - [SEO-03](05-seo.md#13-seo-03-generar-sitemapxml): Generar sitemap.xml
  - [SEO-04](05-seo.md#14-seo-04-generar-robotstxt): Generar robots.txt
  - [SEO-06](05-seo.md#31-seo-06-canónicas-y-contenido-duplicado): Canónicas y contenido duplicado
  - [SEO-11](05-seo.md#36-seo-11-enlazado-interno-y-arquitectura-de-la-información): Enlazado interno y arquitectura de la información
  - [SEO-12](05-seo.md#41-seo-12-favicon): Favicon
  - [SEO-13](05-seo.md#42-seo-13-open-graph-y-vista-previa-al-compartir): Open Graph y vista previa al compartir
  - [REN-05](06-rendimiento.md#32-ren-05-fuentes-web-y-javascript-de-terceros): Fuentes web y JavaScript de terceros
  - [REN-06](06-rendimiento.md#33-ren-06-presupuesto-de-rendimiento-y-monitorización-con-datos-reales): Presupuesto de rendimiento y monitorización con datos reales
  - [SEG-05](08-seguridad-y-operacion.md#22-seg-05-disponibilidad-errores-y-registros): Disponibilidad, errores y registros
  - [POST-03](09-post-lanzamiento.md#22-post-03-revisión-de-enlaces-rotos-y-calidad-del-contenido): Revisión de enlaces rotos y calidad del contenido

**Según condiciones (◐)**

- [ACC-01](01-accesibilidad.md#11-acc-01-obligaciones-legales-de-accesibilidad): Obligaciones legales de accesibilidad
- [ACC-03](01-accesibilidad.md#61-acc-03-documentos-descargables-y-contenido-de-terceros): Documentos descargables y contenido de terceros
- [PRIV-10](02-privacidad-cookies-y-comunicaciones.md#35-priv-10-grabación-de-sesiones-session-replay): Grabación de sesiones (session replay)
- [PRIV-11](02-privacidad-cookies-y-comunicaciones.md#36-priv-11-microsoft-clarity): Microsoft Clarity
- [PRIV-14](02-privacidad-cookies-y-comunicaciones.md#42-priv-14-consentimiento-para-datos-de-menores): Consentimiento para datos de menores
- [PRIV-15](02-privacidad-cookies-y-comunicaciones.md#51-priv-15-autorización-previa-y-enlace-de-baja-en-el-correo-comercial): Autorización previa y enlace de baja en el correo comercial
- [PRIV-16](02-privacidad-cookies-y-comunicaciones.md#52-priv-16-cumplimiento-de-can-spam-y-su-multa-por-correo): Cumplimiento de CAN-SPAM y su multa por correo
- [COM-03](03-consumo-y-comercio.md#13-com-03-renovación-y-cobros-recurrentes-antes-del-pago): Renovación y cobros recurrentes antes del pago
- [COM-04](03-consumo-y-comercio.md#14-com-04-política-de-reembolsos-y-desistimiento): Política de reembolsos y desistimiento
- [COM-05](03-consumo-y-comercio.md#21-com-05-eliminar-gastos-ocultos): Eliminar gastos ocultos
- [COM-09](03-consumo-y-comercio.md#31-com-09-resolución-de-litigios-adr-y-retirada-del-enlace-a-la-plataforma-odr): Resolución de litigios (ADR) y retirada del enlace a la plataforma ODR
- [COM-10](03-consumo-y-comercio.md#32-com-10-contenido-y-servicios-digitales-conformidad-y-actualizaciones): Contenido y servicios digitales: conformidad y actualizaciones
- [SEO-09](05-seo.md#34-seo-09-datos-estructurados): Datos estructurados
- [SEO-10](05-seo.md#35-seo-10-hreflang-para-versiones-por-idioma-o-región): hreflang para versiones por idioma o región
- [REN-07](06-rendimiento.md#34-ren-07-vídeo-y-contenido-incrustado): Vídeo y contenido incrustado
- [UX-01](07-diseno-y-experiencia-de-usuario.md#11-ux-01-acción-principal-clara-y-reducción-de-opciones): Acción principal clara y reducción de opciones
- [UX-02](07-diseno-y-experiencia-de-usuario.md#12-ux-02-design-tokens): Design tokens
- [UX-03](07-diseno-y-experiencia-de-usuario.md#21-ux-03-estados-de-carga-skeletons-spinners-y-barras-de-progreso): Estados de carga: skeletons, spinners y barras de progreso
- [UX-04](07-diseno-y-experiencia-de-usuario.md#22-ux-04-página-de-confirmación-tras-una-conversión): Página de confirmación tras una conversión

### 4.5 Servicios para menores (`MEN`)

**Aplican (●)**

- **Prioridad Alta**
  - [PRIV-01](02-privacidad-cookies-y-comunicaciones.md#11-priv-01-determinar-qué-jurisdicciones-te-aplican): Determinar qué jurisdicciones te aplican
  - [PRIV-02](02-privacidad-cookies-y-comunicaciones.md#21-priv-02-política-de-privacidad): Política de privacidad
  - [PRIV-03](02-privacidad-cookies-y-comunicaciones.md#22-priv-03-no-recopilar-datos-innecesarios): No recopilar datos innecesarios
  - [PRIV-04](02-privacidad-cookies-y-comunicaciones.md#23-priv-04-comprobar-los-formularios-de-consentimiento): Comprobar los formularios de consentimiento
  - [PRIV-05](02-privacidad-cookies-y-comunicaciones.md#24-priv-05-proceso-de-eliminación-de-datos-y-ejercicio-de-derechos): Proceso de eliminación de datos y ejercicio de derechos
  - [PRIV-06](02-privacidad-cookies-y-comunicaciones.md#31-priv-06-política-de-cookies): Política de cookies
  - [PRIV-07](02-privacidad-cookies-y-comunicaciones.md#32-priv-07-banner-de-consentimiento-de-cookies): Banner de consentimiento de cookies
  - [PRIV-08](02-privacidad-cookies-y-comunicaciones.md#33-priv-08-auditar-sdks-y-servicios-de-terceros): Auditar SDKs y servicios de terceros
  - [PRIV-10](02-privacidad-cookies-y-comunicaciones.md#35-priv-10-grabación-de-sesiones-session-replay): Grabación de sesiones (session replay)
  - [PRIV-14](02-privacidad-cookies-y-comunicaciones.md#42-priv-14-consentimiento-para-datos-de-menores): Consentimiento para datos de menores
  - [PRIV-17](02-privacidad-cookies-y-comunicaciones.md#61-priv-17-registro-de-tratamientos-eipd-y-delegado-de-protección-de-datos): Registro de tratamientos, EIPD y delegado de protección de datos
  - [PRIV-18](02-privacidad-cookies-y-comunicaciones.md#62-priv-18-brechas-de-seguridad-e-incidentes): Brechas de seguridad e incidentes
  - [COM-06](03-consumo-y-comercio.md#22-com-06-eliminar-patrones-oscuros): Eliminar patrones oscuros
  - [PI-01](04-propiedad-intelectual-y-contenido.md#11-pi-01-licenciar-fuentes-e-imágenes): Licenciar fuentes e imágenes
  - [PI-04](04-propiedad-intelectual-y-contenido.md#22-pi-04-derechos-de-imagen-de-las-personas): Derechos de imagen de las personas
  - [SEO-08](05-seo.md#33-seo-08-compatibilidad-móvil-e-indexación-centrada-en-móviles): Compatibilidad móvil e indexación centrada en móviles
  - [REN-01](06-rendimiento.md#11-ren-01-medir-con-pagespeed-insights): Medir con PageSpeed Insights
  - [REN-02](06-rendimiento.md#12-ren-02-revisar-core-web-vitals): Revisar Core Web Vitals
  - [REN-03](06-rendimiento.md#21-ren-03-comprimir-imágenes-y-usar-formatos-modernos): Comprimir imágenes y usar formatos modernos
  - [REN-04](06-rendimiento.md#31-ren-04-caché-http-cdn-y-compresión): Caché HTTP, CDN y compresión
  - [SEG-01](08-seguridad-y-operacion.md#11-seg-01-https-y-cabeceras-de-seguridad): HTTPS y cabeceras de seguridad
  - [SEG-02](08-seguridad-y-operacion.md#12-seg-02-secretos-accesos-y-autenticación-multifactor): Secretos, accesos y autenticación multifactor
  - [SEG-03](08-seguridad-y-operacion.md#13-seg-03-actualizaciones-y-análisis-de-vulnerabilidades): Actualizaciones y análisis de vulnerabilidades
  - [SEG-04](08-seguridad-y-operacion.md#21-seg-04-copias-de-seguridad-y-restauración-probada): Copias de seguridad y restauración probada
  - [POST-01](09-post-lanzamiento.md#11-post-01-testear-formularios): Testear formularios
  - [POST-02](09-post-lanzamiento.md#21-post-02-plan-de-revisiones-periódicas): Plan de revisiones periódicas
- **Prioridad Media**
  - [PRIV-09](02-privacidad-cookies-y-comunicaciones.md#34-priv-09-cargar-las-fuentes-de-google-desde-tu-propio-servidor): Cargar las fuentes de Google desde tu propio servidor
  - [PRIV-13](02-privacidad-cookies-y-comunicaciones.md#41-priv-13-no-pedir-la-edad-a-los-usuarios): No pedir la edad a los usuarios
  - [SEO-12](05-seo.md#41-seo-12-favicon): Favicon
  - [REN-05](06-rendimiento.md#32-ren-05-fuentes-web-y-javascript-de-terceros): Fuentes web y JavaScript de terceros

**Según condiciones (◐)**

- [ACC-01](01-accesibilidad.md#11-acc-01-obligaciones-legales-de-accesibilidad): Obligaciones legales de accesibilidad
- [ACC-02](01-accesibilidad.md#12-acc-02-declaración-de-accesibilidad-y-canal-para-comunicar-barreras): Declaración de accesibilidad y canal para comunicar barreras
- [ACC-03](01-accesibilidad.md#61-acc-03-documentos-descargables-y-contenido-de-terceros): Documentos descargables y contenido de terceros
- [PRIV-15](02-privacidad-cookies-y-comunicaciones.md#51-priv-15-autorización-previa-y-enlace-de-baja-en-el-correo-comercial): Autorización previa y enlace de baja en el correo comercial
- [PRIV-16](02-privacidad-cookies-y-comunicaciones.md#52-priv-16-cumplimiento-de-can-spam-y-su-multa-por-correo): Cumplimiento de CAN-SPAM y su multa por correo
- [COM-01](03-consumo-y-comercio.md#11-com-01-datos-del-negocio-en-la-web): Datos del negocio en la web
- [COM-02](03-consumo-y-comercio.md#12-com-02-términos-y-condiciones-del-servicio): Términos y condiciones del servicio
- [COM-03](03-consumo-y-comercio.md#13-com-03-renovación-y-cobros-recurrentes-antes-del-pago): Renovación y cobros recurrentes antes del pago
- [COM-04](03-consumo-y-comercio.md#14-com-04-política-de-reembolsos-y-desistimiento): Política de reembolsos y desistimiento
- [COM-05](03-consumo-y-comercio.md#21-com-05-eliminar-gastos-ocultos): Eliminar gastos ocultos
- [COM-08](03-consumo-y-comercio.md#24-com-08-eliminar-afirmaciones-sin-fundamento): Eliminar afirmaciones sin fundamento
- [COM-09](03-consumo-y-comercio.md#31-com-09-resolución-de-litigios-adr-y-retirada-del-enlace-a-la-plataforma-odr): Resolución de litigios (ADR) y retirada del enlace a la plataforma ODR
- [COM-10](03-consumo-y-comercio.md#32-com-10-contenido-y-servicios-digitales-conformidad-y-actualizaciones): Contenido y servicios digitales: conformidad y actualizaciones
- [PI-02](04-propiedad-intelectual-y-contenido.md#12-pi-02-usuarios-que-suben-contenido-avisos-de-infracción-y-agente-dmca): Usuarios que suben contenido: avisos de infracción y agente DMCA
- [PI-03](04-propiedad-intelectual-y-contenido.md#21-pi-03-política-de-uso-aceptable-y-moderación-de-contenido): Política de uso aceptable y moderación de contenido
- [SEO-01](05-seo.md#11-seo-01-registrar-la-web-en-search-console): Registrar la web en Search Console
- [SEO-02](05-seo.md#12-seo-02-solicitar-a-google-que-indexe-la-web): Solicitar a Google que indexe la web
- [SEO-03](05-seo.md#13-seo-03-generar-sitemapxml): Generar sitemap.xml
- [SEO-04](05-seo.md#14-seo-04-generar-robotstxt): Generar robots.txt
- [SEO-05](05-seo.md#21-seo-05-títulos-y-descripciones-personalizados): Títulos y descripciones personalizados
- [SEO-06](05-seo.md#31-seo-06-canónicas-y-contenido-duplicado): Canónicas y contenido duplicado
- [SEO-07](05-seo.md#32-seo-07-redirecciones-301-y-páginas-404): Redirecciones 301 y páginas 404
- [SEO-09](05-seo.md#34-seo-09-datos-estructurados): Datos estructurados
- [SEO-10](05-seo.md#35-seo-10-hreflang-para-versiones-por-idioma-o-región): hreflang para versiones por idioma o región
- [SEO-11](05-seo.md#36-seo-11-enlazado-interno-y-arquitectura-de-la-información): Enlazado interno y arquitectura de la información
- [SEO-13](05-seo.md#42-seo-13-open-graph-y-vista-previa-al-compartir): Open Graph y vista previa al compartir
- [REN-06](06-rendimiento.md#33-ren-06-presupuesto-de-rendimiento-y-monitorización-con-datos-reales): Presupuesto de rendimiento y monitorización con datos reales
- [REN-07](06-rendimiento.md#34-ren-07-vídeo-y-contenido-incrustado): Vídeo y contenido incrustado
- [REN-08](06-rendimiento.md#41-ren-08-índices-en-la-base-de-datos): Índices en la base de datos
- [REN-09](06-rendimiento.md#42-ren-09-evitar-consultas-n1): Evitar consultas N+1
- [UX-01](07-diseno-y-experiencia-de-usuario.md#11-ux-01-acción-principal-clara-y-reducción-de-opciones): Acción principal clara y reducción de opciones
- [UX-02](07-diseno-y-experiencia-de-usuario.md#12-ux-02-design-tokens): Design tokens
- [UX-03](07-diseno-y-experiencia-de-usuario.md#21-ux-03-estados-de-carga-skeletons-spinners-y-barras-de-progreso): Estados de carga: skeletons, spinners y barras de progreso
- [UX-04](07-diseno-y-experiencia-de-usuario.md#22-ux-04-página-de-confirmación-tras-una-conversión): Página de confirmación tras una conversión
- [SEG-05](08-seguridad-y-operacion.md#22-seg-05-disponibilidad-errores-y-registros): Disponibilidad, errores y registros
- [POST-03](09-post-lanzamiento.md#22-post-03-revisión-de-enlaces-rotos-y-calidad-del-contenido): Revisión de enlaces rotos y calidad del contenido

## 5. Vista por región

Para cada región, dónde la regulación es más estricta (●), dónde aplica con matices (◐) y qué medidas legales son propias de otra región (○). Las medidas de SEO, rendimiento y post-lanzamiento son universales y no se repiten aquí.

### 5.1 UE y España (`UE/ES`)

**● Obligación directa o más estricta**

- [ACC-01](01-accesibilidad.md#11-acc-01-obligaciones-legales-de-accesibilidad): Obligaciones legales de accesibilidad
- [ACC-02](01-accesibilidad.md#12-acc-02-declaración-de-accesibilidad-y-canal-para-comunicar-barreras): Declaración de accesibilidad y canal para comunicar barreras
- [ACC-03](01-accesibilidad.md#61-acc-03-documentos-descargables-y-contenido-de-terceros): Documentos descargables y contenido de terceros
- [PRIV-01](02-privacidad-cookies-y-comunicaciones.md#11-priv-01-determinar-qué-jurisdicciones-te-aplican): Determinar qué jurisdicciones te aplican
- [PRIV-02](02-privacidad-cookies-y-comunicaciones.md#21-priv-02-política-de-privacidad): Política de privacidad
- [PRIV-03](02-privacidad-cookies-y-comunicaciones.md#22-priv-03-no-recopilar-datos-innecesarios): No recopilar datos innecesarios
- [PRIV-04](02-privacidad-cookies-y-comunicaciones.md#23-priv-04-comprobar-los-formularios-de-consentimiento): Comprobar los formularios de consentimiento
- [PRIV-05](02-privacidad-cookies-y-comunicaciones.md#24-priv-05-proceso-de-eliminación-de-datos-y-ejercicio-de-derechos): Proceso de eliminación de datos y ejercicio de derechos
- [PRIV-06](02-privacidad-cookies-y-comunicaciones.md#31-priv-06-política-de-cookies): Política de cookies
- [PRIV-07](02-privacidad-cookies-y-comunicaciones.md#32-priv-07-banner-de-consentimiento-de-cookies): Banner de consentimiento de cookies
- [PRIV-08](02-privacidad-cookies-y-comunicaciones.md#33-priv-08-auditar-sdks-y-servicios-de-terceros): Auditar SDKs y servicios de terceros
- [PRIV-09](02-privacidad-cookies-y-comunicaciones.md#34-priv-09-cargar-las-fuentes-de-google-desde-tu-propio-servidor): Cargar las fuentes de Google desde tu propio servidor
- [PRIV-10](02-privacidad-cookies-y-comunicaciones.md#35-priv-10-grabación-de-sesiones-session-replay): Grabación de sesiones (session replay)
- [PRIV-11](02-privacidad-cookies-y-comunicaciones.md#36-priv-11-microsoft-clarity): Microsoft Clarity
- [PRIV-12](02-privacidad-cookies-y-comunicaciones.md#37-priv-12-meta-pixel): Meta Pixel
- [PRIV-13](02-privacidad-cookies-y-comunicaciones.md#41-priv-13-no-pedir-la-edad-a-los-usuarios): No pedir la edad a los usuarios
- [PRIV-14](02-privacidad-cookies-y-comunicaciones.md#42-priv-14-consentimiento-para-datos-de-menores): Consentimiento para datos de menores
- [PRIV-15](02-privacidad-cookies-y-comunicaciones.md#51-priv-15-autorización-previa-y-enlace-de-baja-en-el-correo-comercial): Autorización previa y enlace de baja en el correo comercial
- [PRIV-17](02-privacidad-cookies-y-comunicaciones.md#61-priv-17-registro-de-tratamientos-eipd-y-delegado-de-protección-de-datos): Registro de tratamientos, EIPD y delegado de protección de datos
- [PRIV-18](02-privacidad-cookies-y-comunicaciones.md#62-priv-18-brechas-de-seguridad-e-incidentes): Brechas de seguridad e incidentes
- [COM-01](03-consumo-y-comercio.md#11-com-01-datos-del-negocio-en-la-web): Datos del negocio en la web
- [COM-02](03-consumo-y-comercio.md#12-com-02-términos-y-condiciones-del-servicio): Términos y condiciones del servicio
- [COM-03](03-consumo-y-comercio.md#13-com-03-renovación-y-cobros-recurrentes-antes-del-pago): Renovación y cobros recurrentes antes del pago
- [COM-04](03-consumo-y-comercio.md#14-com-04-política-de-reembolsos-y-desistimiento): Política de reembolsos y desistimiento
- [COM-05](03-consumo-y-comercio.md#21-com-05-eliminar-gastos-ocultos): Eliminar gastos ocultos
- [COM-06](03-consumo-y-comercio.md#22-com-06-eliminar-patrones-oscuros): Eliminar patrones oscuros
- [COM-07](03-consumo-y-comercio.md#23-com-07-eliminar-reseñas-falsas): Eliminar reseñas falsas
- [COM-08](03-consumo-y-comercio.md#24-com-08-eliminar-afirmaciones-sin-fundamento): Eliminar afirmaciones sin fundamento
- [COM-09](03-consumo-y-comercio.md#31-com-09-resolución-de-litigios-adr-y-retirada-del-enlace-a-la-plataforma-odr): Resolución de litigios (ADR) y retirada del enlace a la plataforma ODR
- [COM-10](03-consumo-y-comercio.md#32-com-10-contenido-y-servicios-digitales-conformidad-y-actualizaciones): Contenido y servicios digitales: conformidad y actualizaciones
- [PI-01](04-propiedad-intelectual-y-contenido.md#11-pi-01-licenciar-fuentes-e-imágenes): Licenciar fuentes e imágenes
- [PI-02](04-propiedad-intelectual-y-contenido.md#12-pi-02-usuarios-que-suben-contenido-avisos-de-infracción-y-agente-dmca): Usuarios que suben contenido: avisos de infracción y agente DMCA
- [PI-03](04-propiedad-intelectual-y-contenido.md#21-pi-03-política-de-uso-aceptable-y-moderación-de-contenido): Política de uso aceptable y moderación de contenido
- [PI-04](04-propiedad-intelectual-y-contenido.md#22-pi-04-derechos-de-imagen-de-las-personas): Derechos de imagen de las personas

**◐ Con matices o por otra norma**

- Ninguna

**○ Sin equivalente relevante**

- [PRIV-16](02-privacidad-cookies-y-comunicaciones.md#52-priv-16-cumplimiento-de-can-spam-y-su-multa-por-correo): Cumplimiento de CAN-SPAM y su multa por correo

### 5.2 EE. UU. (`EE. UU.`)

**● Obligación directa o más estricta**

- [PRIV-01](02-privacidad-cookies-y-comunicaciones.md#11-priv-01-determinar-qué-jurisdicciones-te-aplican): Determinar qué jurisdicciones te aplican
- [PRIV-08](02-privacidad-cookies-y-comunicaciones.md#33-priv-08-auditar-sdks-y-servicios-de-terceros): Auditar SDKs y servicios de terceros
- [PRIV-10](02-privacidad-cookies-y-comunicaciones.md#35-priv-10-grabación-de-sesiones-session-replay): Grabación de sesiones (session replay)
- [PRIV-13](02-privacidad-cookies-y-comunicaciones.md#41-priv-13-no-pedir-la-edad-a-los-usuarios): No pedir la edad a los usuarios
- [PRIV-14](02-privacidad-cookies-y-comunicaciones.md#42-priv-14-consentimiento-para-datos-de-menores): Consentimiento para datos de menores
- [PRIV-16](02-privacidad-cookies-y-comunicaciones.md#52-priv-16-cumplimiento-de-can-spam-y-su-multa-por-correo): Cumplimiento de CAN-SPAM y su multa por correo
- [PRIV-18](02-privacidad-cookies-y-comunicaciones.md#62-priv-18-brechas-de-seguridad-e-incidentes): Brechas de seguridad e incidentes
- [COM-03](03-consumo-y-comercio.md#13-com-03-renovación-y-cobros-recurrentes-antes-del-pago): Renovación y cobros recurrentes antes del pago
- [COM-07](03-consumo-y-comercio.md#23-com-07-eliminar-reseñas-falsas): Eliminar reseñas falsas
- [COM-08](03-consumo-y-comercio.md#24-com-08-eliminar-afirmaciones-sin-fundamento): Eliminar afirmaciones sin fundamento
- [PI-01](04-propiedad-intelectual-y-contenido.md#11-pi-01-licenciar-fuentes-e-imágenes): Licenciar fuentes e imágenes
- [PI-02](04-propiedad-intelectual-y-contenido.md#12-pi-02-usuarios-que-suben-contenido-avisos-de-infracción-y-agente-dmca): Usuarios que suben contenido: avisos de infracción y agente DMCA

**◐ Con matices o por otra norma**

- [ACC-01](01-accesibilidad.md#11-acc-01-obligaciones-legales-de-accesibilidad): Obligaciones legales de accesibilidad
- [ACC-02](01-accesibilidad.md#12-acc-02-declaración-de-accesibilidad-y-canal-para-comunicar-barreras): Declaración de accesibilidad y canal para comunicar barreras
- [ACC-03](01-accesibilidad.md#61-acc-03-documentos-descargables-y-contenido-de-terceros): Documentos descargables y contenido de terceros
- [PRIV-02](02-privacidad-cookies-y-comunicaciones.md#21-priv-02-política-de-privacidad): Política de privacidad
- [PRIV-03](02-privacidad-cookies-y-comunicaciones.md#22-priv-03-no-recopilar-datos-innecesarios): No recopilar datos innecesarios
- [PRIV-04](02-privacidad-cookies-y-comunicaciones.md#23-priv-04-comprobar-los-formularios-de-consentimiento): Comprobar los formularios de consentimiento
- [PRIV-05](02-privacidad-cookies-y-comunicaciones.md#24-priv-05-proceso-de-eliminación-de-datos-y-ejercicio-de-derechos): Proceso de eliminación de datos y ejercicio de derechos
- [PRIV-07](02-privacidad-cookies-y-comunicaciones.md#32-priv-07-banner-de-consentimiento-de-cookies): Banner de consentimiento de cookies
- [PRIV-11](02-privacidad-cookies-y-comunicaciones.md#36-priv-11-microsoft-clarity): Microsoft Clarity
- [PRIV-12](02-privacidad-cookies-y-comunicaciones.md#37-priv-12-meta-pixel): Meta Pixel
- [PRIV-15](02-privacidad-cookies-y-comunicaciones.md#51-priv-15-autorización-previa-y-enlace-de-baja-en-el-correo-comercial): Autorización previa y enlace de baja en el correo comercial
- [COM-02](03-consumo-y-comercio.md#12-com-02-términos-y-condiciones-del-servicio): Términos y condiciones del servicio
- [COM-04](03-consumo-y-comercio.md#14-com-04-política-de-reembolsos-y-desistimiento): Política de reembolsos y desistimiento
- [COM-05](03-consumo-y-comercio.md#21-com-05-eliminar-gastos-ocultos): Eliminar gastos ocultos
- [COM-06](03-consumo-y-comercio.md#22-com-06-eliminar-patrones-oscuros): Eliminar patrones oscuros
- [PI-03](04-propiedad-intelectual-y-contenido.md#21-pi-03-política-de-uso-aceptable-y-moderación-de-contenido): Política de uso aceptable y moderación de contenido
- [PI-04](04-propiedad-intelectual-y-contenido.md#22-pi-04-derechos-de-imagen-de-las-personas): Derechos de imagen de las personas

**○ Sin equivalente relevante**

- [PRIV-06](02-privacidad-cookies-y-comunicaciones.md#31-priv-06-política-de-cookies): Política de cookies
- [PRIV-09](02-privacidad-cookies-y-comunicaciones.md#34-priv-09-cargar-las-fuentes-de-google-desde-tu-propio-servidor): Cargar las fuentes de Google desde tu propio servidor
- [PRIV-17](02-privacidad-cookies-y-comunicaciones.md#61-priv-17-registro-de-tratamientos-eipd-y-delegado-de-protección-de-datos): Registro de tratamientos, EIPD y delegado de protección de datos
- [COM-01](03-consumo-y-comercio.md#11-com-01-datos-del-negocio-en-la-web): Datos del negocio en la web
- [COM-09](03-consumo-y-comercio.md#31-com-09-resolución-de-litigios-adr-y-retirada-del-enlace-a-la-plataforma-odr): Resolución de litigios (ADR) y retirada del enlace a la plataforma ODR
- [COM-10](03-consumo-y-comercio.md#32-com-10-contenido-y-servicios-digitales-conformidad-y-actualizaciones): Contenido y servicios digitales: conformidad y actualizaciones

### 5.3 Reino Unido (`UK`)

**● Obligación directa o más estricta**

- [PRIV-01](02-privacidad-cookies-y-comunicaciones.md#11-priv-01-determinar-qué-jurisdicciones-te-aplican): Determinar qué jurisdicciones te aplican
- [PRIV-02](02-privacidad-cookies-y-comunicaciones.md#21-priv-02-política-de-privacidad): Política de privacidad
- [PRIV-03](02-privacidad-cookies-y-comunicaciones.md#22-priv-03-no-recopilar-datos-innecesarios): No recopilar datos innecesarios
- [PRIV-04](02-privacidad-cookies-y-comunicaciones.md#23-priv-04-comprobar-los-formularios-de-consentimiento): Comprobar los formularios de consentimiento
- [PRIV-05](02-privacidad-cookies-y-comunicaciones.md#24-priv-05-proceso-de-eliminación-de-datos-y-ejercicio-de-derechos): Proceso de eliminación de datos y ejercicio de derechos
- [PRIV-06](02-privacidad-cookies-y-comunicaciones.md#31-priv-06-política-de-cookies): Política de cookies
- [PRIV-07](02-privacidad-cookies-y-comunicaciones.md#32-priv-07-banner-de-consentimiento-de-cookies): Banner de consentimiento de cookies
- [PRIV-08](02-privacidad-cookies-y-comunicaciones.md#33-priv-08-auditar-sdks-y-servicios-de-terceros): Auditar SDKs y servicios de terceros
- [PRIV-10](02-privacidad-cookies-y-comunicaciones.md#35-priv-10-grabación-de-sesiones-session-replay): Grabación de sesiones (session replay)
- [PRIV-11](02-privacidad-cookies-y-comunicaciones.md#36-priv-11-microsoft-clarity): Microsoft Clarity
- [PRIV-12](02-privacidad-cookies-y-comunicaciones.md#37-priv-12-meta-pixel): Meta Pixel
- [PRIV-13](02-privacidad-cookies-y-comunicaciones.md#41-priv-13-no-pedir-la-edad-a-los-usuarios): No pedir la edad a los usuarios
- [PRIV-14](02-privacidad-cookies-y-comunicaciones.md#42-priv-14-consentimiento-para-datos-de-menores): Consentimiento para datos de menores
- [PRIV-15](02-privacidad-cookies-y-comunicaciones.md#51-priv-15-autorización-previa-y-enlace-de-baja-en-el-correo-comercial): Autorización previa y enlace de baja en el correo comercial
- [PRIV-17](02-privacidad-cookies-y-comunicaciones.md#61-priv-17-registro-de-tratamientos-eipd-y-delegado-de-protección-de-datos): Registro de tratamientos, EIPD y delegado de protección de datos
- [PRIV-18](02-privacidad-cookies-y-comunicaciones.md#62-priv-18-brechas-de-seguridad-e-incidentes): Brechas de seguridad e incidentes
- [COM-01](03-consumo-y-comercio.md#11-com-01-datos-del-negocio-en-la-web): Datos del negocio en la web
- [COM-02](03-consumo-y-comercio.md#12-com-02-términos-y-condiciones-del-servicio): Términos y condiciones del servicio
- [COM-03](03-consumo-y-comercio.md#13-com-03-renovación-y-cobros-recurrentes-antes-del-pago): Renovación y cobros recurrentes antes del pago
- [COM-04](03-consumo-y-comercio.md#14-com-04-política-de-reembolsos-y-desistimiento): Política de reembolsos y desistimiento
- [COM-05](03-consumo-y-comercio.md#21-com-05-eliminar-gastos-ocultos): Eliminar gastos ocultos
- [COM-06](03-consumo-y-comercio.md#22-com-06-eliminar-patrones-oscuros): Eliminar patrones oscuros
- [COM-07](03-consumo-y-comercio.md#23-com-07-eliminar-reseñas-falsas): Eliminar reseñas falsas
- [COM-08](03-consumo-y-comercio.md#24-com-08-eliminar-afirmaciones-sin-fundamento): Eliminar afirmaciones sin fundamento
- [COM-10](03-consumo-y-comercio.md#32-com-10-contenido-y-servicios-digitales-conformidad-y-actualizaciones): Contenido y servicios digitales: conformidad y actualizaciones
- [PI-01](04-propiedad-intelectual-y-contenido.md#11-pi-01-licenciar-fuentes-e-imágenes): Licenciar fuentes e imágenes
- [PI-02](04-propiedad-intelectual-y-contenido.md#12-pi-02-usuarios-que-suben-contenido-avisos-de-infracción-y-agente-dmca): Usuarios que suben contenido: avisos de infracción y agente DMCA
- [PI-03](04-propiedad-intelectual-y-contenido.md#21-pi-03-política-de-uso-aceptable-y-moderación-de-contenido): Política de uso aceptable y moderación de contenido

**◐ Con matices o por otra norma**

- [ACC-01](01-accesibilidad.md#11-acc-01-obligaciones-legales-de-accesibilidad): Obligaciones legales de accesibilidad
- [ACC-02](01-accesibilidad.md#12-acc-02-declaración-de-accesibilidad-y-canal-para-comunicar-barreras): Declaración de accesibilidad y canal para comunicar barreras
- [ACC-03](01-accesibilidad.md#61-acc-03-documentos-descargables-y-contenido-de-terceros): Documentos descargables y contenido de terceros
- [PRIV-09](02-privacidad-cookies-y-comunicaciones.md#34-priv-09-cargar-las-fuentes-de-google-desde-tu-propio-servidor): Cargar las fuentes de Google desde tu propio servidor
- [COM-09](03-consumo-y-comercio.md#31-com-09-resolución-de-litigios-adr-y-retirada-del-enlace-a-la-plataforma-odr): Resolución de litigios (ADR) y retirada del enlace a la plataforma ODR
- [PI-04](04-propiedad-intelectual-y-contenido.md#22-pi-04-derechos-de-imagen-de-las-personas): Derechos de imagen de las personas

**○ Sin equivalente relevante**

- [PRIV-16](02-privacidad-cookies-y-comunicaciones.md#52-priv-16-cumplimiento-de-can-spam-y-su-multa-por-correo): Cumplimiento de CAN-SPAM y su multa por correo

### 5.4 Latinoamérica (`LATAM`)

**● Obligación directa o más estricta**

- [PRIV-01](02-privacidad-cookies-y-comunicaciones.md#11-priv-01-determinar-qué-jurisdicciones-te-aplican): Determinar qué jurisdicciones te aplican
- [PRIV-02](02-privacidad-cookies-y-comunicaciones.md#21-priv-02-política-de-privacidad): Política de privacidad
- [PRIV-03](02-privacidad-cookies-y-comunicaciones.md#22-priv-03-no-recopilar-datos-innecesarios): No recopilar datos innecesarios
- [PRIV-04](02-privacidad-cookies-y-comunicaciones.md#23-priv-04-comprobar-los-formularios-de-consentimiento): Comprobar los formularios de consentimiento
- [PRIV-05](02-privacidad-cookies-y-comunicaciones.md#24-priv-05-proceso-de-eliminación-de-datos-y-ejercicio-de-derechos): Proceso de eliminación de datos y ejercicio de derechos
- [PRIV-08](02-privacidad-cookies-y-comunicaciones.md#33-priv-08-auditar-sdks-y-servicios-de-terceros): Auditar SDKs y servicios de terceros
- [PRIV-13](02-privacidad-cookies-y-comunicaciones.md#41-priv-13-no-pedir-la-edad-a-los-usuarios): No pedir la edad a los usuarios
- [PRIV-14](02-privacidad-cookies-y-comunicaciones.md#42-priv-14-consentimiento-para-datos-de-menores): Consentimiento para datos de menores
- [PRIV-18](02-privacidad-cookies-y-comunicaciones.md#62-priv-18-brechas-de-seguridad-e-incidentes): Brechas de seguridad e incidentes
- [COM-04](03-consumo-y-comercio.md#14-com-04-política-de-reembolsos-y-desistimiento): Política de reembolsos y desistimiento
- [COM-05](03-consumo-y-comercio.md#21-com-05-eliminar-gastos-ocultos): Eliminar gastos ocultos
- [COM-08](03-consumo-y-comercio.md#24-com-08-eliminar-afirmaciones-sin-fundamento): Eliminar afirmaciones sin fundamento
- [PI-01](04-propiedad-intelectual-y-contenido.md#11-pi-01-licenciar-fuentes-e-imágenes): Licenciar fuentes e imágenes

**◐ Con matices o por otra norma**

- [ACC-01](01-accesibilidad.md#11-acc-01-obligaciones-legales-de-accesibilidad): Obligaciones legales de accesibilidad
- [ACC-03](01-accesibilidad.md#61-acc-03-documentos-descargables-y-contenido-de-terceros): Documentos descargables y contenido de terceros
- [PRIV-06](02-privacidad-cookies-y-comunicaciones.md#31-priv-06-política-de-cookies): Política de cookies
- [PRIV-07](02-privacidad-cookies-y-comunicaciones.md#32-priv-07-banner-de-consentimiento-de-cookies): Banner de consentimiento de cookies
- [PRIV-10](02-privacidad-cookies-y-comunicaciones.md#35-priv-10-grabación-de-sesiones-session-replay): Grabación de sesiones (session replay)
- [PRIV-11](02-privacidad-cookies-y-comunicaciones.md#36-priv-11-microsoft-clarity): Microsoft Clarity
- [PRIV-12](02-privacidad-cookies-y-comunicaciones.md#37-priv-12-meta-pixel): Meta Pixel
- [PRIV-15](02-privacidad-cookies-y-comunicaciones.md#51-priv-15-autorización-previa-y-enlace-de-baja-en-el-correo-comercial): Autorización previa y enlace de baja en el correo comercial
- [PRIV-17](02-privacidad-cookies-y-comunicaciones.md#61-priv-17-registro-de-tratamientos-eipd-y-delegado-de-protección-de-datos): Registro de tratamientos, EIPD y delegado de protección de datos
- [COM-01](03-consumo-y-comercio.md#11-com-01-datos-del-negocio-en-la-web): Datos del negocio en la web
- [COM-02](03-consumo-y-comercio.md#12-com-02-términos-y-condiciones-del-servicio): Términos y condiciones del servicio
- [COM-03](03-consumo-y-comercio.md#13-com-03-renovación-y-cobros-recurrentes-antes-del-pago): Renovación y cobros recurrentes antes del pago
- [COM-06](03-consumo-y-comercio.md#22-com-06-eliminar-patrones-oscuros): Eliminar patrones oscuros
- [COM-07](03-consumo-y-comercio.md#23-com-07-eliminar-reseñas-falsas): Eliminar reseñas falsas
- [COM-10](03-consumo-y-comercio.md#32-com-10-contenido-y-servicios-digitales-conformidad-y-actualizaciones): Contenido y servicios digitales: conformidad y actualizaciones
- [PI-02](04-propiedad-intelectual-y-contenido.md#12-pi-02-usuarios-que-suben-contenido-avisos-de-infracción-y-agente-dmca): Usuarios que suben contenido: avisos de infracción y agente DMCA
- [PI-03](04-propiedad-intelectual-y-contenido.md#21-pi-03-política-de-uso-aceptable-y-moderación-de-contenido): Política de uso aceptable y moderación de contenido
- [PI-04](04-propiedad-intelectual-y-contenido.md#22-pi-04-derechos-de-imagen-de-las-personas): Derechos de imagen de las personas

**○ Sin equivalente relevante**

- [ACC-02](01-accesibilidad.md#12-acc-02-declaración-de-accesibilidad-y-canal-para-comunicar-barreras): Declaración de accesibilidad y canal para comunicar barreras
- [PRIV-09](02-privacidad-cookies-y-comunicaciones.md#34-priv-09-cargar-las-fuentes-de-google-desde-tu-propio-servidor): Cargar las fuentes de Google desde tu propio servidor
- [PRIV-16](02-privacidad-cookies-y-comunicaciones.md#52-priv-16-cumplimiento-de-can-spam-y-su-multa-por-correo): Cumplimiento de CAN-SPAM y su multa por correo
- [COM-09](03-consumo-y-comercio.md#31-com-09-resolución-de-litigios-adr-y-retirada-del-enlace-a-la-plataforma-odr): Resolución de litigios (ADR) y retirada del enlace a la plataforma ODR
