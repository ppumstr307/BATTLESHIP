def main():

    import pygame, sys
    import random
    import Battleship_Drag
    import random

    pygame.init()

    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption('Battleship Simulator')

    grid_size = 10
    col = 'black'
    run = True
    color = (219, 112, 147)
    color_safe = (146, 179, 240)
    cube_size = 50
    chance=15
    
    cur_chnc_p1=0
    cur_chnc_bot=0

    # Ships coordinates
    p1_ships = Battleship_Drag.p1_ship_loca
    bot_ships = Battleship_Drag.p2_ship_loca
    print(p1_ships)
    print(bot_ships)
    # Initialize hit and miss squares
    hit_squares_p1 = []
    hit_squares_bot = []
    miss_squares = []

    global p1_ship_des,bot_ship_des
    p1_ship_des=0
    bot_ship_des=0


    p1_ships_refined=[]
    for l in range(0, 6):
        len_p1_ship = p1_ships[l][1][0] - p1_ships[l][0][0]
        box_len_p1_ship = len_p1_ship // cube_size

        print('Length of Ship for P1: ', box_len_p1_ship, 'blocks\n')

        cor=0
        while cor < (box_len_p1_ship*50):
            w, s = p1_ships[l][0]
            col_ = (w+cor) // cube_size
            row_ = (s) // cube_size

            p1_ships_refined.append((row_, col_))
            cor+=50

    bot_ships_refined=[]
    for z in range(0, 6):
        len_bot_ship = bot_ships[z][1][0] - bot_ships[z][0][0]
        box_len_bot_ship = len_bot_ship // cube_size

        print('Length of Ship for P2: ', box_len_bot_ship, 'blocks\n')

        cor=0
        while cor < (box_len_bot_ship*50):
            w, s = bot_ships[z][0]
            col_ = (w+cor) // cube_size
            row_ = (s) // cube_size

            bot_ships_refined.append((row_, col_))
            cor+=50



    print('P1 Ships Location: ', p1_ships_refined, '\n')
    print('P2 Ships Location: ', bot_ships_refined, '\n')

    while run:
        screen.fill('white')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    col = x // cube_size
                    row = y // cube_size

                    
                    if row >= 1 and col >=13 and row <= 10 and col <= 22:
                        if (row, col) in bot_ships_refined:
                            print('Shot fired at: ',(row, col))
                            print('Thats a Hit!')
                            hit_squares_bot.append((row, col))
                            cur_chnc_p1+=1
                            p1_ship_des+=1
                            print('Ammo Fired by Player 1: ',cur_chnc_p1, 'Units')
                            print('Ammo left for Player 1: ', (15-cur_chnc_p1), 'Units')
                            print()

                        else:
                            cur_chnc_p1+=1 
                            miss_squares.append((row, col))
                            print('Ammo Fired by Player 1: ',cur_chnc_p1, 'Units')
                            print('Ammo left for Player 1: ', (15-cur_chnc_p1), 'Units')
                            print()

                        row = random.randint(1,10)
                        col = random.randint(1,10)

                        if (row, col) in p1_ships_refined:
                            print('Shot fired at: ',(row, col))
                            print('Thats a Hit!')
                            hit_squares_p1.append((row, col))
                            cur_chnc_bot+=1
                            bot_ship_des+=1
                            print('Ammo Fired by Bot: ',cur_chnc_bot, 'Units')
                            print('Ammo left for Bot: ', (15-cur_chnc_bot), 'Units')
                            print()

                        else:
                            miss_squares.append((row, col))
                            cur_chnc_bot+=1
                            print('Ammo Fired by Bot: ',cur_chnc_bot, 'Units')
                            print('Ammo left for Bot: ', (15-cur_chnc_bot), 'Units')
                            print()
                            
                    else:
                        pass

        # Draw hit and miss squares
        for row, col in hit_squares_p1:
            pygame.draw.rect(screen, color, pygame.Rect(col * cube_size+20, row * cube_size+20, cube_size-18, cube_size-18), border_radius = 15)
        for row, col in hit_squares_bot:
            pygame.draw.rect(screen, color, pygame.Rect(col * cube_size+20, row * cube_size+20, cube_size-18, cube_size-18), border_radius = 15)
        for row, col in miss_squares:
            pygame.draw.rect(screen, color_safe, pygame.Rect(col * cube_size+20, row * cube_size+20, cube_size-18, cube_size-18), border_radius = 15)

        # Grid
        for x in range(1, grid_size + 2):
            pygame.draw.line(screen, col, (60, 10 + x * cube_size), (560, 10 + x * cube_size), 2)
            pygame.draw.line(screen, col, (10 + x * cube_size, 60), (10 + x * cube_size, 560), 2)

        # Grid 2
        for x in range(1, grid_size + 2):
            pygame.draw.line(screen, col, (610+50, 10 + x * cube_size), (1110+50, 10 + x * cube_size), 2)
            pygame.draw.line(screen, col, (550+50 + 10 + x * cube_size, 60), (550 +50+ 10 + x * cube_size, 560), 2)

        spacing = 564
        txt_spacing = 40

        # Text
        font = pygame.font.Font('Zector.ttf', 25)
        font1 = pygame.font.Font('Zector.ttf', 40)

        text = font1.render('Click in one of the boxes to shoot!', True, 'black')
        a = font.render('A', True, 'black')
        b = font.render('B', True, 'black')
        c = font.render('C', True, 'black')
        d = font.render('D', True, 'black')
        e = font.render('E', True, 'black')
        f = font.render('F', True, 'black')
        g = font.render('G', True, 'black')
        h = font.render('H', True, 'black')
        i = font.render('I', True, 'black')
        j = font.render('J', True, 'black')

        a1 = font.render('1', True, 'black')
        a2 = font.render('2', True, 'black')
        a3 = font.render('3', True, 'black')
        a4 = font.render('4', True, 'black')
        a5 = font.render('5', True, 'black')
        a6 = font.render('6', True, 'black')
        a7 = font.render('7', True, 'black')
        a8 = font.render('8', True, 'black')
        a9 = font.render('9', True, 'black')
        a10 = font.render('10', True, 'black')

        # Text 1

        screen.blit(text,(300,10))
        screen.blit(a, (txt_spacing, 74))
        screen.blit(b, (txt_spacing, 74 + cube_size))
        screen.blit(c, (txt_spacing, 74 + (2 * cube_size)))
        screen.blit(d, (txt_spacing, 74 + (3 * cube_size)))
        screen.blit(e, (txt_spacing, 74 + (4 * cube_size)))
        screen.blit(f, (txt_spacing, 74 + (5 * cube_size)))
        screen.blit(g, (txt_spacing, 74 + (6 * cube_size)))
        screen.blit(h, (txt_spacing, 74 + (7 * cube_size)))
        screen.blit(i, (txt_spacing, 74 + (8 * cube_size)))
        screen.blit(j, (txt_spacing, 74 + (9 * cube_size)))

        screen.blit(a1, (78, spacing))
        screen.blit(a2, (78 + cube_size, spacing))
        screen.blit(a3, (78 + (2 * cube_size), spacing))
        screen.blit(a4, (78 + (3 * cube_size), spacing))
        screen.blit(a5, (78 + (4 * cube_size), spacing))
        screen.blit(a6, (78 + (5 * cube_size), spacing))
        screen.blit(a7, (78 + (6 * cube_size), spacing))
        screen.blit(a8, (78 + (7 * cube_size), spacing))
        screen.blit(a9, (78 + (8 * cube_size), spacing))
        screen.blit(a10, (76 + (9 * cube_size), spacing))

        txt_spacing = txt_spacing + 40

        # Text 2
        screen.blit(a, (txt_spacing + 552, 72))
        screen.blit(b, (txt_spacing + 552, 72 + cube_size))
        screen.blit(c, (txt_spacing + 552, 72 + (2 * cube_size)))
        screen.blit(d, (txt_spacing + 552, 72 + (3 * cube_size)))
        screen.blit(e, (txt_spacing + 552, 72 + (4 * cube_size)))
        screen.blit(f, (txt_spacing + 552, 72 + (5 * cube_size)))
        screen.blit(g, (txt_spacing + 552, 72 + (6 * cube_size)))
        screen.blit(h, (txt_spacing + 552, 72 + (7 * cube_size)))
        screen.blit(i, (txt_spacing + 552, 72 + (8 * cube_size)))
        screen.blit(j, (txt_spacing + 552, 72 + (9 * cube_size)))

        screen.blit(a1, (78 + 40 + 552, spacing))
        screen.blit(a2, (78 + 40 + cube_size + 552, spacing))
        screen.blit(a3, (78 + 40 + (2 * cube_size) + 552, spacing))
        screen.blit(a4, (78 + 40 + (3 * cube_size) + 552, spacing))
        screen.blit(a5, (78 + 40 + (4 * cube_size) + 552, spacing))
        screen.blit(a6, (78 + 40 + (5 * cube_size) + 552, spacing))
        screen.blit(a7, (78 + 40 + (6 * cube_size) + 552, spacing))
        screen.blit(a8, (78 + 40 + (7 * cube_size) + 552, spacing))
        screen.blit(a9, (78 + 40 + (8 * cube_size) + 552, spacing))
        screen.blit(a10, (72 + 40 + (9 * cube_size) + 552, spacing))

        if cur_chnc_p1==cur_chnc_bot==chance:
            run=False

        pygame.display.update()
        pygame.display.flip()


    if p1_ship_des>bot_ship_des:
        print('Player 1 win')
        background_colour =(255,255,255)#(40,194,199)

        screen = pygame.display.set_mode((800,600+25+10)) 
        pygame.display.set_caption('Battleship Simulator') 
        screen.fill(background_colour) 
         
        font = pygame.font.Font('Zector.ttf',75)
        font_small = pygame.font.Font('Zector.ttf',45)

        header = font.render('OUT OF AMMUNITIONS',True,'black')
        text = font_small.render('Player 1 Got the Most Hits',True,'black')

        menu_img = pygame.image.load('Exit_button_Img.jpg').convert_alpha()
        menu_hov_img = pygame.image.load('Hov_exit_Image.jpg').convert_alpha()
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

        button_menu = Button(320, 400, menu_img, 0.7)

        running=True
        while running:
            screen.fill('white')

            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    running = False

            if button_menu.draw()[0]:
                running = False
            if button_menu.draw()[1]:
                #print('Hovering on Play')
                button_menu = Button(320, 400, menu_hov_img, 0.7)
            else:
                button_menu = Button(320, 400, menu_img, 0.7)

            screen.blit(header,(50,50))
            screen.blit(text,(100,150))

            pygame.display.update()

    elif bot_ship_des>p1_ship_des:
        print('Lost by a Bot LMAO')
        background_colour =(255,255,255)#(40,194,199)

        screen = pygame.display.set_mode((800,600+25+10)) 
        pygame.display.set_caption('Battleship Simulator') 
        screen.fill(background_colour) 
          
        font = pygame.font.Font('Zector.ttf',75)
        font_small = pygame.font.Font('Zector.ttf',45)

        header = font.render('OUT OF AMMUNITIONS',True,'black')
        text = font_small.render('Lost by a Bot LMAO',True,'black')

        menu_img = pygame.image.load('Exit_button_Img.jpg').convert_alpha()
        menu_hov_img = pygame.image.load('Hov_exit_Image.jpg').convert_alpha()
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

        button_menu = Button(320, 400, menu_img, 0.7)

        running=True
        while running:
            screen.fill('white')

            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    running = False

            if button_menu.draw()[0]:
                running = False

            if button_menu.draw()[1]:
                #print('Hovering on Play')
                button_menu = Button(320, 400, menu_hov_img, 0.7)
            else:
                button_menu = Button(320, 400, menu_img, 0.7)

            screen.blit(header,(50,50))
            screen.blit(text,(100,150))

            pygame.display.update()

    else:
        print('Now thats a Tie!!')
        background_colour =(255,255,255)#(40,194,199)

        screen = pygame.display.set_mode((800,600+25+10)) 
        pygame.display.set_caption('Battleship Simulator') 
        screen.fill(background_colour) 
          
        font = pygame.font.Font('Zector.ttf',75)
        font_small = pygame.font.Font('Zector.ttf',45)

        header = font.render('OUT OF AMMUNITIONS',True,'black')
        text = font_small.render('Thats a draw!!!',True,'black') 

        menu_img = pygame.image.load('Exit_button_Img.jpg').convert_alpha()
        menu_hov_img = pygame.image.load('Hov_exit_Image.jpg').convert_alpha()
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

        button_menu = Button(320, 400, menu_img, 0.7)
        running=True
        while running:
            screen.fill('white')

            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    running = False
            
            if button_menu.draw()[0]:
                running = False

            if button_menu.draw()[1]:
                #print('Hovering on Play')
                button_menu = Button(320, 400, menu_hov_img, 0.7)
            else:
                button_menu = Button(320, 400, menu_img, 0.7)

            screen.blit(header,(50,50))
            screen.blit(text,(235,150))

            pygame.display.update()
            pygame.display.flip()

    pygame.quit()
