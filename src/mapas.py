"""
Módulo de mapas con retos de dificultad progresiva para la Kata de Tux.
"""
from src.entidades import Posicion, Nieve, HieloGrueso
from src.mundo import Mundo
from src.tux import Tux


def cargar_mapa_reto1() -> tuple[Mundo, Tux]:
    """Reto 1: El Recorrido en Serpiente (Principiante)."""
    mundo = Mundo(filas=5, columnas=5)
    for y in range(5):
        for x in range(5):
            mundo.colocar_item(Posicion(x, y), Nieve(cantidad=1))
    
    tux = Tux(mundo, pos_inicial=Posicion(0, 0), energia_inicial=30)
    return mundo, tux


def cargar_mapa_reto2() -> tuple[Mundo, Tux]:
    """Reto 2: El Laberinto de Hielo (Intermedio)."""
    mundo = Mundo(filas=5, columnas=5)
    
    obstaculos = [
        (1, 0), (1, 1), (1, 2),
        (3, 1), (3, 2), (3, 3), (3, 4),
        (0, 4)
    ]
    for x, y in obstaculos:
        mundo.colocar_item(Posicion(x, y), HieloGrueso())
        
    mundo.colocar_item(Posicion(4, 4), Nieve(cantidad=20))
    tux = Tux(mundo, pos_inicial=Posicion(0, 0), energia_inicial=25)
    return mundo, tux


def cargar_mapa_reto3() -> tuple[Mundo, Tux]:
    """Reto 3: Mochila y Batería Limitada (Avanzado)."""
    mundo = Mundo(filas=6, columnas=6)
    
    mundo.colocar_item(Posicion(0, 2), Nieve(cantidad=3))
    mundo.colocar_item(Posicion(1, 5), Nieve(cantidad=12))
    mundo.colocar_item(Posicion(3, 1), Nieve(cantidad=5))
    mundo.colocar_item(Posicion(5, 0), Nieve(cantidad=15))
    mundo.colocar_item(Posicion(4, 4), Nieve(cantidad=4))
    
    obstaculos = [(2, 2), (2, 3)]
    for x, y in obstaculos:
        mundo.colocar_item(Posicion(x, y), HieloGrueso())
        
    tux = Tux(mundo, pos_inicial=Posicion(0, 0), energia_inicial=18)
    return mundo, tux


def cargar_mapa_reto4() -> tuple[Mundo, Tux]:
    """Reto 4: El Vendedor Ambulante Antártico / TSP (Experto)."""
    mundo = Mundo(filas=8, columnas=8)
    
    puntos_nieve = [(1, 1), (6, 1), (1, 6), (6, 6), (3, 3), (4, 4)]
    for x, y in puntos_nieve:
        mundo.colocar_item(Posicion(x, y), Nieve(cantidad=10))
        
    obstaculos = [
        (2, 3), (3, 2), (4, 5), (5, 4),
        (2, 0), (2, 1), (2, 5), (2, 6),
        (5, 1), (5, 2), (5, 6), (5, 7),
        (0, 3), (7, 4)
    ]
    for x, y in obstaculos:
        mundo.colocar_item(Posicion(x, y), HieloGrueso())
        
    tux = Tux(mundo, pos_inicial=Posicion(0, 0), energia_inicial=42)
    return mundo, tux