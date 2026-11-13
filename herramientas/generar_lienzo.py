#!/usr/bin/env python3
"""Genera index.html (lienzo vacío) y style.css a partir de objetivo.js.

Uso (desde la raíz del repositorio):  python herramientas/generar_lienzo.py

Ejecútalo UNA vez al preparar el repositorio, antes de abrirlo al alumnado:
sobrescribe index.html y deja todas las celdas sin pintar.
"""
import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent


def cargar_objetivo():
    texto = (RAIZ / "objetivo.js").read_text(encoding="utf-8")
    cuerpo = re.split(r"^const OBJETIVO\s*=", texto, maxsplit=1, flags=re.M)[1]
    return json.loads(cuerpo.strip().rstrip(";"))


def generar_html(obj):
    n = len(obj["sprite"]) * obj["escala"]
    lineas = []
    for fila in range(1, n + 1):
        lineas.append(f"<!-- Fila {fila} -->")
        for col in range(1, n + 1):
            lineas.append(
                f'<div class="cell" id="c-{fila}-{col}" '
                f'title="Fila {fila}, Columna {col}"></div>'
            )
    celdas = "\n".join(lineas)
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pixel War EDE</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Pixel War EDE</h1>
  <p class="instrucciones">Pinta <strong>una</strong> celda por <em>pull request</em>: busca su línea más abajo y añade el color a la clase, por ejemplo <code>class="cell rojo"</code>.</p>
  <main class="tablero">
    <section>
      <h2>Lienzo</h2>
      <div class="lienzo" id="lienzo" style="--n: {n}">
<!-- LIENZO:INICIO -->
{celdas}
<!-- LIENZO:FIN -->
      </div>
    </section>
    <section>
      <h2>Objetivo</h2>
      <div class="lienzo objetivo" id="objetivo" style="--n: {n}"></div>
      <p id="progreso"></p>
      <h2>Paleta</h2>
      <ul id="paleta"></ul>
    </section>
  </main>
  <script src="objetivo.js"></script>
  <script src="guia.js"></script>
</body>
</html>
"""


def generar_css(obj):
    colores = "\n".join(
        f".{nombre} {{ background-color: {hexa}; }}"
        for nombre, hexa in obj["paleta"].items()
    )
    return f"""/* Generado por herramientas/generar_lienzo.py. Los colores salen de objetivo.js. */
* {{ box-sizing: border-box; }}

body {{
  margin: 0;
  padding: 16px;
  font-family: system-ui, sans-serif;
  background: #f4f4f6;
  color: #1d1d24;
}}

.tablero {{
  display: flex;
  flex-wrap: wrap;
  gap: 32px;
  align-items: flex-start;
}}

.lienzo {{
  display: grid;
  grid-template-columns: repeat(var(--n), var(--celda, 32px));
  border: 1px solid #c8c8d0;
  width: max-content;
  background:
    repeating-conic-gradient(#e6e6ea 0% 25%, #fafafa 0% 50%) 0 0 / 16px 16px;
}}

.objetivo {{ --celda: 16px; }}

.cell {{
  width: var(--celda, 32px);
  height: var(--celda, 32px);
  border: 1px solid rgba(0, 0, 0, 0.08);
}}

.cell.resaltada {{ outline: 3px solid #1e88e5; outline-offset: -3px; }}

/* Celdas con un color que no toca (las marca guia.js) */
.cell.incorrecta {{
  background-image: repeating-linear-gradient(45deg, rgba(0, 0, 0, 0.45) 0 2px, transparent 2px 6px);
}}

#paleta {{
  list-style: none;
  padding: 0;
  display: grid;
  grid-template-columns: repeat(2, max-content);
  gap: 4px 16px;
}}

#paleta span {{
  display: inline-block;
  width: 16px;
  height: 16px;
  margin-right: 6px;
  vertical-align: middle;
  border: 1px solid #0003;
}}

@media (max-width: 600px) {{
  .lienzo {{ --celda: 18px; }}
  .objetivo {{ --celda: 10px; }}
}}

/* Paleta: las 18 clases de color que puede usar el alumnado */
{colores}
"""


def main():
    obj = cargar_objetivo()
    (RAIZ / "index.html").write_text(generar_html(obj), encoding="utf-8", newline="\n")
    (RAIZ / "style.css").write_text(generar_css(obj), encoding="utf-8", newline="\n")
    n = len(obj["sprite"]) * obj["escala"]
    pintables = sum(c != "." for fila in obj["sprite"] for c in fila) * obj["escala"] ** 2
    print(f"Lienzo de {n}x{n} generado: {pintables} celdas a pintar.")


if __name__ == "__main__":
    main()
