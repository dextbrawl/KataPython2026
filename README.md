# KataPython2026: Tux en la Antártida 🐧❄️

¡Bienvenido/a a la **KataP del Aula de Software Libre**! En esta kata de programación orientada a objetos (POO) y algoritmos en Python, tu misión es ayudar a **Tux**, el pingüino de Linux, a explorar la Antártida, recolectar nieve para poder hacer su iglú y esquivar bloques de hielo.

Este proyecto sigue una metodología guiada por pruebas (TDD): irás implementando las clases y métodos paso a paso para hacer pasar la suite de tests (`pytest`), y finalmente programarás algoritmos de automatización para resolver el juego en la terminal.

---

## 🛠️ Requisitos

- **Python 3.9** o superior.
- Las dependencias del proyecto están en `requirements.txt`. La aplicación utiliza principalmente la biblioteca estándar de Python; `pytest` se incluye para ejecutar la suite de pruebas unitarias.

---

## 💻 Preparar el entorno

Desde la carpeta raíz del proyecto, crea y activa un entorno virtual:

### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows (PowerShell)

Instala linux!

Con el entorno activado, actualiza `pip` e instala las dependencias:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Para salir del entorno virtual cuando termines:

```bash
deactivate
```

*Recuerda activar de nuevo el entorno con `source .venv/bin/activate` cada vez que abras una terminal nueva para trabajar en el proyecto.*

---

## 🗺️ Estructura del Proyecto

```text
KataPython2026/
├── src/
│   ├── entidades.py    # Clase Posicion, Item, Nieve, HieloGrueso (Fase 1)
│   ├── mundo.py        # Clase Mundo (Matriz NxM y gestión de celdas) (Fase 2)
│   ├── tux.py          # Clase Tux (Atributos, energía e inventario) (Fase 3)
│   └── render.py       # Renderizador del tablero en consola con emojis
├── tests/
│   ├── test_fase1_2.py # Pruebas para Entidades y el Mundo
│   └── test_fase3.py   # Pruebas para el Agente Tux
├── requirements.txt    # Dependencias (pytest)
├── main.py             # Script ejecutable y retos de automatización (Fase 4)
└── README.md           # Guía e instrucciones
```

---

## 🎯 Progresión de la Kata

La kata está dividida en 4 fases incrementales:

### 🔹 Fase 1: Entidades Básicas (`src/entidades.py`)
- Implementa la clase inmutable `Posicion(x, y)` con su método `mover(dx, dy)`.
- Define la clase base `Item` y sus subclases `Nieve` (con cantidad) y `HieloGrueso` (obstáculo no recolectable).

### 🔹 Fase 2: El Mundo y la Matriz (`src/mundo.py`)
- Implementa la clase `Mundo(filas, columnas)` que maneja el tablero mediante una matriz/lista anidada.
- Añade validaciones de límites con `es_posicion_valida(pos)` y métodos para consultar (`obtener_item`), colocar (`colocar_item`) y retirar elementos (`retirar_item`).

### 🔹 Fase 3: El Agente Tux (`src/tux.py`)
- Define la clase `Tux` que almacena su posición, energía disponible e inventario de nieve.
- Implementa el método `mover(direccion)` para desplazarse en 4 direcciones (`"arriba"`, `"abajo"`, `"izquierda"`, `"derecha"`), validando colisiones con el hielo, límites del mundo y gasto de energía.
- Implementa `recolectar()` para añadir la nieve de la celda actual al inventario de Tux.

### 🔹 Fase 4: Automatización y Retos (`main.py`)
- Escribe algoritmos en `main.py` para que Tux explore la Antártida de manera autónoma, recolecte recursos y optimice su energía.

---

## 🧪 Ejecutar Pruebas (Tests)

Para comprobar si tu código cumple los requisitos de cada fase, ejecuta la suite de pruebas con `pytest`:

```bash
python -m pytest
```

Para ejecutar únicamente los tests de una fase específica:

```bash
python -m pytest tests/test_fase1_2.py
python -m pytest tests/test_fase3.py
```

También puedes probar los módulos directamente desde la raíz ejecutando fragmentos rápidos en Python:

```bash
python -c 'from src.entidades import Nieve, Posicion; from src.mundo import Mundo; mundo = Mundo(filas=3, columnas=3); mundo.colocar_item(Posicion(1, 1), Nieve(cantidad=5)); print(mundo.obtener_item(Posicion(1, 1)).nombre)'
```

---

## 🚀 Ejecutar el Juego

Una vez hayas superado los tests unitarios, ejecuta la simulación visual en la consola:

```bash
python main.py
```

Verás cómo **Tux** (`🐧`) interactúa con el mundo (`❄️`, `🧊`) paso a paso en la terminal. ¡Buena suerte completando todos los retos! 🐧✨