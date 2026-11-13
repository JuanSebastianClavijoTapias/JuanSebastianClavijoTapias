#!/usr/bin/env python3
"""Grafica en PIXEL ART de lineas de codigo por proyecto.
Datos medidos sobre los repos reales (sin .venv, node_modules, migraciones)."""
import os

OUT = "/home/sebastian-clavijo/github_perfil/assets/grafica-lineas.svg"

# (proyecto, lineas, nota)  — datos medidos, no estimados
DATOS = [
    ("AesthetiCare", 36982),
    ("KanView",      20449),
    ("Balance",      12910),
    ("Orion",        11685),
    ("ReqAI",         7544),
]
TOTAL = sum(n for _, n in DATOS)

# ---- geometria de pixel ----
BLOQUE, HUECO = 13, 2
PASO = BLOQUE + HUECO
X_LABEL, X_BARRA, ALTO_FILA = 18, 190, 34
MARGEN_SUP = 54

ANCHO = X_BARRA + 38 * PASO + 156
ALTO = MARGEN_SUP + len(DATOS) * ALTO_FILA + 46

RAMPA = ["#1B3A5C", "#1E6FA8", "#1E90FF", "#00E5FF", "#5FFBF1"]

s = []
s.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{ANCHO}" height="{ALTO}" '
         f'viewBox="0 0 {ANCHO} {ALTO}" font-family="ui-monospace,SFMono-Regular,Menlo,monospace">')
s.append(f'<rect width="{ANCHO}" height="{ALTO}" fill="#0B0E14"/>')

# titulo
s.append(f'<text x="18" y="24" fill="#00E5FF" font-size="11" letter-spacing="3">LÍNEAS DE CÓDIGO POR PROYECTO</text>')
s.append(f'<text x="18" y="40" fill="#7C8797" font-size="10" letter-spacing="1">'
         f'medido sobre el repositorio · sin dependencias ni migraciones</text>')
# regla de acento
s.append(f'<rect x="18" y="46" width="54" height="2" fill="#E5502E"/>')
# leyenda: que significa un bloque
LX = ANCHO - 18
s.append(f'<rect x="{LX-140}" y="18" width="13" height="13" fill="#1E90FF"/>')
s.append(f'<text x="{LX-122}" y="28" fill="#7C8797" font-size="9.5" letter-spacing="0.6">1 bloque = 1.000 líneas</text>')

for i, (nombre, lineas) in enumerate(DATOS):
    y = MARGEN_SUP + i * ALTO_FILA
    # etiqueta
    s.append(f'<text x="{X_LABEL}" y="{y+BLOQUE+2}" fill="#A6ABB4" font-size="11.5">{nombre}</text>')
    # barra en bloques de pixel (1 bloque = 1000 lineas)
    bloques = max(1, round(lineas / 1000))
    color = RAMPA[min(len(RAMPA)-1, 1 + i % 4)]
    for b in range(bloques):
        x = X_BARRA + b * PASO
        s.append(f'<rect x="{x}" y="{y}" width="{BLOQUE}" height="{BLOQUE}" fill="{color}"/>')
    # valor alineado en una columna fija a la derecha
    s.append(f'<text x="{ANCHO-18}" y="{y+BLOQUE+1}" text-anchor="end" '
             f'fill="#F2F0ED" font-size="12">{lineas:,}</text>'.replace(",", "."))

# total
yt = MARGEN_SUP + len(DATOS) * ALTO_FILA + 12
s.append(f'<rect x="18" y="{yt-10}" width="{ANCHO-36}" height="1" fill="#1E2430"/>')
s.append(f'<text x="18" y="{yt+14}" fill="#7C8797" font-size="10.5" letter-spacing="1.5">TOTAL</text>')
s.append(f'<text x="{X_BARRA}" y="{yt+14}" fill="#5C6675" font-size="10" letter-spacing="1">líneas en 5 proyectos</text>')
s.append(f'<text x="{ANCHO-18}" y="{yt+16}" text-anchor="end" fill="#00E5FF" font-size="15">{TOTAL:,}</text>'.replace(",", "."))
s.append("</svg>")

open(OUT, "w", encoding="utf-8").write("\n".join(s))
print(f"  {os.path.basename(OUT)}  {os.path.getsize(OUT)} bytes  {ANCHO}x{ALTO}")
print(f"  total real: {TOTAL} lineas")
for n, l in DATOS:
    print(f"    {n:14} {l:>7}  ({round(l/1000)} bloques)")
