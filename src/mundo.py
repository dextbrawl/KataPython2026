from typing import Optional, List
from src.entidades import Posicion, Item

class Mundo:
    def __init__(self, filas: int, columnas: int):
        self.filas = filas
        self.columnas = columnas
        # Matriz llena de None por defecto
        self._grid: List[List[Optional[Item]]] = [
            [None for _ in range(columnas)] for _ in range(filas)
        ]

    def es_posicion_valida(self, pos: Posicion) -> bool:
        """Comprueba si la posición está dentro de los límites de la matriz."""
        return 0 <= pos.x < self.columnas and 0 <= pos.y < self.filas

    def obtener_item(self, pos: Posicion) -> Optional[Item]:
        """Obtiene el item de una posición dada."""
        if not self.es_posicion_valida(pos):
            raise IndexError("Posición fuera de los límites del mundo.")
        return self._grid[pos.y][pos.x]

    def colocar_item(self, pos: Posicion, item: Optional[Item]) -> None:
        """Coloca un item en una posición determinada."""
        if not self.es_posicion_valida(pos):
            raise IndexError("Posición fuera de los límites del mundo.")
        self._grid[pos.y][pos.x] = item

    def retirar_item(self, pos: Posicion) -> Optional[Item]:
        """Retira y devuelve el item en la posición dada."""
        item = self.obtener_item(pos)
        self.colocar_item(pos, None)
        return item