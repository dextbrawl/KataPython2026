import time
from src.entidades import Posicion, Nieve, HieloGrueso
from src.mundo import Mundo
from src.tux import Tux
from src.render import RenderizadorMundo


def cargar_mapa_antartida() -> tuple[Mundo, Tux]:
    """Crea un mapa de 5x5 con nieve y bloques de hielo obstáculo."""
    mundo = Mundo(filas=5, columnas=5)

    # Colocar nieve en varias celdas
    mundo.colocar_item(Posicion(1, 0), Nieve(cantidad=2))
    mundo.colocar_item(Posicion(2, 0), Nieve(cantidad=1))
    mundo.colocar_item(Posicion(4, 1), Nieve(cantidad=4))
    mundo.colocar_item(Posicion(0, 3), Nieve(cantidad=3))
    mundo.colocar_item(Posicion(3, 4), Nieve(cantidad=5))

    # Colocar obstáculos de Hielo Grueso
    mundo.colocar_item(Posicion(2, 1), HieloGrueso())
    mundo.colocar_item(Posicion(2, 2), HieloGrueso())
    mundo.colocar_item(Posicion(1, 3), HieloGrueso())

    # Instanciar a Tux en la posición inicial (0,0)
    tux = Tux(mundo, pos_inicial=Posicion(0, 0), energia_inicial=30)
    return mundo, tux


# =====================================================================
#  LÓGICA DEL ALUMNO (Reto de Automatización)
# =====================================================================
def algoritmo_recolector(tux: Tux, mundo: Mundo):
    """
    Función que los alumnos deben implementar para que Tux 
    recorra el mapa, recolecte la nieve y esquive los obstáculos.
    """
    # Ejemplo de recorrido manual/simple (los alumnos crearán bucles/algoritmos):
    movimientos = [
        "derecha", "recolectar",
        "derecha", "recolectar",
        "abajo",
        "abajo",
        "izquierda", "izquierda", "recolectar",
        "abajo",
        "derecha", "derecha", "derecha", "recolectar"
    ]

    for accion in movimientos:
        # Renderizado visual paso a paso
        RenderizadorMundo.dibujar(mundo, tux)
        time.sleep(1)

        if accion == "recolectar":
            # Usamos un bloque try-except o comprobamos si el método está implementado
            # por si el alumno prueba main.py antes de llegar a la fase 3
            try:
                cantidad = tux.recolectar()
                if cantidad and cantidad > 0:
                    print(f"✨ ¡Tux recolectó {cantidad} de nieve!")
            except TypeError:
                pass # Si devuelve None porque no está implementado
        else:
            exito = tux.mover(accion)
            if not exito:
                print(f"⚠️ ¡No se pudo mover hacia '{accion}'!")

    # Render final
    RenderizadorMundo.dibujar(mundo, tux)


if __name__ == "__main__":
    print("🐧 ¡Iniciando la Kata de Tux en la Antártida!")
    mundo, tux = cargar_mapa_antartida()
    algoritmo_recolector(tux, mundo)
    
    # Manejo de seguridad en caso de que inventario no esté inicializado todavía en Tux
    inv = getattr(tux, 'inventario', {})
    nieve = inv.get('Nieve', 0) if isinstance(inv, dict) else 0
    print(f"🎉 ¡Juego terminado! Nieve total en inventario: {nieve}")
