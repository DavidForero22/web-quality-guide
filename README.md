# Recomendaciones para sitios web

Guía de buenas prácticas legales, de accesibilidad, SEO, rendimiento y mantenimiento para sitios y aplicaciones web. Cada medida indica su **prioridad**, el **sector** al que más afecta y la **región** donde la norma es más estricta.

> Última verificación: **2026-10-10**. Es una guía técnica y de buenas prácticas, **no asesoramiento jurídico**. Revisa los casos concretos con un profesional y comprueba el estado de las normas que están cambiando ([lista de cambios pendientes](guia/11-correcciones-y-verificacion.md)).

<!-- INDICE -->
**Índice**

- [1. Qué es este repositorio](#1-qué-es-este-repositorio)
- [2. Cómo está organizado](#2-cómo-está-organizado)
- [3. Cómo leer las fichas](#3-cómo-leer-las-fichas)
- [4. Cómo usar la guía en tu proyecto](#4-cómo-usar-la-guía-en-tu-proyecto)
- [5. Índice de medidas](#5-índice-de-medidas)
  - [5.1 Accesibilidad](#51-accesibilidad)
  - [5.2 Privacidad, cookies y comunicaciones](#52-privacidad-cookies-y-comunicaciones)
  - [5.3 Consumo y comercio](#53-consumo-y-comercio)
  - [5.4 Propiedad intelectual y contenido](#54-propiedad-intelectual-y-contenido)
  - [5.5 SEO](#55-seo)
  - [5.6 Rendimiento](#56-rendimiento)
  - [5.7 Diseño y experiencia de usuario](#57-diseño-y-experiencia-de-usuario)
  - [5.8 Seguridad y operación](#58-seguridad-y-operación)
  - [5.9 Post-lanzamiento y mantenimiento](#59-post-lanzamiento-y-mantenimiento)
- [6. Mantenimiento](#6-mantenimiento)
<!-- /INDICE -->

## 1. Qué es este repositorio

Recopila y contrasta varias listas de medidas (WCAG 2.2 AA, SEO y rendimiento, privacidad y cookies, comercio y transparencia, accesibilidad y pruebas). Se eliminaron duplicados, se corrigieron las afirmaciones que no resistían la verificación y cada medida se clasificó para poder filtrarla según tu proyecto.

La base jurídica es la **UE y España**. Se señalan las diferencias con **EE. UU., Reino Unido y Latinoamérica**.

**Fuera de alcance:** fiscalidad (IVA, facturación electrónica), sectores regulados (juego, salud, finanzas), marca y dominios. Consulta a un profesional del sector si aplican a tu proyecto.

## 2. Cómo está organizado

| Archivo | Contenido |
|---|---|
| [guia/01-accesibilidad.md](guia/01-accesibilidad.md) | Marco legal de accesibilidad y los 55 criterios de WCAG 2.2 A y AA |
| [guia/02-privacidad-cookies-y-comunicaciones.md](guia/02-privacidad-cookies-y-comunicaciones.md) | RGPD, cookies, terceros, menores y comunicaciones comerciales |
| [guia/03-consumo-y-comercio.md](guia/03-consumo-y-comercio.md) | Términos, suscripciones, devoluciones, precios, patrones oscuros, reseñas y afirmaciones |
| [guia/04-propiedad-intelectual-y-contenido.md](guia/04-propiedad-intelectual-y-contenido.md) | Licencias y contenido de usuarios |
| [guia/05-seo.md](guia/05-seo.md) | Indexación, sitemap, robots.txt, títulos y descripciones |
| [guia/06-rendimiento.md](guia/06-rendimiento.md) | PageSpeed Insights, Core Web Vitals e imágenes |
| [guia/07-diseno-y-experiencia-de-usuario.md](guia/07-diseno-y-experiencia-de-usuario.md) | Acción principal, design tokens, estados de carga y páginas de confirmación |
| [guia/08-seguridad-y-operacion.md](guia/08-seguridad-y-operacion.md) | HTTPS, cabeceras, accesos, actualizaciones, copias y monitorización |
| [guia/09-post-lanzamiento.md](guia/09-post-lanzamiento.md) | Pruebas tras publicar y calendario de revisiones |
| [guia/10-matriz.md](guia/10-matriz.md) | Vista transversal: prioridad, sector y región (generada) |
| [guia/11-correcciones-y-verificacion.md](guia/11-correcciones-y-verificacion.md) | Qué se corrigió, qué se fusionó y qué normas están cambiando |

## 3. Cómo leer las fichas

Cada medida tiene una ficha con estos campos:

| Campo | Valores |
|---|---|
| **Prioridad** | **Alta**: afecta a la mayoría de proyectos y tiene riesgo legal o de experiencia alto. **Media**: aporta valor claro o depende del contexto. **Baja**: opcional o de uso muy específico. |
| **Naturaleza** | **Obligación legal** · **Obligación legal condicionada** (solo si cumples ciertas condiciones: actividad, tamaño, mercado) · **Buena práctica** · **Opcional** |
| **Sectores** | `INF` informativo, educativo o blog · `TIE` tienda online · `SUS` suscripción o SaaS (pago recurrente) · `UGC` plataforma con contenido de usuarios · `MEN` servicios dirigidos a menores |
| **Regiones** | `UE/ES` Unión Europea y España · `EE. UU.` · `UK` Reino Unido · `LATAM` Latinoamérica |
| **Verificación** | ✅ Correcta · ⚠️ Matizada (cierta, con precisiones) · ❌ Corregida · ➕ Añadida (no estaba en las listas originales) |

**Símbolos de sector y región**

| Símbolo | En un sector | En una región |
|---|---|---|
| ● | Aplica o es prioritaria | Obligación directa o regulación más estricta |
| ◐ | Aplica según condiciones | Aplica con matices, por otra norma o solo en parte |
| ○ | No suele aplicar | Sin equivalente relevante |

Las medidas que no son legales (SEO, rendimiento, diseño y seguridad técnica) llevan ● en todas las regiones: son universales.

## 4. Cómo usar la guía en tu proyecto

1. **Identifica tu sector** (puedes ser varios: una tienda con blog es `TIE` + `INF`).
2. **Identifica tus regiones**: dónde estás, dónde están tus usuarios y a quién vendes. Empieza por [PRIV-01](guia/02-privacidad-cookies-y-comunicaciones.md#11-priv-01-determinar-qué-jurisdicciones-te-aplican).
3. **Abre la [matriz](guia/10-matriz.md)** y trabaja primero las medidas con prioridad Alta marcadas con ● en tu sector y tu región.
4. **Añade las condicionales (◐)** que te apliquen y revisa las medidas opcionales si adoptas esa herramienta.
5. **Programa las revisiones** con el [calendario de post-lanzamiento](guia/09-post-lanzamiento.md).

## 5. Índice de medidas

<!-- MEDIDAS -->
### 5.1 Accesibilidad

Archivo: [guia/01-accesibilidad.md](guia/01-accesibilidad.md) · 3 medida legal y 55 criterios WCAG

- **Marco legal**
  - [ACC-01](guia/01-accesibilidad.md#11-acc-01-obligaciones-legales-de-accesibilidad): Obligaciones legales de accesibilidad — *Alta · Obligación legal condicionada*
  - [ACC-02](guia/01-accesibilidad.md#12-acc-02-declaración-de-accesibilidad-y-canal-para-comunicar-barreras): Declaración de accesibilidad y canal para comunicar barreras — *Media · Obligación legal condicionada*
- **Principio 1: Perceptible**
  - [WCAG 1.1.1](guia/01-accesibilidad.md#21-wcag-111-contenido-no-textual-a): Contenido no textual (A) — *Alta · Nivel A*
  - [WCAG 1.2.1](guia/01-accesibilidad.md#22-wcag-121-solo-audio-y-solo-vídeo-pregrabado-a): Solo audio y solo vídeo, pregrabado (A) — *Media · Nivel A*
  - [WCAG 1.2.2](guia/01-accesibilidad.md#23-wcag-122-subtítulos-pregrabado-a): Subtítulos, pregrabado (A) — *Alta · Nivel A*
  - [WCAG 1.2.3](guia/01-accesibilidad.md#24-wcag-123-audiodescripción-o-alternativa-para-medios-pregrabado-a): Audiodescripción o alternativa para medios, pregrabado (A) — *Media · Nivel A*
  - [WCAG 1.2.4](guia/01-accesibilidad.md#25-wcag-124-subtítulos-en-directo-aa): Subtítulos en directo (AA) — *Media · Nivel AA*
  - [WCAG 1.2.5](guia/01-accesibilidad.md#26-wcag-125-audiodescripción-pregrabado-aa): Audiodescripción, pregrabado (AA) — *Media · Nivel AA*
  - [WCAG 1.3.1](guia/01-accesibilidad.md#27-wcag-131-información-y-relaciones-a): Información y relaciones (A) — *Alta · Nivel A*
  - [WCAG 1.3.2](guia/01-accesibilidad.md#28-wcag-132-secuencia-significativa-a): Secuencia significativa (A) — *Alta · Nivel A*
  - [WCAG 1.3.3](guia/01-accesibilidad.md#29-wcag-133-características-sensoriales-a): Características sensoriales (A) — *Media · Nivel A*
  - [WCAG 1.3.4](guia/01-accesibilidad.md#210-wcag-134-orientación-aa): Orientación (AA) — *Media · Nivel AA*
  - [WCAG 1.3.5](guia/01-accesibilidad.md#211-wcag-135-identificar-el-propósito-de-la-entrada-aa): Identificar el propósito de la entrada (AA) — *Media · Nivel AA*
  - [WCAG 1.4.1](guia/01-accesibilidad.md#212-wcag-141-uso-del-color-a): Uso del color (A) — *Alta · Nivel A*
  - [WCAG 1.4.2](guia/01-accesibilidad.md#213-wcag-142-control-del-audio-a): Control del audio (A) — *Media · Nivel A*
  - [WCAG 1.4.3](guia/01-accesibilidad.md#214-wcag-143-contraste-mínimo-aa): Contraste mínimo (AA) — *Alta · Nivel AA*
  - [WCAG 1.4.4](guia/01-accesibilidad.md#215-wcag-144-cambio-de-tamaño-del-texto-aa): Cambio de tamaño del texto (AA) — *Alta · Nivel AA*
  - [WCAG 1.4.5](guia/01-accesibilidad.md#216-wcag-145-imágenes-de-texto-aa): Imágenes de texto (AA) — *Media · Nivel AA*
  - [WCAG 1.4.10](guia/01-accesibilidad.md#217-wcag-1410-reflujo-aa): Reflujo (AA) — *Alta · Nivel AA*
  - [WCAG 1.4.11](guia/01-accesibilidad.md#218-wcag-1411-contraste-no-textual-aa): Contraste no textual (AA) — *Alta · Nivel AA*
  - [WCAG 1.4.12](guia/01-accesibilidad.md#219-wcag-1412-espaciado-del-texto-aa): Espaciado del texto (AA) — *Media · Nivel AA*
  - [WCAG 1.4.13](guia/01-accesibilidad.md#220-wcag-1413-contenido-al-pasar-el-puntero-o-recibir-foco-aa): Contenido al pasar el puntero o recibir foco (AA) — *Media · Nivel AA*
- **Principio 2: Operable**
  - [WCAG 2.1.1](guia/01-accesibilidad.md#31-wcag-211-teclado-a): Teclado (A) — *Alta · Nivel A*
  - [WCAG 2.1.2](guia/01-accesibilidad.md#32-wcag-212-sin-trampas-para-el-foco-del-teclado-a): Sin trampas para el foco del teclado (A) — *Alta · Nivel A*
  - [WCAG 2.1.4](guia/01-accesibilidad.md#33-wcag-214-atajos-de-teclado-de-un-solo-carácter-a): Atajos de teclado de un solo carácter (A) — *Media · Nivel A*
  - [WCAG 2.2.1](guia/01-accesibilidad.md#34-wcag-221-tiempo-ajustable-a): Tiempo ajustable (A) — *Media · Nivel A*
  - [WCAG 2.2.2](guia/01-accesibilidad.md#35-wcag-222-pausar-detener-ocultar-a): Pausar, detener, ocultar (A) — *Media · Nivel A*
  - [WCAG 2.3.1](guia/01-accesibilidad.md#36-wcag-231-umbral-de-tres-destellos-o-menos-a): Umbral de tres destellos o menos (A) — *Alta · Nivel A*
  - [WCAG 2.4.1](guia/01-accesibilidad.md#37-wcag-241-evitar-bloques-a): Evitar bloques (A) — *Alta · Nivel A*
  - [WCAG 2.4.2](guia/01-accesibilidad.md#38-wcag-242-titulado-de-páginas-a): Titulado de páginas (A) — *Alta · Nivel A*
  - [WCAG 2.4.3](guia/01-accesibilidad.md#39-wcag-243-orden-del-foco-a): Orden del foco (A) — *Alta · Nivel A*
  - [WCAG 2.4.4](guia/01-accesibilidad.md#310-wcag-244-propósito-de-los-enlaces-en-contexto-a): Propósito de los enlaces, en contexto (A) — *Alta · Nivel A*
  - [WCAG 2.4.5](guia/01-accesibilidad.md#311-wcag-245-múltiples-vías-aa): Múltiples vías (AA) — *Media · Nivel AA*
  - [WCAG 2.4.6](guia/01-accesibilidad.md#312-wcag-246-encabezados-y-etiquetas-aa): Encabezados y etiquetas (AA) — *Media · Nivel AA*
  - [WCAG 2.4.7](guia/01-accesibilidad.md#313-wcag-247-foco-visible-aa): Foco visible (AA) — *Alta · Nivel AA*
  - [WCAG 2.4.11](guia/01-accesibilidad.md#314-wcag-2411-foco-no-oculto-mínimo-aa): Foco no oculto, mínimo (AA) — *Alta · Nivel AA*
  - [WCAG 2.5.1](guia/01-accesibilidad.md#315-wcag-251-gestos-del-puntero-a): Gestos del puntero (A) — *Media · Nivel A*
  - [WCAG 2.5.2](guia/01-accesibilidad.md#316-wcag-252-cancelación-del-puntero-a): Cancelación del puntero (A) — *Media · Nivel A*
  - [WCAG 2.5.3](guia/01-accesibilidad.md#317-wcag-253-etiqueta-en-el-nombre-a): Etiqueta en el nombre (A) — *Media · Nivel A*
  - [WCAG 2.5.4](guia/01-accesibilidad.md#318-wcag-254-activación-por-movimiento-a): Activación por movimiento (A) — *Media · Nivel A*
  - [WCAG 2.5.7](guia/01-accesibilidad.md#319-wcag-257-movimientos-de-arrastre-aa): Movimientos de arrastre (AA) — *Media · Nivel AA*
  - [WCAG 2.5.8](guia/01-accesibilidad.md#320-wcag-258-tamaño-del-objetivo-mínimo-aa): Tamaño del objetivo, mínimo (AA) — *Alta · Nivel AA*
- **Principio 3: Comprensible**
  - [WCAG 3.1.1](guia/01-accesibilidad.md#41-wcag-311-idioma-de-la-página-a): Idioma de la página (A) — *Alta · Nivel A*
  - [WCAG 3.1.2](guia/01-accesibilidad.md#42-wcag-312-idioma-de-las-partes-aa): Idioma de las partes (AA) — *Media · Nivel AA*
  - [WCAG 3.2.1](guia/01-accesibilidad.md#43-wcag-321-al-recibir-el-foco-a): Al recibir el foco (A) — *Alta · Nivel A*
  - [WCAG 3.2.2](guia/01-accesibilidad.md#44-wcag-322-al-recibir-entradas-a): Al recibir entradas (A) — *Alta · Nivel A*
  - [WCAG 3.2.3](guia/01-accesibilidad.md#45-wcag-323-navegación-coherente-aa): Navegación coherente (AA) — *Media · Nivel AA*
  - [WCAG 3.2.4](guia/01-accesibilidad.md#46-wcag-324-identificación-coherente-aa): Identificación coherente (AA) — *Media · Nivel AA*
  - [WCAG 3.2.6](guia/01-accesibilidad.md#47-wcag-326-ayuda-coherente-a): Ayuda coherente (A) — *Media · Nivel A*
  - [WCAG 3.3.1](guia/01-accesibilidad.md#48-wcag-331-identificación-de-errores-a): Identificación de errores (A) — *Alta · Nivel A*
  - [WCAG 3.3.2](guia/01-accesibilidad.md#49-wcag-332-etiquetas-o-instrucciones-a): Etiquetas o instrucciones (A) — *Alta · Nivel A*
  - [WCAG 3.3.3](guia/01-accesibilidad.md#410-wcag-333-sugerencias-ante-errores-aa): Sugerencias ante errores (AA) — *Media · Nivel AA*
  - [WCAG 3.3.4](guia/01-accesibilidad.md#411-wcag-334-prevención-de-errores-legales-financieros-o-de-datos-aa): Prevención de errores, legales, financieros o de datos (AA) — *Media · Nivel AA*
  - [WCAG 3.3.7](guia/01-accesibilidad.md#412-wcag-337-entrada-redundante-a): Entrada redundante (A) — *Media · Nivel A*
  - [WCAG 3.3.8](guia/01-accesibilidad.md#413-wcag-338-autenticación-accesible-mínimo-aa): Autenticación accesible, mínimo (AA) — *Alta · Nivel AA*
- **Principio 4: Robusto**
  - [WCAG 4.1.2](guia/01-accesibilidad.md#51-wcag-412-nombre-función-valor-a): Nombre, función, valor (A) — *Alta · Nivel A*
  - [WCAG 4.1.3](guia/01-accesibilidad.md#52-wcag-413-mensajes-de-estado-aa): Mensajes de estado (AA) — *Media · Nivel AA*
- **Documentos y contenido de terceros**
  - [ACC-03](guia/01-accesibilidad.md#61-acc-03-documentos-descargables-y-contenido-de-terceros): Documentos descargables y contenido de terceros — *Media · Obligación legal condicionada*

### 5.2 Privacidad, cookies y comunicaciones

Archivo: [guia/02-privacidad-cookies-y-comunicaciones.md](guia/02-privacidad-cookies-y-comunicaciones.md) · 18 medidas

- **Alcance jurídico**
  - [PRIV-01](guia/02-privacidad-cookies-y-comunicaciones.md#11-priv-01-determinar-qué-jurisdicciones-te-aplican): Determinar qué jurisdicciones te aplican — *Alta · Obligación legal*
- **Información, base jurídica y derechos**
  - [PRIV-02](guia/02-privacidad-cookies-y-comunicaciones.md#21-priv-02-política-de-privacidad): Política de privacidad — *Alta · Obligación legal*
  - [PRIV-03](guia/02-privacidad-cookies-y-comunicaciones.md#22-priv-03-no-recopilar-datos-innecesarios): No recopilar datos innecesarios — *Alta · Obligación legal*
  - [PRIV-04](guia/02-privacidad-cookies-y-comunicaciones.md#23-priv-04-comprobar-los-formularios-de-consentimiento): Comprobar los formularios de consentimiento — *Alta · Obligación legal condicionada*
  - [PRIV-05](guia/02-privacidad-cookies-y-comunicaciones.md#24-priv-05-proceso-de-eliminación-de-datos-y-ejercicio-de-derechos): Proceso de eliminación de datos y ejercicio de derechos — *Alta · Obligación legal*
- **Cookies y tecnologías de seguimiento**
  - [PRIV-06](guia/02-privacidad-cookies-y-comunicaciones.md#31-priv-06-política-de-cookies): Política de cookies — *Alta · Obligación legal condicionada*
  - [PRIV-07](guia/02-privacidad-cookies-y-comunicaciones.md#32-priv-07-banner-de-consentimiento-de-cookies): Banner de consentimiento de cookies — *Alta · Obligación legal condicionada*
  - [PRIV-08](guia/02-privacidad-cookies-y-comunicaciones.md#33-priv-08-auditar-sdks-y-servicios-de-terceros): Auditar SDKs y servicios de terceros — *Alta · Obligación legal*
  - [PRIV-09](guia/02-privacidad-cookies-y-comunicaciones.md#34-priv-09-cargar-las-fuentes-de-google-desde-tu-propio-servidor): Cargar las fuentes de Google desde tu propio servidor — *Media · Buena práctica*
  - [PRIV-10](guia/02-privacidad-cookies-y-comunicaciones.md#35-priv-10-grabación-de-sesiones-session-replay): Grabación de sesiones (session replay) — *Alta · Obligación legal condicionada*
  - [PRIV-11](guia/02-privacidad-cookies-y-comunicaciones.md#36-priv-11-microsoft-clarity): Microsoft Clarity — *Baja · Opcional*
  - [PRIV-12](guia/02-privacidad-cookies-y-comunicaciones.md#37-priv-12-meta-pixel): Meta Pixel — *Baja · Opcional*
- **Menores**
  - [PRIV-13](guia/02-privacidad-cookies-y-comunicaciones.md#41-priv-13-no-pedir-la-edad-a-los-usuarios): No pedir la edad a los usuarios — *Media · Buena práctica*
  - [PRIV-14](guia/02-privacidad-cookies-y-comunicaciones.md#42-priv-14-consentimiento-para-datos-de-menores): Consentimiento para datos de menores — *Alta · Obligación legal condicionada*
- **Comunicaciones comerciales**
  - [PRIV-15](guia/02-privacidad-cookies-y-comunicaciones.md#51-priv-15-autorización-previa-y-enlace-de-baja-en-el-correo-comercial): Autorización previa y enlace de baja en el correo comercial — *Alta · Obligación legal*
  - [PRIV-16](guia/02-privacidad-cookies-y-comunicaciones.md#52-priv-16-cumplimiento-de-can-spam-y-su-multa-por-correo): Cumplimiento de CAN-SPAM y su multa por correo — *Media · Obligación legal condicionada*
- **Responsabilidad proactiva y brechas**
  - [PRIV-17](guia/02-privacidad-cookies-y-comunicaciones.md#61-priv-17-registro-de-tratamientos-eipd-y-delegado-de-protección-de-datos): Registro de tratamientos, EIPD y delegado de protección de datos — *Alta · Obligación legal*
  - [PRIV-18](guia/02-privacidad-cookies-y-comunicaciones.md#62-priv-18-brechas-de-seguridad-e-incidentes): Brechas de seguridad e incidentes — *Alta · Obligación legal*

### 5.3 Consumo y comercio

Archivo: [guia/03-consumo-y-comercio.md](guia/03-consumo-y-comercio.md) · 10 medidas

- **Identificación y contratación**
  - [COM-01](guia/03-consumo-y-comercio.md#11-com-01-datos-del-negocio-en-la-web): Datos del negocio en la web — *Alta · Obligación legal*
  - [COM-02](guia/03-consumo-y-comercio.md#12-com-02-términos-y-condiciones-del-servicio): Términos y condiciones del servicio — *Alta · Obligación legal condicionada*
  - [COM-03](guia/03-consumo-y-comercio.md#13-com-03-renovación-y-cobros-recurrentes-antes-del-pago): Renovación y cobros recurrentes antes del pago — *Alta · Obligación legal*
  - [COM-04](guia/03-consumo-y-comercio.md#14-com-04-política-de-reembolsos-y-desistimiento): Política de reembolsos y desistimiento — *Alta · Obligación legal*
- **Transparencia y prácticas comerciales**
  - [COM-05](guia/03-consumo-y-comercio.md#21-com-05-eliminar-gastos-ocultos): Eliminar gastos ocultos — *Alta · Obligación legal*
  - [COM-06](guia/03-consumo-y-comercio.md#22-com-06-eliminar-patrones-oscuros): Eliminar patrones oscuros — *Alta · Obligación legal*
  - [COM-07](guia/03-consumo-y-comercio.md#23-com-07-eliminar-reseñas-falsas): Eliminar reseñas falsas — *Alta · Obligación legal*
  - [COM-08](guia/03-consumo-y-comercio.md#24-com-08-eliminar-afirmaciones-sin-fundamento): Eliminar afirmaciones sin fundamento — *Alta · Obligación legal*
- **Garantías y resolución de conflictos**
  - [COM-09](guia/03-consumo-y-comercio.md#31-com-09-resolución-de-litigios-adr-y-retirada-del-enlace-a-la-plataforma-odr): Resolución de litigios (ADR) y retirada del enlace a la plataforma ODR — *Media · Obligación legal condicionada*
  - [COM-10](guia/03-consumo-y-comercio.md#32-com-10-contenido-y-servicios-digitales-conformidad-y-actualizaciones): Contenido y servicios digitales: conformidad y actualizaciones — *Alta · Obligación legal*

### 5.4 Propiedad intelectual y contenido

Archivo: [guia/04-propiedad-intelectual-y-contenido.md](guia/04-propiedad-intelectual-y-contenido.md) · 4 medidas

- **Recursos de terceros**
  - [PI-01](guia/04-propiedad-intelectual-y-contenido.md#11-pi-01-licenciar-fuentes-e-imágenes): Licenciar fuentes e imágenes — *Alta · Obligación legal*
  - [PI-02](guia/04-propiedad-intelectual-y-contenido.md#12-pi-02-usuarios-que-suben-contenido-avisos-de-infracción-y-agente-dmca): Usuarios que suben contenido: avisos de infracción y agente DMCA — *Media · Obligación legal condicionada*
- **Contenido y personas**
  - [PI-03](guia/04-propiedad-intelectual-y-contenido.md#21-pi-03-política-de-uso-aceptable-y-moderación-de-contenido): Política de uso aceptable y moderación de contenido — *Alta · Obligación legal condicionada*
  - [PI-04](guia/04-propiedad-intelectual-y-contenido.md#22-pi-04-derechos-de-imagen-de-las-personas): Derechos de imagen de las personas — *Alta · Obligación legal*

### 5.5 SEO

Archivo: [guia/05-seo.md](guia/05-seo.md) · 13 medidas

- **Presencia e indexación**
  - [SEO-01](guia/05-seo.md#11-seo-01-registrar-la-web-en-search-console): Registrar la web en Search Console — *Alta · Buena práctica*
  - [SEO-02](guia/05-seo.md#12-seo-02-solicitar-a-google-que-indexe-la-web): Solicitar a Google que indexe la web — *Media · Buena práctica*
  - [SEO-03](guia/05-seo.md#13-seo-03-generar-sitemapxml): Generar sitemap.xml — *Media · Buena práctica*
  - [SEO-04](guia/05-seo.md#14-seo-04-generar-robotstxt): Generar robots.txt — *Media · Buena práctica*
- **Contenido en resultados**
  - [SEO-05](guia/05-seo.md#21-seo-05-títulos-y-descripciones-personalizados): Títulos y descripciones personalizados — *Alta · Buena práctica*
- **Estructura y señales técnicas**
  - [SEO-06](guia/05-seo.md#31-seo-06-canónicas-y-contenido-duplicado): Canónicas y contenido duplicado — *Media · Buena práctica*
  - [SEO-07](guia/05-seo.md#32-seo-07-redirecciones-301-y-páginas-404): Redirecciones 301 y páginas 404 — *Alta · Buena práctica*
  - [SEO-08](guia/05-seo.md#33-seo-08-compatibilidad-móvil-e-indexación-centrada-en-móviles): Compatibilidad móvil e indexación centrada en móviles — *Alta · Buena práctica*
  - [SEO-09](guia/05-seo.md#34-seo-09-datos-estructurados): Datos estructurados — *Media · Buena práctica*
  - [SEO-10](guia/05-seo.md#35-seo-10-hreflang-para-versiones-por-idioma-o-región): hreflang para versiones por idioma o región — *Media · Buena práctica*
  - [SEO-11](guia/05-seo.md#36-seo-11-enlazado-interno-y-arquitectura-de-la-información): Enlazado interno y arquitectura de la información — *Media · Buena práctica*
- **Identidad y vista previa**
  - [SEO-12](guia/05-seo.md#41-seo-12-favicon): Favicon — *Media · Buena práctica*
  - [SEO-13](guia/05-seo.md#42-seo-13-open-graph-y-vista-previa-al-compartir): Open Graph y vista previa al compartir — *Media · Buena práctica*

### 5.6 Rendimiento

Archivo: [guia/06-rendimiento.md](guia/06-rendimiento.md) · 9 medidas

- **Medición**
  - [REN-01](guia/06-rendimiento.md#11-ren-01-medir-con-pagespeed-insights): Medir con PageSpeed Insights — *Alta · Buena práctica*
  - [REN-02](guia/06-rendimiento.md#12-ren-02-revisar-core-web-vitals): Revisar Core Web Vitals — *Alta · Buena práctica*
- **Recursos**
  - [REN-03](guia/06-rendimiento.md#21-ren-03-comprimir-imágenes-y-usar-formatos-modernos): Comprimir imágenes y usar formatos modernos — *Alta · Buena práctica*
- **Entrega y carga**
  - [REN-04](guia/06-rendimiento.md#31-ren-04-caché-http-cdn-y-compresión): Caché HTTP, CDN y compresión — *Alta · Buena práctica*
  - [REN-05](guia/06-rendimiento.md#32-ren-05-fuentes-web-y-javascript-de-terceros): Fuentes web y JavaScript de terceros — *Media · Buena práctica*
  - [REN-06](guia/06-rendimiento.md#33-ren-06-presupuesto-de-rendimiento-y-monitorización-con-datos-reales): Presupuesto de rendimiento y monitorización con datos reales — *Media · Buena práctica*
  - [REN-07](guia/06-rendimiento.md#34-ren-07-vídeo-y-contenido-incrustado): Vídeo y contenido incrustado — *Media · Buena práctica*
- **Base de datos**
  - [REN-08](guia/06-rendimiento.md#41-ren-08-índices-en-la-base-de-datos): Índices en la base de datos — *Alta · Buena práctica*
  - [REN-09](guia/06-rendimiento.md#42-ren-09-evitar-consultas-n1): Evitar consultas N+1 — *Alta · Buena práctica*

### 5.7 Diseño y experiencia de usuario

Archivo: [guia/07-diseno-y-experiencia-de-usuario.md](guia/07-diseno-y-experiencia-de-usuario.md) · 4 medidas

- **Claridad y consistencia**
  - [UX-01](guia/07-diseno-y-experiencia-de-usuario.md#11-ux-01-acción-principal-clara-y-reducción-de-opciones): Acción principal clara y reducción de opciones — *Media · Buena práctica*
  - [UX-02](guia/07-diseno-y-experiencia-de-usuario.md#12-ux-02-design-tokens): Design tokens — *Media · Buena práctica*
- **Estados y conversión**
  - [UX-03](guia/07-diseno-y-experiencia-de-usuario.md#21-ux-03-estados-de-carga-skeletons-spinners-y-barras-de-progreso): Estados de carga: skeletons, spinners y barras de progreso — *Baja · Buena práctica*
  - [UX-04](guia/07-diseno-y-experiencia-de-usuario.md#22-ux-04-página-de-confirmación-tras-una-conversión): Página de confirmación tras una conversión — *Media · Buena práctica*

### 5.8 Seguridad y operación

Archivo: [guia/08-seguridad-y-operacion.md](guia/08-seguridad-y-operacion.md) · 5 medidas

- **Protección del sitio**
  - [SEG-01](guia/08-seguridad-y-operacion.md#11-seg-01-https-y-cabeceras-de-seguridad): HTTPS y cabeceras de seguridad — *Alta · Obligación legal condicionada*
  - [SEG-02](guia/08-seguridad-y-operacion.md#12-seg-02-secretos-accesos-y-autenticación-multifactor): Secretos, accesos y autenticación multifactor — *Alta · Buena práctica*
  - [SEG-03](guia/08-seguridad-y-operacion.md#13-seg-03-actualizaciones-y-análisis-de-vulnerabilidades): Actualizaciones y análisis de vulnerabilidades — *Alta · Buena práctica*
- **Continuidad y observabilidad**
  - [SEG-04](guia/08-seguridad-y-operacion.md#21-seg-04-copias-de-seguridad-y-restauración-probada): Copias de seguridad y restauración probada — *Alta · Buena práctica*
  - [SEG-05](guia/08-seguridad-y-operacion.md#22-seg-05-disponibilidad-errores-y-registros): Disponibilidad, errores y registros — *Media · Buena práctica*

### 5.9 Post-lanzamiento y mantenimiento

Archivo: [guia/09-post-lanzamiento.md](guia/09-post-lanzamiento.md) · 3 medidas

- **Verificación tras la publicación**
  - [POST-01](guia/09-post-lanzamiento.md#11-post-01-testear-formularios): Testear formularios — *Alta · Buena práctica*
- **Mantenimiento recurrente**
  - [POST-02](guia/09-post-lanzamiento.md#21-post-02-plan-de-revisiones-periódicas): Plan de revisiones periódicas — *Alta · Buena práctica*
  - [POST-03](guia/09-post-lanzamiento.md#22-post-03-revisión-de-enlaces-rotos-y-calidad-del-contenido): Revisión de enlaces rotos y calidad del contenido — *Media · Buena práctica*
<!-- /MEDIDAS -->

## 6. Mantenimiento

Los números de los encabezados, los índices, los enlaces cruzados, la matriz y el índice de medidas se **generan automáticamente**. Después de editar o añadir una medida, ejecuta:

```bash
python herramientas/actualizar-indices.py
```

Para añadir una medida, escribe un encabezado de nivel 3 con su identificador (`### PRIV-17: Título`), la ficha con los cinco campos y, en el texto, enlaza otras medidas con `[[ID]]` (por ejemplo, `[[PRIV-08]]` o `[[WCAG 1.4.3]]`). El script numera los encabezados y resuelve los enlaces.

Plantilla de ficha:

```markdown
### PRIV-17: Título de la medida

- **Prioridad:** Alta
- **Naturaleza:** Obligación legal
- **Sectores:** INF ◐ · TIE ● · SUS ● · UGC ● · MEN ●
- **Regiones:** UE/ES ● · EE. UU. ◐ · UK ● · LATAM ◐
- **Verificación:** ✅ Correcta
```
