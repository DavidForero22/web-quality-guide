# Correcciones y verificación

> Última verificación: 2026-10-10 · [Volver al README](../README.md)

Resultado de contrastar las listas originales (generadas con Perplexity) con fuentes oficiales y comentarios jurídicos. En general eran **bastante correctas**; hay **una corrección clara**, varios matices importantes y algunos datos que han cambiado.

<!-- INDICE -->
**Índice**

- [1. Método y alcance de la verificación](#1-método-y-alcance-de-la-verificación)
- [2. Correcciones a las listas originales](#2-correcciones-a-las-listas-originales)
- [3. Medidas duplicadas fusionadas](#3-medidas-duplicadas-fusionadas)
- [4. Incorporación de las lagunas propuestas](#4-incorporación-de-las-lagunas-propuestas)
- [5. Incorporación del listado de buenas prácticas de diseño y rendimiento](#5-incorporación-del-listado-de-buenas-prácticas-de-diseño-y-rendimiento)
- [6. Cambios normativos a vigilar](#6-cambios-normativos-a-vigilar)
<!-- /INDICE -->

## 1. Método y alcance de la verificación

- Fecha de verificación: **2026-10-10**.
- Se priorizaron fuentes primarias: documentación de Google Search Central y web.dev, W3C (WCAG 2.2), BOE (LSSI-CE), Oficina de Derechos de Autor de EE. UU., Microsoft Learn, FTC y EUR-Lex.
- Cuando no se pudo abrir la fuente primaria, la afirmación se contrastó con despachos de abogados o prensa especializada y así consta en la ficha («fuentes secundarias»).
- Esta guía no sustituye al asesoramiento jurídico. En los puntos donde la norma está cambiando, comprueba el estado en la fuente oficial antes de actuar.

**Limitaciones conocidas**

- No se pudo abrir el PDF oficial de la Guía de cookies de la AEPD; el criterio de «aceptar y rechazar al mismo nivel» se confirmó en análisis de despachos.
- Los textos consolidados del TRLGDCU (arts. 98, 102, 103) se contrastaron con comentarios jurídicos y jurisprudencia del TJUE; el art. 20 sí se leyó en el BOE.
- Las referencias a Latinoamérica (LGPD, Chile, México) proceden de fuentes secundarias y no cubren todos los países.
- Los importes de sanciones y plazos de EE. UU. cambian cada año; verifica la cifra vigente.

## 2. Correcciones a las listas originales

| Afirmación de la lista original | Veredicto | Corrección o matiz | Ficha |
|---|---|---|---|
| WCAG 3.2.6 Ayuda coherente es **Nivel AA** | ❌ Incorrecta | Es **Nivel A** en WCAG 2.2 | [WCAG 3.2.6](01-accesibilidad.md#47-wcag-326-ayuda-coherente-a) |
| Imágenes decorativas: `aria-hidden="true"` | ⚠️ Matizada | Para `<img>` decorativas se usa `alt=""`; `aria-hidden` es para iconos SVG o de fuente | [WCAG 1.1.1](01-accesibilidad.md#21-wcag-111-contenido-no-textual-a) |
| «Pedir la edad va contra COPPA» (corregida ya en la lista) | ✅ Correcta la corrección | COPPA aplica a servicios dirigidos a menores de 13 o con conocimiento efectivo; la regla enmendada tuvo plazo el 22-4-2026; España: 14 años, con proyecto para elevarlo a 16 | [PRIV-13](02-privacidad-cookies-y-comunicaciones.md#41-priv-13-no-pedir-la-edad-a-los-usuarios) |
| Google Fonts: sentencia alemana de 100 € | ✅ Correcta | Es de primera instancia (LG München I, 3 O 17493/20); no es multa automática ni vinculante fuera de su jurisdicción | [PRIV-09](02-privacidad-cookies-y-comunicaciones.md#34-priv-09-cargar-las-fuentes-de-google-desde-tu-propio-servidor) |
| Session replay: no siempre graba cada tecla | ✅ Correcta | En EE. UU. la jurisprudencia está dividida; SB 690 no es ley (en *suspense file* desde 5-8-2026) | [PRIV-10](02-privacidad-cookies-y-comunicaciones.md#35-priv-10-grabación-de-sesiones-session-replay) |
| CAN-SPAM: hasta 53.088 $ por correo | ✅ Correcta | Máximo teórico por mensaje; la FTC mantuvo en 2026 los importes de 2025 | [PRIV-16](02-privacidad-cookies-y-comunicaciones.md#52-priv-16-cumplimiento-de-can-spam-y-su-multa-por-correo) |
| «6 €» por un agente DMCA | ⚠️ Matizada | Son **6 $**; cubre designar, enmendar o renovar; caduca a los 3 años | [PI-02](04-propiedad-intelectual-y-contenido.md#12-pi-02-usuarios-que-suben-contenido-avisos-de-infracción-y-agente-dmca) |
| Términos de renovación «junto al botón» | ⚠️ Matizada | No hay regla literal de proximidad, pero el botón debe indicar la obligación de pago (art. 98.2 TRLGDCU; C-249/21, C-400/22) | [COM-03](03-consumo-y-comercio.md#13-com-03-renovación-y-cobros-recurrentes-antes-del-pago) |
| Desistimiento de 14 días con excepciones | ✅ Correcta | Desde 19-6-2026 aplica además la **función de desistimiento online** (Directiva 2023/2673) | [COM-04](03-consumo-y-comercio.md#14-com-04-política-de-reembolsos-y-desistimiento) |
| LSSI alcanza sitios con beneficio indirecto | ✅ Correcta | Confirmado en el anexo de la LSSI: servicios no remunerados que sean actividad económica para el prestador | [COM-01](03-consumo-y-comercio.md#11-com-01-datos-del-negocio-en-la-web) |
| EAA aplicable desde 28-6-2025; microempresas exentas | ✅ Correcta | Referencia técnica EN 301 549 v3.2.1 (WCAG 2.1) hasta que se cite la v4.1.1 (WCAG 2.2) | [ACC-01](01-accesibilidad.md#11-acc-01-obligaciones-legales-de-accesibilidad) |
| Banner de cookies: aceptar y rechazar comparables | ✅ Correcta | Criterio de la Guía de la AEPD; plazo de adaptación vencido el 11-1-2024 | [PRIV-07](02-privacidad-cookies-y-comunicaciones.md#32-priv-07-banner-de-consentimiento-de-cookies) |
| Microsoft Clarity: opcional y con cautela | ✅ Correcta | Desde 31-10-2025 exige señal de consentimiento para EEE, Reino Unido y Suiza | [PRIV-11](02-privacidad-cookies-y-comunicaciones.md#36-priv-11-microsoft-clarity) |
| Meta Pixel: no cargarlo antes del consentimiento | ✅ Correcta | La responsabilidad es del titular de la web; la API de conversiones no evita la base jurídica | [PRIV-12](02-privacidad-cookies-y-comunicaciones.md#37-priv-12-meta-pixel) |
| LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1 en percentil 75 | ✅ Correcta | INP sustituyó a FID en 2024; aprobar no garantiza posicionamiento | [REN-02](06-rendimiento.md#12-ren-02-revisar-core-web-vitals) |
| Search Console es gratuita y no es requisito | ✅ Correcta | Confirmado en la ayuda de Google | [SEO-01](05-seo.md#11-seo-01-registrar-la-web-en-search-console) |
| Solicitar indexación no garantiza inclusión | ✅ Correcta | Hay cuota; para muchas URLs, sitemap | [SEO-02](05-seo.md#12-seo-02-solicitar-a-google-que-indexe-la-web) |
| robots.txt no sirve para ocultar páginas | ✅ Correcta | Usar `noindex` o contraseña; no combinar con bloqueo de rastreo | [SEO-04](05-seo.md#14-seo-04-generar-robotstxt) |
| `meta keywords`: Google no la usa | ✅ Correcta | Desde 2009 | [SEO-05](05-seo.md#21-seo-05-títulos-y-descripciones-personalizados) |
| WebP no es obligatorio | ✅ Correcta | Lo importante es tamaño adecuado y compresión; considera AVIF y `srcset` | [REN-03](06-rendimiento.md#21-ren-03-comprimir-imágenes-y-usar-formatos-modernos) |
| Reseñas falsas: medidas razonables y transparencia | ✅ Correcta | Norma de la FTC en vigor desde 21-10-2024 | [COM-07](03-consumo-y-comercio.md#23-com-07-eliminar-reseñas-falsas) |
| «Revisar leyes locales»: el RGPD puede aplicar fuera de la UE | ✅ Correcta | Art. 3.2 RGPD | [PRIV-01](02-privacidad-cookies-y-comunicaciones.md#11-priv-01-determinar-qué-jurisdicciones-te-aplican) |

## 3. Medidas duplicadas fusionadas

| Medida repetida | Dónde queda |
|---|---|
| Texto alt en imágenes (SEO y accesibilidad) | [WCAG 1.1.1](01-accesibilidad.md#21-wcag-111-contenido-no-textual-a) (con referencia desde [SEO-05](05-seo.md#21-seo-05-títulos-y-descripciones-personalizados)) |
| Corregir contraste de color | [WCAG 1.4.3](01-accesibilidad.md#214-wcag-143-contraste-mínimo-aa) |
| Añadir navegación por teclado | [WCAG 2.1.1](01-accesibilidad.md#31-wcag-211-teclado-a), [WCAG 2.1.2](01-accesibilidad.md#32-wcag-212-sin-trampas-para-el-foco-del-teclado-a) y [WCAG 2.4.7](01-accesibilidad.md#313-wcag-247-foco-visible-aa) |
| Términos de renovación junto al botón de pago / junto al pago | [COM-03](03-consumo-y-comercio.md#13-com-03-renovación-y-cobros-recurrentes-antes-del-pago) |

## 4. Incorporación de las lagunas propuestas

Las listas originales incluían una sección de «posibles lagunas» sin desarrollar. Se desarrollaron (con otro informe de Perplexity), se contrastaron con fuentes primarias y se clasificaron así:

**Añadidas como medida nueva**

| Medida | Ficha |
|---|---|
| Declaración de accesibilidad y canal de barreras | [ACC-02](01-accesibilidad.md#12-acc-02-declaración-de-accesibilidad-y-canal-para-comunicar-barreras) |
| PDF, documentos y contenido de terceros | [ACC-03](01-accesibilidad.md#61-acc-03-documentos-descargables-y-contenido-de-terceros) |
| Registro de tratamientos, EIPD y DPD | [PRIV-17](02-privacidad-cookies-y-comunicaciones.md#61-priv-17-registro-de-tratamientos-eipd-y-delegado-de-protección-de-datos) |
| Brechas e incidentes (fusiona dos puntos) | [PRIV-18](02-privacidad-cookies-y-comunicaciones.md#62-priv-18-brechas-de-seguridad-e-incidentes) |
| Resolución de litigios y fin de la plataforma ODR | [COM-09](03-consumo-y-comercio.md#31-com-09-resolución-de-litigios-adr-y-retirada-del-enlace-a-la-plataforma-odr) |
| Contenido y servicios digitales (Directiva 2019/770) | [COM-10](03-consumo-y-comercio.md#32-com-10-contenido-y-servicios-digitales-conformidad-y-actualizaciones) |
| Uso aceptable y moderación | [PI-03](04-propiedad-intelectual-y-contenido.md#21-pi-03-política-de-uso-aceptable-y-moderación-de-contenido) |
| Derechos de imagen | [PI-04](04-propiedad-intelectual-y-contenido.md#22-pi-04-derechos-de-imagen-de-las-personas) |
| Canónicas, redirecciones, móvil, datos estructurados, hreflang y enlazado interno | [SEO-06](05-seo.md#31-seo-06-canónicas-y-contenido-duplicado), [SEO-07](05-seo.md#32-seo-07-redirecciones-301-y-páginas-404), [SEO-08](05-seo.md#33-seo-08-compatibilidad-móvil-e-indexación-centrada-en-móviles), [SEO-09](05-seo.md#34-seo-09-datos-estructurados), [SEO-10](05-seo.md#35-seo-10-hreflang-para-versiones-por-idioma-o-región), [SEO-11](05-seo.md#36-seo-11-enlazado-interno-y-arquitectura-de-la-información) |
| Caché y compresión, fuentes y JS de terceros, presupuesto, vídeo e incrustados | [REN-04](06-rendimiento.md#31-ren-04-caché-http-cdn-y-compresión), [REN-05](06-rendimiento.md#32-ren-05-fuentes-web-y-javascript-de-terceros), [REN-06](06-rendimiento.md#33-ren-06-presupuesto-de-rendimiento-y-monitorización-con-datos-reales), [REN-07](06-rendimiento.md#34-ren-07-vídeo-y-contenido-incrustado) |
| HTTPS y cabeceras, secretos y MFA, actualizaciones, copias, disponibilidad y registros | [SEG-01](08-seguridad-y-operacion.md#11-seg-01-https-y-cabeceras-de-seguridad), [SEG-02](08-seguridad-y-operacion.md#12-seg-02-secretos-accesos-y-autenticación-multifactor), [SEG-03](08-seguridad-y-operacion.md#13-seg-03-actualizaciones-y-análisis-de-vulnerabilidades), [SEG-04](08-seguridad-y-operacion.md#21-seg-04-copias-de-seguridad-y-restauración-probada), [SEG-05](08-seguridad-y-operacion.md#22-seg-05-disponibilidad-errores-y-registros) |
| Enlaces rotos y calidad del contenido | [POST-03](09-post-lanzamiento.md#22-post-03-revisión-de-enlaces-rotos-y-calidad-del-contenido) |

**Integradas en una ficha existente**

| Punto | Dónde |
|---|---|
| «Pago o consentimiento» y muros de cookies | [PRIV-07](02-privacidad-cookies-y-comunicaciones.md#32-priv-07-banner-de-consentimiento-de-cookies) |
| Global Privacy Control y «Your Privacy Choices» | [PRIV-07](02-privacidad-cookies-y-comunicaciones.md#32-priv-07-banner-de-consentimiento-de-cookies) |
| SMS, WhatsApp y llamadas | [PRIV-15](02-privacidad-cookies-y-comunicaciones.md#51-priv-15-autorización-previa-y-enlace-de-baja-en-el-correo-comercial) |
| Pruebas con usuarios de tecnologías de apoyo y criterios AAA | Sección «Cómo comprobar» de [Accesibilidad](01-accesibilidad.md) |
| Publicidad de influencers y afiliación | [COM-08](03-consumo-y-comercio.md#24-com-08-eliminar-afirmaciones-sin-fundamento) |
| Mercados en línea (DSA) y art. 17 de la Directiva de copyright | [PI-02](04-propiedad-intelectual-y-contenido.md#12-pi-02-usuarios-que-suben-contenido-avisos-de-infracción-y-agente-dmca) |
| Licencias de datos, datasets y APIs | [PI-01](04-propiedad-intelectual-y-contenido.md#11-pi-01-licenciar-fuentes-e-imágenes) |

**Descartadas**

| Punto | Motivo |
|---|---|
| Facturación electrónica, IVA y OSS | Es fiscalidad, no práctica web. Además cambia deprisa: el 5-10-2026 Hacienda anunció el aplazamiento de Verifactu a octubre de 2028 (pendiente de formalizar), y la factura electrónica B2B (RD 238/2026) arranca en octubre de 2027 para grandes empresas. Son obligaciones distintas |
| Normas sectoriales (juego, salud, finanzas) | Demasiado genérico; esta guía no cubre sectores regulados |
| Marca, dominios y signos distintivos | Estrategia de negocio, no práctica web |
| Ley 10/2025 como medida propia | Solo aplica a servicios básicos de interés general y a grandes empresas; queda como nota en [COM-03](03-consumo-y-comercio.md#13-com-03-renovación-y-cobros-recurrentes-antes-del-pago) |
| Criterios AAA como medida | Fuera del alcance A/AA; queda una nota en «Cómo comprobar» |

**Precisiones del contraste**

- La plataforma europea ODR dejó de prestar servicios el 20-7-2025 (Reglamento 2024/3228).
- La Ley 10/2025 tiene un ámbito limitado: servicios básicos de interés general y empresas con 250 o más trabajadores, 50 M€ de facturación o 43 M€ de balance.
- La Guía de cookies de la AEPD se actualizó en 2024 para incorporar los criterios del CEPD sobre «consentir o pagar»; admite el muro de cookies con alternativa equivalente, no necesariamente gratuita.
- En `hreflang`, `UK` es un código de región reservado que Google ignora: usa `en-GB`.

## 5. Incorporación del listado de buenas prácticas de diseño y rendimiento

Un tercer listado de Perplexity proponía 16 prácticas. Se contrastaron con fuentes primarias y se clasificaron así:

**Añadidas como medida nueva**

| Práctica | Ficha |
|---|---|
| Índices en la base de datos | [REN-08](06-rendimiento.md#41-ren-08-índices-en-la-base-de-datos) |
| Consultas N+1 | [REN-09](06-rendimiento.md#42-ren-09-evitar-consultas-n1) |
| Favicon | [SEO-12](05-seo.md#41-seo-12-favicon) |
| Open Graph image | [SEO-13](05-seo.md#42-seo-13-open-graph-y-vista-previa-al-compartir) |
| «Violar la ley de Hick» y CTA above the fold (fusionadas) | [UX-01](07-diseno-y-experiencia-de-usuario.md#11-ux-01-acción-principal-clara-y-reducción-de-opciones) |
| Design tokens | [UX-02](07-diseno-y-experiencia-de-usuario.md#12-ux-02-design-tokens) |
| Skeletons en carga | [UX-03](07-diseno-y-experiencia-de-usuario.md#21-ux-03-estados-de-carga-skeletons-spinners-y-barras-de-progreso) |
| Thank you page | [UX-04](07-diseno-y-experiencia-de-usuario.md#22-ux-04-página-de-confirmación-tras-una-conversión) |

**Integradas en una ficha existente**

| Práctica | Dónde |
|---|---|
| Form error states | [WCAG 3.3.1](01-accesibilidad.md#48-wcag-331-identificación-de-errores-a) (patrón de validación y resumen de errores) |
| Dirección de contacto real | [COM-01](03-consumo-y-comercio.md#11-com-01-datos-del-negocio-en-la-web) (más allá del mínimo legal) |
| WebP o AVIF | [REN-03](06-rendimiento.md#21-ren-03-comprimir-imágenes-y-usar-formatos-modernos) (cuándo elegir cada uno) |

**Descartadas por duplicadas**

| Práctica | Ya cubierta en |
|---|---|
| No seguir estándares de accesibilidad | Todo el archivo [Accesibilidad](01-accesibilidad.md) |
| No comprimir assets | [REN-03](06-rendimiento.md#21-ren-03-comprimir-imágenes-y-usar-formatos-modernos) y [REN-04](06-rendimiento.md#31-ren-04-caché-http-cdn-y-compresión) |
| Crear página 404 | [SEO-07](05-seo.md#32-seo-07-redirecciones-301-y-páginas-404) |
| Meta title por página | [SEO-05](05-seo.md#21-seo-05-títulos-y-descripciones-personalizados) |
| Meta description por página | [SEO-05](05-seo.md#21-seo-05-títulos-y-descripciones-personalizados) |

**Precisiones del contraste**

- El listado citaba documentación de PostgreSQL 7.2 (obsoleta); se sustituyó por la actual.
- Los argumentos sobre *above the fold* se apoyaban en blogs; se sustituyeron por el estudio de seguimiento ocular de NN/g (2018): alrededor del 57 % del tiempo de visualización cae sobre el pliegue y el 74 % en las dos primeras pantallas.
- Sobre skeletons, NN/g los presenta como una herramienta complementaria y marca umbrales de uso; no se pudo confirmar en la página el resultado del estudio citado por el listado según el cual se perciben a veces como más lentos.
- Sobre favicon, Google exige 8 × 8 px como mínimo y recomienda más de 48 × 48 px; el listado hablaba solo de 16 a 32 px como tamaño de diseño.
- Open Graph: Meta recomienda 1200 × 630 px y fija 600 × 315 px como mínimo para la vista previa grande; 1200 × 630 no es un requisito.
- El artículo de NN/g sobre la ley de Hick no estaba disponible; la ficha se apoya en una fuente secundaria y lo marca.

## 6. Cambios normativos a vigilar

Estado a **2026-10-10**. Varias normas están por cambiar o acaban de entrar en vigor; revisa su estado antes de decidir y actualiza las fichas afectadas.

| Cambio | Estado | Fecha clave | Fichas afectadas |
|---|---|---|---|
| Función de desistimiento online (Directiva 2023/2673) | Aplicable; transposición en España pendiente según la OCU (junio de 2026) | 19-6-2026 | [COM-04](03-consumo-y-comercio.md#14-com-04-política-de-reembolsos-y-desistimiento) |
| Afirmaciones medioambientales (Directiva 2024/825) | Aplicable | 27-9-2026 | [COM-08](03-consumo-y-comercio.md#24-com-08-eliminar-afirmaciones-sin-fundamento) |
| EN 301 549 v4.1.1 (WCAG 2.2) | Publicada; pendiente de citación en el DOUE | Citación prevista nov–dic 2026 | [ACC-01](01-accesibilidad.md#11-acc-01-obligaciones-legales-de-accesibilidad) |
| Ley 10/2025 de atención a la clientela (solo servicios básicos y grandes empresas) | En vigor; plazo de adaptación de un año | 28-12-2026 | [COM-03](03-consumo-y-comercio.md#13-com-03-renovación-y-cobros-recurrentes-antes-del-pago) |
| Chile, Ley 21.719 de datos personales | Prevista su entrada en vigor; hay un proyecto de aplazamiento a 2027 | 1-12-2026 | [PRIV-01](02-privacidad-cookies-y-comunicaciones.md#11-priv-01-determinar-qué-jurisdicciones-te-aplican) |
| *Digital Omnibus* (RGPD y cookies) | En tramitación en el Consejo y el Parlamento | Sin fecha | [PRIV-07](02-privacidad-cookies-y-comunicaciones.md#32-priv-07-banner-de-consentimiento-de-cookies) |
| *Digital Fairness Act* | Propuesta de la Comisión esperada en noviembre de 2026 | Adopción improbable antes de finales de 2027 | [COM-03](03-consumo-y-comercio.md#13-com-03-renovación-y-cobros-recurrentes-antes-del-pago), [COM-06](03-consumo-y-comercio.md#22-com-06-eliminar-patrones-oscuros) |
| Menores en entornos digitales (España) | Proyecto de ley orgánica en el Congreso | Sin fecha | [PRIV-13](02-privacidad-cookies-y-comunicaciones.md#41-priv-13-no-pedir-la-edad-a-los-usuarios), [PRIV-14](02-privacidad-cookies-y-comunicaciones.md#42-priv-14-consentimiento-para-datos-de-menores) |
| Régimen de suscripciones (DMCCA, Reino Unido) | Entrada en vigor anunciada | Enero de 2027 | [COM-03](03-consumo-y-comercio.md#13-com-03-renovación-y-cobros-recurrentes-antes-del-pago) |
| ADA Título II (EE. UU.) | Plazos aplazados un año | 26-4-2027 y 26-4-2028 | [ACC-01](01-accesibilidad.md#11-acc-01-obligaciones-legales-de-accesibilidad) |
| Regla «Click-to-Cancel» (FTC) | Anulada en 2025; nuevo proceso iniciado en 2026 | Sin fecha | [COM-03](03-consumo-y-comercio.md#13-com-03-renovación-y-cobros-recurrentes-antes-del-pago) |
| SB 690 (California, CIPA) | En el *suspense file* desde el 5-8-2026 | Sin fecha | [PRIV-10](02-privacidad-cookies-y-comunicaciones.md#35-priv-10-grabación-de-sesiones-session-replay) |
| Marco UE-EE. UU. de privacidad (recurso C-703/25 P) | Pendiente ante el Tribunal de Justicia | Sin fecha | [PRIV-08](02-privacidad-cookies-y-comunicaciones.md#33-priv-08-auditar-sdks-y-servicios-de-terceros) |
