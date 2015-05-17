# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 19:23:43 2015

@author: gaetanduron
"""

import pygame

if ( __name__ == "__main__" ):
    pygame.init()
    
    window_size = window_width, window_height = 640, 480
    window = pygame.display.set_mode(window_size)
    
    running = True
    
    while ( running ):
        for event in pygame.event.get():
            if ( event.type == pygame.QUIT):
                running = False
            elif (event.key == pygame.locals.K_ESCAPE):
                pygame.quit()
                running = False 
                
    pygame.quit()