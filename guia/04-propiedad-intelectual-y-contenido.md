# Propiedad intelectual y contenido

> Última verificación: 2026-10-10 · [Volver al README](../README.md)

Derechos sobre las fuentes, imágenes y otros recursos que usas, y responsabilidad por el contenido que suben tus usuarios.

> Esto es una guía técnica y de buenas prácticas, no asesoramiento jurídico.

<!-- INDICE -->
**Índice**

- [1. Recursos de terceros](#1-recursos-de-terceros)
  - [1.1 PI-01: Licenciar fuentes e imágenes](#11-pi-01-licenciar-fuentes-e-imágenes)
  - [1.2 PI-02: Usuarios que suben contenido: avisos de infracción y agente DMCA](#12-pi-02-usuarios-que-suben-contenido-avisos-de-infracción-y-agente-dmca)
- [2. Posibles lagunas](#2-posibles-lagunas)
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
- EE. UU.: registrar el agente en el directorio de la Copyright Office y mostrar sus datos en la web; anotar la fecha de renovación (ver [POST-02](07-post-lanzamiento.md#21-post-02-plan-de-revisiones-periódicas)).
- UE: los servicios de alojamiento deben tener un mecanismo de notificación y acción fácil de usar, y motivar sus decisiones (arts. 16 y 17 DSA). Las microempresas y pequeñas empresas que sean plataformas en línea están exentas de las obligaciones adicionales de plataforma (sección 3), **no** del mecanismo de notificación.
- España: responsabilidad del prestador de alojamiento limitada al conocimiento efectivo y actuación diligente (art. 16 LSSI, ahora coordinada con el DSA).
- Reino Unido: servicios con contenido de usuarios pueden estar sujetos a la *Online Safety Act* (Ofcom).

**Fuentes**

- [Copyright Office: DMCA Designated Agent Directory, preguntas frecuentes](https://www.copyright.gov/dmca-directory/faq.html)
- [DSA arts. 6, 16 y 19 (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2022/2065/oj)
- [LSSI-CE art. 16 (BOE)](https://www.boe.es/buscar/act.php?id=BOE-A-2002-13758)

## 2. Posibles lagunas

Medidas relevantes que **no estaban en tus listas** y no se han desarrollado:

- Política de uso aceptable y de moderación de contenido.
- Protección de marca, nombres de dominio y signos distintivos propios.
- Cumplimiento de la Directiva europea sobre derechos de autor en el mercado único digital (art. 17) para plataformas de intercambio de contenidos.
- Derechos de imagen y de las personas que aparecen en el contenido (consentimiento de retrato).
- Licencias de datos y datasets, y condiciones de las APIs de terceros.
