import pygame

pygame.init()

win = pygame.display.set_mode((720, 480))
pygame.display.set_caption("Experiment", "hello")

walkRight = [pygame.image.load("R1.png"), pygame.image.load("R2.png"), pygame.image.load("R3.png"),
             pygame.image.load("R4.png"), pygame.image.load("R5.png"), pygame.image.load("R6.png"),
             pygame.image.load("R7.png"), pygame.image.load("R8.png"), pygame.image.load("R9.png")]
#ctrl+K
#ctrl+alt+k
#ctrl+shift+k