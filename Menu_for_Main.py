import pygame, sys
import Main
import Info_for_Menu

pygame.init()
background_colour =(255,255,255)#(40,194,199)

screen = pygame.display.set_mode((1250,650+25+10)) 
pygame.display.set_caption('Battleship Simulator') 
screen.fill(background_colour) 
  
 
font=pygame.font.Font('Zector.ttf',75)
text=font.render('BATTLESHIP SIMULATOR',True,'black')

play_img = pygame.image.load('Play_button_img.jpg').convert_alpha()
play_hov_img = pygame.image.load('Hov_play_Image.jpg').convert_alpha()

exit_img = pygame.image.load('Exit_button_Img.jpg').convert_alpha()
exit_hov_img = pygame.image.load('Hov_exit_Image.jpg').convert_alpha()

info_img = pygame.image.load('Info_button_Img.jpg').convert_alpha()
info_hov_img = pygame.image.load('Hov_info_Image.jpg').convert_alpha()

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


button_play = Button(520, 200, play_img, 1)
button_exit = Button(520, 500, exit_img, 1)
button_info = Button(520, 350, info_img, 1)

running = True
while running:
    screen.fill(background_colour) 

    if button_play.draw()[0]:
        Main.main()

    if button_exit.draw()[0]:
        running = False

    if button_info.draw()[0]:
        Info_for_Menu.info()

    if button_play.draw()[1]:
        #print('Hovering on Play')
        button_play = Button(520, 200, play_hov_img, 1)
    else:
        button_play = Button(520, 200, play_img, 1)

    if button_exit.draw()[1]:
        #print('Hovering on Exit')
        button_exit = Button(520, 500, exit_hov_img, 1)
    else:
        button_exit = Button(520, 500, exit_img, 1)

    if button_info.draw()[1]:
        #print('Hovering on Exit')
        button_info = Button(520, 350, info_hov_img, 1)
    else:
        button_info = Button(520, 350, info_img, 1)


    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False


    screen.blit(text,(280,50))
    pygame.display.update()
    pygame.display.flip()
    
pygame.quit()