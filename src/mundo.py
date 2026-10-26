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
        """
        TODO Fase 2: Comprueba si la posición está dentro de los límites de la matriz.
        Retorna True si pos.x está entre 0 y columnas-1, y pos.y está entre 0 y filas-1.
        """
        pass

    def obtener_item(self, pos: Posicion) -> Optional[Item]:
        """
        TODO Fase 2: Devuelve el item alojado en la matriz en la posición indicada.
        Asegúrate de validar la posición primero usando self.es_posicion_valida. 
        Si no es válida, lanza: raise IndexError("Posición fuera de los límites del mundo.")
        """
        pass

    def colocar_item(self, pos: Posicion, item: Optional[Item]) -> None:
        """
        TODO Fase 2: Coloca el item en la matriz en la posición indicada.
        Recuerda validar los límites lanzando IndexError si la posición no existe.
        """
        pass

    def retirar_item(self, pos: Posicion) -> Optional[Item]:
        """
        TODO Fase 2: Retira el item de la posición (lo sustituye por None en la matriz) 
        y devuelve el item que había originalmente en esa celda.
        """
        pass
