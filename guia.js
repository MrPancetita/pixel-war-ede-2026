// Dibuja el objetivo, la paleta y el progreso, y enlaza cada celda del lienzo
// con su celda objetivo al pasar el ratón. No hace falta tocar este archivo.
(function () {
  const obj = OBJETIVO;
  const n = obj.sprite.length * obj.escala;

  function objetivoDe(fila, col) {
    const letra = obj.sprite[Math.floor((fila - 1) / obj.escala)][Math.floor((col - 1) / obj.escala)];
    return letra === "." ? null : obj.leyenda[letra];
  }

  const lienzo = document.getElementById("lienzo");
  const panelObjetivo = document.getElementById("objetivo");
  let total = 0;
  let correctas = 0;
  let incorrectas = 0;

  for (let fila = 1; fila <= n; fila++) {
    for (let col = 1; col <= n; col++) {
      const color = objetivoDe(fila, col);
      const celdaObj = document.createElement("div");
      celdaObj.className = "cell" + (color ? " " + color : "");
      celdaObj.id = `o-${fila}-${col}`;
      celdaObj.title = `Fila ${fila}, Columna ${col}: ${color || "vacía (no se pinta)"}`;
      panelObjetivo.appendChild(celdaObj);

      const celda = document.getElementById(`c-${fila}-${col}`);
      if (!celda) continue;
      celda.title = `Fila ${fila}, Columna ${col} · objetivo: ${color || "vacía (no se pinta)"}`;
      const pintada = [...celda.classList].find((c) => c in obj.paleta) || null;
      if (color) {
        total++;
        if (pintada === color) correctas++;
      }
      if (pintada && pintada !== color) {
        incorrectas++;
        celda.classList.add("incorrecta");
        celda.title += ` · ⚠ tiene ${pintada}: ¡arréglala!`;
      }
      celda.addEventListener("mouseenter", () => celdaObj.classList.add("resaltada"));
      celda.addEventListener("mouseleave", () => celdaObj.classList.remove("resaltada"));
    }
  }

  const pct = total ? Math.round((100 * correctas) / total) : 0;
  document.getElementById("progreso").textContent =
    `Progreso: ${correctas} de ${total} celdas (${pct} %)` +
    (incorrectas ? ` · ⚠ ${incorrectas} con color incorrecto (rayadas)` : "");

  const paleta = document.getElementById("paleta");
  for (const [nombre, hexa] of Object.entries(obj.paleta)) {
    const li = document.createElement("li");
    const muestra = document.createElement("span");
    muestra.style.background = hexa;
    li.appendChild(muestra);
    li.appendChild(document.createTextNode(nombre));
    paleta.appendChild(li);
  }

  lienzo.setAttribute("aria-label", `Lienzo de ${n} por ${n} celdas`);
})();
