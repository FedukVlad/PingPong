from pygame import *
from random import randint

font.init()
fon = font.Font(None, 24)
lose_R = fon.render("Right Player LOSE", True, (180, 0, 0))
lose_L = fon.render("Left Player LOSE", True, (180, 0, 0))
window = display.set_mode((720, 480))
display.set_caption("PingPong")
background = transform.scale(image.load("background.jpg"), (720, 480))

class GameSprite(sprite.Sprite):
    def __init__(self, sp_image, x, y, speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(sp_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def create(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_R(self):
        keys = key.get_pressed()
        if (keys[K_w] or keys[K_d]) and self.rect.y > 5:
           self.rect.y -= self.speed
        if (keys[K_s] or keys[K_a]) and self.rect.y< 720 - 80:
           self.rect.y += self.speed
    
    def update_L(self):
        keys = key.get_pressed()
        if (keys[K_UP] or keys[K_RIGHT]) and self.rect.y > 5:
           self.rect.y -= self.speed
        if (keys[K_DOWN] or keys[K_LEFT]) and self.rect.y< 720 - 80:
           self.rect.y += self.speed

racket_R = Player("racket.png", 25, 320, 3, 10, 80)
racket_L = Player("racket.png", 695, 320, 3, 10, 80)
ball = GameSprite("tenis_ball.png", 335, 335, 1, 50, 50)

rand = randint(0, 3)
speed_y = 1
speed_x = 2
win_height = 480
win_width = 720

finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:   
        window.blit(background, (0, 0))
        racket_R.create()
        racket_L.create()
        ball.create()
        racket_R.update_R()
        racket_L.update_L()

        if rand == 0:
            ball.rect.y += speed_y
            ball.rect.x += speed_x
        elif rand == 1:
            ball.rect.y += speed_y
            ball.rect.x -= speed_x
        elif rand == 2:
            ball.rect.y -= speed_y
            ball.rect.x += speed_x
        elif rand == 3:
            ball.rect.y -= speed_y
            ball.rect.x -= speed_x

        if sprite.collide_rect(racket_R, ball) or sprite.collide_rect(racket_L, ball):
            speed_x *= -1
        elif ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1
        elif ball.rect.x < 0:
            window.blit(lose_R, (5, 5))
            finish = True
        elif ball.rect.x > win_width:
            window.blit(lose_L, (5, 5))
            finish = True
            
    else:
        finish = False
        ball.rect.x = 335
        ball.rect.y = 335
        time.delay(2000) 
    display.update()
    time.delay(5)