from src.mundo import Mundo
from src.tux import Tux
from src.entidades import Posicion, Nieve, HieloGrueso

def test_tux_movimiento_basico():
    mundo = Mundo(5, 5)
    tux = Tux(mundo, pos_inicial=Posicion(2, 2), energia_inicial=10)
    
    assert tux.mover("derecha") is True
    assert tux.posicion == Posicion(3, 2)
    assert tux.energia == 9

def test_tux_colision_hielo():
    mundo = Mundo(3, 3)
    mundo.colocar_item(Posicion(1, 0), HieloGrueso())
    tux = Tux(mundo, pos_inicial=Posicion(0, 0))
    
    # Intenta moverse hacia el hielo grueso
    assert tux.mover("derecha") is False
    assert tux.posicion == Posicion(0, 0)  # No cambia de posición
    assert tux.energia == 20  # Tampoco consume energía si choca

def test_tux_recoleccion_nieve():
    mundo = Mundo(3, 3)
    pos_nieve = Posicion(0, 1)
    mundo.colocar_item(pos_nieve, Nieve(cantidad=3))
    
    tux = Tux(mundo, pos_inicial=Posicion(0, 0))
    tux.mover("abajo")
    
    nieve_recolectada = tux.recolectar()
    assert nieve_recolectada == 3
    assert tux.inventario["Nieve"] == 3
    assert mundo.obtener_item(pos_nieve) is None  # La celda queda limpia

def test_sin_energia_no_puede_moverse():
    mundo = Mundo(3, 3)
    tux = Tux(mundo, pos_inicial=Posicion(0, 0), energia_inicial=0)
    
    assert tux.mover("derecha") is False
    assert tux.posicion == Posicion(0, 0)