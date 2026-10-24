# 🐧 Enunciados de la Fase 4: Retos de Automatización

En esta fase final, tu objetivo es escribir scripts que controlen a Tux para resolver problemas en distintos escenarios de la Antártida.

---

### Reto 1: El Recorrido en Serpiente
* **Escenario:** Un área despejada de 5x5 repleta de nieve en todas las casillas.
* **Misión:** Diseña un algoritmo de barrido (en zig-zag o serpiente) para limpiar **toda** la nieve del mapa.
* **Límite:** 30 unidades de energía.
* **Aprenderás:** Control de bucles anidados, condiciones de movimiento y barrido de matrices.

---

### Reto 2: El Laberinto de Hielo 
* **Escenario:** Tux se encuentra en la esquina superior izquierda (0,0) y hay un gran depósito con 20 unidades de nieve en la esquina opuesta (4,4), pero el camino está bloqueado por un laberinto de bloques de `HieloGrueso`.
* **Misión:** Llega al depósito de nieve esquivando los bloques sin chocar y recolecta el botín.
* **Límite:** 25 unidades de energía.
* **Aprenderás:** Algoritmos de esquive de obstáculos y búsqueda de caminos (Pathfinding).

---

### Reto 3: Mochila y Batería Limitada 
* **Escenario:** Un mapa de 6x6 con 5 depósitos de nieve de distintos tamaños y ubicaciones. Tux arranca con la energía muy justa (18 unidades).
* **Misión:** Diseña una estrategia que maximice la cantidad total de nieve recolectada antes de que Tux se quede sin energía.
* **Límite:** 18 unidades de energía.
* **Aprenderás:** Algoritmos codiciosos (Greedy), evaluación de costes/beneficios y problemas de optimización espacial.

---

### Reto 4: El Vendedor Ambulante Antártico
* **Escenario:** Una amplia zona de 8x8 con 6 depósitos aislados de nieve (10 unidades cada uno) y un denso entramado de murallas de hielo.
* **Misión:** Recoge la nieve de los 6 depósitos y regresa a la casilla inicial (0,0). La energía está calculada con precisión exacta para el recorrido óptimo.
* **Límite:** 42 unidades de energía.
* **Aprenderás:** Algoritmos de búsqueda de caminos óptimos (A* / Dijkstra) combinados con la resolución del Problema del Viajante de Comercio (TSP).