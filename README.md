# Pixel War EDE

Entre toda la clase vamos a pintar un sprite de *Realm of the Mad God*, celda a celda, usando Git y GitHub: cada celda es una *pull request*.

> *Realm of the Mad God* es un MMO gratuito de disparos tipo *bullet hell* que salió en 2010. Es famoso por sus gráficos *pixel art*: personajes y enemigos dibujados en cuadrículas diminutas de 8 × 8 píxeles, perfectas para pintarlas entre todos. Nuestro objetivo es un bandido.

**Mira cómo va el dibujo:** <https://scontreraslopez.github.io/pixel-war-ede-2026/>

## Reglas

1. Cada *pull request* cambia **una sola celda**: cambia **una línea** de `index.html` y nada más.
2. La celda tiene que quedar como en el dibujo **objetivo**. Abre la página y pasa el ratón por el lienzo: verás la fila, la columna y el color que le toca a cada celda.
3. Tienes que hacer **2 celdas**, con **al menos 48 horas** entre una y otra (si la primera se fusiona el lunes a las 10:00, la segunda no entra hasta el miércoles a las 10:00). Puedes abrir la segunda PR antes: el bot la dejará esperando y la fusionará cuando te toque.
4. Si tu PR tiene **conflictos**, tendrás que resolverlos tú (el bot te explica cómo).
5. Un bot revisa tu PR en cuanto la abres o haces `push`: si es válida y no tiene conflictos, la fusiona sola. Si no, te deja un comentario explicando qué pasa.
6. **Cuidado con el saboteador:** de vez en cuando el bot pinta una celda de un color que no toca. En la página se ven **rayadas**. Arreglarlas también cuenta como una de tus celdas:
    - Si la celda es del dibujo, cambia el color por el correcto: `class="cell verde"` → `class="cell rojo"`.
    - Si la celda es de fondo, quítale el color: `class="cell verde"` → `class="cell"`.

## Cómo pintar una celda

<<<<<<< HEAD
=======
> [!IMPORTANT]
> Sigue por favor esta mini-guía paso a paso. Si no, el bot no podrá fusionar tu PR y tendrás que arreglarlo tú.
> celda 5-7 es un ejemplo: cambia el número de celda y el color por los que tú quieras pintar.

>>>>>>> 59963d70a93944c31f1f41e96ae26bf9497e9da0
1. Haz un **fork** de este repositorio y clónalo. Lo más cómodo es hacerlo todo de una vez con `gh repo fork scontreraslopez/pixel-war-ede-2026 --clone`, que además te deja configurado el remoto `upstream`. Si haces el fork desde la web, añádelo tú después de clonar:

    ```bash
    git remote add upstream https://github.com/scontreraslopez/pixel-war-ede-2026.git
    ```

2. Crea una rama para tu celda: `git switch -c celda-5-7`
3. Abre `index.html`, busca la línea de tu celda (por ejemplo, `id="c-5-7"`) y añade el color a la clase. En este ejemplo el color es inventado: usa el que te diga la página para **tu** celda.

    ```html
    <div class="cell rojo" id="c-5-7" title="Fila 5, Columna 7"></div>
    ```

4. Guarda el archivo **sin formatear** (el repositorio ya trae desactivado el formateo automático de VS Code; si usas otro editor, ojo).
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
- Si queda **en espera**, se fusionará sola cuando te toque. El bot repasa las PR pendientes de vez en cuando, y **a veces tarda varias horas**: no te preocupes si se fusiona más tarde de la hora que te dijo.
- **Mientras tu PR siga abierta, puede cambiar de estado.** Si otra persona o el saboteador cambian tu celda o la de al lado, tu PR pasará a tener un **conflicto** que tendrás que resolver tú. Si no lo resuelves, tu celda no entra nunca.
- **Después de resolver un conflicto y hacer `push`**, lo normal es que el bot fusione tu PR al momento. Pero a veces se queda en cola hasta la siguiente revisión automática, que **puede tardar varias horas**. Mientras tanto puede seguir teniendo la etiqueta `conflicto`: si ya lo has resuelto, ten paciencia.

<<<<<<< HEAD
> [!WARNING]
> ¡Asegúrate de que tu PR ha sido aceptada! Puede tardar un rato, y seguramente alguna vez fallará algo. Es muy importante que compruebes que tu PR se ha aceptado e integrado en el proyecto, porque si no, no podré calificarte positivamente la actividad.

=======
> [!NOTE]
> Esta es la **primera versión** del juego y el bot puede fallar. Si algo se queda atascado, no te preocupes: revisaré a mano las PR afectadas hasta que lo arregle. Tú asegúrate de haber hecho bien tu parte.

> [!WARNING]
> ¡Asegúrate de que tu PR ha sido aceptada! Puede tardar un rato, y seguramente alguna vez fallará algo. Es muy importante que compruebes que tu PR se ha aceptado e integrado en el proyecto, porque si no, no podré calificarte positivamente la actividad.

>>>>>>> 59963d70a93944c31f1f41e96ae26bf9497e9da0
Tu celda solo está hecha cuando la PR tiene la etiqueta **`pintado`**. Hasta entonces, revisa de vez en cuando la campana 🔔 de notificaciones de GitHub o tu correo: cada vez que el bot comenta en tu PR, te llega un aviso.

Si pasan **30 minutos** desde que abriste la PR (o desde tu último `push`) y el bot no ha comentado **nada**, avisa al profesor.

## Etiquetas del bot

| Etiqueta | Significado |
| --- | --- |
| `pintado` | ¡Fusionada! Tu celda ya está en el dibujo. |
| `en-espera` | Es válida, pero aún no te toca (hiciste tu última celda hace menos de 48 horas, o ya tienes tus 2 celdas). Se fusionará sola cuando te toque. |
| `conflicto` | Alguien (otra persona o el saboteador) ha cambiado tu celda o la de al lado. Resuelve el conflicto y haz `push`: deja tu celda con tu cambio y las demás como estén en `main`. |
| `no-valida` | No cumple las reglas. Lee el comentario, corrígelo y haz `push` a la misma rama. |

## Notas del profesor

Es muy fácil que me olvide de cómo configurar esto, así que dejo aquí anotaciones para mí mismo y para quien quiera repetir la experiencia. No hace falta que lo leas, pero tampoco hace daño: así sabrás qué pasa detrás de las bambalinas.

### Piezas

| Archivo | Para qué sirve |
| --- | --- |
| `objetivo.js` | Dibujo objetivo, leyenda y paleta. Lo leen la página (`guia.js`) y el bot. |
| `herramientas/generar_lienzo.py` | Genera `index.html` (lienzo vacío) y `style.css` a partir de `objetivo.js`. **Sobrescribe el lienzo.** |
| `.github/pixelbot/pixelbot.py` | El bot: valida, fusiona, etiqueta, comenta y sabotea. Solo usa la API de GitHub; nunca ejecuta código de las PR. |
| `.github/workflows/pixelbot.yml` | Lanza el bot con cada PR (`pull_request_target`), cada 15 min (`schedule`) y a mano (`workflow_dispatch`). |
| `.github/workflows/pages.yml` | Publica la página en GitHub Pages. El bot lo lanza explícitamente cuando cambia `main`. |

### Puesta en marcha (una vez por curso)

1. Cambiar `objetivo.js` si se quiere otro dibujo y ejecutar `python herramientas/generar_lienzo.py`.
2. *Settings → Pages → Source:* **GitHub Actions**.
3. La rama `main` **no** puede estar protegida: el bot hace commits directos para sabotear. Si se protege, el sabotaje falla en silencio (solo sale en el log).
4. Crear a mano las etiquetas `pintado`, `en-espera`, `conflicto` y `no-valida` con color y descripción. Si no existen, el bot las crea sin color ni descripción.
5. Configurar las variables (abajo) y repasar el checklist de antes de abrir.

### Variables del bot

Son **variables del repositorio**, no secretos: *Settings → Secrets and variables → Actions → Variables*, o con `gh variable set NOMBRE --body VALOR`. Si una variable no existe, se usa el valor por defecto.

| Variable | Por defecto | Qué hace |
| --- | --- | --- |
| `ALUMNOS` | (todos) | Usuarios de GitHub de la clase, separados por comas o espacios. Si no existe, puede participar cualquiera. |
| `MAX_PR_FASE1` | `2` | Celdas por alumno en la fase normal. |
| `DIAS_ENTRE_PR_FASE1` | `2` | Días (× 24 h exactas) entre una fusión y la siguiente del mismo alumno. |
| `FECHA_SPRINT` | (sin sprint) | `AAAA-MM-DD`. Desde ese día no hay límite de celdas, solo cooldown. |
| `COOLDOWN_SPRINT_MIN` | `60` | Minutos entre celdas durante el sprint. |
| `SABOTAJE_CADA_MIN` | (sin sabotaje) | Como mucho un sabotaje aleatorio cada N minutos (solo en ejecuciones programadas o manuales). |
<<<<<<< HEAD
| `SABOTAJE_MAX` | `5` | Si ya hay N celdas incorrectas en `main`, no sabotea más hasta que se arreglen. |
| `CONFLICTO_DESDE_PR` | (desactivado) | A partir de la PR número N de cada alumno, **todas** sus PR reciben un conflicto forzado. Con `2` y `MAX_PR_FASE1=2`, la segunda celda de cada alumno tiene conflicto seguro (y, en el sprint, todas las siguientes). |

Configuración del curso 2026-27: `MAX_PR_FASE1=2`, `DIAS_ENTRE_PR_FASE1=2`, `SABOTAJE_CADA_MIN=15`, `CONFLICTO_DESDE_PR=2`.
=======
| `SABOTAJE_MAX` | `5` | Si ya hay N celdas incorrectas en `main`, no sabotea más hasta que se arreglen. Es un tope de celdas incorrectas **a la vez**, no de sabotajes en total. El sabotaje aleatorio solo pinta celdas **vacías**, así que nunca estropea una celda que ya estaba bien. |
| `CONFLICTO_DESDE_PR` | (desactivado) | A partir de la PR número N de cada alumno, **todas** sus PR reciben un conflicto forzado. Con `2` y `MAX_PR_FASE1=2`, la segunda celda de cada alumno tiene conflicto seguro (y, en el sprint, todas las siguientes). |

Configuración del curso 2026-27: `MAX_PR_FASE1=2`, `DIAS_ENTRE_PR_FASE1=2`, `SABOTAJE_CADA_MIN=15`, `SABOTAJE_MAX=40`, `CONFLICTO_DESDE_PR=2`.
>>>>>>> 59963d70a93944c31f1f41e96ae26bf9497e9da0

### Cómo decide el bot

Para cada PR abierta, en este orden:

1. Ignora los borradores, las PR a otra rama y las PR de `OWNER`/`MEMBER`/`COLLABORATOR` (**las mías no las toca**: para probar hay que usar otra cuenta).
2. Si existe `ALUMNOS` y el autor no está → `no-valida`.
3. Valida el diff (una línea de `index.html`, solo la clase, color de la paleta y del objetivo; o quitar el color de una celda de fondo) → si falla, `no-valida`.
4. Si al autor no le toca todavía (límite o 48 h) → `en-espera`.
5. **Conflicto forzado:** si es su PR número `CONFLICTO_DESDE_PR` o posterior y aún no se le ha forzado en esta PR, el bot pinta esa misma celda en `main` de un color incorrecto (commit "Sabotaje dirigido del bot: …"), pone `conflicto` y comenta. Solo pasa una vez por PR: tras resolverlo, la PR sigue el flujo normal.
6. Si GitHub dice que tiene conflictos → `conflicto`. Si GitHub aún no lo ha calculado (pasa justo después de un `push`), no hace nada y lo mira en la siguiente ejecución.
7. Fusiona (método *merge*, no *squash*, para que la segunda PR del alumno no arrastre la primera) → `pintado`.

El **historial** de cada alumno se calcula con las PR cerradas, fusionadas y con la etiqueta `pintado`. **No sale de `main`**: aunque se reinicie el lienzo, las PR fusionadas siguen contando. Por eso conviene probar con una cuenta que no sea de ningún alumno.

### Ojo: el cron de GitHub no cumple los 15 minutos

GitHub retrasa mucho los `schedule` de los repositorios con poca actividad: en noviembre de 2026 se ejecutaba cada 4–8 horas. Las PR nuevas y los `push` se revisan al momento (`pull_request_target`), pero **las PR en espera, las detecciones de conflicto tras otra fusión y el sabotaje aleatorio van al ritmo del cron**.

- Forzar una pasada: `gh workflow run pixelbot.yml` (o el botón *Run workflow* en *Actions*).
- Si hace falta más regularidad: una tarea programada (en el PC o en un servicio de cron externo) que ejecute ese mismo comando cada 15 minutos.

### Probar antes de abrir

Con una cuenta secundaria que **no** sea colaboradora del repositorio:

```bash
gh variable set DIAS_ENTRE_PR_FASE1 --body 0   # sin esperas entre PR
gh variable set MAX_PR_FASE1 --body 10         # que la cuenta de prueba no se quede sin celdas
```

1. Desde la cuenta de prueba, abrir una PR que pinte una celda vacía con su color correcto. Su primera PR debe fusionarse sola (`pintado`).
2. Abrir una segunda PR: debe aparecer al momento el commit "Sabotaje dirigido del bot" en `main`, la etiqueta `conflicto` y dos comentarios (el sabotaje y las instrucciones).
3. Resolver el conflicto como lo haría un alumno, hacer `push` y lanzar `gh workflow run pixelbot.yml`: debe fusionarse (`pintado`) y la página actualizarse en un minuto.
4. Probar también una PR mal hecha (dos líneas, color equivocado…) → `no-valida` con su explicación.

### Checklist antes de abrir la actividad

- [ ] `DIAS_ENTRE_PR_FASE1` a `2` y `MAX_PR_FASE1` a `2` (o borrarlas: `gh variable delete …`).
- [ ] `ALUMNOS` con la lista de la clase (si se quiere limitar).
- [ ] `FECHA_SPRINT` si va a haber sprint final.
- [ ] Decidir cómo empieza el lienzo: vacío (`generar_lienzo.py` y commit) o con algunas celdas saboteadas para que haya cosas que arreglar desde el principio. Si ya hay `SABOTAJE_MAX` celdas incorrectas, el sabotaje aleatorio no se activa hasta que se arreglen.
- [ ] Comprobar que la página publicada coincide con `main`.

### Problemas frecuentes

- **"Lo he resuelto y no se fusiona":** después de un `push`, GitHub tarda en calcular si hay conflictos y el bot lo deja para la siguiente pasada → `gh workflow run pixelbot.yml`.
- **`no-valida` tras resolver un conflicto:** casi siempre han tocado también la línea de otra celda (por ejemplo, "arreglando" la saboteada). Tienen que dejarla exactamente como esté en `main`.
- **"Alguien se te ha adelantado":** otra PR ya dejó la celda con ese color. Tienen que actualizar desde `upstream/main` y elegir otra.
- **PR sin comentario del bot:** mirar la ejecución en *Actions*. Si un alumno ha abierto la PR como borrador o contra otra rama, el bot la ignora.

### Evaluar

Celdas fusionadas por alumno:

```bash
gh pr list --state merged --label pintado -L 500 --json author \
  --jq 'group_by(.author.login)[] | "\(.[0].author.login): \(length)"'
```

### Seguridad

El workflow usa `pull_request_target`, que da permisos de escritura aunque la PR venga de un fork. Es seguro **solo** porque descarga `main` y nunca el código de la PR. No cambiar el `checkout` para que use la rama de la PR.
