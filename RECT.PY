import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
green=(0, 255, 0)
blue=(0, 0, 255)
red=(255, 0, 0)
yellow=pygame.Color('yellow')
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, green, pygame.Rect(30, 30, 60, 60))
    pygame.draw.rect(screen, blue, pygame.Rect(100, 100, 60, 60))
    pygame.draw.rect(screen, red, pygame.Rect(170, 170, 60, 60))
    pygame.draw.circle(screen, yellow,(300,100),50)
    pygame.display.flip()