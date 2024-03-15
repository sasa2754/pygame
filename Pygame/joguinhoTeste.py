import pygame
from pygame.locals import *
#from pygame.sprite import Sprite
from sys import exit
import time

pygame.init()

largura = 640
altura = 480
meioLargura = largura/2
meioAltura = altura/2
x = meioLargura - (50/2)
yColoridoV = 0
yColoridoL = 0
yColoridoA = 0
yColoridoVe = 0
yColoridoAz = 0
yColoridoI = 0
yColoridoVi = 0
xBranco = -50
alturaBranco = 100
yBranco = meioAltura - (alturaBranco/2)
velocidadeColoridos = 3
linhaBrancaAumentando = 40
linhaPretaAumentando = 2
relogio = pygame.time.Clock()
fonte = pygame.font.SysFont("arial", 40, True, False)
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Joguinho lindo")
frame = 140
while True:
#for para caso o X seja clicado, fechar a tela, da erro se não tiver :)
    relogio.tick(frame)
    #tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    mensagem = "Arco-íris"
    textoFormatado = fonte.render(mensagem, True,(255,255,255)) 
#parametros quadrado(rect) (r,g,b),(x,y,largura,altura)         
    pygame.draw.rect(tela, (255,0,0),(x-210,yColoridoV,50,50)) #vermelho
    pygame.draw.rect(tela, (255,127,0),(x-140,yColoridoL,50,50)) #laranja
    pygame.draw.rect(tela, (255,255,0),(x-70,yColoridoA,50,50)) #amarelo
    pygame.draw.rect(tela, (0,255,0),(x,yColoridoVe,50,50)) #verde
    pygame.draw.rect(tela, (0,0,255),(x+70,yColoridoAz,50,50)) #azul
    pygame.draw.rect(tela, (46,43,95),(x+140,yColoridoI,50,50)) #indigo
    pygame.draw.rect(tela, (139,0,255),(x+210,yColoridoVi,50,50)) #violeta
    pygame.draw.rect(tela, (255,255,255),(xBranco,yBranco,50,alturaBranco)) #branco
    yColoridoV += velocidadeColoridos
    
  

    if yColoridoV >= meioAltura/2:
        yColoridoL += velocidadeColoridos
        if yColoridoL >= meioAltura/2:
            yColoridoA += velocidadeColoridos
            if yColoridoA >= meioAltura/2:
                yColoridoVe += velocidadeColoridos
                if yColoridoVe >= meioAltura/2:
                    yColoridoAz += velocidadeColoridos
                    if yColoridoAz >= meioAltura/2:
                        yColoridoI += velocidadeColoridos
                        if yColoridoI >= meioAltura/2:
                            yColoridoVi += velocidadeColoridos

    if yColoridoV >= yBranco:
        xBranco += 2
    if xBranco >= largura:
        #tela.blit(textoFormatado,(meioLargura-85,meioAltura-30))
        pygame.draw.line(tela,(255,255,255),(0,240),(640,240), linhaBrancaAumentando)
        linhaBrancaAumentando += 3
        if linhaBrancaAumentando >= 486:
            #tela.fill((0,0,0))
            pygame.draw.line(tela,(0,0,0),(0,0),(646,0), linhaPretaAumentando) #linha de cima
            linhaPretaAumentando += 4
            if linhaPretaAumentando >= 960:
                tela.fill((0,0,0))
                tela.blit(textoFormatado,(meioLargura-85,meioAltura-30))
        # if xBranco >= largura:
        #     time.sleep(1.5)
        #     tela.fill((0,0,0))


    #Quando os coloridos chegarem no final da tela
    '''if yColorido >= 480: 
        frame += 20
        yColorido = 0'''
    
#parametros circulo(circle) ((r,g,b),(x,y),raio)
    #pygame.draw.circle(tela, (120,0,255),(meioLargura, meioAltura), 40)
#parametros linha(line) (r,g,b),(x,y(incio)), (x,y(fim)), (largura da linha)
    #pygame.draw.line(tela,(255,255,0),(390,0),(390,600), 5)

#Controlando um objeto
    #if event.type == KEYDOWN:
    # if event.key == K_a: 
    #     x -=20

    
    pygame.display.update()


#ficou mt poggers ~gabi
#obg gabi <3 ~Sasá