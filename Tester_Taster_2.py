import pygame
pygame.init()

screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption('Battleship Simulator') 
screen.fill((255,255,255))

color=(69, 237, 212)
red_color=(252, 3, 3)

class Button():
    def __init__(self, color, x, y, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)
        

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x, y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                
                if pygame.mouse.get_pressed()[0] == 1:
                    return True, True

                return True, False

        return False, False

a1=Button(color, 60, 60, 50, 50)


running = True
while running == True:
    pos=pygame.mouse.get_pos()
    
    a1.draw(screen)
    
    if a1.isOver(pos)[0]:
        if a1.isOver(pos)[1]:
            a1=Button(red_color, 60, 60, 50, 50)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    pygame.display.update()

pygame.quit()