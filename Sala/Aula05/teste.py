import pygame
pygame.init()
x= 400
y=300
pos_x = 100
pos_y = 300
velocidade = 20
velocidade_outros = 20
fundo = pygame.image.load('pista.png')
carro = pygame.image.load('carrinho1.png')
carrinho = pygame.image.load("carrinho2.png")
janela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Criando um jogo com Python")

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

        comandos = pygame.key.get_pressed()

        if comandos[pygame.K_UP]:
            y -= velocidade
        if comandos[pygame.K_DOWN]:
            y += velocidade
        if comandos[pygame.K_RIGHT]:
            x += velocidade
        if comandos[pygame.K_LEFT]:
            x -= velocidade

        if (pos_y <= -200):
            pos_y = 600

        pos_y -= velocidade_outros

    janela.blit(fundo, (0,0))
    janela.blit(carro, (x,y))
    janela.blit(carrinho, (pos_x, pos_y))
    pygame.display.update()

pygame.quit()
