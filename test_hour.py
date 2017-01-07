#!/usr/bin/env python

import pygame, sys
import ac
from pygame.locals import *

black = (0,0,0)
txtcolor = (255,255,255)



fullscreen=True





if __name__ == "__main__":
	
	if len(sys.argv)>1:
		if sys.argv[1].lower()=='-d':
			fullscreen=False
		
	
	app=ac.App(fullscreen)
	
	
	app.add(ac.Panel_Hour())
	app.add(ac.Panel(txt='Second Panel'))
	app.add(ac.Panel(txt='Third Panel'))
	
	app.loop()
