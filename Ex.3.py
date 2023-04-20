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
    
    
    def isMouseOn(self):
        mouseX , mouseY=pg.mouse.get_pos()
        if mouseX >= self.x and mouseX <= self.x+self.w and mouseY >= self.y and mouseY <= self.y + self.h:
            return True
        else:
            return False
    def isMouseOff(self):
        mouseX , mouseY=pg.mouse.get_pressed()
        if mouseX == 0 and mouseY == 0:
            return True
        else:
            return False
btn = Button(700,400,80,50) # สร้าง Object จากคลาส Button ขึ้นมา
class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)
    def isMouseOn(self):
        mouseX , mouseY=pg.mouse.get_pos()
        if mouseX >= self.x and mouseX <= self.x+self.w and mouseY >= self.y and mouseY <= self.y + self.h:
            return True
        else:
            return False

class InputnumBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if event.unicode.isnumeric():
                        self.text += event.unicode
                    else:
                        return False
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)
    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)
    def isMouseOn(self):
        mouseX , mouseY=pg.mouse.get_pos()
        if mouseX >= self.x and mouseX <= self.x+self.w and mouseY >= self.y and mouseY <= self.y + self.h:
            return True
        else:
            return False
        
import sys
import pygame as pg

pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))

COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font(None, 32)

input_box1 = InputBox(100, 100, 140, 32) # สร้าง InputBox1
input_box2 = InputBox(100, 200, 140, 32) # สร้าง InputBox2
input_box3 = InputnumBox(100, 300, 140, 32) # สร้าง InputBox3
input_boxes = [input_box1, input_box2, input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
run = True


while run:
    screen.fill((255, 255, 255))
    font = pg.font.Font('freesansbold.ttf', 20  ) # font and fontsize
    btn.draw(screen)
    text = font.render('First name', True, (0,0,250), (250,250,250)) # (text,is smooth?,letter color,background color)
    textRect = text.get_rect() # text size
    textRect.center = (200,70)
    screen.blit(text, textRect)

    text = font.render('Last name', True, (0,0,250), (250,250,250))
    textRect = text.get_rect()
    textRect.center = (200,170)
    screen.blit(text, textRect)

    text = font.render('Age', True, (0,0,250), (250,250,250))
    textRect = text.get_rect()
    textRect.center = (200,270)
    screen.blit(text, textRect)

    text = font.render('Submit', True, (0,0,250), (250,0,0))
    textRect = text.get_rect()
    textRect.center = (740,420)
    screen.blit(text, textRect)


    if btn.isMouseOn():
        if pg.mouse.get_pressed()==(1,0,0):
            font = pg.font.Font('freesansbold.ttf', 20  ) # font and fontsize
            btn.draw(screen)
            text = font.render('Hello '+str(input_box1.text)+' '+str(input_box2.text)+'! You are  '+str(input_box3.text)+' year old.', True, (0,0,250), (250,250,250)) # (text,is smooth?,letter color,background color)
            textRect = text.get_rect() # text size
            textRect.center = (350,400)
            screen.blit(text, textRect)
            

    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้

        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
        
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    pg.time.delay(1)
    pg.display.update()