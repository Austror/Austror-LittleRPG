#!/usr/bin/env python2
# -*-coding:utf-8 -*-

try:
    import os, sys
    from constantes import *
    from fonctions import *
    import pygame
    from pygame.locals import *
except ImportError, err:
    raise SystemExit, err

fenetre = pygame.display.set_mode(TAILLE_FENETRE)

pygame.display.flip()

while tableau == 0:

    afficher_erreur("test")
    
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
