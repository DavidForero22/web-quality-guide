# Privacidad, cookies y comunicaciones

> Última verificación: 2026-10-10 · [Volver al README](../README.md)

Protección de datos personales, cookies y tecnologías de seguimiento, terceros, menores y comunicaciones comerciales. La base es el **RGPD** y la **LSSI-CE** (UE/España); en cada medida se indica qué cambia en EE. UU., Reino Unido y Latinoamérica.

> Esto es una guía técnica y de buenas prácticas, no asesoramiento jurídico. Contrasta los casos concretos con un profesional.

<!-- INDICE -->
**Índice**

- [1. Alcance jurídico](#1-alcance-jurídico)
  - [1.1 PRIV-01: Determinar qué jurisdicciones te aplican](#11-priv-01-determinar-qué-jurisdicciones-te-aplican)
- [2. Información, base jurídica y derechos](#2-información-base-jurídica-y-derechos)
  - [2.1 PRIV-02: Política de privacidad](#21-priv-02-política-de-privacidad)
  - [2.2 PRIV-03: No recopilar datos innecesarios](#22-priv-03-no-recopilar-datos-innecesarios)
  - [2.3 PRIV-04: Comprobar los formularios de consentimiento](#23-priv-04-comprobar-los-formularios-de-consentimiento)
  - [2.4 PRIV-05: Proceso de eliminación de datos y ejercicio de derechos](#24-priv-05-proceso-de-eliminación-de-datos-y-ejercicio-de-derechos)
- [3. Cookies y tecnologías de seguimiento](#3-cookies-y-tecnologías-de-seguimiento)
  - [3.1 PRIV-06: Política de cookies](#31-priv-06-política-de-cookies)
  - [3.2 PRIV-07: Banner de consentimiento de cookies](#32-priv-07-banner-de-consentimiento-de-cookies)
  - [3.3 PRIV-08: Auditar SDKs y servicios de terceros](#33-priv-08-auditar-sdks-y-servicios-de-terceros)
  - [3.4 PRIV-09: Cargar las fuentes de Google desde tu propio servidor](#34-priv-09-cargar-las-fuentes-de-google-desde-tu-propio-servidor)
  - [3.5 PRIV-10: Grabación de sesiones (session replay)](#35-priv-10-grabación-de-sesiones-session-replay)
  - [3.6 PRIV-11: Microsoft Clarity](#36-priv-11-microsoft-clarity)
  - [3.7 PRIV-12: Meta Pixel](#37-priv-12-meta-pixel)
- [4. Menores](#4-menores)
  - [4.1 PRIV-13: No pedir la edad a los usuarios](#41-priv-13-no-pedir-la-edad-a-los-usuarios)
  - [4.2 PRIV-14: Consentimiento para datos de menores](#42-priv-14-consentimiento-para-datos-de-menores)
- [5. Comunicaciones comerciales](#5-comunicaciones-comerciales)
  - [5.1 PRIV-15: Autorización previa y enlace de baja en el correo comercial](#51-priv-15-autorización-previa-y-enlace-de-baja-en-el-correo-comercial)
  - [5.2 PRIV-16: Cumplimiento de CAN-SPAM y su multa por correo](#52-priv-16-cumplimiento-de-can-spam-y-su-multa-por-correo)
- [6. Responsabilidad proactiva y brechas](#6-responsabilidad-proactiva-y-brechas)
  - [6.1 PRIV-17: Registro de tratamientos, EIPD y delegado de protección de datos](#61-priv-17-registro-de-tratamientos-eipd-y-delegado-de-protección-de-datos)
  - [6.2 PRIV-18: Brechas de seguridad e incidentes](#62-priv-18-brechas-de-seguridad-e-incidentes)
<!-- /INDICE -->

## 1. Alcance jurídico

### 1.1 PRIV-01: Determinar qué jurisdicciones te aplican

- **Prioridad:** Alta
- **Naturaleza:** Obligación legal
- **Sectores:** INF ● · TIE ● · SUS ● · UGC ● · MEN ●
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ✅ Correcta

**De qué trata.** El país donde está tu empresa no es el único relevante. Si vendes fuera, ofreces servicios a personas de otros territorios o haces seguimiento de su comportamiento, pueden aplicarte reglas de privacidad, consumo, publicidad, menores y accesibilidad de esos territorios.

**Qué hacer**

- Hacer un mapa: dónde estás establecido, dónde están tus usuarios, en qué idiomas y monedas ofreces el servicio, y qué terceros reciben datos.
- Aplicar el estándar más exigente de los mercados donde operas como línea base (en la práctica, suele ser el RGPD) y añadir los extras regionales.
- Revisar el mapa cuando abras un mercado nuevo o añadas una herramienta de seguimiento.

**Normas de referencia por región**

| Región | Privacidad | Cookies y comunicaciones | Menores |
|---|---|---|---|
| UE / España | RGPD · LOPDGDD (Ley Orgánica 3/2018) | Directiva ePrivacy · LSSI-CE arts. 21 y 22 | RGPD art. 8 · LOPDGDD art. 7 (14 años) |
| EE. UU. | Sin ley federal general; leyes estatales (CCPA/CPRA en California y otros estados) · FTC Act | CAN-SPAM (correo) · leyes estatales de grabación de comunicaciones | COPPA (menores de 13) |
| Reino Unido | UK GDPR · Data Protection Act 2018 · Data (Use and Access) Act 2025 | PECR | UK GDPR art. 8 (13 años) · Children's Code |
| Latinoamérica | Brasil: LGPD · México: nueva LFPDPPP (2025) · Chile: Ley 21.719 (prevista para 1-12-2026, con proyecto de aplazamiento) · Argentina, Colombia: leyes propias | Reglas propias de cada país | Brasil: LGPD art. 14 y ECA Digital (en vigor desde 17-3-2026) |

**Alcance extraterritorial del RGPD.** Se aplica a responsables establecidos fuera de la UE cuando ofrecen bienes o servicios a personas en la UE o monitorizan su comportamiento allí (art. 3.2).

**Fuentes**

- [RGPD (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [LOPDGDD (BOE)](https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673)
- [Garrigues: nueva ley mexicana de datos personales](https://www.garrigues.com/es_ES/noticia/mexico-nueva-ley-federal-proteccion-datos-personales-posesion-particulares-introduce)
- [Garrigues: ley chilena 21.719](https://www.garrigues.com/es_ES/noticia/evolucion-regulacion-datos-personales-chile-modernizacion-marco-normativo-nueva.md)
- [Lefosse: ECA Digital (Brasil)](https://lefosse.com/noticias/alerta/eca-digital-entra-em-vigor-em-17-de-marco-como-se-preparar/)

## 2. Información, base jurídica y derechos

### 2.1 PRIV-02: Política de privacidad

- **Prioridad:** Alta
- **Naturaleza:** Obligación legal
- **Sectores:** INF ◐ · TIE ● · SUS ● · UGC ● · MEN ●
- **Regiones:** UE/ES ● · EE. UU. ◐ · UK ● · LATAM ●
- **Verificación:** ✅ Correcta

**De qué trata.** Informar a las personas, en el momento de recoger sus datos, de quién los trata, para qué, con qué base jurídica, quién los recibe, cuánto se conservan y cómo ejercer sus derechos. Aplica cuando tratas datos personales (formularios, cuentas, analítica con identificadores, pagos, correo).

**Qué hacer**

- Redactarla a partir de lo que realmente hace tu web: formularios, analítica, proveedores y operaciones reales. Copiar una plantilla sin revisarla es un riesgo.
- Incluir: identidad y contacto del responsable (y delegado de protección de datos si lo hay), finalidades, base jurídica de cada una, destinatarios, transferencias internacionales, plazos de conservación, derechos, derecho a retirar el consentimiento y a reclamar ante la autoridad (en España, la AEPD), y origen de los datos si no vienen del interesado.
- Usar **información por capas** (art. 11 LOPDGDD): resumen en el punto de recogida con enlace a la política completa.
- Mantenerla actualizada cada vez que añadas una herramienta, un proveedor o una finalidad.

**Por región**

- **UE/ES:** arts. 13 y 14 RGPD; la obligación de informar nace **al recoger** los datos.
- **EE. UU.:** no existe una obligación federal general, pero California (CalOPPA y CCPA/CPRA) exige política de privacidad y *aviso en el momento de la recogida* para empresas dentro de su ámbito, y la FTC sanciona prácticas contrarias a lo prometido.
- **UK:** igual que la UE (UK GDPR).
- **LATAM:** «aviso de privacidad» (México), art. 9 LGPD (Brasil).

**Fuentes**

- [RGPD arts. 13 y 14 (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [AEPD](https://www.aepd.es/)

### 2.2 PRIV-03: No recopilar datos innecesarios

- **Prioridad:** Alta
- **Naturaleza:** Obligación legal
- **Sectores:** INF ● · TIE ● · SUS ● · UGC ● · MEN ●
- **Regiones:** UE/ES ● · EE. UU. ◐ · UK ● · LATAM ●
- **Verificación:** ✅ Correcta

**De qué trata.** Recoger solo los datos adecuados, pertinentes y limitados a lo necesario para el fin declarado (**minimización**, art. 5.1.c RGPD, junto con protección de datos desde el diseño, art. 25). También reduce el impacto de una fuga y el trabajo de gestión.

**Qué hacer**

- Revisar cada campo de cada formulario: ¿qué decisión o servicio depende de este dato? Si ninguno, elimínalo.
- Evitar fecha de nacimiento, teléfono o dirección cuando no sean necesarios.
- Definir plazos de conservación y borrar o anonimizar al cumplirse.
- Limitar la analítica a lo que realmente vas a usar.

**Por región.** UE/UK/Brasil lo reconocen como principio expreso. California (CPRA) incorpora la minimización como obligación para empresas en su ámbito; en el resto de EE. UU. se aplica de forma indirecta (FTC, leyes estatales de nueva generación).

**Fuentes:** [RGPD art. 5 (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2016/679/oj)

### 2.3 PRIV-04: Comprobar los formularios de consentimiento

- **Prioridad:** Alta
- **Naturaleza:** Obligación legal condicionada
- **Sectores:** INF ◐ · TIE ● · SUS ● · UGC ● · MEN ●
- **Regiones:** UE/ES ● · EE. UU. ◐ · UK ● · LATAM ●
- **Verificación:** ✅ Correcta

**De qué trata.** Cuando basas un tratamiento en el consentimiento, éste debe ser libre, específico, informado e inequívoco, y debes poder demostrar quién consintió, qué y cuándo. No todo tratamiento necesita consentimiento: el contrato o el interés legítimo pueden ser otras bases.

**Qué hacer**

- Casillas **sin premarcar** (el TJUE lo confirmó en *Planet49*, C-673/17).
- Una casilla por finalidad; no agrupes privacidad, marketing y cesión a terceros.
- No condicionar el servicio a un consentimiento que no es necesario para prestarlo.
- Registrar el consentimiento: identificador, fecha y hora, versión del texto y canal.
- Facilitar retirarlo con la misma sencillez con la que se dio.

**Por región.** UE/UK y Brasil siguen el modelo de consentimiento previo; en EE. UU. suele operar el modelo de *opt-out* (salvo datos sensibles y menores en varios estados).

**Fuentes**

- [RGPD arts. 4.11 y 7 (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [TJUE C-673/17, *Planet49*](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:62017CJ0673)

### 2.4 PRIV-05: Proceso de eliminación de datos y ejercicio de derechos

- **Prioridad:** Alta (proceso) · Media (botón específico)
- **Naturaleza:** Obligación legal
- **Sectores:** INF ◐ · TIE ● · SUS ● · UGC ● · MEN ●
- **Regiones:** UE/ES ● · EE. UU. ◐ · UK ● · LATAM ●
- **Verificación:** ✅ Correcta

**De qué trata.** Debes facilitar el ejercicio de derechos (acceso, rectificación, supresión, oposición, limitación, portabilidad) y responder en plazo. **No** implica tener un botón público de «borrar mis datos»: basta un canal claro y un procedimiento interno.

**Qué hacer**

- Publicar un canal (correo o formulario) y un procedimiento para verificar la identidad.
- Responder en **un mes** (ampliable en casos complejos; art. 12.3 RGPD).
- Documentar las excepciones a la supresión (obligaciones legales, conservación para reclamaciones, art. 17.3 RGPD) y, en España, el **bloqueo** de datos (art. 32 LOPDGDD).
- Propagar la supresión a los encargados y terceros a los que hayas comunicado datos.

**Por región.** California reconoce derechos de acceso, supresión y exclusión de venta/compartición, con plazos propios (45 días como regla general para acceso y supresión). Brasil reconoce derechos equivalentes (art. 18 LGPD).

**Fuentes:** [RGPD arts. 12 a 22 (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2016/679/oj)

## 3. Cookies y tecnologías de seguimiento

### 3.1 PRIV-06: Política de cookies

- **Prioridad:** Alta
- **Naturaleza:** Obligación legal condicionada
- **Sectores:** INF ● · TIE ● · SUS ● · UGC ● · MEN ●
- **Regiones:** UE/ES ● · EE. UU. ○ · UK ● · LATAM ◐
- **Verificación:** ✅ Correcta

**De qué trata.** Informar de qué cookies y tecnologías similares usas, con qué finalidad, quién las gestiona, cuánto duran y cómo aceptarlas, rechazarlas o retirar el consentimiento. Aplica si usas cookies o almacenamiento local sujetos a consentimiento.

**Qué hacer**

- **Auditar lo que realmente carga la web** antes de redactarla (ver [PRIV-08](02-privacidad-cookies-y-comunicaciones.md#33-priv-08-auditar-sdks-y-servicios-de-terceros)).
- Clasificar: técnicas/necesarias (exentas), personalización, analítica y publicidad (requieren consentimiento).
- Indicar para cada una: nombre, titular (propia o de tercero), finalidad, duración.
- Enlazarla desde el banner y desde el pie de página.

**Matiz.** Las cookies técnicas estrictamente necesarias o para transmitir una comunicación pueden estar exentas (art. 22.2 LSSI); **la analítica y la publicidad no lo están automáticamente**.

**Por región.** En España, art. 22.2 LSSI y Guía de cookies de la AEPD. En el Reino Unido, la Data (Use and Access) Act 2025 introduce excepciones al consentimiento (por ejemplo, para cierta analítica estadística con condiciones), vigentes desde febrero de 2026; la publicidad y el seguimiento para perfilado siguen necesitando consentimiento. En EE. UU. no existe una obligación general de política de cookies; se integra en la política de privacidad y los avisos estatales.

**Fuentes**

- [LSSI-CE (BOE)](https://www.boe.es/buscar/act.php?id=BOE-A-2002-13758)
- [Guía de cookies de la AEPD](https://www.aepd.es/documento/guia-cookies.pdf)
- [ICO: qué es PECR](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/what-are-pecr)
- [Bratby Law: DUAA, cambios en vigor](https://bratby.law/data-use-and-access-act-2025-commencement/)

### 3.2 PRIV-07: Banner de consentimiento de cookies

- **Prioridad:** Alta
- **Naturaleza:** Obligación legal condicionada
- **Sectores:** INF ● · TIE ● · SUS ● · UGC ● · MEN ●
- **Regiones:** UE/ES ● · EE. UU. ◐ · UK ● · LATAM ◐
- **Verificación:** ✅ Correcta

**De qué trata.** Recoger una decisión válida **antes** de activar cualquier tecnología que requiera consentimiento. El banner no legitima por sí solo un tratamiento ni sustituye a una configuración técnica correcta.

**Qué hacer**

- **Aceptar y rechazar** a la vez, en la primera capa, con visibilidad, formato y facilidad comparables. Un banner con solo «Aceptar» y «Configurar» ya no cumple el criterio de la AEPD (plazo de adaptación vencido el 11-1-2024).
- **No cargar** scripts no exentos hasta que haya consentimiento (bloqueo previo real, no solo ocultar).
- No considerar consentimiento el desplazamiento o la navegación continuada.
- Permitir cambiar la decisión en cualquier momento (enlace persistente) y renovarla periódicamente (la guía de la AEPD sugiere no superar 24 meses).
- Probar el resultado en el navegador (pestaña Red): con «Rechazar», no deben salir peticiones a terceros de analítica o publicidad.
- Si usas servicios de Google con publicidad o medición en el EEE, integrar las señales de consentimiento que exige su política de consentimiento de usuarios de la UE (*Consent Mode*).

**Por región.** UE/UK: consentimiento previo. EE. UU.: modelo de *opt-out* con enlace «No vender ni compartir mi información personal» y respeto de la señal *Global Privacy Control* en California. LATAM: Brasil exige base legal (consentimiento) y la ANPD publicó una guía de cookies.

**Muros de cookies («pago o consentimiento»).** Condicionar el acceso a aceptar cookies no es ilícito siempre, pero tampoco es válido automáticamente. La Guía de la AEPD lo admite si se informa al usuario, se ofrece una alternativa **genuinamente equivalente** que no use cookies no exentas y la ofrece el propio editor; no exige que esa alternativa sea gratuita. El dictamen 08/2024 del CEPD es más restrictivo para grandes plataformas con publicidad comportamental. Valora cada caso y documenta por qué ambas opciones son razonables.

**Señal GPC y enlaces de exclusión (EE. UU.).** Si estás sujeto a la ley de privacidad de California (u otros estados con previsiones parecidas), debes tratar la señal *Global Privacy Control* del navegador como solicitud válida de exclusión de venta o compartición y ofrecer el enlace «Do Not Sell or Share My Personal Information» o «Your Privacy Choices» donde corresponda. No es una obligación general para una web dirigida solo a España.

**En movimiento.** La propuesta «Digital Omnibus» de la UE pretende mover las reglas de cookies al RGPD (nuevos arts. 88a y 88b) y ampliar las excepciones; sigue en tramitación (2025/0360(COD)).

**Fuentes**

- [Cuatrecasas: nuevo criterio de la AEPD sobre cookies](https://www.cuatrecasas.com/es/spain/propiedad-intelectual/art/entra-vigor-nuevo-criterio-aepd-uso-de-cookies)
- [Guía de cookies de la AEPD](https://www.aepd.es/documento/guia-cookies.pdf)
- [Hogan Lovells: nueva guía de cookies en España (pago o consentimiento)](https://www.hoganlovells.com/es/publications/nueva-guia-sobre-el-uso-de-cookies-en-espana)
- [Simmons & Simmons: dictamen 08/2024 del CEPD sobre «consentir o pagar»](https://www.simmons-simmons.com/en/publications/clvpeiyzw00s0ua8c0jyqml42/key-points-from-edpb-opinion-08-2024-on-consent-or-pay-models)
- [Observatorio Legislativo: Digital Omnibus 2025/0360(COD)](https://oeil.secure.europarl.europa.eu/oeil/en/procedure-file?reference=2025/0360(COD))

### 3.3 PRIV-08: Auditar SDKs y servicios de terceros

- **Prioridad:** Alta
- **Naturaleza:** Obligación legal
- **Sectores:** INF ● · TIE ● · SUS ● · UGC ● · MEN ●
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ✅ Correcta

**De qué trata.** Inventariar analítica, píxeles, chat, fuentes, mapas, vídeo, pasarelas y gestores de etiquetas, y comprobar qué datos transmiten, cuándo se activan, dónde se procesan y con qué contratos. **Un proveedor externo no elimina tus responsabilidades como responsable del tratamiento.**

**Qué hacer**

- Crear un inventario: servicio, finalidad, datos que envía, momento de activación, país de tratamiento, base jurídica, contrato.
- Contrato de encargado del tratamiento cuando el proveedor trate datos por tu cuenta (art. 28 RGPD).
- Para transferencias fuera del EEE, comprobar la salvaguarda (decisión de adecuación, cláusulas contractuales tipo). El *EU-US Data Privacy Framework* está vigente, con un recurso pendiente ante el Tribunal de Justicia (C-703/25 P).
- Repetir el escaneo en cada versión y al añadir un tag nuevo (ver [POST-02](09-post-lanzamiento.md#21-post-02-plan-de-revisiones-periódicas)).

**Fuentes**

- [RGPD arts. 28 y 44 a 49 (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [WilmerHale: recurso contra el Data Privacy Framework](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20251201-european-court-of-justice-to-review-challenge-to-eu-us-data-privacy-framework)

### 3.4 PRIV-09: Cargar las fuentes de Google desde tu propio servidor

- **Prioridad:** Media
- **Naturaleza:** Buena práctica
- **Sectores:** INF ● · TIE ● · SUS ● · UGC ● · MEN ●
- **Regiones:** UE/ES ● · EE. UU. ○ · UK ◐ · LATAM ○
- **Verificación:** ⚠️ Matizada

**De qué trata.** Cargar las fuentes desde los servidores de Google transmite la dirección IP y otros datos del visitante a un tercero. Alojarlas localmente elimina esa transferencia y esa dependencia.

**Qué hacer**

- Descargar las fuentes necesarias (solo los pesos y subconjuntos que uses) y servirlas desde tu dominio.
- Comprobar la licencia de cada fuente (la mayoría de las de Google Fonts son libres).
- Verificar en la pestaña Red que no quedan peticiones a `fonts.googleapis.com` ni `fonts.gstatic.com`.

**Matices sobre la lista original**

- **No está prohibido automáticamente.** Existe una sentencia concreta del *Landgericht* de Múnich I (20-1-2022, 3 O 17493/20) que concedió **100 €** de indemnización por daño inmaterial a un visitante cuya IP se había transmitido a Google sin justificación. Es una sentencia de **primera instancia, alemana**; no vincula a otros países ni constituye una multa automática. Su razonamiento fue que las fuentes podían servirse localmente.
- Desde 2020 el navegador particiona la caché por sitio, así que la ventaja de «fuente ya en caché de otro sitio» desapareció. Alojarlas localmente solo mejora el rendimiento si además usas una CDN y HTTP/2: mídelo (ver [REN-05](06-rendimiento.md#32-ren-05-fuentes-web-y-javascript-de-terceros)).

**Fuentes:** [IHK Bergische Region: LG München I, 3 O 17493/20](https://www.ihk.de/bergische/recht-und-steuern/wettbewerbsrecht/google-fonts-5646176)

### 3.5 PRIV-10: Grabación de sesiones (session replay)

- **Prioridad:** Alta (si lo utilizas)
- **Naturaleza:** Obligación legal condicionada
- **Sectores:** INF ◐ · TIE ● · SUS ● · UGC ◐ · MEN ●
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ◐
- **Verificación:** ⚠️ Matizada

**De qué trata.** Herramientas que reconstruyen la visita de un usuario (clics, movimientos, desplazamientos y contenido visible). **No siempre graban cada tecla**: depende de la herramienta y de la configuración. Pero pueden capturar datos personales que aparezcan en pantalla o se escriban en campos.

**Qué hacer**

- Decidir si de verdad lo necesitas; si no, no lo instales.
- **Enmascarar por defecto** campos de contraseña, pago, datos personales y mensajes; excluir páginas sensibles (cuenta, salud, pago).
- Pedir **consentimiento previo** en la UE/UK cuando acceda o almacene información en el dispositivo; informar en la política de privacidad y de cookies; evaluar base jurídica y, si procede, una evaluación de impacto.
- Revisar el contrato con el proveedor y el lugar de tratamiento.

**Contexto en EE. UU.** Existen demandas por «interceptación» de comunicaciones (en California, CIPA, Penal Code § 631) con criterios judiciales divididos: algunos tribunales han desestimado reclamaciones y otros las han admitido. El proyecto SB 690, que pretendía limitarlas, quedó en el comité de Asignaciones (*suspense file*) el 5-8-2026 y no es ley. **No lo instales a ciegas.**

**Fuentes**

- [Duane Morris: SB 690 en pausa](https://www.duanemorris.com/alerts/california_sb690_stalls_assembly_cipa_liability_remains_least_through_2026_0725.html)
- [Inside Class Actions: resumen 2025 de demandas por wiretapping](https://www.insideclassactions.com/2026/01/27/2025-website-wiretapping-roundup/)

### 3.6 PRIV-11: Microsoft Clarity

- **Prioridad:** Baja (como requisito) · alta cautela si lo adoptas
- **Naturaleza:** Opcional
- **Sectores:** INF ◐ · TIE ◐ · SUS ◐ · UGC ◐ · MEN ○
- **Regiones:** UE/ES ● · EE. UU. ◐ · UK ● · LATAM ◐
- **Verificación:** ✅ Correcta

**De qué trata.** Herramienta gratuita de mapas de calor y grabaciones. Es **opcional**: no es una obligación ni una solución de cumplimiento.

**Qué hacer**

- Tratarla como session replay: ver [PRIV-10](02-privacidad-cookies-y-comunicaciones.md#35-priv-10-grabación-de-sesiones-session-replay).
- Desde el **31 de octubre de 2025** Clarity exige una señal de consentimiento válida para visitas originadas en el EEE, Reino Unido y Suiza: si no se la envías, las funciones quedan limitadas. Pásale el estado de consentimiento desde tu banner.
- Configurar enmascarado y excluir páginas sensibles.

**Fuentes:** [Microsoft Learn: Clarity consent mode](https://learn.microsoft.com/en-us/clarity/consent-mode)

### 3.7 PRIV-12: Meta Pixel

- **Prioridad:** Baja (como requisito) · alta cautela si lo adoptas
- **Naturaleza:** Opcional
- **Sectores:** INF ○ · TIE ◐ · SUS ◐ · UGC ○ · MEN ○
- **Regiones:** UE/ES ● · EE. UU. ◐ · UK ● · LATAM ◐
- **Verificación:** ✅ Correcta

**De qué trata.** Solo tiene sentido si necesitas medición publicitaria o remarketing en las plataformas de Meta.

**Qué hacer**

- **En la UE/UK, no cargarlo antes de obtener el consentimiento** para tecnologías no esenciales: bloquea su ejecución hasta entonces.
- Recordar que la responsabilidad es del titular de la web: Meta traslada a cada anunciante la obligación de cumplir.
- No asumir que la API de conversiones (envío desde el servidor) evita la necesidad de base jurídica: sigue tratando datos personales.
- Evitar su uso en páginas o formularios con datos sensibles (salud, finanzas, menores).
- Actualizar la política de privacidad, la de cookies y el inventario de terceros ([PRIV-08](02-privacidad-cookies-y-comunicaciones.md#33-priv-08-auditar-sdks-y-servicios-de-terceros)).

**Por región.** En EE. UU. puede considerarse «venta» o «compartición» de datos a efectos de las leyes estatales: exige enlace de exclusión y respeto de señales como GPC.

**Fuentes:** [Meta for Developers: Meta Pixel y RGPD](https://developers.facebook.com/docs/meta-pixel/implementation/gdpr)

## 4. Menores

### 4.1 PRIV-13: No pedir la edad a los usuarios

- **Prioridad:** Media
- **Naturaleza:** Buena práctica
- **Sectores:** INF ◐ · TIE ◐ · SUS ◐ · UGC ● · MEN ●
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ⚠️ Matizada

**De qué trata.** Decidir si preguntas la edad y qué haces con la respuesta. La lista original ya corregía el mito «pedir la edad va contra COPPA»: es falso.

**Qué hacer**

- Si tu servicio **no está dirigido a menores** y no necesitas conocer la edad, no la pidas (minimización, [PRIV-03](02-privacidad-cookies-y-comunicaciones.md#22-priv-03-no-recopilar-datos-innecesarios)).
- Si debes comprobar que alguien supera un umbral, usa una pantalla de edad **neutra** (no sugiere la respuesta «correcta») y no animes a mentir.
- Si descubres que tratas datos de un menor, aplica las reglas correspondientes (ver [PRIV-14](02-privacidad-cookies-y-comunicaciones.md#42-priv-14-consentimiento-para-datos-de-menores)); saberlo cambia tu situación jurídica.
- Si ofreces un servicio infantil, diseña protecciones adecuadas en lugar de asumir que una casilla de edad lo resuelve.

**Por región**

| Región | Regla |
|---|---|
| EE. UU. | COPPA se aplica a sitios **dirigidos a menores de 13** y a servicios generales que tienen **conocimiento efectivo** de recoger datos de menores; no obliga a las webs generales a preguntar la edad. La regla enmendada tuvo plazo de cumplimiento el 22-4-2026. |
| UE | Edad de consentimiento digital entre 13 y 16 años según el país (art. 8 RGPD). |
| España | **14 años** (art. 7 LOPDGDD) cuando la base es el consentimiento. El proyecto de ley orgánica de protección de menores en entornos digitales propone elevarla a 16; sigue en tramitación parlamentaria (septiembre de 2026). |
| Reino Unido | 13 años; *Children's Code* para servicios con probable acceso de menores. |
| Brasil | LGPD art. 14 y ECA Digital (vigente desde 17-3-2026). |

**Fuentes**

- [Davis Polk: COPPA, nuevas obligaciones en vigor](https://www.davispolk.com/insights/client-update/ftc-prioritizes-coppa-enforcement-new-compliance-obligations-take-effect)
- [Osborne Clarke: proyecto de ley de menores en entornos digitales](https://www.osborneclarke.com/es/insights/espana-busca-proteger-los-menores-en-el-entorno-digital-claves-del-proyecto-de-ley)
- [FTC: privacidad infantil (COPPA)](https://www.ftc.gov/business-guidance/privacy-security/childrens-privacy)

### 4.2 PRIV-14: Consentimiento para datos de menores

- **Prioridad:** Alta (solo si aplica)
- **Naturaleza:** Obligación legal condicionada
- **Sectores:** INF ○ · TIE ○ · SUS ◐ · UGC ◐ · MEN ●
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ✅ Correcta

**De qué trata.** No es una casilla universal. Si ofreces servicios **directamente a menores** y tratas datos basándote en consentimiento, hay reglas específicas sobre autorización parental, edad mínima y esfuerzos razonables de verificación.

**Qué hacer**

- Identificar si tu servicio se dirige a menores o es probable que lo usen.
- Por debajo del umbral nacional (España: 14), obtener el consentimiento de quien tenga la patria potestad o tutela y hacer **esfuerzos razonables** por verificarlo (art. 8.2 RGPD).
- En EE. UU., aplicar COPPA: consentimiento parental verificable; la regla enmendada exige además consentimiento separado para ciertas cesiones a terceros.
- Proteger por defecto: no perfilar ni mostrar publicidad basada en perfiles a menores (art. 28.2 DSA para plataformas en línea).
- Redactar la información en lenguaje adecuado a su edad.

**Fuentes**

- [RGPD art. 8 (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [DSA (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2022/2065/oj)

## 5. Comunicaciones comerciales

### 5.1 PRIV-15: Autorización previa y enlace de baja en el correo comercial

- **Prioridad:** Alta (si envías marketing)
- **Naturaleza:** Obligación legal
- **Sectores:** INF ◐ · TIE ● · SUS ● · UGC ◐ · MEN ◐
- **Regiones:** UE/ES ● · EE. UU. ◐ · UK ● · LATAM ◐
- **Verificación:** ✅ Correcta

**De qué trata.** En España, las comunicaciones comerciales electrónicas exigen **autorización previa** (art. 21.1 LSSI). Existe una excepción limitada (art. 21.2): clientes con relación contractual previa, datos obtenidos lícitamente y productos o servicios **similares** de la propia empresa. En todos los casos debe poder ejercerse la oposición de forma **sencilla y gratuita**, al recoger los datos y en **cada** comunicación.

**Qué hacer**

- Pedir consentimiento específico para marketing (ver [PRIV-04](02-privacidad-cookies-y-comunicaciones.md#23-priv-04-comprobar-los-formularios-de-consentimiento)); no equipararlo a aceptar la política de privacidad.
- Incluir en cada envío un enlace de baja de un solo paso, sin iniciar sesión ni pedir datos extra.
- Procesar bajas sin demora y mantener una lista de supresión.
- Recordar que **el enlace de baja no sustituye al permiso** para enviar el correo.
- Los mensajes estrictamente transaccionales (confirmación de pedido) no son comunicaciones comerciales, pero no los uses como vehículo de promoción.
- Buena práctica de entregabilidad: cabecera `List-Unsubscribe` con baja en un clic para envíos masivos.

**Otros canales.** Separa por canal y finalidad. El art. 21 LSSI cubre el correo y los medios electrónicos individuales equivalentes, incluidos los mensajes móviles (SMS y mensajería); las **llamadas** comerciales tienen reglas propias de telecomunicaciones. No extrapoles sin más el consentimiento obtenido para el correo a otros canales: recógelo, regístralo y respétalo por canal.

**Por región.** UE/UK: consentimiento previo (con excepción para clientes). EE. UU.: modelo de exclusión, ver [PRIV-16](02-privacidad-cookies-y-comunicaciones.md#52-priv-16-cumplimiento-de-can-spam-y-su-multa-por-correo). Brasil: LGPD exige base legal y respeto a la oposición.

**Fuentes:** [LSSI-CE, arts. 21 y 22 (BOE)](https://www.boe.es/buscar/act.php?id=BOE-A-2002-13758)

### 5.2 PRIV-16: Cumplimiento de CAN-SPAM y su multa por correo

- **Prioridad:** Media (si operas en EE. UU.)
- **Naturaleza:** Obligación legal condicionada
- **Sectores:** INF ◐ · TIE ● · SUS ● · UGC ◐ · MEN ◐
- **Regiones:** UE/ES ○ · EE. UU. ● · UK ○ · LATAM ○
- **Verificación:** ⚠️ Matizada

**De qué trata.** La ley federal estadounidense CAN-SPAM regula **todo** correo comercial (también B2B). La cifra de la lista es correcta: la sanción máxima es de **53.088 $ por cada correo infractor**; la FTC mantuvo en 2026 los importes de 2025, sin nueva actualización.

**Matices sobre la lista original**

- Es un **máximo teórico por mensaje**, no una multa automática; los acuerdos reales suelen ser muy inferiores.
- No se aplica «por ser desarrollador en España»: importa a quién envías, la actividad y la jurisdicción. Si haces marketing por correo a destinatarios en EE. UU., debes cumplirla además de la normativa local.

**Requisitos principales**

- Cabeceras (*From*, *To*, *Reply-To*) y asunto veraces.
- Identificar el mensaje como publicidad.
- Incluir una **dirección postal física** válida del remitente.
- Ofrecer un mecanismo claro de exclusión, gratuito y sin pedir datos más allá del correo; operativo al menos 30 días tras el envío.
- Atender la exclusión en un máximo de **10 días hábiles** y no vender ni ceder esas direcciones.
- Eres responsable aunque contrates a un proveedor de envío.

**Fuentes**

- [FTC: guía de cumplimiento de CAN-SPAM](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business)
- [16 CFR 1.98: importes de sanciones civiles ajustados por inflación](https://www.federal-regs.com/title/16/part-1/1.98/)

## 6. Responsabilidad proactiva y brechas

### 6.1 PRIV-17: Registro de tratamientos, EIPD y delegado de protección de datos

- **Prioridad:** Alta
- **Naturaleza:** Obligación legal
- **Sectores:** INF ◐ · TIE ● · SUS ● · UGC ● · MEN ●
- **Regiones:** UE/ES ● · EE. UU. ○ · UK ● · LATAM ◐
- **Verificación:** ➕ Añadida

**De qué trata.** Tres piezas de la responsabilidad proactiva del RGPD que se suelen confundir: el **registro de actividades de tratamiento** (art. 30), la **evaluación de impacto** (EIPD, art. 35) y el **delegado de protección de datos** (DPD, art. 37). Ninguna se exige «por tener una web», pero sí por lo que haces con los datos.

**Qué hacer**

- **Registro (art. 30):** documentar por escrito cada actividad de tratamiento (finalidad, categorías de datos e interesados, destinatarios, transferencias, plazos, medidas de seguridad). La excepción para organizaciones de menos de 250 personas es **limitada**: no cubre tratamientos no ocasionales, de riesgo o de datos especiales; en la práctica, un negocio con clientes o suscriptores suele estar dentro.
- **EIPD (art. 35):** hacerla *antes* de empezar un tratamiento que probablemente entrañe alto riesgo. Consulta las listas de la AEPD (tratamientos que la requieren y tratamientos exentos): ejemplos habituales son la elaboración de perfiles a gran escala, la monitorización sistemática, el tratamiento a gran escala de datos de menores o la biometría. En caso de duda, hacerla es buena práctica.
- **DPD (art. 37):** obligatorio para organismos públicos, para quien tenga como actividad principal la observación habitual y sistemática a gran escala, o el tratamiento a gran escala de datos especiales. La LOPDGDD (art. 34) añade entidades concretas (centros docentes, aseguradoras, entidades financieras, centros sanitarios, entre otras). Si lo nombras voluntariamente, asumes sus obligaciones y debes comunicarlo a la AEPD.
- Mantenerlo vivo: actualizar el registro al cambiar herramientas o finalidades (ver [PRIV-08](02-privacidad-cookies-y-comunicaciones.md#33-priv-08-auditar-sdks-y-servicios-de-terceros)).

**En movimiento.** El paquete «Digital Omnibus» propone modificar la excepción del art. 30.5 (elevar el umbral de 250 a 750 personas, salvo alto riesgo); a fecha de esta guía no está aprobado.

**Fuentes**

- [RGPD arts. 30, 35 y 37 (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [AEPD: listas de tratamientos que requieren EIPD (art. 35.4)](https://www.aepd.es/documento/listas-dpia-es-35-4.pdf)
- [LOPDGDD (BOE)](https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673)

### 6.2 PRIV-18: Brechas de seguridad e incidentes

- **Prioridad:** Alta
- **Naturaleza:** Obligación legal
- **Sectores:** INF ◐ · TIE ● · SUS ● · UGC ● · MEN ●
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ➕ Añadida

**De qué trata.** Un proceso para detectar, evaluar, contener y comunicar incidentes que afecten a datos personales (pérdida, destrucción, alteración, acceso o comunicación no autorizados; incluye la indisponibilidad, por ejemplo un *ransomware*). Fusiona los puntos «brechas» y «plan de respuesta a incidentes».

**Qué hacer**

- Definir responsables, canal interno de aviso y pasos de contención antes de que ocurra.
- **Documentar toda brecha**, se notifique o no (art. 33.5 RGPD).
- **Notificar a la autoridad** sin dilación indebida y, de ser posible, en un máximo de **72 horas** desde que tengas conocimiento, **salvo** que sea improbable que suponga un riesgo para las personas. No toda incidencia debe notificarse. En España, a través de la herramienta *Comunica-Brecha RGPD* de la AEPD.
- **Comunicar a los afectados** cuando el riesgo sea **alto** (art. 34), con lenguaje claro y recomendaciones de protección.
- Exigir en los contratos que tus proveedores te avisen sin demora (art. 33.2).
- Ensayar el plan al menos una vez al año ([POST-02](09-post-lanzamiento.md#21-post-02-plan-de-revisiones-periódicas)).

**Por región.** EE. UU.: todos los estados tienen leyes de notificación de brechas, con definiciones y plazos distintos. Reino Unido: igual que la UE (UK GDPR). Brasil: la LGPD exige comunicar incidentes relevantes a la autoridad y a los titulares.

**Fuentes**

- [RGPD arts. 33 y 34 (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [ISMS Forum: guía práctica de brechas de datos (2022)](https://www.ismsforum.es/ficheros/descargas/guiabrechasdatos2022v411663223489.pdf)
