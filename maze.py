#створи гру "Лабіринт"!
from pygame import *
import pygame_menu

mixer.init()
font.init()
init()

WIDTH = 700
HEIGHT = 500
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Лабіринт")
clock = time.Clock()
mixer.music.load("jungles.ogg")
mixer.music.play
mixer.music.set_volume(1)
#задай фон сцени
win_sound = mixer.Sound("money.ogg")
kick_sound = mixer.Sound("kick.ogg")

font1 = font.SysFont("Imapct", 50)
result = font1.render("", True, (255,0,0))
class GameSprite(sprite.Sprite):
    def __init__(self, image_name, x, y, width, height):
        super().__init__()
        self.img = transform.scale(image.load(image_name), (width, height))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
    
        

        def draw(self):
            window.blit(self.imgm, self.rect)

class Player(GameSprite):
    def __init__(self):
        super().__init__("hero.png", 200, 200, 75, 75)
        self.speed = 5
        self.hp = 100

    def update (self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect. ax > 0:
            self.rect.x -= self.speed
        if keys [K_RIGHT] and self.rect.x < WIDTH - self.width:
            self.rect.x -= self.speed
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[k_DOWM] and self.rect.y <HEIGTH - self.height:
            self.rect.y += self.speed
class Enemy(GameSprite):
    def __init__ (self, x, y):
        super().__init__("cyborg.png", x, y, 75, 75)
        self.speed = 3
        self.direction = "left"

    def update(self):
        if self.rect.x <= WIDTH - 300:
            self.direction = "right"
        if self.rect.x >= WIDTH - 100:
            self.direction = "left"
        
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
            
    

class Wall(sprite.Sprite):
    def __init__(self, x, y, width, height, color = (255, 113, 13)):
        super().__init__()
        self.img = Surface((width, height))
        self.rect = self.img.get_rect()
        self.img.fill(color)
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
        
class Treasure(GameSprite):
    def __init__(self):
        super(). __init__("treasure.png", WIDTH - 120, HEIGHT - 100, 75, 75)


    def draw(self):
        window.blit(self.img, self.rect)
        
        
bg_image  = transform.scale(image.load("background.jpg"), (WIDTH, HEIGHT))
player = Player()
cyborg = Enemy(WIDTH - 150, HEIGHT - 200)
gold = Treasure()

wall1 = Wall(x = 50, y = 50, width = 20, height = 200)
wall2 = Wall(x = 200, y = 300, width = 300, height = 20)
walls = [wall1, wall2]
#створи 2 спрайти та розмісти їх на 
def start_game():
    global game, run
    game = True
    run = True


menu = pygame_menu.Menu("Лабіринт", 400, 300, theme = pygame_menu.themes.THEME_BLUE )
menu.add.button("Грати", start_game)
menu.add.button("Вихід", pygame_menu.events.EXIT)

menu.mainloop(window)

player = Player()
cyborg = Enemy(350, 300)
wall1 = Wall(x = 50, y = 50, width = 30,heigth = 200)
run = Falseл
game = False
clock = time.Clock()
FPS = 60
finish = False
while run:


    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type ==KEYDOWN:
            if e.key == K_ESCAPE:
                menu.enable()
                menu.mainloop(window)
    player.update
    for w in walls:
        w.draw()
        if sprite.collide_rect(player, w):
            result = font1.render("Ти програв!", True, (255,0,0))
            finish = True
            kick_sound.play()

        playe.draw()
        cyborg.draw()
        gold.draw()
    else:
        window.blit(result, (200, 200))
    display.update()
    clock.tick(FPS)
#оброби подію «клік за кнопкою "Закрити вікно"»