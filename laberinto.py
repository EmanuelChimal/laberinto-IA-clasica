import pygame
import random
from collections import deque

# Configuración de Pygame
pygame.init()
ANCHO, ALTO = 600, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Resolución de Laberinto con IA Clásica")
