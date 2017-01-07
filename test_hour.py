#!/usr/bin/env python

import pygame, sys
import ac
from pygame.locals import *

black = (0,0,0)
txtcolor = (255,255,255)


def init(debug=True):
	pygame.init()
	if debug:
		screen= pygame.display.set_mode((480,320)) #,pygame.FULLSCREEN
	else:
		screen= pygame.display.set_mode((480,320),pygame.FULLSCREEN	) #,
	pygame.display.set_caption('Alarm clock')
	return screen
	


if __name__ == "__main__":
	
	screen=init(False)
	font=pygame.font.SysFont('Arial', 50)
	
	while True: # main game loop
		
		screen.fill((black))
		screen.blit(font.render(ac.get_time(), True, (txtcolor)), (20, 150))
		
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
				
			if event.type == pygame.KEYDOWN:
            #print event.key
				if event.key in [pygame.K_ESCAPE,pygame.K_q] :
					pygame.quit()
					sys.exit()
       
		pygame.display.update()
