#!/usr/bin/env python3
"""Genera una grafica de contribuciones en PIXEL ART a partir de los datos
reales de GitHub. SVG: nitido a cualquier tamano y pesa unos pocos KB."""
import json, os
from collections import OrderedDict

SRC = "/home/sebastian-clavijo/github_perfil/_contrib.json"
OUT = "/home/sebastian-clavijo/github_perfil/assets/grafica-pixeles.svg"

d = json.load(open(SRC))
u = d["data"]["user"]
cal = u["contributionsCollection"]["contributionCalendar"]
weeks = [w["contributionDays"] for w in cal["weeks"]]
total = cal["totalContributions"]

# ---- escala de color en pixel blocks (rampa cian -> azul) ----
RAMPA = ["#12161F", "#1B3A5C", "#1E6FA8", "#1E90FF", "#00E5FF"]
def nivel(n):
    if n == 0: return 0
    if n <= 2:  return 1
    if n <= 5:  return 2
    if n <= 8:  return 3
    return 4

CEL, HUECO = 12, 2
PASO = CEL + HUECO
MARGEN_IZQ, MARGEN_SUP = 46, 30
ANCHO = MARGEN_IZQ + len(weeks) * PASO + 10
ALTO = MARGEN_SUP + 7 * PASO + 16

MESES = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]
DIAS = ["lun", "", "mie", "", "vie", "", "dom"]

partes = []
partes.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{ANCHO}" height="{ALTO}" '
              f'viewBox="0 0 {ANCHO} {ALTO}" font-family="ui-monospace,SFMono-Regular,Menlo,monospace">')
partes.append(f'<rect width="{ANCHO}" height="{ALTO}" fill="#0B0E14"/>')

# etiquetas de mes (cuando cambia el mes en la primera fila de la semana)
visto = None
for i, w in enumerate(weeks):
    mes = w[0]["date"][5:7]
    if mes != visto:
        visto = mes
        x = MARGEN_IZQ + i * PASO
        partes.append(f'<text x="{x}" y="18" fill="#7C8797" font-size="10">{MESES[int(mes)-1]}</text>')

# etiquetas de dia
for fila, txt in enumerate(DIAS):
    if txt:
        y = MARGEN_SUP + fila * PASO + CEL - 2
        partes.append(f'<text x="6" y="{y}" fill="#7C8797" font-size="10">{txt}</text>')

# la reticula de pixeles
for i, w in enumerate(weeks):
    for fila, day in enumerate(w):
        n = day["contributionCount"]
        x = MARGEN_IZQ + i * PASO
        y = MARGEN_SUP + fila * PASO
        c = RAMPA[nivel(n)]
        op = "" if n == 0 else ' opacity="0.95"'
        partes.append(f'<rect x="{x}" y="{y}" width="{CEL}" height="{CEL}" fill="{c}"{op}>'
                      f'<title>{day["date"]}: {n}</title></rect>')

# total, en la esquina
partes.append(f'<text x="{ANCHO-10}" y="{ALTO-4}" fill="#5C6675" font-size="10" '
              f'text-anchor="end">{total} contribuciones · ultimo año</text>')
partes.append("</svg>")

open(OUT, "w", encoding="utf-8").write("\n".join(partes))
print(f"  {os.path.basename(OUT)}  {os.path.getsize(OUT)} bytes  {ANCHO}x{ALTO}")
print(f"  semanas {len(weeks)} · total {total}")

# resumen por nivel, para saber cuanta area queda encendida
from collections import Counter
cnt = Counter()
for w in weeks:
    for day in w:
        cnt[nivel(day["contributionCount"])] += 1
print("  distribucion de pixeles por nivel:", dict(sorted(cnt.items())))
