import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'
import pygame
from pygame.locals import *
import pygame.key
import random


pygame.init()

start = False
si = True
jhp = 100
grounding = True
x = 0
y = 0
gx = 0
ex = 150
ey = 100
px = 0
py = 0
flash = 6
bulleting = False
proj_mimage = pygame.image.load("projectile.png")
proj_image = pygame.image.load("projectile.png")
enemyspr = pygame.image.load("Enemy.png")
font = pygame.font.SysFont("Roboto", 30)
font_large = pygame.font.SysFont("Roboto", 50)
    
#setup
screen_info = pygame.display.Info()
width = screen_info.current_w
height = 350
p_sprite = "player_right.png"

#colors
black = (0, 0, 0)
white = (255, 255, 255)


screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
fps = pygame.time.Clock()
screen.fill(black)
        
class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(p_sprite)
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, 0)
        self.rect.move_ip(0, 0)
    def update(self):
        self.rect.center = (x, 320)
        self.image = pygame.image.load(p_sprite)
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.w = 10
        self.rect.h = 1
        self.rect.center = (0, 0)
        self.rect.move_ip(0, 0)
    def update(self):
        self.rect.center = (ex, ey)
        self.image = enemyspr
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
class proj(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("projectile.png")
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.rect.move_ip(0, 0)
    def update(self):
        self.rect.center = (px, py)
        self.image = proj_image
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
class ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Ground.png")
        self.rect = self.image.get_rect()
        self.rect.center = (0, 320)
        self.rect.move_ip(0, 0)
    def update(self):
        self.rect.center = (gx, 320)
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        

        

tg = ground()
te = enemy()
tp = player()
tpr = proj()
ed = "left"
edv = "down"
pd = "r"
level = 1
t = 0

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            
    keys = pygame.key.get_pressed()
    
    
    if start == False:
        if not(keys[K_e]):
            title = font_large.render("TANK GAME", True, white)
            screen.blit(title, (125, 100))
            start_b = font.render("press (e) to start", True, white)
            screen.blit(start_b, (150, 200))
        else:
            title = font_large.render("START", True, white)
            screen.blit(title, (125, 100))
            start = True
        
    else:   
    
        
        
    #enemy movement VVV
        if ed == "left":
            ex += level
            if random.randint(0, 30) == 15:
                ed = "right"
        if ed == "right":
            ex = ex - level
            if random.randint(0, 30) == 15:
                ed = "left"
        if ex > 400:
            ed = "right"
        if ex < 25:
            ed = "left"
    
            
        if edv == "up":
            ey = ey - (level)
            if random.randint(0, 30) == 15:
                edv = "down"
        if edv == "down":
            ey += (level)
            if random.randint(0, 30) == 15:
                edv = "up"
        if ey > 100:
            edv = "up"
        if ey < 1:
            edv = "down"
    #enemy movement ^^^
    
                
        keys = pygame.key.get_pressed()
        
    
        
        if keys[K_SPACE]:
            if bulleting == False:
                bulleting = True
                if keys[K_RIGHT] and keys[K_UP]:
                    pd = "ur"
                    proj_image = pygame.transform.rotate(proj_mimage, -45)
                else: 
                    if keys[K_RIGHT] and not(keys[K_UP]):
                        pd = "r"
                        proj_image = pygame.transform.rotate(proj_mimage, -90)
                    else:   
                        if keys[K_UP]:
                            pd = "u"
                            proj_image = pygame.transform.rotate(proj_mimage, 0)
                if keys[K_LEFT] and keys[K_UP]:
                    pd = "ul"
                    proj_image = pygame.transform.rotate(proj_mimage, 45)
                else:
                    if keys[K_LEFT]:
                        pd = "l"
                        proj_image = pygame.transform.rotate(proj_mimage, 90)
        y = 320
        if bulleting:
            if pd == "u":
                py = py - 10
            if pd == "r":
                px = px + 10
            if pd == "l":
                px = px - 10
            if pd == "ur":
                px = px + 10
                py = py - 10
            if pd == "ul":
                px = px - 10
                py = py - 10
            if py < 2 or px > 500 or px < 1:
                bulleting = False
                if pd == "ur":
                    py = y - 50
                else:
                    py = y
                if pd == "ul":
                    px = x - 20
                else:
                    px = x
        else:
            proj_image = pygame.transform.rotate(proj_mimage, 90)
            py = y
            px = x
     
        if grounding:
            gx += 200
            if gx > 500:
                gx = 0
                grounding = False
        
        grounding = True
    
        #sprite
    
        if keys[K_d]:
            x += 2
            p_sprite = "player_right.png"
            
        if keys[K_a]:
            x = x - 2
            p_sprite = "player_left.png"
            
        if keys[K_RIGHT]:
            p_sprite = "player_right.png"
            
        if keys[K_LEFT]:
            p_sprite = "player_left.png"
            
        if keys[K_UP] and keys[K_RIGHT]:
            p_sprite = "player_ur.png"
            
        else:
            if keys[K_UP] and keys[K_LEFT]:
                p_sprite = "player_ul.png"
            else:
                if keys[K_UP]:
                    p_sprite = "pu.png"
                    
        
    
        if pygame.sprite.collide_rect(te, tpr):
            flash = 0
            jhp = jhp - 0.05
        else:
            if level > 3 and jhp < 100:
                jhp += 0.001 * level
        if jhp < 1:
            px = 0
            py = 0
            level += 1
            jhp = 100
    
        if flash < 5:
            if si:
                screen.fill(white)
                si = False
            else:
                if si == False:
                    screen.fill(black)
                    si = True
            flash += 1
        else:
            screen.fill(black)
        
    
    
        
    
            
        y = 300
        
        tg.update()
        tg.draw(screen)
        tpr.update()
        tpr.draw(screen)
        te.update()
        te.draw(screen)
        tp.update()
        tp.draw(screen)
        jethpt = font.render("Jet HP   " + str(jhp), True, white)
        lvlt = font.render("lvl   " + str(level), True, white)
        screen.blit(jethpt, (320, 20))
        screen.blit(lvlt, (25, 20))
        
    pygame.display.update()