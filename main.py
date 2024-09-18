import pygame 
import numpy as np 
import random 

pygame.init() 

screen_width = 900 
screen_height = 600 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_icon(pygame.image.load('./assets/tank.png'))
pygame.display.set_caption('Tankie')

bg = pygame.image.load('./assets/bg-white.jpg')
font = pygame.font.SysFont('Arial', 20) 




tank_size = 50 
my_tank_img = pygame.transform.scale(pygame.image.load('./assets/tank.png'), (tank_size, tank_size))
bullet_size = 20
my_bullet_img = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('./assets/tank.png'), (bullet_size, bullet_size)), 90)

start_pos_x = (screen_width - tank_size) / 2
start_pos_y = (screen_height - tank_size) / 2



class Tank:
    global tank_posx, tank_posy, tank_direction

    def __init__(self, color, size, posx, posy, speed): 
        self.color = color 
        self.size = size 
        self.posx = posx 
        self.posy = posy 
        self.speed = speed 
        if color == 'green': 
            self.img = my_tank_img

    def draw(self): 
        screen.blit(self.img, (self.posx, self.posy))

    def move(self, direction): 
        if direction == 'up' and self.posy - self.speed > 0: 
            self.posy -= self.speed
            self.img = pygame.transform.rotate(my_tank_img, 0)
        elif direction == 'down' and self.posy + self.speed + self.size < screen_height: 
            self.posy += self.speed
            self.img = pygame.transform.rotate(my_tank_img, 180)
        elif direction == 'right' and self.posx + self.speed + self.size < screen_width: 
            self.posx += self.speed
            self.img = pygame.transform.rotate(my_tank_img, 270)
        elif direction == 'left' and self.posx - self.speed > 0: 
            self.posx -= self.speed
            self.img = pygame.transform.rotate(my_tank_img, 90)

        tank_posx = self.posx
        tank_posy = self.posy
        tank_direction = direction

my_tank = Tank('green', 50, start_pos_x, start_pos_y, 5)



class Attack: 
    def __init__(self, color, img, posx, posy, direction, speed): 
        self.color = color 
        self.img = img
        self.posx = posx 
        self.posy = posy 
        self.direction = direction 
        self.speed = speed 
        self.fire = False

    def draw(self): 
        screen.blit(self.img, (self.posx, self.posy))

    def update_state(self): 
        self.posx = tank_posx + tank_size / 2 
        self.posy = tank_posy + tank_size / 2 
        self.direction = tank_direction 

    def active(self): 
        if self.direction == 'up' and self.posy - self.speed > 0: 
            self.posy -= self.speed
            self.img = pygame.transform.rotate(my_tank_img, 0)
            self.draw()
        elif self.direction == 'down' and self.posy + self.speed + self.size < screen_height: 
            self.posy += self.speed
            self.img = pygame.transform.rotate(my_tank_img, 180)
            self.draw()
        elif self.direction == 'right' and self.posx + self.speed + self.size < screen_width: 
            self.posx += self.speed
            self.img = pygame.transform.rotate(my_tank_img, 270)
            self.draw()
        elif self.direction == 'left' and self.posx - self.speed > 0: 
            self.posx -= self.speed
            self.img = pygame.transform.rotate(my_tank_img, 90)
            self.draw()
        # else: 
        #     bullets.remove(self)

bullets = []





def main(): 
    running = True
    playing = True
    FPS = 60 
    clock = pygame.time.Clock()

    def draw_screen(): 
        screen.blit(bg, (0,0)) 
        my_tank.draw()
        for bullet in bullets: 
            bullet.active()

        pygame.display.update()

    while running: 
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]: 
            playing = not playing
        if keys[pygame.K_UP]: 
            my_tank.move('up')
        if keys[pygame.K_DOWN]: 
            my_tank.move('down')
        if keys[pygame.K_RIGHT]: 
            my_tank.move('right')
        if keys[pygame.K_LEFT]: 
            my_tank.move('left')
        # if keys[pygame.K_x]: 
        #     bullet = Attack('green', my_bullet_img, 0, 0, 'up', 20)
        #     bullets.append(bullet)
        #     print(len(np.unique(bullets)))
            

        if playing: draw_screen()
            

main()




