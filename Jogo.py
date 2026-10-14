#Configurações 
import pygame
import random

pygame.init () 
pygame.displey.ste_caption("Jogo snake Python")
Largura,altura = 600,400
pygame.display.set_model ((Largura,altura))
relogio = pygame.time.Clock()
#cores 
preta = (0,0,0)
azul = (0,0,255)
laranja = (255,127,0)
branca = (255,255,255)

#Paramentros 
tamanho_quadrado = 10
velociddae = 15

def rodar_jogo():
    fim_jogo = False

    while not fim_jogo:

        for eventos in pygame.eventos.get():

            if eventos.type == pygame.QUIT:
                fim_jogo = True


#Loop infinto 

# Desnhas objetos 
#TPontuação
#Cobrinha
#Comida

#Criar a loga de terminar 
#Cobra bater na parede 
#Bter na propria 

#Interações do jogo com o Usario 