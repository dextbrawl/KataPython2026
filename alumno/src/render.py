from typing import Optional
from src.entidades import HieloGrueso, Nieve
from src.mundo import Mundo
from src.tux import Tux

class RenderizadorMundo:
    EMOJIS = {"tux": "🐧", "nieve": "❄️ ", "hielo": "🧊", "vacio": "⬜"}

    @staticmethod
    def dibujar(mundo: Mundo, tux: Optional[Tux] = None) -> None:
        print("\n" + "=" * (mundo.columnas * 3))
        for y in range(mundo.filas):
            fila_str = ""
            for x in range(mundo.columnas):
                if tux and tux.posicion.x == x and tux.posicion.y == y:
                    fila_str += RenderizadorMundo.EMOJIS["tux"]
                else:
                    # Accedemos directamente con getattr por seguridad si la matriz no está bien inicializada
                    item = getattr(mundo, '_grid', [[None]*mundo.columnas for _ in range(mundo.filas)])[y][x]
                    if isinstance(item, Nieve): fila_str += RenderizadorMundo.EMOJIS["nieve"]
                    elif isinstance(item, HieloGrueso): fila_str += RenderizadorMundo.EMOJIS["hielo"]
                    else: fila_str += RenderizadorMundo.EMOJIS["vacio"]
            print(fila_str)
        if tux:
            energia = getattr(tux, 'energia', '?')
            inventario = getattr(tux, 'inventario', {}).get('Nieve', '?')
            print(f"\nEnergía: {energia} | Inventario Nieve: {inventario}")
        print("=" * (mundo.columnas * 3) + "\n")
