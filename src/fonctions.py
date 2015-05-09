#!/usr/bin/env python2
# -*-coding:utf-8 -*-

try:
    import os, sys
    import pygame
    from pygame.locals import *
    from rpg import *
    from constantes import *
except ImportError, err:
    raise SystemExit, err

def afficher_erreur(erreur):
    fenetre = pygame.display.set_mode((320, 100))
    police = pygame.font.Font(None, 60)
    texte = police.render(erreur, True, (0,0,0))
    fenetre.blit(texte, (20, 20))
    pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
