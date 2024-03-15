import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Definindo o tamanho da tela e outras configurações
largura = 640
altura = 480
tamanho_bloco = 40
escala = 1.35  # Fator de escala para aumentar o tamanho dos blocos
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pac-Man")

# Definindo cores
BRANCO = (255, 255, 255)
AZUL = (0, 0, 200)
PRETO = (0,0,0)
# Definindo o layout das paredes
mapa_paredes = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Função para desenhar as paredes
def desenhar_paredes():
    for linha in range(len(mapa_paredes)):
        for coluna in range(len(mapa_paredes[linha])):
            if mapa_paredes[linha][coluna] == 1:
                x = coluna * tamanho_bloco * escala
                y = linha * tamanho_bloco * escala
                largura_bloco = altura_bloco = tamanho_bloco * escala
                pygame.draw.rect(tela, AZUL, (x, y, largura_bloco, altura_bloco))

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Preenche a tela com a cor branca
    tela.fill(PRETO)

    # Desenha as paredes
    desenhar_paredes()

    # Atualiza a tela
    pygame.display.flip()
