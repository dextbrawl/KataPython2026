import pytest
from src.entidades import Posicion, Nieve, HieloGrueso
from src.mundo import Mundo

def test_posicion_creacion_y_movimiento():
    p1 = Posicion(2, 3)
    p2 = p1.mover(1, -1)
    assert p2.x == 3
    assert p2.y == 2
    assert p1.x == 2  # Debe ser inmutable

def test_mundo_limites():
    mundo = Mundo(filas=5, columnas=5)
    assert mundo.es_posicion_valida(Posicion(0, 0)) is True
    assert mundo.es_posicion_valida(Posicion(4, 4)) is True
    assert mundo.es_posicion_valida(Posicion(5, 5)) is False
    assert mundo.es_posicion_valida(Posicion(-1, 0)) is False

def test_colocar_y_obtener_items():
    mundo = Mundo(filas=3, columnas=3)
    pos = Posicion(1, 1)
    nieve = Nieve(cantidad=5)
    
    mundo.colocar_item(pos, nieve)
    item_recuperado = mundo.obtener_item(pos)
    
    assert item_recuperado is not None
    assert item_recuperado.nombre == "Nieve"
    assert item_recuperado.cantidad == 5

def test_retirar_item():
    mundo = Mundo(filas=3, columnas=3)
    pos = Posicion(0, 2)
    hielo = HieloGrueso()
    
    mundo.colocar_item(pos, hielo)
    item_retirado = mundo.retirar_item(pos)
    
    assert item_retirado == hielo
    assert mundo.obtener_item(pos) is None

def test_acceso_fuera_de_limites_lanza_excepcion():
    mundo = Mundo(filas=3, columnas=3)
    pos_invalida = Posicion(10, 10)
    
    with pytest.raises(IndexError):
        mundo.obtener_item(pos_invalida)