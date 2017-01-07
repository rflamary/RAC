

import time
import pygame, sys
from pygame.locals import *

format_time="%H:%M:%S"
format_date="%A %d %B" #%x

screen_size=(480,320)
black = (0,0,0)
white = (255,255,255)

col_back=black
h_corner=100
v_corner=100

def get_time():
	return time.strftime(format_time)
def get_date():
	return time.strftime(format_date)


def init(screen_size=screen_size,fullscreen=False):
	"""init pygame and returns screen"""
	pygame.init()
	if fullscreen:
		screen= pygame.display.set_mode(screen_size,pygame.FULLSCREEN) #,pygame.FULLSCREEN
	else:
		screen= pygame.display.set_mode(screen_size) #,
	pygame.display.set_caption('Alarm clock')
	return screen
	
def put_txt(screen,txt,pos,font,txtcolor):
	screen.blit(font.render(txt, True, (txtcolor)), pos)
	
	
class Panel(object):
	
	def __init__(self,txt='Hello World',font='Arial',fs=50,pos=(5, 50),c=white,fonts=None):
		self.txt=txt
		self.txt_pos=pos
		self.font=pygame.font.SysFont('Arial', 50)
		self.pos=pos
		self.c=c
		if not fonts is None:
			self.set_fonts(fonts)
		
	def update(self,screen):

		put_txt(screen,self.txt,self.pos,self.font,self.c)
		
	def apply_event(self,event):
		pass
		
	def set_fonts(self,dic):
		self.fonts=dict()
		for key in dic:
			self.fonts[key]=dic[key]
			self.fonts[key]['font2']=pygame.font.SysFont(dic[key]['font'], dic[key]['fs'])
			
	def put_txt(self,screen,txt,pos,font):
		put_txt(screen,txt,pos,self.fonts[font]['font2'],self.fonts[font]['c'])		
		
	
class Panel_Hour(Panel):
	
	def update(self,screen):

		put_txt(screen,get_time(),self.pos,self.font,self.c)
		put_txt(screen,get_date(),(5, 100),self.font,self.c)
	
class App(object):
	
	def __init__(self,fullscreen):
		self.screen=init(fullscreen=fullscreen)
		self.lst_pan=[]
		self.cur_pan=0
		
	def nb_pan(self):
		return len(self.lst_pan)
		
	def add(self,panel):
		self.lst_pan.append(panel)
		
	def loop(self):
		
		while True: # main game loop
		
			self.screen.fill((col_back))

			if self.nb_pan():
				self.lst_pan[self.cur_pan].update(self.screen)
			
			for event in pygame.event.get():
				
				if self.nb_pan():
					self.lst_pan[self.cur_pan].apply_event(event)
				
				
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
					
				if event.type ==  pygame.MOUSEBUTTONDOWN:
					print(event)
					
					# test upper left corner
					if (event.pos[0]<h_corner) and (event.pos[1]<v_corner):
						self.cur_pan= (self.cur_pan-1) % self.nb_pan()
					
					# test upper right corner
					if (event.pos[0]>screen_size[0]-h_corner) and (event.pos[1]<v_corner):
						self.cur_pan= (self.cur_pan+1) % self.nb_pan()
											
				if event.type == pygame.KEYDOWN:
					print(event)
					if event.key in [pygame.K_ESCAPE,pygame.K_q] :
						pygame.quit()
						sys.exit()
						
					if event.key in [pygame.K_RIGHT,] :	
						self.cur_pan= (self.cur_pan+1) % self.nb_pan()
					
					if event.key in [pygame.K_LEFT,] :	
						self.cur_pan= (self.cur_pan-1) % self.nb_pan()						
						
		   
			pygame.display.update()
		
	
	
		
	
		
	
	
