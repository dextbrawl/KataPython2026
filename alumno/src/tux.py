from typing import Dict, Optional
from src.entidades import Posicion, Nieve, HieloGrueso
from src.mundo import Mundo

class Tux:
    def __init__(self, mundo: Mundo, pos_inicial: Posicion, energia_inicial: int = 20):
        if not mundo.es_posicion_valida(pos_inicial):
            raise ValueError("La posición inicial está fuera de los límites del mundo.")
        
        self.mundo = mundo
        self.posicion = pos_inicial
        self.energia = energia_inicial
        self.energia_maxima = energia_inicial  # lo usa el renderizador para la barra
        self.inventario: Dict[str, int] = {"Nieve": 0}

    def mover(self, direccion: str) -> bool:
        """
        TODO Fase 3: Mueve a Tux en una dirección ('arriba', 'abajo', 'izquierda', 'derecha').
        Requerimientos: 
            - Verificar que la energía sea mayor a 0. De lo contrario, devolver false
            - Recomendable mapear la dirección a un incremento (por ejemplo, 'arriba' -> dx=0, dy=-1)
            - Calcular nueva posición y verificar que es válida en el mundo o si hay un obstáculo
            - Si es válido, actualiza la posición, resta 1 de energía y devuelve true
        """
        pass

    def recolectar(self) -> int:
        """
        TODO Fase 3: Recolecta el ítem de la celda actual si es Nieve.
        Requerimientos:
            - Obtén el item de la posición actual
            - Si el item es Nieve, suma la cantidad al inventario
            - Retira el item del mundo utilizando el método de la fase 2
            - Devuelve la cantidad recolectada
        """
        pass
