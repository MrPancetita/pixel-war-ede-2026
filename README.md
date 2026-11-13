# Pixel War EDE 🎨

Entre toda la clase vamos a pintar un sprite de *Realm of the Mad God*, celda a celda, usando Git y GitHub: cada celda es una *pull request*.

**Mira cómo va el dibujo:** `https://scontreraslopez.github.io/pixel-war-ede-2026/`

## Reglas

1. Cada *pull request* cambia **una sola celda**: cambia **una línea** de `index.html` y nada más.
2. La celda tiene que quedar como en el dibujo **objetivo**. Abre la página y pasa el ratón por el lienzo: verás la fila, la columna y el color que le toca a cada celda.
3. Tienes que hacer **2 celdas**, con **al menos 48 horas** entre una y otra (si la primera se fusiona el lunes a las 10:00, la segunda no entra hasta el miércoles a las 10:00). Puedes abrir la segunda PR antes: el bot la dejará esperando y la fusionará cuando te toque.
4. Si tu PR tiene **conflictos**, tendrás que resolverlos tú (el bot te explica cómo).
5. Un bot revisa las PR cada pocos minutos: si tu PR es válida y no tiene conflictos, la fusiona sola. Si no, te deja un comentario explicando qué pasa.
6. **Cuidado con el saboteador:** de vez en cuando el bot pinta una celda de un color que no toca. En la página se ven **rayadas**. Arreglarlas también cuenta como una de tus celdas:
    - Si la celda es del dibujo, cambia el color por el correcto: `class="cell verde"` → `class="cell rojo"`.
    - Si la celda es de fondo, quítale el color: `class="cell verde"` → `class="cell"`.

## Cómo pintar una celda

1. Haz un **fork** de este repositorio y clónalo (o directamente `gh repo fork USUARIO-PROFE/NOMBRE-REPO --clone`).
2. Crea una rama para tu celda: `git switch -c celda-5-7`
3. Abre `index.html`, busca la línea de tu celda (por ejemplo, `id="c-5-7"`) y añade el color a la clase:

    ```html
    <div class="cell rojo" id="c-5-7" title="Fila 5, Columna 7"></div>
    ```

4. Guarda **sin formatear** el archivo (el repositorio ya trae desactivado el formateo automático de VS Code; si usas otro editor, ojo).
5. Commit y push:

    ```bash
    git add index.html
    git commit -m "feat: pinta la celda (5, 7) de rojo"
    git push origin celda-5-7
    ```

6. Abre la *pull request* desde tu fork hacia este repositorio y espera al comentario del bot.

**Antes de tu segunda celda**, actualiza tu `main` con lo que han pintado los demás:

```bash
git switch main
git pull upstream main
git switch -c celda-OTRA
```

## Después de abrir la PR: ¡estate atento!

Abrir la PR **no significa que tu celda esté pintada**. Tu PR queda pendiente de revisión por el bot:

- **En unos minutos** el bot la revisa y te deja un comentario y una etiqueta (mira la tabla de abajo).
- Si queda **en espera**, se fusiona sola cuando te toque. El bot pasa a revisarla **cada 15 minutos más o menos**, así que puede tardar un poco más de la hora que te diga.
- **Mientras tu PR siga abierta, puede cambiar de estado.** Si otra persona o el saboteador cambian tu celda o la de al lado, tu PR pasará a tener un **conflicto** que tendrás que resolver tú. Si no lo resuelves, tu celda no entra nunca.

Tu celda solo está hecha cuando la PR tiene la etiqueta **`pintado`**. Hasta entonces, revisa de vez en cuando la campana 🔔 de notificaciones de GitHub o tu correo: cada vez que el bot comenta en tu PR te llega un aviso.

Si pasan **30 minutos** desde que abriste la PR y el bot no ha comentado nada, avisa al profesor.

## Etiquetas del bot

| Etiqueta | Significado |
| --- | --- |
| `pintado` | ¡Fusionada! Tu celda ya está en el dibujo. |
| `en-espera` | Es válida, pero aún no te toca (hiciste tu última celda hace menos de 48 horas, o ya tienes tus 2 celdas). Se fusionará sola cuando te toque. |
| `conflicto` | Alguien (otra persona o el saboteador) ha cambiado tu celda o la de al lado. Resuelve el conflicto y haz `push`: deja tu celda con tu cambio y las demás como estén en `main`. |
| `no-valida` | No cumple las reglas. Lee el comentario, corrígelo y haz `push` a la misma rama. |
