from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class Posicion:
    x: int
    y: int

    def mover(self, dx: int, dy: int) -> "Posicion":
        """
        TODO Fase 1: Implementa el método mover.
        Debe devolver una NUEVA instancia de Posicion sumando dx a 'x' y dy a 'y'.
        Nota: Recuerda que esta clase es inmutable (frozen=True).
        """
        pass

class Item:
    def __init__(self, nombre: str, recolectable: bool = True):
        self.nombre = nombre
        self.recolectable = recolectable

class Nieve(Item):
    def __init__(self, cantidad: int = 1):
        """
        TODO Fase 1: Llama al constructor de la clase padre (Item) usando super().__init__().
        Pásale como nombre "Nieve" y recolectable=True. 
        Luego, guarda la 'cantidad' en un atributo de la instancia.
        """
        pass

class HieloGrueso(Item):
    def __init__(self):
        """
        TODO Fase 1: Llama al constructor de la clase padre (Item).
        Pásale como nombre "Hielo Grueso" y recolectable=False.
        """
        pass
