import pygame

#initiate the game
pygame.init()

#screen
screen = pygame.display.set_mode((800, 600))

#title
pygame.display.set_caption("Stop The Wolf")
icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #test

        screen.fill((0, 0, 0))
        pygame.display.update()