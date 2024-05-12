import pygame
pygame.init()

rotation_angle = 0
p1_ship_not_placed=True
p2_ship_not_placed=True

col = 'black'

'''button_color = (90, 90, 90)
hover_color = (130, 130, 130)'''

scr_width = 700
scr_height = 1200
screen = pygame.display.set_mode((scr_height, scr_width))

cube_size = 50
grid_size = 10

font = pygame.font.Font('Zector.ttf', 25)
fonta = pygame.font.Font('Zector.ttf',40)


show_img = False
#hover=False

waiting_img=pygame.image.load('wait.jpg')
ship_a = pygame.image.load('shipa.jpg').convert()
ship_b = pygame.image.load('shipb.jpg').convert()
ship_c = pygame.image.load('shipc.jpg').convert()
ship_d = pygame.image.load('shipd.jpg').convert()

confirm_btn_press_cnt=0
confirm_img = pygame.image.load('Confirm_button_Img.jpg').convert_alpha()
confirm_hov_img = pygame.image.load('Hov_confirm_Image.jpg').convert_alpha()

# Confirm button
#confirm_btn = pygame.Rect(990, 3, 100, 50)
#btn1 = pygame.Rect(556, 563, 104, 54)

p1_ship_loca = []
p2_ship_loca = []

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

class drag_obj:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = image.get_rect()
        self.rect.topleft = (x, y)
        self.dragging = False
        self.rotation_angle = 0

    def rotate(self):
        # Rotate the image by 90 degrees to the right
        self.rotation_angle = (self.rotation_angle + 90) % 360
        self.image = pygame.transform.rotate(self.image, -90)  # Negative angle to rotate right

    def draw(self):
        screen.blit(self.image, self.rect.topleft)

    def update(self):
        if self.dragging:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            snap_x = (mouse_x // grid_size) * grid_size +1 
            snap_y = (mouse_y // grid_size) * grid_size +1
            self.rect.topleft = (snap_x, snap_y)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.dragging = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # Right-click
            if self.rect.collidepoint(event.pos):
                self.rotate()


text=fonta.render('Hold and drag to insert ships!',True,'black')
a=font.render('A',True,'black')
b=font.render('B',True,'black')
c=font.render('C',True,'black')
d=font.render('D',True,'black')
e=font.render('E',True,'black')
f=font.render('F',True,'black')
g=font.render('G',True,'black')
h=font.render('H',True,'black')
i=font.render('I',True,'black')
j=font.render('J',True,'black')

a1=font.render('1',True,'black')
a2=font.render('2',True,'black')
a3=font.render('3',True,'black')
a4=font.render('4',True,'black')
a5=font.render('5',True,'black')
a6=font.render('6',True,'black')
a7=font.render('7',True,'black')
a8=font.render('8',True,'black')
a9=font.render('9',True,'black')
a10=font.render('10',True,'black')



objects_p1 = [drag_obj(87, 625, ship_a),
              drag_obj(952-15, 625, ship_a),
              drag_obj(275-25, 625, ship_b),
              drag_obj(383-25, 625, ship_b),
              drag_obj(493-25, 625, ship_c),
              drag_obj(753-25,625,ship_d)
              ]

objects_p2 = [drag_obj(87, 625, ship_a),
              drag_obj(952-15, 625, ship_a),
              drag_obj(275-25, 625, ship_b),
              drag_obj(383-25, 625, ship_b),
              drag_obj(493-25, 625, ship_c),
              drag_obj(753-25,625,ship_d)
              ]

# Create a list to store the coordinates of the rectangles
rectangle_coordinates_list = []
rectangle_coordinates_list1 = []

confirm_btn = Button(990, 3, confirm_img, 0.5)

running = True
while running:
    screen.fill('White')
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        for obj in objects_p1:
            obj.handle_event(event)
        for obj in objects_p2:
            obj.handle_event(event)
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if confirm_btn.draw()[0]:
                show_img = True
                print('Confirm Button Clicked')
                confirm_btn_press_cnt+=1
                # Create a list to store the coordinates of the current set of rectangles
                if p1_ship_not_placed:
                                
                    current_rectangles = []
                    # Iterate through the objects_p1 and get their coordinates in the specified order
                    for obj in objects_p1:
                        topleft = (obj.rect.topleft[0]-1,obj.rect.topleft[1]-1)
                        topright = (obj.rect.topright[0]-1, obj.rect.topleft[1]-1)
                        bottomleft = (obj.rect.topleft[0]-1, obj.rect.bottomleft[1]-1)
                        bottomright = (obj.rect.bottomright[0]-1,obj.rect.bottomright[1]-1)
                        current_rectangles.append([topleft, topright, bottomleft, bottomright])
                    # Append the current set of coordinates to the main list
                    rectangle_coordinates_list.append(current_rectangles)
                    p1_ship_not_placed=False

                else:
                    current_rectangles1 = []
                    # Iterate through the objects_p1 and get their coordinates in the specified order
                    for obj in objects_p2:
                        topleft = (obj.rect.topleft[0]-1,obj.rect.topleft[1]-1)
                        topright = (obj.rect.topright[0]-1, obj.rect.topleft[1]-1)
                        bottomleft = (obj.rect.topleft[0]-1, obj.rect.bottomleft[1]-1)
                        bottomright = (obj.rect.bottomright[0]-1,obj.rect.bottomright[1]-1)
                        current_rectangles1.append([topleft, topright, bottomleft, bottomright])
                    # Append the current set of coordinates to the main list
                    rectangle_coordinates_list1.append(current_rectangles1)
                    p2_ship_not_placed=False

    if confirm_btn.draw()[1]:
        #print('Hovering on Play')
        confirm_btn = Button(990, 3, confirm_hov_img, 0.5)
    else:
        confirm_btn = Button(990, 3, confirm_img, 0.5)
    
    if confirm_btn_press_cnt ==3:
        running=False
    
    spacing = 564
    txt_spacing = 40
    # text
    screen.blit(text,(300,10))
    screen.blit(a,(txt_spacing,74))
    screen.blit(b,(txt_spacing,74+cube_size))
    screen.blit(c,(txt_spacing,74+(2*cube_size)))
    screen.blit(d,(txt_spacing,74+(3*cube_size)))
    screen.blit(e,(txt_spacing,74+(4*cube_size)))
    screen.blit(f,(txt_spacing,74+(5*cube_size)))
    screen.blit(g,(txt_spacing,74+(6*cube_size)))
    screen.blit(h,(txt_spacing,74+(7*cube_size)))
    screen.blit(i,(txt_spacing,74+(8*cube_size)))
    screen.blit(j,(txt_spacing,74+(9*cube_size)))

    screen.blit(a1,(78,spacing))
    screen.blit(a2,(78+cube_size,spacing))
    screen.blit(a3,(78+(2*cube_size),spacing))
    screen.blit(a4,(78+(3*cube_size),spacing))
    screen.blit(a5,(78+(4*cube_size),spacing))
    screen.blit(a6,(78+(5*cube_size),spacing))
    screen.blit(a7,(78+(6*cube_size),spacing))
    screen.blit(a8,(78+(7*cube_size),spacing))
    screen.blit(a9,(78+(8*cube_size),spacing))
    screen.blit(a10,(76+(9*cube_size),spacing))
    
    #text2 
    txt_spacing=txt_spacing+40
    
    screen.blit(a,(txt_spacing+552,72))
    screen.blit(b,(txt_spacing+552,72+cube_size))
    screen.blit(c,(txt_spacing+552,72+(2*cube_size)))
    screen.blit(d,(txt_spacing+552,72+(3*cube_size)))
    screen.blit(e,(txt_spacing+552,72+(4*cube_size)))
    screen.blit(f,(txt_spacing+552,72+(5*cube_size)))
    screen.blit(g,(txt_spacing+552,72+(6*cube_size)))
    screen.blit(h,(txt_spacing+552,72+(7*cube_size)))
    screen.blit(i,(txt_spacing+552,72+(8*cube_size)))
    screen.blit(j,(txt_spacing+552,72+(9*cube_size)))

    screen.blit(a1,(78+40+552,spacing))
    screen.blit(a2,(78+40+cube_size+552,spacing))
    screen.blit(a3,(78+40+(2*cube_size)+552,spacing))
    screen.blit(a4,(78+40+(3*cube_size)+552,spacing))
    screen.blit(a5,(78+40+(4*cube_size)+552,spacing))
    screen.blit(a6,(78+40+(5*cube_size)+552,spacing))
    screen.blit(a7,(78+40+(6*cube_size)+552,spacing))
    screen.blit(a8,(78+40+(7*cube_size)+552,spacing))
    screen.blit(a9,(78+40+(8*cube_size)+552,spacing))
    screen.blit(a10,(72+40+(9*cube_size)+552,spacing))

    # ... (your other drawing code)

    # grid
    for x in range(1, grid_size + 2):
        pygame.draw.line(screen, col, (60, 10 + x * cube_size), (560, 10 + x * cube_size), 2)
        pygame.draw.line(screen, col, (10 + x * cube_size, 60), (10 + x * cube_size, 560), 2)

    # grid2
    for x in range(1, grid_size + 2):
        pygame.draw.line(screen, col, (650, 10 + x * cube_size), (1150, 10 + x * cube_size), 2)
        pygame.draw.line(screen, col, (590 + 10 + x * cube_size, 60), (590 + 10 + x * cube_size, 560), 2)
    

    if p1_ship_not_placed:
            
        for obj in objects_p1:
            obj.update()
            obj.draw()
    else:
        for obj1 in objects_p2:
            obj1.update()
            obj1.draw()

    if show_img:
        screen.blit(waiting_img, (60, 60))

    if confirm_btn_press_cnt>=2:
        screen.blit(waiting_img,(650,60))

    # battleship toggler
    pygame.draw.line(screen, col, (82, 620), (1090, 620), 2)
    pygame.draw.line(screen, col, (82, 680), (1090, 680), 2)
    
    pygame.draw.line(screen, col, (82, 620), (82, 680), 2)
    pygame.draw.line(screen, col, (268-25, 620), (268-25, 680), 2)
    pygame.draw.line(screen, col, (378-25, 620), (378-25, 680), 2)
    pygame.draw.line(screen, col, (488-25, 620), (488-25, 680), 2)
    pygame.draw.line(screen, col, (747-25, 620), (747-25, 680), 2)
    pygame.draw.line(screen, col, (957-25, 620), (957-25, 680), 2)
    pygame.draw.line(screen, col, (1090, 620), (1090, 680), 2)

    pygame.display.update()
    pygame.display.flip()

for i in rectangle_coordinates_list:
    for j in i:
        p1_ship_loca.append(j)

for i in rectangle_coordinates_list1:
    for j in i:
        p2_ship_loca.append(j)

pygame.quit()