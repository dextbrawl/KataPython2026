from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class Posicion:
    x: int
    y: int

    def mover(self, dx: int, dy: int) -> "Posicion":
        """Devuelve una nueva posición sumando los desplazamientos."""
        return Posicion(self.x + dx, self.y + dy)


class Item:
    def __init__(self, nombre: str, recolectable: bool = True):
        self.nombre = nombre
        self.recolectable = recolectable


class Nieve(Item):
    def __init__(self, cantidad: int = 1):
        super().__init__(nombre="Nieve", recolectable=True)
        self.cantidad = cantidad


class HieloGrueso(Item):
    def __init__(self):
        super().__init__(nombre="Hielo Grueso", recolectable=False)