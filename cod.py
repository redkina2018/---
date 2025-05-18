from pygame import *
from random import *

#необходимые классы
class GameSprite(sprite.Sprite):
    def __init__(self,pl_image,pl_y,pl_x,pl_speed,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(pl_image),(size_x,size_y))
        self.speed = pl_speed
        self.rect =self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y
    def show_pl(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def move_l(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x >= 1:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x <= 634:
            self.rect.x += self.speed

#игровая сцена:
back = (200, 255, 255) #цвет фона (background)
window = display.set_mode((600, 500))
window.fill(back)
clock = time.Clock()

#флаги, отвечающие за состояние игры
game = True
finish = False

#ля перемещения мяча

speed_x = randint(1,2)
if speed_x ==1:
    speed_x =3
else: 
    speed_x = -3
speed_y = -3
#создаю спрайты ракеток и мяча
racket1 = Player('platform.png',200,10,5,50,100)
ball = GameSprite('ball.png',200,250,3,50,50)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        racket1.move_l()
        #racket2.move_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y


        if ball.rect.y < 0 or ball.rect.y > 450:
            speed_y *= -1.05
        '''if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            speed_x*=-1'''


    racket1.show_pl()
    ball.show_pl()
    display.update()
    clock.tick(60)




