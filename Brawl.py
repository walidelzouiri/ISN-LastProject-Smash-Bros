# -*- coding: utf-8 -*-*
import pygame

pygame.init()

fenetre = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN, 32)
pygame.display.set_caption("Brawl")



clock = pygame.time.Clock()
continuer = 1
while continuer == 1:
    clock.tick(60)

pygame.quit()