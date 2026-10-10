# Seguridad y operación

> Última verificación: 2026-10-10 · [Volver al README](../README.md)

Medidas técnicas que mantienen el sitio seguro y disponible. Muchas deben existir **antes** de publicar y revisarse de forma continua, por eso no están dentro del post-lanzamiento. El RGPD exige medidas técnicas y organizativas **adecuadas al riesgo** (art. 32); estas fichas son la base razonable para un sitio corriente y se ajustan al tamaño y la criticidad.

> Esto es una guía técnica y de buenas prácticas, no asesoramiento jurídico. Los sitios de ciertos sectores o tamaños tienen obligaciones de ciberseguridad propias que esta guía no cubre.

<!-- INDICE -->
**Índice**

- [1. Protección del sitio](#1-protección-del-sitio)
  - [1.1 SEG-01: HTTPS y cabeceras de seguridad](#11-seg-01-https-y-cabeceras-de-seguridad)
  - [1.2 SEG-02: Secretos, accesos y autenticación multifactor](#12-seg-02-secretos-accesos-y-autenticación-multifactor)
  - [1.3 SEG-03: Actualizaciones y análisis de vulnerabilidades](#13-seg-03-actualizaciones-y-análisis-de-vulnerabilidades)
- [2. Continuidad y observabilidad](#2-continuidad-y-observabilidad)
  - [2.1 SEG-04: Copias de seguridad y restauración probada](#21-seg-04-copias-de-seguridad-y-restauración-probada)
  - [2.2 SEG-05: Disponibilidad, errores y registros](#22-seg-05-disponibilidad-errores-y-registros)
<!-- /INDICE -->

## 1. Protección del sitio

### 1.1 SEG-01: HTTPS y cabeceras de seguridad

- **Prioridad:** Alta
- **Naturaleza:** Obligación legal condicionada
- **Sectores:** INF ● · TIE ● · SUS ● · UGC ● · MEN ●
- **Regiones:** UE/ES ● · EE. UU. ◐ · UK ● · LATAM ●
- **Verificación:** ➕ Añadida

**De qué trata.** Cifrar todo el tráfico y configurar las cabeceras de respuesta que limitan clases enteras de ataques. HTTPS es la base: sin él, formularios, sesiones y datos personales viajan en claro. La obligación legal deriva de aplicar medidas adecuadas al riesgo cuando tratas datos personales (art. 32 RGPD).

**Qué hacer**

- Servir **todo** el sitio por HTTPS, redirigir HTTP a HTTPS y eliminar el contenido mixto. Automatizar la renovación del certificado.
- `Strict-Transport-Security` (HSTS) cuando HTTPS funcione de forma estable en todos los subdominios: un certificado caducado con un `max-age` largo bloquea el acceso, así que pruébalo antes de añadir `preload`.
- `Content-Security-Policy`: empezar en modo **solo informe** (`Content-Security-Policy-Report-Only`), observar las infracciones y endurecer progresivamente. Evita el JavaScript en línea.
- `X-Content-Type-Options: nosniff`, `Referrer-Policy` explícita (p. ej. `strict-origin-when-cross-origin`) y `Permissions-Policy` desactivando lo que no uses.
- Control de incrustación con `frame-ancestors` (CSP) en lugar de `X-Frame-Options`.
- **No uses** `X-XSS-Protection` (obsoleta) ni `Public-Key-Pins`.
- Cookies de sesión con `Secure`, `HttpOnly` y `SameSite`.

**Matiz.** Una CSP restrictiva sin pruebas puede romper funciones legítimas (pagos, mapas, analítica con consentimiento). Pruébala en un entorno previo. HTTPS además es una señal que Google prefiere al elegir la URL canónica (ver [SEO-06](05-seo.md#31-seo-06-canónicas-y-contenido-duplicado)).

**Fuentes**

- [OWASP: HTTP Headers Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html)
- [OWASP: Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
- [RGPD art. 32 (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2016/679/oj)

### 1.2 SEG-02: Secretos, accesos y autenticación multifactor

- **Prioridad:** Alta
- **Naturaleza:** Buena práctica
- **Sectores:** INF ● · TIE ● · SUS ● · UGC ● · MEN ●
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ➕ Añadida

**De qué trata.** Proteger las credenciales y los puntos de acceso al sitio: panel del CMS, hosting, DNS, registrador de dominio, correo del dominio, repositorio y proveedores. Un acceso comprometido a cualquiera de ellos equivale a perder el sitio.

**Qué hacer**

- **Autenticación multifactor** en todas las cuentas administrativas (CMS, hosting, DNS, registrador, correo, repositorio, pasarelas de pago). Mejor con aplicación autenticadora o llaves de seguridad que con SMS.
- **Secretos fuera del código:** claves de API, tokens y contraseñas de base de datos en un gestor de secretos o variables de entorno, nunca en el repositorio. Rotarlos si se exponen y revisar el historial.
- **Mínimo privilegio:** cada persona y servicio con los permisos que necesita. Cuentas nombradas, no compartidas.
- Contraseñas únicas y gestor de contraseñas; bloquear o limitar intentos de acceso.
- Revisar periódicamente quién tiene acceso y dar de baja cuentas de personas o proveedores que ya no lo necesitan.
- Si tu sitio tiene inicio de sesión de usuarios, no bloquees pegar contraseñas ni los gestores de contraseñas ([WCAG 3.3.8](01-accesibilidad.md#413-wcag-338-autenticación-accesible-mínimo-aa)).

**Fuentes**

- [OWASP: Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
- [OWASP: Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

### 1.3 SEG-03: Actualizaciones y análisis de vulnerabilidades

- **Prioridad:** Alta
- **Naturaleza:** Buena práctica
- **Sectores:** INF ● · TIE ● · SUS ● · UGC ● · MEN ●
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ➕ Añadida

**De qué trata.** Mantener el CMS, los complementos, las librerías y el servidor con un riesgo razonable. La mayoría de los incidentes en sitios corrientes explotan componentes desactualizados con vulnerabilidades ya publicadas.

**Qué hacer**

- Inventariar componentes: CMS, plugins y temas, dependencias de código, servidor y runtime.
- Activar actualizaciones automáticas para parches de seguridad y revisar el resto en una ventana fija. La frecuencia depende de la exposición y la criticidad.
- Usar un análisis de dependencias (por ejemplo, el de tu gestor de paquetes o el de la plataforma de código) y suscribirte a los avisos de seguridad de los componentes críticos.
- **Reducir superficie:** eliminar plugins, temas y cuentas que no uses; no mantener software sin soporte.
- Probar las actualizaciones en un entorno previo antes de producción y poder revertir.
- Tomar el [OWASP Top 10](https://owasp.org/www-project-top-ten/) como lista de categorías a revisar en desarrollos propios.

**Fuentes:** [OWASP Top 10](https://owasp.org/www-project-top-ten/)

## 2. Continuidad y observabilidad

### 2.1 SEG-04: Copias de seguridad y restauración probada

- **Prioridad:** Alta (si perder el sitio o sus datos tendría impacto)
- **Naturaleza:** Buena práctica
- **Sectores:** INF ◐ · TIE ● · SUS ● · UGC ● · MEN ●
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ➕ Añadida

**De qué trata.** Tener copias recientes, separadas del servidor original y **comprobar que se pueden restaurar**. Una copia que nunca se ha restaurado es una hipótesis. También es la defensa principal frente al ransomware y a los errores humanos.

**Qué hacer**

- Definir qué se copia (base de datos, archivos subidos, configuración) y con qué frecuencia, según cuánto trabajo o dato puedas permitirte perder.
- Guardar copias fuera del entorno de producción y, si es posible, inmutables o desconectadas; cifrarlas.
- **Probar la restauración** de forma periódica y medir cuánto tarda.
- Documentar el procedimiento para que pueda hacerlo otra persona.
- Definir cuánto tiempo conservas las copias: los datos personales que ya hayas suprimido de producción no deben conservarse indefinidamente en ellas (ver [PRIV-05](02-privacidad-cookies-y-comunicaciones.md#24-priv-05-proceso-de-eliminación-de-datos-y-ejercicio-de-derechos)).

**Fuentes:** [CISA: guía contra el ransomware](https://www.cisa.gov/stopransomware/ransomware-guide)

### 2.2 SEG-05: Disponibilidad, errores y registros

- **Prioridad:** Media
- **Naturaleza:** Buena práctica
- **Sectores:** INF ◐ · TIE ● · SUS ● · UGC ● · MEN ◐
- **Regiones:** UE/ES ● · EE. UU. ● · UK ● · LATAM ●
- **Verificación:** ➕ Añadida

**De qué trata.** Enterarte de que el sitio falla antes de que lo haga un usuario, y conservar la información necesaria para investigar incidentes sin acumular datos personales de más.

**Qué hacer**

- Monitorizar la disponibilidad desde fuera (comprobaciones periódicas de las páginas y flujos críticos) y recibir alertas en un canal que alguien lea.
- Registrar errores de servidor y de cliente, y revisarlos tras cada despliegue.
- **Minimizar los registros:** no guardar contraseñas, tokens, datos de pago ni campos de formulario completos; limitar las direcciones IP y otros identificadores a lo necesario; fijar plazos de conservación y restringir quién accede.
- Para CSP, el modo solo informe permite observar infracciones antes de aplicar la política ([SEG-01](07-seguridad-y-operacion.md#11-seg-01-https-y-cabeceras-de-seguridad)).
- Los registros son también la base para detectar y documentar brechas ([PRIV-18](02-privacidad-cookies-y-comunicaciones.md#62-priv-18-brechas-de-seguridad-e-incidentes)).

**Fuentes:** [OWASP: Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
