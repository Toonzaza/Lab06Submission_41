# class Rectangle:
#     def __init__(self,x=0,y=0,w=0,h=0):
#         self.x = x # Position X
#         self.y = y # Position Y
#         self.w = w # Width
#         self.h = h # Height
#         self.r = 250
#         self.g = 0
#         self.b = 0
#     def draw(self,screen):
#         pg.draw.rect(screen,(self.r,self.g,self.b),(self.x,self.y,self.w,self.h))
# class Button(Rectangle):
#     def __init__(self, x=0, y=0, w=0, h=0):
#         Rectangle.__init__(self, x, y, w, h)
# import sys 
# import pygame as pg

# pg.init()
# run = True
# win_x, win_y = 800, 480
# screen = pg.display.set_mode((win_x, win_y))
# btn = Button(20,20,100,100) # สร้าง Object จากคลาส Button ขึ้นมา

# while(run):
#     screen.fill((255, 255, 255))
#     btn.r = 250
#     btn.g = 0
#     btn.b = 0
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#         if event.type == pg.KEYDOWN and event.key == pg.K_d: #ปุ่มถูกกดลงและเป็นปุ่ม D
#             btn.x +=10
#         if event.type == pg.KEYDOWN and event.key == pg.K_a: #ปุ่มถูกกดลงและเป็นปุ่ม D
#             btn.x -=10
#         if event.type == pg.KEYDOWN and event.key == pg.K_w: #ปุ่มถูกกดลงและเป็นปุ่ม D
#             btn.y -=10
#         if event.type == pg.KEYDOWN and event.key == pg.K_s: #ปุ่มถูกกดลงและเป็นปุ่ม D
#             btn.y +=10
#     btn.draw(screen)       
#     pg.display.update()
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#             run = False







class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.r = 250
        self.g = 0
        self.b = 0
    def draw(self,screen):
        pg.draw.rect(screen,(self.r,self.g,self.b),(self.x,self.y,self.w,self.h))
class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
import sys 
import pygame as pg
import time
pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,100,100) # สร้าง Object จากคลาส Button ขึ้นมา

status_w = False
status_a = False
status_s = False
status_d = False

while(1):
    screen.fill((255, 255, 255))
    btn.r = 250
    btn.g = 0
    btn.b = 0
    # status_w = False
    # status_a = False
    # status_s = False
    # status_d = False
    if status_w :
        btn.y -= 1
        pg.time.delay(2)
    if status_a :
        btn.x -= 1
        pg.time.delay(2)
    if status_s :
        btn.y += 1
        pg.time.delay(2)
    if status_d :
        btn.x +=1
        pg.time.delay(2)

    # pg.display.update()
    # pg.time.delay(2)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.KEYDOWN and event.key == pg.K_w: #ปุ่มถูกกดลงและเป็นปุ่ม D
            status_w = True
            print("Key w down")
        if event.type == pg.KEYUP and event.key == pg.K_w: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            print("Key w up")
            status_w= False


        if event.type == pg.KEYDOWN and event.key == pg.K_a: #ปุ่มถูกกดลงและเป็นปุ่ม D
            status_a = True
            print("Key a down")
        if event.type == pg.KEYUP and event.key == pg.K_a: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            print("Key a up")
            status_a = False


        if event.type == pg.KEYDOWN and event.key == pg.K_s: #ปุ่มถูกกดลงและเป็นปุ่ม D
            status_s = True
            print("Key s down")
        if event.type == pg.KEYUP and event.key == pg.K_s: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            print("Key s up")
            status_s = False

        if event.type == pg.KEYDOWN and event.key == pg.K_d: #ปุ่มถูกกดลงและเป็นปุ่ม D
            status_d = True
            print("Key d down")
        if event.type == pg.KEYUP and event.key == pg.K_d: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            print("Key d up")
            status_d = False

    btn.draw(screen)       
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
