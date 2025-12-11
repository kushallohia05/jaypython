import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
green=(0, 255, 0)
blue=(0, 0, 255)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, green, pygame.Rect(30, 30, 100, 60))
    pygame.draw.rect(screen, blue, pygame.Rect(100, 100, 100, 60))
    pygame.display.flip()