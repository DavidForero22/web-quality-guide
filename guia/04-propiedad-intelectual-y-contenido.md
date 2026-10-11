# Propiedad intelectual y contenido

> Última verificación: 2026-10-10 · [Volver al README](../README.md)

Derechos sobre las fuentes, imágenes y otros recursos que usas, y responsabilidad por el contenido que suben tus usuarios.

> Esto es una guía técnica y de buenas prácticas, no asesoramiento jurídico.

<!-- INDICE -->
**Índice**

- [1. Recursos de terceros](#1-recursos-de-terceros)
  - [1.1 PI-01: Licenciar fuentes e imágenes](#11-pi-01-licenciar-fuentes-e-imágenes)
  - [1.2 PI-02: Usuarios que suben contenido: avisos de infracción y agente DMCA](#12-pi-02-usuarios-que-suben-contenido-avisos-de-infracción-y-agente-dmca)
- [2. Contenido y personas](#2-contenido-y-personas)
  - [2.1 PI-03: Política de uso aceptable y moderación de contenido](#21-pi-03-política-de-uso-aceptable-y-moderación-de-contenido)
  - [2.2 PI-04: Derechos de imagen de las personas](#22-pi-04-derechos-de-imagen-de-las-personas)
<!-- /INDICE -->

## 1. Recursos de terceros

### 1.1 PI-01: Licenciar fuentes e imágenes

- **Prioridad:** Alta
- **Naturaleza:** Obligación legal
- **Sectores:** INF ● · TIE ● · SUS ● · UGC ● · MEN ●
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ✅ Correcta

**De qué trata.** Verificar que tienes derechos de uso sobre cada recurso (tipografías, imágenes, iconos, música, vídeo, plantillas, código) y que la licencia permite tu uso concreto: comercial, modificación, redistribución, uso en plantillas o en producto final.

**Qué hacer**

- Mantener un registro: recurso, autor, licencia, URL de origen, fecha y comprobante de compra.
- Revisar condiciones que se pasan por alto: la licencia de **fuente web** suele ser distinta de la de escritorio; **Creative Commons** puede exigir atribución (BY), prohibir uso comercial (NC) o prohibir obras derivadas (ND).
- Comprobar las licencias del **código** de terceros (MIT, Apache, GPL: algunas exigen atribución o liberar tus modificaciones).
- Respetar los términos de las **herramientas de generación de imágenes con IA** respecto al uso comercial.
- Para **datos, datasets y APIs de terceros**: revisar permisos de reutilización, atribución, restricciones comerciales, límites técnicos (cuotas, caché) y condiciones de salida o continuidad si el proveedor cambia o retira el servicio.
- Para las imágenes **subidas por usuarios**: definir en los términos qué permisos concede el usuario (licencia no exclusiva para operar el servicio) y garantizar que tiene derechos; ver [PI-02](04-propiedad-intelectual-y-contenido.md#12-pi-02-usuarios-que-suben-contenido-avisos-de-infracción-y-agente-dmca).

**Por región.** Los derechos de autor se reconocen en prácticamente todos los países por tratados internacionales. En EE. UU. el *fair use* es una defensa que se decide caso por caso: no es una licencia en la que apoyarse por defecto.

**Fuentes:** [Creative Commons: licencias](https://creativecommons.org/share-your-work/cclicenses/)

### 1.2 PI-02: Usuarios que suben contenido: avisos de infracción y agente DMCA

- **Prioridad:** Media (si alojas contenido de usuarios, y más si buscas operar en EE. UU.) · Baja (sitio corriente sin subidas)
- **Naturaleza:** Obligación legal condicionada
- **Sectores:** INF ○ · TIE ◐ · SUS ◐ · UGC ● · MEN ◐
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ◐
- **Verificación:** ⚠️ Matizada

**De qué trata.** Si permites que los usuarios suban fotos u otro contenido, necesitas un procedimiento para recibir y gestionar avisos de infracción. En EE. UU. un **agente designado DMCA** es uno de los requisitos para acogerse al «puerto seguro» de la sección 512; en la UE existen obligaciones propias.

**Matices sobre la lista original**

- La cifra **existe**: la Oficina de Derechos de Autor de EE. UU. cobra **6 $** por designar, enmendar o renovar un agente (la lista decía «6 €»; la moneda es el dólar).
- **Pagarla no elimina el riesgo de demanda** ni es un requisito general para toda web que acepte fotos: es una de las condiciones para acogerse a ciertas protecciones de puerto seguro, que además exigen gestionar avisos y contraavisos, aplicar una política de infractores reincidentes y no tener conocimiento efectivo de la infracción.
- La designación **caduca a los 3 años** salvo que se renueve; un registro caducado equivale a no tener agente.
- En la UE las reglas son distintas y dependen del tipo de servicio.

**Qué hacer**

- Publicar un procedimiento de notificación accesible y un contacto específico.
- EE. UU.: registrar el agente en el directorio de la Copyright Office y mostrar sus datos en la web; anotar la fecha de renovación (ver [POST-02](09-post-lanzamiento.md#21-post-02-plan-de-revisiones-periódicas)).
- UE: los servicios de alojamiento deben tener un mecanismo de notificación y acción fácil de usar, y motivar sus decisiones (arts. 16 y 17 DSA). Las microempresas y pequeñas empresas que sean plataformas en línea están exentas de las obligaciones adicionales de plataforma (sección 3), **no** del mecanismo de notificación.
- España: responsabilidad del prestador de alojamiento limitada al conocimiento efectivo y actuación diligente (art. 16 LSSI, ahora coordinada con el DSA).
- Reino Unido: servicios con contenido de usuarios pueden estar sujetos a la *Online Safety Act* (Ofcom).

**Alcance de otras normas**

- **DSA, mercados en línea:** la trazabilidad de comerciantes y otras obligaciones reforzadas se dirigen a los **mercados en línea** que conectan consumidores con vendedores terceros, no a cualquier tienda que venda sus propios productos. Las obligaciones concretas varían por tipo y tamaño del servicio.
- **Directiva de derechos de autor, art. 17:** aplica a los proveedores de servicios para compartir contenidos en línea (plataformas cuyo fin principal es almacenar y dar acceso a gran cantidad de obras subidas por usuarios), no a cualquier sitio con comentarios o que aloje archivos.

**Fuentes**

- [Copyright Office: DMCA Designated Agent Directory, preguntas frecuentes](https://www.copyright.gov/dmca-directory/faq.html)
- [DSA arts. 6, 16 y 19 (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2022/2065/oj)
- [LSSI-CE art. 16 (BOE)](https://www.boe.es/buscar/act.php?id=BOE-A-2002-13758)
- [Directiva (UE) 2019/790, art. 17](https://eur-lex.europa.eu/eli/dir/2019/790/oj)

## 2. Contenido y personas

### 2.1 PI-03: Política de uso aceptable y moderación de contenido

- **Prioridad:** Alta (si permites publicar, compartir o comentar)
- **Naturaleza:** Obligación legal condicionada
- **Sectores:** INF ◐ · TIE ◐ · SUS ◐ · UGC ● · MEN ◐
- **Regiones:** UE/ES ● · EE. UU. ◐ · UK ● · LATAM ◐
- **Verificación:** ➕ Añadida

**De qué trata.** Reglas claras sobre qué se puede publicar y cómo se modera. Para una web corporativa estática basta una política sencilla; si hay contenido de usuarios, es el contrato que sostiene tus decisiones de retirada.

**Qué hacer**

- Redactar una política de uso aceptable en lenguaje claro: qué está prohibido, qué consecuencias tiene y cómo se reclama una decisión.
- **UE:** los términos de todo servicio intermediario deben informar de las restricciones al contenido de los usuarios y de las políticas de moderación, incluidas las herramientas automatizadas y la revisión humana, y avisar de cambios significativos (art. 14 DSA). No hay exención para microempresas en este artículo.
- Conectar la política con el canal de notificación de contenido ilegal ([PI-02](04-propiedad-intelectual-y-contenido.md#12-pi-02-usuarios-que-suben-contenido-avisos-de-infracción-y-agente-dmca)) y con la protección de menores ([PRIV-14](02-privacidad-cookies-y-comunicaciones.md#42-priv-14-consentimiento-para-datos-de-menores)).
- Registrar las decisiones de moderación y su motivo.
- **Reino Unido:** los servicios con contenido de usuarios pueden estar sujetos a la *Online Safety Act*; evalúa si te alcanza.

**Fuentes:** [DSA, art. 14 (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2022/2065/oj)

### 2.2 PI-04: Derechos de imagen de las personas

- **Prioridad:** Alta (si publicas imágenes de personas identificables)
- **Naturaleza:** Obligación legal
- **Sectores:** INF ◐ · TIE ◐ · SUS ○ · UGC ● · MEN ●
- **Regiones:** UE/ES ● · EE. UU. ◐ · UK ◐ · LATAM ◐
- **Verificación:** ➕ Añadida

**De qué trata.** Publicar la imagen de una persona identificable afecta a dos normas a la vez: el derecho a la propia imagen (en España, LO 1/1982) y la protección de datos (RGPD y LOPDGDD). No basta con que la foto sea visible en otro sitio: su visibilidad pública no equivale a autorización.

**Qué hacer**

- Obtener el consentimiento expreso de la persona, **específico para cada uso** (web, redes, material comercial). Un permiso para un uso no sirve para otro.
- Para menores, el consentimiento de quienes ejerzan la patria potestad; por debajo de 14 años lo recomienda la AEPD y la LO 1/1996 impide cualquier uso contrario a su interés aunque exista consentimiento.
- No reutilizar fotos de perfiles de redes sociales sin permiso (la jurisprudencia del Tribunal Supremo exige consentimiento expreso).
- Con bancos de imágenes, comprobar que cubren el uso comercial y que incluyen autorización de las personas que aparecen (*model release*).
- Conservar la prueba del consentimiento y poder retirar la imagen si se revoca.

**Por región.** EE. UU.: derecho de publicidad regulado por cada estado. Reino Unido y LATAM: reglas nacionales sobre imagen y datos personales.

**Fuentes**

- [LO 1/1982 (BOE)](https://www.boe.es/buscar/act.php?id=BOE-A-1982-11196)
- [AEPD](https://www.aepd.es/)
