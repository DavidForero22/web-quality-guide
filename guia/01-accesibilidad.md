# Accesibilidad

> Última verificación: 2026-10-10 · [Volver al README](../README.md)

Cubre el marco legal de accesibilidad y los **55 criterios de WCAG 2.2 niveles A y AA**. Las medidas de la segunda lista que eran duplicados de WCAG (texto alternativo, contraste, navegación por teclado) quedan fusionadas en sus criterios.

<!-- INDICE -->
**Índice**

- [1. Marco legal](#1-marco-legal)
  - [1.1 ACC-01: Obligaciones legales de accesibilidad](#11-acc-01-obligaciones-legales-de-accesibilidad)
  - [1.2 ACC-02: Declaración de accesibilidad y canal para comunicar barreras](#12-acc-02-declaración-de-accesibilidad-y-canal-para-comunicar-barreras)
- [2. Principio 1: Perceptible](#2-principio-1-perceptible)
  - [2.1 WCAG 1.1.1: Contenido no textual (A)](#21-wcag-111-contenido-no-textual-a)
  - [2.2 WCAG 1.2.1: Solo audio y solo vídeo, pregrabado (A)](#22-wcag-121-solo-audio-y-solo-vídeo-pregrabado-a)
  - [2.3 WCAG 1.2.2: Subtítulos, pregrabado (A)](#23-wcag-122-subtítulos-pregrabado-a)
  - [2.4 WCAG 1.2.3: Audiodescripción o alternativa para medios, pregrabado (A)](#24-wcag-123-audiodescripción-o-alternativa-para-medios-pregrabado-a)
  - [2.5 WCAG 1.2.4: Subtítulos en directo (AA)](#25-wcag-124-subtítulos-en-directo-aa)
  - [2.6 WCAG 1.2.5: Audiodescripción, pregrabado (AA)](#26-wcag-125-audiodescripción-pregrabado-aa)
  - [2.7 WCAG 1.3.1: Información y relaciones (A)](#27-wcag-131-información-y-relaciones-a)
  - [2.8 WCAG 1.3.2: Secuencia significativa (A)](#28-wcag-132-secuencia-significativa-a)
  - [2.9 WCAG 1.3.3: Características sensoriales (A)](#29-wcag-133-características-sensoriales-a)
  - [2.10 WCAG 1.3.4: Orientación (AA)](#210-wcag-134-orientación-aa)
  - [2.11 WCAG 1.3.5: Identificar el propósito de la entrada (AA)](#211-wcag-135-identificar-el-propósito-de-la-entrada-aa)
  - [2.12 WCAG 1.4.1: Uso del color (A)](#212-wcag-141-uso-del-color-a)
  - [2.13 WCAG 1.4.2: Control del audio (A)](#213-wcag-142-control-del-audio-a)
  - [2.14 WCAG 1.4.3: Contraste mínimo (AA)](#214-wcag-143-contraste-mínimo-aa)
  - [2.15 WCAG 1.4.4: Cambio de tamaño del texto (AA)](#215-wcag-144-cambio-de-tamaño-del-texto-aa)
  - [2.16 WCAG 1.4.5: Imágenes de texto (AA)](#216-wcag-145-imágenes-de-texto-aa)
  - [2.17 WCAG 1.4.10: Reflujo (AA)](#217-wcag-1410-reflujo-aa)
  - [2.18 WCAG 1.4.11: Contraste no textual (AA)](#218-wcag-1411-contraste-no-textual-aa)
  - [2.19 WCAG 1.4.12: Espaciado del texto (AA)](#219-wcag-1412-espaciado-del-texto-aa)
  - [2.20 WCAG 1.4.13: Contenido al pasar el puntero o recibir foco (AA)](#220-wcag-1413-contenido-al-pasar-el-puntero-o-recibir-foco-aa)
- [3. Principio 2: Operable](#3-principio-2-operable)
  - [3.1 WCAG 2.1.1: Teclado (A)](#31-wcag-211-teclado-a)
  - [3.2 WCAG 2.1.2: Sin trampas para el foco del teclado (A)](#32-wcag-212-sin-trampas-para-el-foco-del-teclado-a)
  - [3.3 WCAG 2.1.4: Atajos de teclado de un solo carácter (A)](#33-wcag-214-atajos-de-teclado-de-un-solo-carácter-a)
  - [3.4 WCAG 2.2.1: Tiempo ajustable (A)](#34-wcag-221-tiempo-ajustable-a)
  - [3.5 WCAG 2.2.2: Pausar, detener, ocultar (A)](#35-wcag-222-pausar-detener-ocultar-a)
  - [3.6 WCAG 2.3.1: Umbral de tres destellos o menos (A)](#36-wcag-231-umbral-de-tres-destellos-o-menos-a)
  - [3.7 WCAG 2.4.1: Evitar bloques (A)](#37-wcag-241-evitar-bloques-a)
  - [3.8 WCAG 2.4.2: Titulado de páginas (A)](#38-wcag-242-titulado-de-páginas-a)
  - [3.9 WCAG 2.4.3: Orden del foco (A)](#39-wcag-243-orden-del-foco-a)
  - [3.10 WCAG 2.4.4: Propósito de los enlaces, en contexto (A)](#310-wcag-244-propósito-de-los-enlaces-en-contexto-a)
  - [3.11 WCAG 2.4.5: Múltiples vías (AA)](#311-wcag-245-múltiples-vías-aa)
  - [3.12 WCAG 2.4.6: Encabezados y etiquetas (AA)](#312-wcag-246-encabezados-y-etiquetas-aa)
  - [3.13 WCAG 2.4.7: Foco visible (AA)](#313-wcag-247-foco-visible-aa)
  - [3.14 WCAG 2.4.11: Foco no oculto, mínimo (AA)](#314-wcag-2411-foco-no-oculto-mínimo-aa)
  - [3.15 WCAG 2.5.1: Gestos del puntero (A)](#315-wcag-251-gestos-del-puntero-a)
  - [3.16 WCAG 2.5.2: Cancelación del puntero (A)](#316-wcag-252-cancelación-del-puntero-a)
  - [3.17 WCAG 2.5.3: Etiqueta en el nombre (A)](#317-wcag-253-etiqueta-en-el-nombre-a)
  - [3.18 WCAG 2.5.4: Activación por movimiento (A)](#318-wcag-254-activación-por-movimiento-a)
  - [3.19 WCAG 2.5.7: Movimientos de arrastre (AA)](#319-wcag-257-movimientos-de-arrastre-aa)
  - [3.20 WCAG 2.5.8: Tamaño del objetivo, mínimo (AA)](#320-wcag-258-tamaño-del-objetivo-mínimo-aa)
- [4. Principio 3: Comprensible](#4-principio-3-comprensible)
  - [4.1 WCAG 3.1.1: Idioma de la página (A)](#41-wcag-311-idioma-de-la-página-a)
  - [4.2 WCAG 3.1.2: Idioma de las partes (AA)](#42-wcag-312-idioma-de-las-partes-aa)
  - [4.3 WCAG 3.2.1: Al recibir el foco (A)](#43-wcag-321-al-recibir-el-foco-a)
  - [4.4 WCAG 3.2.2: Al recibir entradas (A)](#44-wcag-322-al-recibir-entradas-a)
  - [4.5 WCAG 3.2.3: Navegación coherente (AA)](#45-wcag-323-navegación-coherente-aa)
  - [4.6 WCAG 3.2.4: Identificación coherente (AA)](#46-wcag-324-identificación-coherente-aa)
  - [4.7 WCAG 3.2.6: Ayuda coherente (A)](#47-wcag-326-ayuda-coherente-a)
  - [4.8 WCAG 3.3.1: Identificación de errores (A)](#48-wcag-331-identificación-de-errores-a)
  - [4.9 WCAG 3.3.2: Etiquetas o instrucciones (A)](#49-wcag-332-etiquetas-o-instrucciones-a)
  - [4.10 WCAG 3.3.3: Sugerencias ante errores (AA)](#410-wcag-333-sugerencias-ante-errores-aa)
  - [4.11 WCAG 3.3.4: Prevención de errores, legales, financieros o de datos (AA)](#411-wcag-334-prevención-de-errores-legales-financieros-o-de-datos-aa)
  - [4.12 WCAG 3.3.7: Entrada redundante (A)](#412-wcag-337-entrada-redundante-a)
  - [4.13 WCAG 3.3.8: Autenticación accesible, mínimo (AA)](#413-wcag-338-autenticación-accesible-mínimo-aa)
- [5. Principio 4: Robusto](#5-principio-4-robusto)
  - [5.1 WCAG 4.1.2: Nombre, función, valor (A)](#51-wcag-412-nombre-función-valor-a)
  - [5.2 WCAG 4.1.3: Mensajes de estado (AA)](#52-wcag-413-mensajes-de-estado-aa)
- [6. Documentos y contenido de terceros](#6-documentos-y-contenido-de-terceros)
  - [6.1 ACC-03: Documentos descargables y contenido de terceros](#61-acc-03-documentos-descargables-y-contenido-de-terceros)
- [7. Cómo comprobar la conformidad](#7-cómo-comprobar-la-conformidad)
<!-- /INDICE -->

## 1. Marco legal

### 1.1 ACC-01: Obligaciones legales de accesibilidad

- **Prioridad:** Alta
- **Naturaleza:** Obligación legal condicionada
- **Sectores:** INF ◐ · TIE ● · SUS ● · UGC ◐ · MEN ◐
- **Regiones:** UE/ES ● · EE. UU. ◐ · UK ◐ · LATAM ◐
- **Verificación:** ⚠️ Matizada

**De qué trata.** Determinar si la accesibilidad de tu sitio es una obligación legal y con qué estándar técnico, según tu actividad, tamaño y mercado. La lista original lo planteaba solo para España/UE; aquí se añaden los equivalentes en otras regiones para que puedas etiquetar tu proyecto.

**Qué hacer**

- Comprobar si tu servicio está en el ámbito de la Ley Europea de Accesibilidad: comercio electrónico, banca para consumidores, comunicaciones electrónicas, servicios audiovisuales, transporte de viajeros y libros electrónicos, entre otros.
- Comprobar si eres microempresa (menos de 10 empleados **y** menos de 2 M€ de volumen de negocio o balance): si solo prestas servicios, estás exenta; si vendes productos, la exención no aplica.
- Si eres administración o sector público, aplican además las normas propias (Directiva 2016/2102 y su transposición).
- Adoptar **WCAG 2.2 AA** como objetivo técnico: cubre con margen tanto el estándar europeo vigente como el que está en camino.

**Matices sobre la lista original**

- La Ley Europea de Accesibilidad (Directiva 2019/882) se aplica desde el **28 de junio de 2025**. En España la transpone la Ley 11/2023, de 8 de mayo. Hay periodos transitorios para contratos de servicios anteriores a esa fecha (máximo cinco años).
- La referencia técnica es la norma **EN 301 549**. La versión vigente con presunción de conformidad (v3.2.1) se basa en **WCAG 2.1 AA**. La v4.1.1 (basada en WCAG 2.2) se publicó el 2 de septiembre de 2026 y está pendiente de citarse en el Diario Oficial de la UE (estimado entre finales de noviembre y mediados de diciembre de 2026). WCAG 2.2 AA es, por tanto, un superconjunto seguro.
- Las sanciones en España se rigen por la normativa sectorial y, de forma supletoria, por el título III del Real Decreto Legislativo 1/2013 (multas de 301 € a 1.000.000 € según las fuentes consultadas; verifica el rango en el BOE).

**Equivalentes en otras regiones**

| Región | Norma | Alcance práctico |
|---|---|---|
| UE / España | Directiva 2019/882 · Ley 11/2023 · Directiva 2016/2102 (sector público) | Obligación directa para los servicios cubiertos. |
| EE. UU. | ADA Título III (sector privado) · ADA Título II (administraciones) · Sección 508 (federal) | No hay norma técnica oficial para el sector privado: los tribunales y el DOJ toman WCAG como referencia y las demandas contra comercios online son habituales. Para Título II el DOJ fijó WCAG 2.1 AA y retrasó los plazos un año: **26 de abril de 2027** (50.000 o más habitantes) y **26 de abril de 2028** (resto). |
| Reino Unido | Equality Act 2010 (ajustes razonables) · Public Sector Bodies Accessibility Regulations 2018 | Deber de ajustes razonables también en el sector privado; WCAG 2.2 AA es la referencia habitual. |
| Latinoamérica | Brasil: Ley 13.146/2015 (LBI); otros países con leyes de discapacidad | Brasil exige accesibilidad en sitios de empresas con sede o representación en el país; en el resto, revisa la normativa nacional. |

**Fuentes**

- [Directiva (UE) 2019/882, Ley Europea de Accesibilidad](https://eur-lex.europa.eu/eli/dir/2019/882/oj)
- [Ley 11/2023, de 8 de mayo (BOE)](https://www.boe.es/eli/es/l/2023/05/08/11)
- [Fieldfisher: claves de la transposición española](https://www.fieldfisher.com/es-es/locations/espana/actualidad/accesibilidad-obligatoria-claves-de-la-transposicion-accesibility-act)
- [Deque: EN 301 549 v4.1.1 publicada](https://www.deque.com/blog/en-301-549-v4-1-1-is-final-what-changed-what-it-means-and-what-you-should-do/)
- [Mondaq: el DOJ retrasa los plazos de ADA Título II](https://www.mondaq.com/unitedstates/media-entertainment-law/1782220/doj-extends-ada-title-ii-digital-accessibility-deadlines-by-one-year)

### 1.2 ACC-02: Declaración de accesibilidad y canal para comunicar barreras

- **Prioridad:** Media (Alta si eres sector público)
- **Naturaleza:** Obligación legal condicionada
- **Sectores:** INF ◐ · TIE ◐ · SUS ◐ · UGC ○ · MEN ◐
- **Regiones:** UE/ES ● · EE. UU. ◐ · UK ◐ · LATAM ○
- **Verificación:** ➕ Añadida

**De qué trata.** Publicar un documento que explique el grado de conformidad del sitio, los contenidos que aún no son accesibles y cómo contactar para comunicar una barrera. Es obligatorio para el sector público; **no es una obligación universal** para cualquier web privada.

**Qué hacer**

- **Sector público (UE/España):** publicar la declaración con el modelo europeo (Decisión de Ejecución (UE) 2018/1523), accesible desde todas las páginas con un enlace «Accesibilidad» y actualizada al menos una vez al año (RD 1112/2018).
- **Sector privado:** los prestadores de servicios cubiertos por la Ley Europea de Accesibilidad deben informar de cómo el servicio cumple los requisitos de accesibilidad. En España hay normas complementarias para ciertas empresas de «especial trascendencia económica» (RD 193/2023). Comprueba el texto aplicable a tu caso en el BOE.
- Aunque no sea obligatoria, es una buena práctica: describe el estándar usado (WCAG 2.2 AA), el estado de conformidad, las limitaciones conocidas y la fecha de la última revisión.
- Ofrecer un **canal** (correo o formulario accesible) para comunicar barreras y comprometerse a un plazo de respuesta; un canal que nadie atiende no cuenta.

**Fuentes**

- [Directiva (UE) 2016/2102](https://eur-lex.europa.eu/eli/dir/2016/2102/oj)
- [Decisión de Ejecución (UE) 2018/1523](https://eur-lex.europa.eu/eli/dec_impl/2018/1523/oj)
- [Nota técnica del Observatorio de Accesibilidad sobre el RD 1112/2018](https://administracionelectronica.gob.es/pae_Home/va/dam/jcr:26caea26-c01c-45f6-ba6b-c23c8918cf8e/2019-02-Nota-tecnica-OBSAE-rd1112-2018-accesibilidad-web.pdf)

## 2. Principio 1: Perceptible

Los usuarios deben poder percibir la información y los componentes de la interfaz.

### 2.1 WCAG 1.1.1: Contenido no textual (A)

- **Nivel:** A · **Prioridad:** Alta · **Aplica si:** hay imágenes, iconos o controles gráficos.

Todo contenido que no sea texto necesita una alternativa textual equivalente. Las imágenes informativas y funcionales llevan un `alt` descriptivo; las decorativas llevan `alt=""` para que los lectores de pantalla las omitan (para iconos SVG o de fuente decorativos se usa `aria-hidden="true"`). No conviertas el `alt` en una lista de palabras clave.

*Fusiona* la medida «Texto alt en imágenes» de la lista de accesibilidad. Un buen `alt` ayuda además a Google a entender las imágenes (ver [SEO-05](05-seo.md#21-seo-05-títulos-y-descripciones-personalizados)).

### 2.2 WCAG 1.2.1: Solo audio y solo vídeo, pregrabado (A)

- **Nivel:** A · **Prioridad:** Media · **Aplica si:** publicas audio o vídeo sin sonido, pregrabados.

Ofrece una transcripción para el audio y una alternativa textual o una pista de audio para el vídeo sin sonido.

### 2.3 WCAG 1.2.2: Subtítulos, pregrabado (A)

- **Nivel:** A · **Prioridad:** Alta · **Aplica si:** publicas vídeo pregrabado con audio.

Todo vídeo pregrabado con audio debe tener subtítulos sincronizados que incluyan diálogos y sonidos relevantes.

### 2.4 WCAG 1.2.3: Audiodescripción o alternativa para medios, pregrabado (A)

- **Nivel:** A · **Prioridad:** Media · **Aplica si:** publicas vídeo pregrabado con información visual relevante.

Proporciona una alternativa en texto (guion descriptivo) o una audiodescripción. Si ya cumples [WCAG 1.2.5](01-accesibilidad.md#26-wcag-125-audiodescripción-pregrabado-aa), este criterio queda cubierto.

### 2.5 WCAG 1.2.4: Subtítulos en directo (AA)

- **Nivel:** AA · **Prioridad:** Media · **Aplica si:** emites vídeo en directo con audio.

El vídeo en directo debe incluir subtítulos, manuales o automáticos con calidad suficiente.

### 2.6 WCAG 1.2.5: Audiodescripción, pregrabado (AA)

- **Nivel:** AA · **Prioridad:** Media · **Aplica si:** tus vídeos transmiten información visual que no está en el audio.

Incluye una pista de audiodescripción que narre la información visual relevante.

### 2.7 WCAG 1.3.1: Información y relaciones (A)

- **Nivel:** A · **Prioridad:** Alta · **Aplica si:** siempre.

La estructura semántica correcta es la base de todo: `<main>`, `<nav>`, `<header>`, encabezados `<h1>`-`<h6>` jerárquicos, listas reales `<ul>`/`<ol>`, tablas con cabeceras y `<label>` asociados a cada campo de formulario. Lo que se ve como estructura debe estar programado como estructura.

### 2.8 WCAG 1.3.2: Secuencia significativa (A)

- **Nivel:** A · **Prioridad:** Alta · **Aplica si:** siempre.

El orden del DOM debe ser lógico y comprensible sin depender solo del CSS. Si reordenas visualmente con `order`, `grid` o posicionamiento, comprueba que la lectura lineal sigue teniendo sentido.

### 2.9 WCAG 1.3.3: Características sensoriales (A)

- **Nivel:** A · **Prioridad:** Media · **Aplica si:** das instrucciones al usuario.

Las instrucciones no deben depender solo de forma, tamaño, ubicación o sonido. «Pulsa el botón verde de la derecha» debe ser «Pulsa el botón *Guardar*».

### 2.10 WCAG 1.3.4: Orientación (AA)

- **Nivel:** AA · **Prioridad:** Media · **Aplica si:** siempre (especialmente en web móvil o PWA).

La interfaz debe funcionar en vertical y en horizontal sin bloquear la orientación, salvo que una orientación concreta sea esencial.

### 2.11 WCAG 1.3.5: Identificar el propósito de la entrada (AA)

- **Nivel:** AA · **Prioridad:** Media · **Aplica si:** pides datos personales del usuario.

Usa los valores estándar del atributo `autocomplete` (`name`, `email`, `tel`, `street-address`, `cc-number`…) en los campos de datos personales. Ayuda a usuarios con discapacidad cognitiva o motriz y a los gestores de contraseñas.

### 2.12 WCAG 1.4.1: Uso del color (A)

- **Nivel:** A · **Prioridad:** Alta · **Aplica si:** siempre.

El color no puede ser el único medio para transmitir información, indicar una acción o mostrar un estado. Añade texto, icono, patrón o subrayado (por ejemplo, enlaces dentro de párrafos o campos con error).

### 2.13 WCAG 1.4.2: Control del audio (A)

- **Nivel:** A · **Prioridad:** Media · **Aplica si:** hay audio que se reproduce automáticamente.

Si un audio suena automáticamente más de 3 segundos, debe poder pausarse, detenerse o silenciarse con un control accesible. Lo más sencillo: no reproducir audio automáticamente.

### 2.14 WCAG 1.4.3: Contraste mínimo (AA)

- **Nivel:** AA · **Prioridad:** Alta · **Aplica si:** siempre.

El texto normal necesita un contraste de al menos **4,5:1** con el fondo; el texto grande (≥ 18 pt, o ≥ 14 pt en negrita) necesita al menos **3:1**. Comprueba también estados `hover`, `disabled` informativos y texto sobre imágenes.

*Fusiona* la medida «Corregir contraste de color» de la lista de accesibilidad.

### 2.15 WCAG 1.4.4: Cambio de tamaño del texto (AA)

- **Nivel:** AA · **Prioridad:** Alta · **Aplica si:** siempre.

El texto debe poder ampliarse hasta un 200 % con el navegador sin perder contenido ni funcionalidad. Usa unidades relativas (`rem`, `em`) y evita alturas fijas en contenedores de texto.

### 2.16 WCAG 1.4.5: Imágenes de texto (AA)

- **Nivel:** AA · **Prioridad:** Media · **Aplica si:** usas imágenes que contienen texto.

Usa texto real, estilizado con CSS, en lugar de imágenes de texto. Excepción: logotipos.

### 2.17 WCAG 1.4.10: Reflujo (AA)

- **Nivel:** AA · **Prioridad:** Alta · **Aplica si:** siempre.

El contenido debe mostrarse sin desplazamiento horizontal a 320 px de ancho CSS (equivale a un zoom del 400 % en pantalla de escritorio). Excepciones: tablas de datos complejas, mapas, diagramas.

### 2.18 WCAG 1.4.11: Contraste no textual (AA)

- **Nivel:** AA · **Prioridad:** Alta · **Aplica si:** siempre.

Los componentes de interfaz (bordes de inputs, botones, iconos funcionales, indicadores de estado) y los gráficos informativos deben tener un contraste de al menos **3:1** con los colores adyacentes.

### 2.19 WCAG 1.4.12: Espaciado del texto (AA)

- **Nivel:** AA · **Prioridad:** Media · **Aplica si:** siempre.

El diseño no debe romperse cuando el usuario aplique interlineado de 1,5, espaciado de párrafo de 2, espaciado de letras de 0,12 y de palabras de 0,16 (múltiplos del tamaño de fuente). Evita contenedores de altura fija con `overflow: hidden`.

### 2.20 WCAG 1.4.13: Contenido al pasar el puntero o recibir foco (AA)

- **Nivel:** AA · **Prioridad:** Media · **Aplica si:** hay tooltips, menús desplegables o popovers al hover/foco.

El contenido emergente debe poder **cerrarse** sin mover el foco (normalmente con `Esc`), ser **permanecible** (no desaparecer al mover el puntero encima) y **persistente** hasta que el usuario lo descarte o deje de ser válido.

## 3. Principio 2: Operable

Los componentes de la interfaz y la navegación deben poder manejarse.

### 3.1 WCAG 2.1.1: Teclado (A)

- **Nivel:** A · **Prioridad:** Alta · **Aplica si:** siempre.

Toda la funcionalidad debe poder ejecutarse solo con teclado (`Tab`, `Mayús+Tab`, `Enter`, `Espacio`, flechas): abrir diálogos, filtrar, ordenar, exportar o importar archivos, etc. Usa elementos nativos (`<button>`, `<a>`) siempre que puedas.

*Fusiona* la medida «Añadir navegación por teclado» de la lista de accesibilidad (junto con [WCAG 2.1.2](01-accesibilidad.md#32-wcag-212-sin-trampas-para-el-foco-del-teclado-a) y [WCAG 2.4.7](01-accesibilidad.md#313-wcag-247-foco-visible-aa)).

### 3.2 WCAG 2.1.2: Sin trampas para el foco del teclado (A)

- **Nivel:** A · **Prioridad:** Alta · **Aplica si:** hay modales, widgets embebidos o editores.

El foco no puede quedar atrapado en un componente. Un modal puede *confinar* el foco mientras está abierto, pero siempre debe poder cerrarse con teclado (`Esc`) y devolver el foco al elemento que lo abrió.

### 3.3 WCAG 2.1.4: Atajos de teclado de un solo carácter (A)

- **Nivel:** A · **Prioridad:** Media · **Aplica si:** implementas atajos de una sola tecla.

Si existen atajos de un solo carácter (sin modificador), deben poder desactivarse, reasignarse o activarse solo al tener foco el componente. Es un problema típico con usuarios de dictado por voz.

### 3.4 WCAG 2.2.1: Tiempo ajustable (A)

- **Nivel:** A · **Prioridad:** Media · **Aplica si:** hay límites de tiempo (sesiones, temporizadores, carritos).

Si hay un límite de tiempo, el usuario debe poder desactivarlo, ajustarlo o ampliarlo (al menos 10 veces), con aviso previo. Excepciones: eventos en tiempo real o cuando el límite es esencial.

### 3.5 WCAG 2.2.2: Pausar, detener, ocultar (A)

- **Nivel:** A · **Prioridad:** Media · **Aplica si:** hay carruseles, animaciones, tickers o información que se actualiza sola.

El movimiento, parpadeo o desplazamiento que dure más de 5 segundos y se muestre junto a otro contenido, y la información que se actualiza automáticamente (por ejemplo, un temporizador de espera), deben poder pausarse, detenerse u ocultarse.

### 3.6 WCAG 2.3.1: Umbral de tres destellos o menos (A)

- **Nivel:** A · **Prioridad:** Alta · **Aplica si:** hay animaciones, vídeo o efectos de pantalla.

Ningún elemento debe destellar más de 3 veces por segundo (riesgo de crisis epilépticas fotosensibles). Respeta además `prefers-reduced-motion`.

### 3.7 WCAG 2.4.1: Evitar bloques (A)

- **Nivel:** A · **Prioridad:** Alta · **Aplica si:** hay cabecera o navegación repetida.

Incluye un enlace «Saltar al contenido principal» (*skip link*) visible al recibir foco, o landmarks bien definidos, para que usuarios de teclado no recorran la navegación en cada página.

### 3.8 WCAG 2.4.2: Titulado de páginas (A)

- **Nivel:** A · **Prioridad:** Alta · **Aplica si:** siempre.

Cada página debe tener un `<title>` descriptivo y único. Es también la base del título que Google muestra en resultados (ver [SEO-05](05-seo.md#21-seo-05-títulos-y-descripciones-personalizados)).

### 3.9 WCAG 2.4.3: Orden del foco (A)

- **Nivel:** A · **Prioridad:** Alta · **Aplica si:** siempre.

La secuencia de tabulación debe ser lógica y coherente con el significado. Evita `tabindex` positivos; gestiona el foco al abrir y cerrar componentes dinámicos.

### 3.10 WCAG 2.4.4: Propósito de los enlaces, en contexto (A)

- **Nivel:** A · **Prioridad:** Alta · **Aplica si:** siempre.

El texto del enlace (o su contexto inmediato) debe explicar a dónde lleva. Evita «Pulsa aquí» y «Leer más» sin contexto accesible.

### 3.11 WCAG 2.4.5: Múltiples vías (AA)

- **Nivel:** AA · **Prioridad:** Media · **Aplica si:** el sitio tiene más de unas pocas páginas.

Ofrece más de una forma de localizar el contenido: menú, buscador, mapa del sitio, filtros o enlaces relacionados. Excepción: páginas que son paso de un proceso.

### 3.12 WCAG 2.4.6: Encabezados y etiquetas (AA)

- **Nivel:** AA · **Prioridad:** Media · **Aplica si:** siempre.

Encabezados y etiquetas de formulario deben describir el tema o el propósito de forma clara.

### 3.13 WCAG 2.4.7: Foco visible (AA)

- **Nivel:** AA · **Prioridad:** Alta · **Aplica si:** siempre.

Todo elemento enfocable por teclado debe mostrar un indicador de foco visible. No quites `outline` sin sustituirlo por un indicador con buen contraste (ver también [WCAG 1.4.11](01-accesibilidad.md#218-wcag-1411-contraste-no-textual-aa)).

### 3.14 WCAG 2.4.11: Foco no oculto, mínimo (AA)

- **Nivel:** AA (novedad 2.2) · **Prioridad:** Alta · **Aplica si:** hay elementos fijos o flotantes (cabeceras *sticky*, banners de cookies, *toasts*, chats).

Un componente que recibe foco no debe quedar completamente oculto por contenido superpuesto creado por el autor. Prueba con el banner de cookies y la cabecera fija abiertos; `scroll-padding-top` ayuda con las cabeceras fijas.

### 3.15 WCAG 2.5.1: Gestos del puntero (A)

- **Nivel:** A · **Prioridad:** Media · **Aplica si:** hay gestos multipunto o de trazo (pellizcar, deslizar con varios dedos, dibujar).

Toda función que requiera esos gestos debe tener una alternativa de puntero único (botón, toque).

### 3.16 WCAG 2.5.2: Cancelación del puntero (A)

- **Nivel:** A · **Prioridad:** Media · **Aplica si:** siempre que haya controles activables con puntero.

La acción debe ejecutarse al soltar (*up event*) o permitir abortarla moviendo el puntero fuera antes de soltar, o deshacerse. Los controles nativos ya lo cumplen.

### 3.17 WCAG 2.5.3: Etiqueta en el nombre (A)

- **Nivel:** A · **Prioridad:** Media · **Aplica si:** controles con texto visible y `aria-label`.

El nombre accesible debe contener el texto visible (idealmente empezar por él) para que funcione el control por voz. Si el botón dice «Enviar pedido», no pongas `aria-label="Confirmar"`.

### 3.18 WCAG 2.5.4: Activación por movimiento (A)

- **Nivel:** A · **Prioridad:** Media · **Aplica si:** la app reacciona al movimiento del dispositivo (agitar, inclinar).

Debe existir una alternativa con un control en pantalla y la opción de desactivar la reacción al movimiento.

### 3.19 WCAG 2.5.7: Movimientos de arrastre (AA)

- **Nivel:** AA (novedad 2.2) · **Prioridad:** Media · **Aplica si:** hay arrastrar y soltar, deslizadores o reordenación.

Toda acción que se haga arrastrando debe poder hacerse también con un puntero único sin arrastre (botones de mover arriba/abajo, clic para seleccionar y clic para colocar).

### 3.20 WCAG 2.5.8: Tamaño del objetivo, mínimo (AA)

- **Nivel:** AA (novedad 2.2) · **Prioridad:** Alta · **Aplica si:** siempre (especialmente en móvil).

Los objetivos de puntero deben medir al menos **24 × 24 px CSS**, o tener espacio suficiente alrededor para que un círculo de 24 px centrado en cada uno no se solape con otro. Excepciones: enlaces dentro de un texto, controles del navegador, tamaño esencial.

## 4. Principio 3: Comprensible

La información y el manejo de la interfaz deben ser comprensibles.

### 4.1 WCAG 3.1.1: Idioma de la página (A)

- **Nivel:** A · **Prioridad:** Alta · **Aplica si:** siempre.

Define el idioma en la etiqueta raíz: `<html lang="es">`. Permite pronunciación correcta en lectores de pantalla y traducción automática.

### 4.2 WCAG 3.1.2: Idioma de las partes (AA)

- **Nivel:** AA · **Prioridad:** Media · **Aplica si:** hay pasajes en otro idioma.

Marca los cambios de idioma con `lang` en el fragmento (frases en inglés, citas, nombres propios cuya pronunciación importe).

### 4.3 WCAG 3.2.1: Al recibir el foco (A)

- **Nivel:** A · **Prioridad:** Alta · **Aplica si:** siempre.

Recibir el foco no debe provocar un cambio de contexto automático (enviar un formulario, abrir una ventana, mover el foco a otra parte).

### 4.4 WCAG 3.2.2: Al recibir entradas (A)

- **Nivel:** A · **Prioridad:** Alta · **Aplica si:** hay formularios o controles de selección.

Cambiar el valor de un campo no debe provocar un cambio de contexto inesperado sin avisar antes (por ejemplo, un `<select>` que navega al elegir una opción).

### 4.5 WCAG 3.2.3: Navegación coherente (AA)

- **Nivel:** AA · **Prioridad:** Media · **Aplica si:** varias páginas comparten navegación.

Los mecanismos de navegación repetidos conservan el mismo orden relativo en todas las páginas.

### 4.6 WCAG 3.2.4: Identificación coherente (AA)

- **Nivel:** AA · **Prioridad:** Media · **Aplica si:** siempre.

Los componentes con la misma función se identifican igual (misma etiqueta, mismo icono, mismo texto alternativo) en todo el sitio.

### 4.7 WCAG 3.2.6: Ayuda coherente (A)

- **Nivel:** A (novedad 2.2) · **Prioridad:** Media · **Aplica si:** ofreces contacto, chat, FAQ o autoservicio de ayuda en varias páginas.

Los mecanismos de ayuda (datos de contacto, formulario, chat, enlace a FAQ) deben aparecer en la **misma posición relativa** en cada página donde se repitan.

> ❌ **Corrección sobre la lista original:** la lista indicaba nivel AA. En WCAG 2.2 este criterio es de **nivel A** (fuente: W3C, «What's New in WCAG 2.2»).

### 4.8 WCAG 3.3.1: Identificación de errores (A)

- **Nivel:** A · **Prioridad:** Alta · **Aplica si:** hay formularios.

Si se detecta un error de entrada, identifica el campo afectado y descríbelo con texto (no solo con color). Asocia el mensaje al campo con `aria-describedby` y mueve el foco o anúncialo.

*Patrón recomendado (W3C y NN/g).* Mensaje **junto al campo** que nombra el problema y dice cómo corregirlo; en formularios largos, un **resumen de errores** al inicio con un enlace a cada campo (con `role="alert"` si la página no se recarga); **foco** al primer campo con error; no depender solo del color (añade icono y texto). **Valida cuando el usuario sale del campo**, no mientras escribe, y comunica las restricciones (formato, longitud) *antes*. Reserva el estilo de error (rojo, advertencia) para errores reales y conserva lo que la persona ya escribió.

*Fusiona* el punto «Form error states» de un listado posterior.

### 4.9 WCAG 3.3.2: Etiquetas o instrucciones (A)

- **Nivel:** A · **Prioridad:** Alta · **Aplica si:** hay formularios.

Cada campo tiene un `<label>` visible y las instrucciones necesarias (formato esperado, campos obligatorios). El `placeholder` no sustituye a la etiqueta.

### 4.10 WCAG 3.3.3: Sugerencias ante errores (AA)

- **Nivel:** AA · **Prioridad:** Media · **Aplica si:** hay formularios con validación.

Cuando detectes un error y conozcas la corrección, sugiérela («El correo debe incluir @»), salvo que comprometa la seguridad.

### 4.11 WCAG 3.3.4: Prevención de errores, legales, financieros o de datos (AA)

- **Nivel:** AA · **Prioridad:** Media · **Aplica si:** hay compras, contratos, envío de datos o borrado de información.

En acciones con consecuencias legales o financieras, o que modifican o borran datos, permite **revisar, confirmar o deshacer** antes de finalizar (por ejemplo, confirmar antes de limpiar los datos guardados).

### 4.12 WCAG 3.3.7: Entrada redundante (A)

- **Nivel:** A (novedad 2.2) · **Prioridad:** Media · **Aplica si:** hay procesos de varios pasos.

No pidas la misma información dos veces en el mismo proceso: autocompleta o permite elegirla. Excepciones: seguridad (repetir contraseña) o cuando el dato ya no sea válido.

### 4.13 WCAG 3.3.8: Autenticación accesible, mínimo (AA)

- **Nivel:** AA (novedad 2.2) · **Prioridad:** Alta · **Aplica si:** hay registro o inicio de sesión.

No exijas una prueba cognitiva (recordar contraseñas sin poder pegarlas, transcribir códigos, resolver puzles) sin una alternativa. Permite pegar y los gestores de contraseñas, y ofrece métodos alternativos (enlace mágico, passkeys, autenticador).

## 5. Principio 4: Robusto

El contenido debe ser interpretable de forma fiable por tecnologías de apoyo.

### 5.1 WCAG 4.1.2: Nombre, función, valor (A)

- **Nivel:** A · **Prioridad:** Alta · **Aplica si:** hay componentes personalizados (pestañas, menús, acordeones, modales).

Cada componente expone nombre, rol, estado y valor a las tecnologías de apoyo. Primero usa HTML nativo; si construyes un componente propio, aplica ARIA (`role`, `aria-expanded`, `aria-controls`, `aria-selected`…) y mantén los estados sincronizados. La primera regla de ARIA: no uses ARIA si hay un elemento nativo equivalente.

### 5.2 WCAG 4.1.3: Mensajes de estado (AA)

- **Nivel:** AA · **Prioridad:** Media · **Aplica si:** la interfaz actualiza contenido sin recargar (resultados, avisos, carga, éxito/error).

Anuncia los cambios de estado mediante regiones vivas (`role="status"`, `aria-live="polite"`, `role="alert"` para errores) **sin mover el foco**. Ejemplos: «3 resultados», «Guardado», «Tiempo agotado».

> Nota: WCAG 2.2 eliminó el criterio 4.1.1 (*Parsing*), por lo que ya no forma parte de A/AA.

## 6. Documentos y contenido de terceros

### 6.1 ACC-03: Documentos descargables y contenido de terceros

- **Prioridad:** Media
- **Naturaleza:** Obligación legal condicionada
- **Sectores:** INF ● · TIE ◐ · SUS ◐ · UGC ◐ · MEN ◐
- **Regiones:** UE/ES ● · EE. UU. ◐ · UK ◐ · LATAM ◐
- **Verificación:** ➕ Añadida

**De qué trata.** La accesibilidad no termina en el HTML: los PDF, documentos de ofimática y el contenido que integras de terceros (vídeo, chat, mapas, reservas, pasarelas de pago, el propio banner de cookies) forman parte del servicio que el usuario experimenta.

**Qué hacer**

- **Documentos:** priorizar HTML para la información esencial. Cuando haya PDF, etiquetarlo (estructura, orden de lectura, encabezados, texto alternativo, idioma, tablas y formularios) y ofrecer una alternativa equivalente si no puede ser accesible.
- **Terceros:** antes de integrar un servicio, pedir su informe de conformidad con la accesibilidad y probarlo con teclado y lector de pantalla; incluirlo en tus pruebas periódicas.
- Si no es posible integrar una versión accesible, ofrecer un canal alternativo equivalente (formulario, correo, teléfono).
- Controlar qué publicas: los avisos, formularios y documentos subidos por tu equipo deben cumplir los mismos criterios que el resto del sitio.

**Matiz.** La Directiva 2016/2102 excluye en el sector público cierto contenido de terceros que el organismo no financia, desarrolla ni controla; no asumas esa exención para un servicio privado donde tú eliges e integras el componente.

**Fuentes**

- [WCAG 2.2 (W3C)](https://www.w3.org/TR/WCAG22/)
- [Directiva (UE) 2016/2102](https://eur-lex.europa.eu/eli/dir/2016/2102/oj)

## 7. Cómo comprobar la conformidad

- **Automático** (axe, Lighthouse, WAVE): detecta una parte de los problemas (contraste, `alt` ausente, etiquetas) pero no sustituye a la revisión manual.
- **Manual con teclado:** recorre todo el sitio con `Tab` y comprueba foco visible, orden, trampas y atajos.
- **Lector de pantalla** (NVDA, VoiceOver) y **zoom al 200 %/400 %** en las plantillas clave.
- **Pruebas con personas usuarias de tecnologías de apoyo** (lector de pantalla, ampliadores, control por voz, teclados alternativos): no son una obligación legal específica, pero son la forma más eficaz de encontrar los problemas que las pruebas automáticas no detectan.
- **Formularios y flujos críticos:** ver [POST-01](09-post-lanzamiento.md#11-post-01-testear-formularios).
- **Nivel AAA:** no es el mínimo legal. Algunos criterios, como 2.4.13 *Apariencia del foco* (AAA, con requisitos de tamaño y contraste del indicador), son una mejora razonable si el diseño lo permite.
