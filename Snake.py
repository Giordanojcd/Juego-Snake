from operator import truediv
from threading import main_thread
from pygame import mixer
import pygame
import random

pygame.display.set_caption("SNAKE 🐍 - Creador GiordanoJCD")

#poner musica ni bien abre el juego
mixer.init()
pygame.mixer.music.load("Assets/music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)

class cuerpo:
    def __init__(self, ventana):
        self.x = 0
        self.y = 0
        self.dir = 0
        self.ventana = ventana
    
    def dibujar(self):
        pygame.draw.rect(self.ventana, (0,255,0), (self.x, self.y, 10, 10))

    def moverse(self):
        if self.dir == 0:
            self.x += 10
        elif self.dir == 1:
            self.x -= 10
        elif self.dir == 2:
            self.y += 10
        elif self.dir == 3:
            self.y -= 10


class manzanas:
    def __init__(self, ventana):
        self.x = random.randrange(40) * 10
        self.y = random.randrange(40) * 10
        self.ventana = ventana
    def dibujar(self):
        pygame.draw.rect(self.ventana, (250,0,0), (self.x, self.y, 10, 10))

    def nueva_manzana(self):
        self.x = random.randrange(40) * 10
        self.y = random.randrange(40) * 10

def refrescar(ventana):
    ventana.fill((0,0,0))
    comida.dibujar()
    for i in range(len(serpiente)):
        serpiente[i].dibujar()

def seguir_cabeza():
    for i in range(len(serpiente)-1):
        serpiente[len(serpiente)- i - 1].x = serpiente[len(serpiente)- i - 2].x
        serpiente[len(serpiente)- i - 1].y = serpiente[len(serpiente)- i - 2].y


def main():
    global serpiente, comida
    ventana = pygame.display.set_mode((400,400))
    bg_image = pygame.image.load("Assets/fondo.jpg").convert_alpha()
    def draw_bg():
        scale_bg = pygame.transform.scale(bg_image,(400,400))
        ventana.blit(scale_bg,(0,0))
    
    comida = manzanas(ventana)
    serpiente = [cuerpo(ventana)]
    draw_bg()

    run = True
    while run:
          
              
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                       serpiente[0].dir = 0
                if event.key == pygame.K_LEFT:
                       serpiente[0].dir = 1
                if event.key == pygame.K_DOWN:
                       serpiente[0].dir = 2
                if event.key == pygame.K_UP:
                       serpiente[0].dir = 3
        
        
        

        serpiente[0].moverse()
        refrescar(ventana)
        
        
        pygame.time.delay(100)
        pygame.display.update() 
        if serpiente[0].x == comida.x and serpiente[0].y == comida.y:
            comida.nueva_manzana()
            serpiente.append(cuerpo(ventana))
        seguir_cabeza()     
        if serpiente[0].x >= 400:
            serpiente[0].x = 0
        if serpiente[0].x < 0:
            serpiente[0].x = 390
        elif serpiente[0].y >=400:
            serpiente[0].y = 0
        elif serpiente[0].y < 0:
            serpiente[0].y = 390
        for i in range(len(serpiente) - 2):
            if serpiente[len(serpiente) - i - 1].x == serpiente[0].x and serpiente[len(serpiente) - i - 1].y == serpiente[0].y:
                run = False
        
if __name__ == '__main__':
    main()
    pygame.quit()