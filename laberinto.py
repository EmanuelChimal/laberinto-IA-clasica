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