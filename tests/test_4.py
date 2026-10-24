import pytest
from src.mapas import (
    cargar_mapa_reto1,
    cargar_mapa_reto2,
    cargar_mapa_reto3,
    cargar_mapa_reto4
)
from src.entidades import Posicion, Nieve, HieloGrueso


def test_carga_reto1():
    mundo, tux = cargar_mapa_reto1()
    
    assert mundo.filas == 5
    assert mundo.columnas == 5
    assert tux.posicion == Posicion(0, 0)
    assert tux.energia == 30
    
    # Verificar que todas las casillas tienen nieve
    nieve_total = 0
    for y in range(5):
        for x in range(5):
            item = mundo.obtener_item(Posicion(x, y))
            assert isinstance(item, Nieve)
            nieve_total += item.cantidad
    assert nieve_total == 25


def test_carga_reto2():
    mundo, tux = cargar_mapa_reto2()
    
    assert mundo.filas == 5
    assert mundo.columnas == 5
    assert tux.posicion == Posicion(0, 0)
    assert tux.energia == 25
    
    # Verificar el tesoro final y un obstáculo de prueba
    tesoro = mundo.obtener_item(Posicion(4, 4))
    assert isinstance(tesoro, Nieve)
    assert tesoro.cantidad == 20
    
    obstaculo = mundo.obtener_item(Posicion(1, 0))
    assert isinstance(obstaculo, HieloGrueso)


def test_carga_reto3():
    mundo, tux = cargar_mapa_reto3()
    
    assert mundo.filas == 6
    assert mundo.columnas == 6
    assert tux.posicion == Posicion(0, 0)
    assert tux.energia == 18
    
    # Verificar que la nieve aislada lejana esté presente
    nieve_lejana = mundo.obtener_item(Posicion(5, 0))
    assert isinstance(nieve_lejana, Nieve)
    assert nieve_lejana.cantidad == 15


def test_carga_reto4():
    mundo, tux = cargar_mapa_reto4()
    
    assert mundo.filas == 8
    assert mundo.columnas == 8
    assert tux.posicion == Posicion(0, 0)
    assert tux.energia == 42
    
    # Verificar que los 6 puntos clave existen
    puntos_nieve = [(1, 1), (6, 1), (1, 6), (6, 6), (3, 3), (4, 4)]
    for x, y in puntos_nieve:
        item = mundo.obtener_item(Posicion(x, y))
        assert isinstance(item, Nieve)
        assert item.cantidad == 10