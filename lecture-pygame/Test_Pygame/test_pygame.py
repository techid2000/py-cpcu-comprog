import pygame

width = 400
height = 400
FPS = 60

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Test_Pygame")

cherprang_img = pygame.image.load("source/BNK48/cherprang.png").convert_alpha()
cherprang_img = pygame.transform.scale(cherprang_img, (400, 400))
cherprang_rect = cherprang_img.get_rect()

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((0,0,0))

    screen.blit(cherprang_img, cherprang_rect)
    pygame.display.flip()
