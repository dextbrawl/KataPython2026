from typing import Optional

from src.entidades import HieloGrueso, Nieve
from src.mundo import Mundo
from src.tux import Tux

class RenderizadorMundo:
    EMOJIS = {
        "tux": "🐧",
        "nieve": "❄️ ",
        "hielo": "🧊",
        "vacio": "⬜"
    }

    @staticmethod
    def dibujar(mundo: Mundo, tux: Optional[Tux] = None) -> None:
        print("\n" + "=" * (mundo.columnas * 3))
        for y in range(mundo.filas):
            fila_str = ""
            for x in range(mundo.columnas):
                # Prioridad 1: Dibuja a Tux si está en esta coordenada
                if tux and tux.posicion.x == x and tux.posicion.y == y:
                    fila_str += RenderizadorMundo.EMOJIS["tux"]
                else:
                    item = mundo._grid[y][x]
                    if isinstance(item, Nieve):
                        fila_str += RenderizadorMundo.EMOJIS["nieve"]
                    elif isinstance(item, HieloGrueso):
                        fila_str += RenderizadorMundo.EMOJIS["hielo"]
                    else:
                        fila_str += RenderizadorMundo.EMOJIS["vacio"]
            print(fila_str)
        
        if tux:
            print(f"\nEnergía: {tux.energia} | Inventario Nieve: {tux.inventario['Nieve']}")
        print("=" * (mundo.columnas * 3) + "\n")