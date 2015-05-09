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
    texte = 
