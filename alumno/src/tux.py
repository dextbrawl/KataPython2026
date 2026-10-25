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
        self.inventario: Dict[str, int] = {"Nieve": 0}

    def mover(self, direccion: str) -> bool:
        """
        TODO Fase 3: Mueve a Tux en una dirección ('arriba', 'abajo', 'izquierda', 'derecha').
        
        Pasos recomendados:
        1. Verifica si la energía es mayor que 0. Si no, retorna False.
        2. Mapea la dirección a un incremento (ej. 'arriba' -> dx=0, dy=-1).
        3. Calcula la nueva posición usando el método 'mover' de Posicion.
        4. Valida si la nueva posición es válida en el mundo.
        5. Valida si hay un obstáculo (HieloGrueso) en el destino.
        6. Si el movimiento es válido, actualiza self.posicion, resta 1 a self.energia y retorna True.
        """
        pass

    def recolectar(self) -> int:
        """
        TODO Fase 3: Recolecta el ítem de la celda actual si es Nieve.
        
        Pasos recomendados:
        1. Obtén el item de la posición actual de Tux.
        2. Si el item es una instancia de Nieve, suma su cantidad a self.inventario["Nieve"].
        3. Retira el item del mundo usando el método correspondiente.
        4. Devuelve la cantidad recolectada (retorna 0 si no había nieve).
        """
        pass
