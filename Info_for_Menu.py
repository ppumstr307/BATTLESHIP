def info():
	import pygame, sys

	pygame.init()
	background_colour =(255,255,255)#(40,194,199)

	screen = pygame.display.set_mode((1250,650+25+10)) 
	pygame.display.set_caption('Battleship Simulator - INFO') 
	screen.fill(background_colour) 
	 
	font=pygame.font.Font('Zector.ttf',65)
	font_small=pygame.font.Font('Zector.ttf',25)
	#text1=font.render('BATTLESHIP SIMULATOR',True,'black')

	text1 = font_small.render('Battleship is a strategy type guessing game for two players. It is played on ruled grids on',True,'black')
	text2 = font_small.render("which each player's fleet of warships are marked. The locations of the fleets are concealed ",True,'black')
	text3 = font_small.render("from the other player. Players take alternate turns calling 'shots' at the other player's ships,",True,'black')
	text4 = font_small.render("and the objective of the game is to destroy the opposing player's fleet. Each player starts",True,'black')
	text5 = font_small.render("with 15 units of ammunition which cannot be refilled. Try to hit as many opponent's ships as",True,'black')
	text6 = font_small.render('possible under the specified rounds of fire',True,'black')
	text = font.render('INFO',True,'black')

	play_img = pygame.image.load('Next_button_Img.jpg').convert_alpha()
	play_hov_img = pygame.image.load('Hov_Next_Image.jpg').convert_alpha()
	exit_img = pygame.image.load('Exit_button_Img.jpg').convert_alpha()
	exit_hov_img = pygame.image.load('Hov_exit_Image.jpg').convert_alpha()


	class Button:
	    def __init__(self, x, y, image, scale):
	        width = image.get_width()
	        height = image.get_height()
	        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
	        self.rect = self.image.get_rect()
	        self.rect.topleft = (x, y)
	        self.clicked = False


	    def draw(self):
	        action = False
	        hover = False

	        pos = pygame.mouse.get_pos()
	        if self.rect.collidepoint(pos):
	            hover = True
	            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
	                self.clicked = True
	                action = True
	        else:
	            hover = False

	        if pygame.mouse.get_pressed()[0] == 0:
	            self.clicked = False

	        screen.blit(self.image, (self.rect.x, self.rect.y))

	        return action, hover

	button_play = Button(900, 500, play_img, 1)
	running = True
	while running:
		screen.fill(background_colour)
		for event in pygame.event.get():
		    if event.type == pygame.QUIT: 
		        running = False

		if button_play.draw()[0]:
			screen = pygame.display.set_mode((1250,650+25+10)) 
			pygame.display.set_caption('Battleship Simulator - INFO') 
			screen.fill(background_colour)

			'''
			Each ship occupies some specific number of cells according to the type of ship.
			The types of ships along with their cell size is mentioned below.
			'''
			text11 = font_small.render('Each ship occupies some specific number of cells according to the type of ship being placed.',True,'black')
			text12 = font_small.render('The types of ships along with their cell size is mentioned below.',True,'black')
			text13 = font_small.render('3 Cells',True,'black')
			text14 = font_small.render('2 Cells',True,'black')
			text15 = font_small.render('5 Cells',True,'black')
			text16 = font_small.render('4 Cells',True,'black')


			ship_a = pygame.image.load('shipa.jpg').convert()
			ship_b = pygame.image.load('shipb.jpg').convert()
			ship_c = pygame.image.load('shipc.jpg').convert()
			ship_d = pygame.image.load('shipd.jpg').convert()

			button_exit = Button(900, 500, exit_img, 1)
			running = True
			while running:
				screen.fill(background_colour)
				for event in pygame.event.get():
				    if event.type == pygame.QUIT: 
				        running = False
				    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				    	if button_exit.draw()[0]:
				    		running = False

				if button_exit.draw()[1]:
			        #print('Hovering on Play')
					button_exit = Button(900, 500, exit_hov_img, 1)
				else:
					button_exit = Button(900, 500, exit_img, 1)


				screen.blit(text,(555,50))
				screen.blit(text11,(10,200))
				screen.blit(text12,(10,250))
				screen.blit(text13,(400,365))
				screen.blit(text14,(400,440))
				screen.blit(text15,(400,515))
				screen.blit(text16,(400,590))

				screen.blit(ship_a, (40, 350))
				screen.blit(ship_b, (40, 425))
				screen.blit(ship_c, (40, 500))
				screen.blit(ship_d, (40,575))

				pygame.display.update()
				pygame.display.flip()

		if button_play.draw()[1]:
	        #print('Hovering on Play')
			button_play = Button(900, 500, play_hov_img, 1)
		else:
			button_play = Button(900, 500, play_img, 1)


		#screen.blit(text1,(280,50))
		screen.blit(text,(555,50))
		screen.blit(text1,(10,200))
		screen.blit(text2,(10,250))
		screen.blit(text3,(10,300))
		screen.blit(text4,(10,350))
		screen.blit(text5,(10,400))
		screen.blit(text6,(10,450))

		pygame.display.update()
		pygame.display.flip()
	    
	pygame.quit()