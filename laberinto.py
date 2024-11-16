import pygame
import random
from collections import deque

# Configuración de Pygame
pygame.init()
ANCHO, ALTO = 600, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Resolución de Laberinto con IA Clásica")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)

# Tamaño del laberinto
FILAS, COLUMNAS = 15, 15
TAMANO_CELDA = ANCHO // COLUMNAS

# Función para generar un laberinto asegurando que el inicio y objetivo estén conectados
def generar_laberinto(filas, columnas):
    laberinto = [[1] * columnas for _ in range(filas)]  # Crea un laberinto lleno de paredes (1)
    
    # Crear el punto de inicio y objetivo
    inicio = (0, 0)
    objetivo = (filas - 1, columnas - 1)
    laberinto[inicio[0]][inicio[1]] = 0
    laberinto[objetivo[0]][objetivo[1]] = 0
    
    # Realizar un camino aleatorio para asegurar que el objetivo sea alcanzable
    for _ in range(filas * columnas // 2):
        x = random.randint(0, filas - 1)
        y = random.randint(0, columnas - 1)
        if laberinto[x][y] == 1:
            laberinto[x][y] = 0

    # Para asegurar que haya un camino válido entre inicio y objetivo, podemos usar BFS para conectar los dos puntos
    camino_conectado = bfs(laberinto, inicio, objetivo)
    if camino_conectado is None:
        # Si no hay camino, modificamos el laberinto hasta que se conecten
        while camino_conectado is None:
            laberinto = [[1] * columnas for _ in range(filas)]
            laberinto[inicio[0]][inicio[1]] = 0
            laberinto[objetivo[0]][objetivo[1]] = 0
            for _ in range(filas * columnas // 2):
                x = random.randint(0, filas - 1)
                y = random.randint(0, columnas - 1)
                if laberinto[x][y] == 1:
                    laberinto[x][y] = 0
            camino_conectado = bfs(laberinto, inicio, objetivo)

    return laberinto, inicio, objetivo

# Función de búsqueda en anchura (BFS)
def bfs(laberinto, inicio, objetivo):
    cola = deque([inicio])
    visitado = {inicio: None}
    
    while cola:
        nodo_actual = cola.popleft()
        if nodo_actual == objetivo:
            return reconstruir_camino(visitado, inicio, objetivo)
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            vecino = (nodo_actual[0] + dx, nodo_actual[1] + dy)
            if 0 <= vecino[0] < FILAS and 0 <= vecino[1] < COLUMNAS and vecino not in visitado and laberinto[vecino[0]][vecino[1]] == 0:
                visitado[vecino] = nodo_actual
                cola.append(vecino)
    
    return None

# Función para reconstruir el camino
def reconstruir_camino(visitado, inicio, objetivo):
    camino = []
    nodo_actual = objetivo
    while nodo_actual is not None:
        camino.append(nodo_actual)
        nodo_actual = visitado[nodo_actual]
    camino.reverse()
    return camino

# Dibujo del laberinto en Pygame
def dibujar_laberinto(laberinto, camino=[]):
    pantalla.fill(BLANCO)
    for x in range(FILAS):
        for y in range(COLUMNAS):
            rect = pygame.Rect(y * TAMANO_CELDA, x * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA)
            if laberinto[x][y] == 1:
                pygame.draw.rect(pantalla, NEGRO, rect)  # Dibuja la pared
            else:
                pygame.draw.rect(pantalla, BLANCO, rect)
    
    # Dibuja el camino encontrado
    for (x, y) in camino:
        rect = pygame.Rect(y * TAMANO_CELDA, x * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA)
        pygame.draw.rect(pantalla, VERDE, rect)

# Programa principal
laberinto, inicio, objetivo = generar_laberinto(FILAS, COLUMNAS)

# Ejecuta la búsqueda y obtiene el camino
camino = bfs(laberinto, inicio, objetivo)

# Bucle principal de Pygame
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Dibuja el laberinto y el camino encontrado
    if camino:
        dibujar_laberinto(laberinto, camino)
    else:
        print("No se encontró un camino.")
    
    pygame.display.flip()  # Actualiza la pantalla

pygame.quit()