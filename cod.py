from pygame import *

#игровая сцена:
back = (200, 255, 255) #цвет фона (background)
window = display.set_mode((600, 500))
window.fill(back)
clock = time.Clock()

#флаги, отвечающие за состояние игры
game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
 
    display.update()
    clock.tick(60)


