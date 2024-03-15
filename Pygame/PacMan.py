import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480
meioLargura = largura/2
meioAltura = altura/2
AZUL = (0,0,255)
PRETO = (0,0,0)
BRANCO = (255,255,255)
xPac = meioLargura
yPac = meioAltura
relogio = pygame.time.Clock()
fonte = pygame.font.SysFont("arial", 30, True, False)
tela = pygame.display.set_mode((largura, altura+50))
pygame.display.set_caption("PacMan")
frame = 50
pontos = 0

while True:
    relogio.tick(frame)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    mensagem = "Pontos: 0"
    textoFormatado = fonte.render(mensagem, True,(255,255,255))
    tela.blit(textoFormatado,(10,altura+8)) #Escrevendo os pontos

    lateralEsquerda = pygame.draw.line(tela,(AZUL),(0,0),(0,altura), 10) #Lateral esquerda
    lateralDireita = pygame.draw.line(tela,(AZUL),(largura-4,0),(largura-4,altura), 10) #Lateral direita
    cima = pygame.draw.line(tela,(AZUL),(0,4),(largura,4), 10) #Cima
    baixo = pygame.draw.line(tela,(AZUL),(0,altura-4),(largura,altura-4), 10) #Baixo

    qudradoMeioLateralEsquerda = pygame.draw.line(tela,(AZUL),(meioLargura-100,meioAltura-50),(meioLargura-100,meioAltura+50), 8) #Quadrado do meio lateral esquerda
    quadradoMeioLateralDireta = pygame.draw.line(tela,(AZUL),(meioLargura+100,meioAltura-50),(meioLargura+100,meioAltura+50), 8)
    quadradoMeioBaixo = pygame.draw.line(tela,(AZUL),(meioLargura-103,meioAltura+50),(meioLargura+104,meioAltura+50), 8)
    quadradoMeioCimaEsquerda = pygame.draw.line(tela,(AZUL),(meioLargura-103,meioAltura-50),(meioLargura-35,meioAltura-50), 8)
    quadradoMeioCimaDireita = pygame.draw.line(tela,(AZUL),(meioLargura+35,meioAltura-50),(meioLargura+104,meioAltura-50), 8)
    
    linhaBaixoEsquerda = pygame.draw.line(tela,(AZUL),(meioLargura-100,meioAltura+125),(meioLargura-100,altura), 8)
    linhaBaixoEsquerdaHorizontal = pygame.draw.line(tela,(AZUL),(meioLargura-175,meioAltura+122),(0,meioAltura+122), 8)
    linhaBaixoEsquerdaHorizontalMeio = pygame.draw.line(tela,(AZUL),(meioLargura-155,meioAltura+180),(55,meioAltura+180), 8)
    linhaBaixoDireita = pygame.draw.line(tela,(AZUL),(meioLargura+100,meioAltura+125),(meioLargura+100,altura), 8)
    linhaBaixoDireitaHorizontal = pygame.draw.line(tela,(AZUL),(meioLargura+175,meioAltura+122),(largura,meioAltura+122), 8)
    linhaBaixoDireitaHorizontalMeio = pygame.draw.line(tela,(AZUL),(meioLargura+155,meioAltura+180),(largura-55,meioAltura+180), 8)
    linhaMeioBaixoCima = pygame.draw.line(tela,(AZUL),(meioLargura-40,meioAltura+127),(meioLargura+40,meioAltura+127), 8)
    linhaMeioBaixoMeio = pygame.draw.line(tela,(AZUL),(meioLargura-40,meioAltura+180),(meioLargura+40,meioAltura+180), 8)

    linhaCimaEsquerda = pygame.draw.line(tela,(AZUL),(meioLargura-100,meioAltura-125),(meioLargura-100,-altura), 8)
    linhaCimaEsquerdaHorizontal = pygame.draw.line(tela,(AZUL),(meioLargura-175,meioAltura-122),(0,meioAltura-122), 8)
    linhaCimaEsquerdaHorizontalMeio = pygame.draw.line(tela,(AZUL),(meioLargura-155,meioAltura-180),(55,meioAltura-180), 8)
    linhaCimaDireita = pygame.draw.line(tela,(AZUL),(meioLargura+100,meioAltura-125),(meioLargura+100,-altura), 8)
    linhaCimaDireitaHorizontal = pygame.draw.line(tela,(AZUL),(meioLargura+175,meioAltura-122),(largura,meioAltura-122), 8)
    linhaCimaDireitaHorizontalMeio = pygame.draw.line(tela,(AZUL),(meioLargura+155,meioAltura-180),(largura-55,meioAltura-180), 8)
    linhaMeioCimaCima = pygame.draw.line(tela,(AZUL),(meioLargura-40,meioAltura-127),(meioLargura+40,meioAltura-127), 8)
    linhaMeioCimaMeio = pygame.draw.line(tela,(AZUL),(meioLargura-40,meioAltura-180),(meioLargura+40,meioAltura-180), 8)

    quadradoEsquerdaBaixo = pygame.draw.line(tela,(AZUL),(meioLargura-175,meioAltura+50),(0,meioAltura+50), 8)
    quadradoEsquerdaCima = pygame.draw.line(tela,(AZUL),(meioLargura-175,meioAltura-50),(0,meioAltura-50), 8)
    qudradolEsquerdaVertical = pygame.draw.line(tela,(AZUL),(meioLargura-175,meioAltura-53),(meioLargura-175,meioAltura+54), 8)

    quadradoDireitaBaixo = pygame.draw.line(tela,(AZUL),(meioLargura+175,meioAltura+50),(largura,meioAltura+50), 8)
    quadradoDireitaCima = pygame.draw.line(tela,(AZUL),(meioLargura+175,meioAltura-50),(largura,meioAltura-50), 8)
    qudradolDireitaVertical = pygame.draw.line(tela,(AZUL),(meioLargura+175,meioAltura-53),(meioLargura+175,meioAltura+54), 8)
    #31 linhas

    pacman = pygame.draw.circle(tela, (255,255,0),(xPac, yPac), 20) #pacman

    if event.type == KEYDOWN:
        if event.key == K_LEFT: 
            xPac -= 8
        if event.key == K_RIGHT: 
            xPac += 8
        if event.key == K_UP: 
            yPac -= 8
        if event.key == K_DOWN: 
            yPac += 8
    
    pygame.display.update()