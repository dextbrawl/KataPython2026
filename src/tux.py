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
        Mueve a Tux en una dirección ('arriba', 'abajo', 'izquierda', 'derecha').
        Gasta 1 de energía si el movimiento es exitoso.
        Retorna True si se movió, False si había un obstáculo o falta de energía.
        """
        if self.energia <= 0:
            return False

        desplazamientos = {
            "arriba": (0, -1),
            "abajo": (0, 1),
            "izquierda": (-1, 0),
            "derecha": (1, 0)
        }

        if direccion not in desplazamientos:
            raise ValueError(f"Dirección no válida: {direccion}")

        dx, dy = desplazamientos[direccion]
        nueva_pos = self.posicion.mover(dx, dy)

        # Validación de límites
        if not self.mundo.es_posicion_valida(nueva_pos):
            return False

        # Validación de obstáculos (HieloGrueso)
        item_en_destino = self.mundo.obtener_item(nueva_pos)
        if isinstance(item_en_destino, HieloGrueso):
            return False

        # Aplicar movimiento
        self.posicion = nueva_pos
        self.energia -= 1
        return True

    def recolectar(self) -> int:
        """
        Recolecta el ítem de la celda actual si es recolectable.
        Devuelve la cantidad de ítems recolectados.
        """
        item = self.mundo.obtener_item(self.posicion)
        if isinstance(item, Nieve):
            cantidad = item.cantidad
            self.inventario["Nieve"] += cantidad
            self.mundo.retirar_item(self.posicion)
            return cantidad
        
        return 0