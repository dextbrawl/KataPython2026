"""
Renderizador de la Antártida para la terminal.

  * Muestra coordenadas (x, y), la cantidad de nieve de cada depósito,
    una barra de energía, el rastro por donde ha pasado Tux y una línea de
    mensaje para contar qué ha pasado en el último paso.
  * Si la salida no es una terminal (pipe, fichero, pytest...) o si defines
    NO_COLOR, cae a un modo simple de solo texto: un tablero tras otro.

Uso (mensaje opcional):

    RenderizadorMundo.dibujar(mundo, tux)
    RenderizadorMundo.dibujar(mundo, tux, "¡Tux recolectó 3 de nieve!")
"""
import atexit
import os
import shutil
import sys
from typing import Optional

from src.entidades import HieloGrueso, Nieve
from src.mundo import Mundo
from src.tux import Tux

_ESC = "\x1b"
_RESET = f"{_ESC}[0m"
_NEGRITA = f"{_ESC}[1m"


def _bg(n: int) -> str:
    return f"{_ESC}[48;5;{n}m"


def _fg(n: int) -> str:
    return f"{_ESC}[38;5;{n}m"


def _col(n: int) -> str:
    """Mueve el cursor a la columna absoluta n (empezando en 1)."""
    return f"{_ESC}[{n}G"


class RenderizadorMundo:
    # "vacio" solo se usa en el modo simple (sin colores).
    EMOJIS = {
        "tux": "🐧",
        "nieve": "❄️",
        "hielo": "🧊",
        "vacio": "· ",
    }

    # --- Configuración -------------------------------------------------
    # None = automático (animado si la salida es una terminal).
    # True / False para forzar el modo animado o el simple.
    animado: Optional[bool] = None

    ANCHO_CELDA = 4   # 2 columnas para el emoji + 2 para la cantidad
    COL_CELDAS = 5    # columna (desde 1) donde empieza la primera celda
    ANCHO_BARRA = 12

    # Colores de la paleta de 256 colores
    _FONDO_A = 195        # casilla clara
    _FONDO_B = 153        # casilla algo más azulada (efecto ajedrez)
    _FONDO_RASTRO = 117   # casilla por la que ya pasó Tux
    _FONDO_HIELO = 67     # bloque de hielo grueso
    _FONDO_TUX = 228      # casilla donde está Tux ahora
    _COLOR_BORDE = 39
    _COLOR_CANTIDAD = 17

    # --- Estado interno (rastro y número de paso) -----------------------
    _mundo_actual: Optional[Mundo] = None
    _paso = 0
    _rastro: set = set()
    _limpiar_pantalla = True
    _terminal_preparada = False

    # ------------------------------------------------------------------
    @classmethod
    def reiniciar(cls) -> None:
        """Olvida el rastro y vuelve a contar los pasos desde 0."""
        cls._paso = 0
        cls._rastro = set()
        cls._limpiar_pantalla = True

    @classmethod
    def dibujar(cls, mundo: Mundo, tux: Optional[Tux] = None, mensaje: str = "") -> None:
        # Un mundo distinto = una partida nueva
        if mundo is not cls._mundo_actual:
            cls._mundo_actual = mundo
            cls.reiniciar()

        paso = cls._paso
        cls._paso += 1
        if tux is not None:
            cls._rastro.add((tux.posicion.x, tux.posicion.y))

        ansi = cls._usa_ansi()
        lineas = cls._construir(mundo, tux, mensaje, paso, ansi)

        if not ansi:
            sys.stdout.write("\n" + "\n".join(lineas) + "\n")
            sys.stdout.flush()
            return

        cls._preparar_terminal()
        filas_terminal = shutil.get_terminal_size().lines
        if len(lineas) < filas_terminal:
            # Todo el cuadro se escribe de una vez: sin parpadeos.
            inicio = f"{_ESC}[2J{_ESC}[H" if cls._limpiar_pantalla else f"{_ESC}[H"
            cuerpo = "\n".join(linea + f"{_ESC}[K" for linea in lineas)
            sys.stdout.write(inicio + cuerpo + f"{_ESC}[J\n")
            cls._limpiar_pantalla = False
        else:
            # La terminal es demasiado baja para redibujar en el sitio.
            sys.stdout.write("\n".join(lineas) + "\n\n")
        sys.stdout.flush()

    # ------------------------------------------------------------------
    @classmethod
    def _usa_ansi(cls) -> bool:
        if cls.animado is not None:
            return cls.animado
        return (
            sys.stdout.isatty()
            and "NO_COLOR" not in os.environ
            and os.environ.get("TERM") != "dumb"
        )

    @classmethod
    def _preparar_terminal(cls) -> None:
        """Oculta el cursor mientras dura la animación y lo restaura al salir."""
        if cls._terminal_preparada:
            return
        if os.name == "nt":
            os.system("")  # activa las secuencias ANSI en la consola de Windows
        sys.stdout.write(f"{_ESC}[?25l")
        sys.stdout.flush()

        def _restaurar() -> None:
            try:
                sys.stdout.write(f"{_ESC}[?25h{_RESET}")
                sys.stdout.flush()
            except Exception:
                pass

        atexit.register(_restaurar)
        cls._terminal_preparada = True

    # ------------------------------------------------------------------
    @staticmethod
    def _item_en(mundo: Mundo, x: int, y: int):
        # Se lee la matriz directamente para que el tablero se pueda pintar
        # aunque el alumno aún no haya implementado obtener_item (Fase 2).
        grid = getattr(mundo, "_grid", None)
        return grid[y][x] if grid else None

    @classmethod
    def _celda(cls, x: int, glifo: str, cantidad, fondo: int, ansi: bool) -> str:
        cant = f"{min(cantidad, 99):<2}" if isinstance(cantidad, int) and cantidad > 0 else "  "
        if not ansi:
            return glifo + cant

        col = cls.COL_CELDAS + cls.ANCHO_CELDA * x
        s = f"{_col(col)}{_bg(fondo)}{' ' * cls.ANCHO_CELDA}"
        if glifo:
            s += f"{_col(col)}{glifo}"
        if cant.strip():
            s += f"{_col(col + 2)}{_NEGRITA}{_fg(cls._COLOR_CANTIDAD)}{cant}"
        return s + _RESET

    @classmethod
    def _fondo(cls, x: int, y: int, hay_tux: bool, item) -> int:
        if hay_tux:
            return cls._FONDO_TUX
        if isinstance(item, HieloGrueso):
            return cls._FONDO_HIELO
        if (x, y) in cls._rastro:
            return cls._FONDO_RASTRO
        return cls._FONDO_A if (x + y) % 2 == 0 else cls._FONDO_B

    @classmethod
    def _construir(cls, mundo: Mundo, tux: Optional[Tux], mensaje: str,
                   paso: int, ansi: bool) -> list:
        borde = (lambda t: f"{_fg(cls._COLOR_BORDE)}{t}{_RESET}") if ansi else (lambda t: t)
        ancho_interior = cls.ANCHO_CELDA * mundo.columnas
        lineas = []

        # Coordenadas X (todo ASCII, así que la alineación no depende de la terminal)
        etiquetas = "".join(f"{x:^{cls.ANCHO_CELDA}}" for x in range(mundo.columnas))
        lineas.append(" " * (cls.COL_CELDAS - 1) + etiquetas)

        # Borde superior con el número de paso
        titulo = f" Paso {paso} "
        if len(titulo) + 2 <= ancho_interior:
            sup = "╔═" + titulo + "═" * (ancho_interior - 2 - len(titulo)) + "╗"
        else:
            sup = "╔" + "═" * ancho_interior + "╗"
        lineas.append("   " + borde(sup))

        # Tablero
        for y in range(mundo.filas):
            fila = f"{y:>2} " + borde("║")
            for x in range(mundo.columnas):
                hay_tux = tux is not None and tux.posicion.x == x and tux.posicion.y == y
                item = cls._item_en(mundo, x, y)
                cantidad = getattr(item, "cantidad", None) if isinstance(item, Nieve) else None

                if hay_tux:
                    glifo = cls.EMOJIS["tux"]
                elif isinstance(item, Nieve):
                    glifo = cls.EMOJIS["nieve"]
                elif isinstance(item, HieloGrueso):
                    glifo = cls.EMOJIS["hielo"]
                else:
                    glifo = "" if ansi else cls.EMOJIS["vacio"]

                fila += cls._celda(x, glifo, cantidad, cls._fondo(x, y, hay_tux, item), ansi)

            if ansi:
                fila += _col(cls.COL_CELDAS + ancho_interior)
            fila += borde("║")
            lineas.append(fila)

        lineas.append("   " + borde("╚" + "═" * ancho_interior + "╝"))

        # Panel de estado
        if tux is not None:
            energia = getattr(tux, "energia", 0)
            maxima = max(getattr(tux, "energia_maxima", energia), energia, 1)
            llenos = round(cls.ANCHO_BARRA * max(energia, 0) / maxima)
            relleno, vacio = "█" * llenos, "░" * (cls.ANCHO_BARRA - llenos)
            if ansi:
                prop = energia / maxima
                color = 46 if prop > 0.5 else 220 if prop > 0.25 else 196
                barra = f"{_fg(color)}{relleno}{_fg(240)}{vacio}{_RESET}"
            else:
                barra = relleno + vacio
            nieve = getattr(tux, "inventario", {}).get("Nieve", 0)
            lineas.append(f"🔋 Energía  {barra} {energia}/{maxima}")
            lineas.append(f"🎒 Nieve: {nieve}    ({tux.posicion.x}, {tux.posicion.y})")

        # Línea de mensaje (siempre se reserva para que el cuadro no cambie de altura)
        lineas.append(f" {mensaje}" if mensaje else "")
        return lineas
