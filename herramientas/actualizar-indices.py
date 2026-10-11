#!/usr/bin/env python3
"""Regenera la numeración de encabezados, los índices, los enlaces cruzados,
el índice de medidas del README y la matriz de prioridad/sector/región.

Uso:  python herramientas/actualizar-indices.py
"""
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
GUIA = RAIZ / "guia"
README = RAIZ / "README.md"
MATRIZ = GUIA / "10-matriz.md"

ID = r"(?:ACC|PRIV|COM|PI|SEO|REN|SEG|UX|POST)-\d+|WCAG \d\.\d\.\d+"
SECTORES = [
    ("INF", "Informativo, educativo o blog"),
    ("TIE", "Tienda online"),
    ("SUS", "Suscripción o SaaS"),
    ("UGC", "Contenido de usuarios"),
    ("MEN", "Servicios para menores"),
]
REGIONES = [
    ("UE/ES", "UE y España"),
    ("EE. UU.", "EE. UU."),
    ("UK", "Reino Unido"),
    ("LATAM", "Latinoamérica"),
]
ORDEN_PRIORIDAD = ["Alta", "Media", "Baja"]
SIMBOLOS_ETIQUETA = {
    "●": "Aplica / prioritaria",
    "◐": "Según condiciones",
    "○": "No suele aplicar",
}
SIMBOLOS_REGION = {
    "●": "Obligación directa o más estricta",
    "◐": "Con matices o por otra norma",
    "○": "Sin equivalente relevante",
}


# ----------------------------------------------------------------- utilidades
def slug(texto):
    """Ancla al estilo de GitHub."""
    s = re.sub(r"[^\w\- ]", "", texto.lower())
    return s.replace(" ", "-")


def lineas_fuera_de_codigo(lineas):
    """Genera (indice, linea) solo para líneas fuera de bloques de código."""
    dentro = False
    for i, l in enumerate(lineas):
        if l.lstrip().startswith("```"):
            dentro = not dentro
            continue
        if not dentro:
            yield i, l


def numerar(texto):
    """Renumera los encabezados H2/H3. Devuelve (texto, lista de encabezados)."""
    lineas = texto.split("\n")
    c2 = c3 = 0
    encabezados = []
    for i, l in lineas_fuera_de_codigo(lineas):
        m = re.match(r"^(#{2,3}) (.*)$", l)
        if not m:
            continue
        nivel = len(m.group(1))
        titulo = re.sub(r"^\d+(?:\.\d+)*\.?\s+", "", m.group(2)).strip()
        if nivel == 2:
            c2 += 1
            c3 = 0
            num = f"{c2}."
            completo = f"{num} {titulo}"
        else:
            c3 += 1
            num = f"{c2}.{c3}"
            completo = f"{num} {titulo}"
        lineas[i] = f"{m.group(1)} {completo}"
        encabezados.append(
            {"nivel": nivel, "titulo": titulo, "completo": completo,
             "ancla": slug(completo), "linea": i}
        )
    return "\n".join(lineas), encabezados


def insertar_indice(texto, encabezados):
    inicio, fin = "<!-- INDICE -->", "<!-- /INDICE -->"
    if inicio not in texto or fin not in texto:
        return texto
    items = []
    for h in encabezados:
        sangria = "  " if h["nivel"] == 3 else ""
        items.append(f"{sangria}- [{h['completo']}](#{h['ancla']})")
    bloque = f"{inicio}\n**Índice**\n\n" + "\n".join(items) + f"\n{fin}"
    return re.sub(re.escape(inicio) + r".*?" + re.escape(fin), lambda _: bloque, texto, flags=re.S)


def parsear_medidas(texto, encabezados, archivo):
    """Extrae identificador y ficha de cada encabezado H3 con ID."""
    lineas = texto.split("\n")
    medidas = []
    seccion = ""
    for idx, h in enumerate(encabezados):
        if h["nivel"] == 2:
            seccion = h["titulo"]
            continue
        m = re.match(rf"^({ID}): (.*)$", h["titulo"])
        if not m:
            continue
        fin = encabezados[idx + 1]["linea"] if idx + 1 < len(encabezados) else len(lineas)
        cuerpo = lineas[h["linea"] + 1: fin]
        ficha = {}
        for l in cuerpo:
            f = re.match(r"- \*\*(Prioridad|Naturaleza|Sectores|Regiones|Verificación):\*\* (.*)", l)
            if f:
                ficha[f.group(1)] = f.group(2).strip()
            w = re.match(r"- \*\*Nivel:\*\* (A{1,3})\b.*?\*\*Prioridad:\*\* (\w+)(?: · \*\*Aplica si:\*\* (.*))?", l)
            if w:
                ficha["Nivel"] = w.group(1)
                ficha["Prioridad"] = w.group(2)
                ficha["Aplica"] = (w.group(3) or "").strip()
        medidas.append({
            "id": m.group(1), "titulo": m.group(2), "ancla": h["ancla"],
            "archivo": archivo, "seccion": seccion, "ficha": ficha,
            "wcag": m.group(1).startswith("WCAG"),
        })
    return medidas


def resolver_enlaces(texto, mapa, prefijo=""):
    """Convierte [[ID]] y [ID](...) en enlaces con el ancla actual."""
    def enlace(id_):
        if id_ not in mapa:
            return None
        arch, ancla = mapa[id_]
        return f"[{id_}]({prefijo}{arch}#{ancla})"

    patron = re.compile(rf"\[\[({ID})\]\]|\[({ID})\]\([^)]*\)")

    def sustituir(m):
        id_ = m.group(1) or m.group(2)
        return enlace(id_) or m.group(0)

    salida = []
    dentro = False
    for l in texto.split("\n"):
        if l.lstrip().startswith("```"):
            dentro = not dentro
            salida.append(l)
            continue
        if dentro:
            salida.append(l)
            continue
        partes = l.split("`")  # los tramos impares son código en línea
        for k in range(0, len(partes), 2):
            partes[k] = patron.sub(sustituir, partes[k])
        salida.append("`".join(partes))
    return "\n".join(salida)


def simbolos(cadena, claves):
    """'INF ◐ · TIE ●' -> {'INF': '◐', 'TIE': '●'}"""
    res = {}
    for clave, _ in claves:
        m = re.search(re.escape(clave) + r"\s*([●◐○])", cadena or "")
        res[clave] = m.group(1) if m else "–"
    return res


def primera_palabra(cadena):
    m = re.match(r"(Alta|Media|Baja)", cadena or "")
    return m.group(1) if m else "–"


# ---------------------------------------------------------------- generación
def enlace_medida(m, prefijo=""):
    return f"[{m['id']}]({prefijo}{m['archivo']}#{m['ancla']})"


def bloque_medidas_readme(medidas, titulos, archivos):
    """Índice de medidas del README, agrupado por archivo y sección."""
    salida = []
    for arch in archivos:
        ms = [m for m in medidas if m["archivo"] == arch]
        if not ms:
            continue
        n_wcag = sum(1 for m in ms if m["wcag"])
        n_otras = len(ms) - n_wcag
        resumen = f"{n_otras} medidas" if not n_wcag else f"{n_otras} medida legal y {n_wcag} criterios WCAG"
        salida.append(f"### {titulos[arch]}")
        salida.append("")
        salida.append(f"Archivo: [guia/{arch}](guia/{arch}) · {resumen}")
        salida.append("")
        secciones = []
        for m in ms:
            if m["seccion"] not in secciones:
                secciones.append(m["seccion"])
        for sec in secciones:
            salida.append(f"- **{sec}**")
            for m in [x for x in ms if x["seccion"] == sec]:
                pr = primera_palabra(m["ficha"].get("Prioridad", ""))
                extra = m["ficha"].get("Naturaleza", "")
                if m["wcag"]:
                    extra = f"Nivel {m['ficha'].get('Nivel', '?')}"
                salida.append(
                    f"  - {enlace_medida(m, 'guia/')}: {m['titulo']} — *{pr} · {extra}*"
                )
        salida.append("")
    return "\n".join(salida).rstrip()


def tabla_matriz(medidas, prefijo=""):
    cab = ["Medida", "Prioridad", "Naturaleza"] + [c for c, _ in SECTORES] + [c for c, _ in REGIONES]
    filas = ["| " + " | ".join(cab) + " |", "|" + "|".join(["---"] * len(cab)) + "|"]
    for m in medidas:
        f = m["ficha"]
        sec = simbolos(f.get("Sectores"), SECTORES)
        reg = simbolos(f.get("Regiones"), REGIONES)
        celdas = [
            f"{enlace_medida(m, prefijo)}: {m['titulo']}",
            primera_palabra(f.get("Prioridad", "")),
            f.get("Naturaleza", "–"),
        ] + [sec[c] for c, _ in SECTORES] + [reg[c] for c, _ in REGIONES]
        filas.append("| " + " | ".join(celdas) + " |")
    return "\n".join(filas)


def lista_por_prioridad(ms):
    salida = []
    for pr in ORDEN_PRIORIDAD:
        grupo = [m for m in ms if primera_palabra(m["ficha"].get("Prioridad", "")) == pr]
        if grupo:
            salida.append(f"- **Prioridad {pr}**")
            salida.extend(f"  - {enlace_medida(m)}: {m['titulo']}" for m in grupo)
    return salida


def lista_simple(ms):
    return [f"- {enlace_medida(m)}: {m['titulo']}" for m in ms] or ["- Ninguna"]


def generar_matriz(medidas, wcag):
    otras = [m for m in medidas if not m["wcag"]]
    L = []
    L.append("# Matriz de prioridad, sector y región")
    L.append("")
    L.append("> Archivo **generado automáticamente** por `herramientas/actualizar-indices.py`. No lo edites a mano: cambia las fichas de cada medida y vuelve a ejecutar el script. · [Volver al README](../README.md)")
    L.append("")
    L.append("Vista transversal de todas las medidas para decidir qué hacer según tu proyecto.")
    L.append("")
    L.append("<!-- INDICE -->")
    L.append("<!-- /INDICE -->")
    L.append("")
    L.append("## Leyenda")
    L.append("")
    L.append("| Sectores | |")
    L.append("|---|---|")
    for c, n in SECTORES:
        L.append(f"| `{c}` | {n} |")
    L.append("")
    L.append("| Regiones | |")
    L.append("|---|---|")
    for c, n in REGIONES:
        L.append(f"| `{c}` | {n} |")
    L.append("")
    L.append("| Símbolo | En un sector | En una región |")
    L.append("|---|---|---|")
    for s in "●◐○":
        L.append(f"| {s} | {SIMBOLOS_ETIQUETA[s]} | {SIMBOLOS_REGION[s]} |")
    L.append("")
    L.append("## Matriz de medidas")
    L.append("")
    L.append("Todas las medidas excepto los criterios WCAG (ver la sección siguiente).")
    L.append("")
    L.append(tabla_matriz(otras))
    L.append("")
    L.append("## Criterios WCAG 2.2 A y AA")
    L.append("")
    L.append("Los " + str(len(wcag)) + " criterios comparten sector y región con [ACC-01](" + f"01-accesibilidad.md#{[m for m in otras if m['id']=='ACC-01'][0]['ancla']}" + "): obligación directa en la UE para los servicios cubiertos, y referencia técnica habitual en EE. UU., Reino Unido y Latinoamérica. Lo que cambia entre criterios es la prioridad y la condición «aplica si».")
    L.append("")
    por_pr = {pr: [m for m in wcag if m["ficha"].get("Prioridad") == pr] for pr in ORDEN_PRIORIDAD}
    for pr in ORDEN_PRIORIDAD:
        if por_pr[pr]:
            L.append(f"- **Prioridad {pr} ({len(por_pr[pr])}):** " + ", ".join(
                f"{enlace_medida(m)}" for m in por_pr[pr]))
    L.append("")
    L.append("## Vista por sector")
    L.append("")
    L.append("Para cada sector, las medidas que aplican (●) agrupadas por prioridad y las que dependen de condiciones (◐). Los criterios WCAG se añaden a todos los sectores con servicios online.")
    L.append("")
    for cod, nombre in SECTORES:
        L.append(f"### {nombre} (`{cod}`)")
        L.append("")
        esenciales = [m for m in otras if simbolos(m["ficha"].get("Sectores"), SECTORES)[cod] == "●"]
        cond = [m for m in otras if simbolos(m["ficha"].get("Sectores"), SECTORES)[cod] == "◐"]
        L.append("**Aplican (●)**")
        L.append("")
        L.extend(lista_por_prioridad(esenciales) or ["- Ninguna"])
        L.append("")
        L.append("**Según condiciones (◐)**")
        L.append("")
        L.extend(lista_simple(cond))
        L.append("")
    L.append("## Vista por región")
    L.append("")
    L.append("Para cada región, dónde la regulación es más estricta (●), dónde aplica con matices (◐) y qué medidas legales son propias de otra región (○). Las medidas de SEO, rendimiento y post-lanzamiento son universales y no se repiten aquí.")
    L.append("")
    legales = [m for m in otras if not m["id"].startswith(("SEO-", "REN-", "SEG-", "UX-", "POST-"))]
    for cod, nombre in REGIONES:
        L.append(f"### {nombre} (`{cod}`)")
        L.append("")
        for simb, etiqueta in (("●", "Obligación directa o más estricta"), ("◐", "Con matices o por otra norma"), ("○", "Sin equivalente relevante")):
            grupo = [m for m in legales if simbolos(m["ficha"].get("Regiones"), REGIONES)[cod] == simb]
            L.append(f"**{simb} {etiqueta}**")
            L.append("")
            L.extend(lista_simple(grupo))
            L.append("")
    return "\n".join(L).rstrip() + "\n"


# ---------------------------------------------------------------------- main
def main():
    archivos = sorted(p.name for p in GUIA.glob("*.md") if p.name != MATRIZ.name)
    textos, medidas, titulos = {}, [], {}

    # Pasada 1: numerar y reunir medidas de los archivos escritos a mano.
    for arch in archivos:
        t = (GUIA / arch).read_text(encoding="utf-8")
        t, enc = numerar(t)
        titulos[arch] = re.match(r"# (.*)", t).group(1)
        textos[arch] = (t, enc)
        medidas.extend(parsear_medidas(t, enc, arch))

    wcag = [m for m in medidas if m["wcag"]]
    mapa = {m["id"]: (m["archivo"], m["ancla"]) for m in medidas}

    # Matriz (archivo generado completo).
    tm = generar_matriz(medidas, wcag)
    tm, enc_m = numerar(tm)
    tm = insertar_indice(tm, enc_m)
    tm = resolver_enlaces(tm, mapa)
    MATRIZ.write_text(tm, encoding="utf-8", newline="\n")

    # Archivos de la guía.
    for arch in archivos:
        t, enc = textos[arch]
        t = insertar_indice(t, enc)
        t = resolver_enlaces(t, mapa)
        (GUIA / arch).write_text(t, encoding="utf-8", newline="\n")

    # README: índice de medidas, numeración, índice y enlaces.
    r = README.read_text(encoding="utf-8")
    bloque = bloque_medidas_readme(medidas, titulos, archivos)
    r = re.sub(
        r"<!-- MEDIDAS -->.*?<!-- /MEDIDAS -->",
        lambda _: f"<!-- MEDIDAS -->\n{bloque}\n<!-- /MEDIDAS -->",
        r, flags=re.S,
    )
    r, enc_r = numerar(r)
    r = insertar_indice(r, enc_r)
    mapa_readme = {k: (f"guia/{a}", an) for k, (a, an) in mapa.items()}
    r = resolver_enlaces(r, mapa_readme)
    README.write_text(r, encoding="utf-8", newline="\n")

    otras = [m for m in medidas if not m["wcag"]]
    print(f"Medidas: {len(otras)} + {len(wcag)} criterios WCAG en {len(archivos)} archivos.")


if __name__ == "__main__":
    main()
