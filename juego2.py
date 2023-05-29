import pygame



# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((1000, 800))
greenLight = pygame.image.load( "imagenes\green_trafficLight.webp" )
greenLight = pygame.transform.scale(greenLight, (500, 400))
clock = pygame.time.Clock()

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit()

    # hay que especificar las cordenadas en las que se quire poner
    screen.blit( greenLight, (250, 200) ) # blit al parecer sirve para sincronizar ambas cosas
    pygame.display.update()
    clock.tick(20)


pygame.quit()
