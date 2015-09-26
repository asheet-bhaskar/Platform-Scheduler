import pygame,sys
import mysql.connector
from datetime import datetime, timedelta
pygame.init()
# cursor in database
obj = mysql.connector.connect(user='root',password='nano',
                              host='127.0.0.1',database ='sepr')
cursor = obj.cursor()
# dimensions of Canvas
w=1050
h=670
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("Scheduler")
white =(255,255,255)
red = (255,0,0)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)
class Canvas():
    def __init__(self,n,o=4):
        self.n = n
        self.o = o
        '''y=10
        pygame.draw.line(screen,red,(0,y),(1050,y),4)
        pygame.draw.line(screen,red,(0,y+15),(1050,y+15),4)
        pygame.draw.line(screen,red,(0,y+30),(1050,y+30),4)
        pygame.draw.line(screen,red,(0,y+45),(1050,y+45),4)'''

        y1 = 50
        i=1
        t=6
        yadd = 30
        while i<=self.n:
            if i==5 or i==6:
                pygame.draw.line(screen,white,(0,y1),(1050,y1),1)
                pygame.draw.line(screen,black,(0,y1),(1050,y1),10)
                pygame.draw.line(screen,white,(0,y1),(1050,y1),1)
                font  = pygame.font.Font(None , 30)
                s= str(i)
                text = font.render(s,1,(250,0,0))
                screen.blit(text, (10,y1+1))
                i+=1
                y1+=40
            else:
                pygame.draw.line(screen,black,(150,y1),(900,y1),6)
                font  = pygame.font.Font(None , 30)
                s= str(i)
                text = font.render(s,1,(250,0,0))
                screen.blit(text, (160,y1+1))
                i+=1
                y1+=30
                
                
        '''y2 = y1+10
        pygame.draw.line(screen,red,(0,y2),(1050,y2),4)
        pygame.draw.line(screen,red,(0,y2+15),(1050,y2+15),4)
        pygame.draw.line(screen,red,(0,y2+30),(1050,y2+30),4)
        pygame.draw.line(screen,red,(0,y2+45),(1050,y2+45),4)'''

        font  = pygame.font.Font(None , 30)
        s= "Arrival"
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (120,450))
        pygame.draw.rect(screen,(150,150,150),(50,470,250,180))
        s1="Train"
        text1= font.render(s1,1,(250,0,0))
        screen.blit(text1,(80,475))
        s2="Time"
        text2= font.render(s2,1,(250,0,0))
        screen.blit(text2,(210,475))
        pygame.draw.line(screen,red,(50,500),(300,500),1)
        pygame.draw.line(screen,red,(200,470),(200,650),1)
        
        
        ss= "Departure"
        text1 = font.render(ss,1,(250,0,0))
        screen.blit(text1, (420,450))
        pygame.draw.rect(screen,(150,150,150),(350,470,250,180))
        ss1="Train"
        text11= font.render(ss1,1,(250,0,0))
        screen.blit(text11,(380,475))
        ss2="Time"
        text22= font.render(ss2,1,(250,0,0))
        screen.blit(text22,(510,475))
        pygame.draw.line(screen,red,(350,500),(600,500),1)
        pygame.draw.line(screen,red,(500,470),(500,650),1)

        s2= "Warning"
        text2 = font.render(s2,1,(250,0,0))
        screen.blit(text2, (720,450))
        pygame.draw.rect(screen,(150,150,150),(650,470,380,180))
        ss1="Train"
        text11= font.render(ss1,1,(250,0,0))
        screen.blit(text11,(680,475))
        ss2="Time"
        text22= font.render(ss2,1,(250,0,0))
        screen.blit(text22,(810,475))
        pygame.draw.line(screen,red,(650,500),(1030,500),1)
        
def first_avail_plat(tr_type):
    if tr_type == "UP":
        cursor.execute(""" select id,status from platform
                           where id<6
                           order by id desc
                       """)
        my_plat = cursor.fetchall()
        obj.commit()
        
    elif tr_type == "DOWN":
        cursor.execute(""" select id,status from platform
                           where id>5
                           order by id 
                       """)
        my_plat = cursor.fetchall()
        obj.commit()
    x=0
    flag=0
    while x<5 and tr_type =="UP":
        t = my_plat[x]
        if t[1] == 0:
            flag = 1
            if x == 0:
                return 5
            elif x == 1:
                return 4
            elif x==2:
                return 3
            elif x == 3:
                return 2
            elif x == 4:
                return 1
            break
        x+=1
    while x<5 and tr_type =="DOWN":
        t = my_plat[x]
        if t[1] == 0:
            flag = 1
            if x == 0:
                return 6
            elif x == 1:
                return 7
            elif x==2:
                return 8
            elif x == 3:
                return 9
            elif x == 4:
                return 10
            break
        x+=1
    if flag == 0:
        return -1


img = pygame.image.load("234.jpg")
imgx=0
imgy=162
img1 = pygame.image.load("234.jpg")
img1x=0
img1y=162
img2 = pygame.image.load("234.jpg")
img2x=0
img2y=162
img4 = pygame.image.load("234.jpg")
img4x=0
img4y=162
pixmov=2
FPS=20
fpsTime = pygame.time.Clock()
ttype="DOWN"

img6 = pygame.image.load("234.jpg")
img6x=1050
img6y=202
img7 = pygame.image.load("234.jpg")
img7x=1050
img7y=202
img8 = pygame.image.load("234.jpg")
img8x=1050
img8y=202
img9 = pygame.image.load("234.jpg")
img9x=1050
img9y=202
img10 = pygame.image.load("234.jpg")
img10x=1050
img10y=202
#______________________________________________________________________________________________________________________________________________________
count =0
while True:
    screen.fill((255,204,153))
    mycanvas = Canvas(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    cursor.execute(""" select tr_name from train
                           order by id 
                    """)
    tr_names = cursor.fetchall()
    obj.commit()
    cursor.execute(""" select tr_type from train
                           order by id 
                    """)
    tr_type = cursor.fetchall()
    obj.commit()
    cursor.execute(""" select tr_no from train
                           order by id 
                    """)
    tr_no = cursor.fetchall()
    obj.commit()
    cursor.execute(""" select arr_time from train
                           order by id 
                    """)
    arr_time = cursor.fetchall()
    obj.commit()
    cursor.execute(""" select dept_time from train
                           order by id 
                    """)
    dept_time = cursor.fetchall()
    obj.commit()
    now = datetime.now().time()
    d1 = datetime(2014, 9, 10, now.hour, now.minute,now.second)
    font  = pygame.font.Font(None , 80)
    s= str(d1.time())
    text = font.render(s,1,blue)
    screen.blit(text, (800,20))

#________________________________________________________________________________________________________________________________________UP
    if imgx>=0 and imgx<=100:
        imgx+=pixmov
        screen.blit(img,(imgx,imgy))
        font  = pygame.font.Font(None , 30)
        s= "Maru Express"
        s2=str(d1.time())
        text2=font.render(s2,1,white)
        text = font.render(s,1,white)
        screen.blit(text, (imgx+20,imgy-2))
        screen.blit(text, (55,503))
        screen.blit(text2, (202,503))
    if imgx>=100:
        n = first_avail_plat("UP")
        if n==5:
            imgy=162
            p1=n
        elif n==4:
            imgy=132
            p1=n
        elif n==3:
            imgy=102
            p1=n
        elif n==2:
            imgy=72
            p1=n
        elif n==1:
            imgy=42
            p1=n
    if imgx>=100 and imgx<=400:
        imgx+=pixmov
        screen.blit(img,(imgx,imgy))
        font  = pygame.font.Font(None , 30)
        s= "Marudhar Express"
        text = font.render(s,1,white)
        screen.blit(text, (imgx+20,imgy-2))
        s1= "Maru Express"
        s2=str(d1.time())
        text2=font.render(s2,1,white)
        text1 = font.render(s1,1,white)
        screen.blit(text1, (55,503))
        screen.blit(text2, (202,503))
        cont=0
    elif imgx>400 and imgx<405:
        screen.blit(img,(imgx,imgy))
        font  = pygame.font.Font(None , 30)
        s= "Marudhar Express"
        text = font.render(s,1,white)
        screen.blit(text, (imgx+20,imgy-2))
        cont+=1
        s1= "Maru Express"
        s2=str(d1.time())
        text2=font.render(s2,1,white)
        text1 = font.render(s1,1,white)
        screen.blit(text1, (55,503))
        screen.blit(text2, (202,503))
    if count>500 and imgx<800:
        imgx+=pixmov
        screen.blit(img,(imgx,imgy))
        font  = pygame.font.Font(None , 30)
        s= "Marudhar Express"
        text = font.render(s,1,white)
        screen.blit(text, (imgx+20,imgy-2))
        s1= "Maru Express"
        s2=str(d1.time())
        text2=font.render(s2,1,white)
        text1 = font.render(s1,1,white)
        screen.blit(text1, (353,503))
        screen.blit(text2, (502,503))
    if imgx>=800 and imgx<1100:
        imgy=162
        imgx+=pixmov
        screen.blit(img,(imgx,imgy))
        font  = pygame.font.Font(None , 30)
        s= "Marudhar Express"
        text = font.render(s,1,white)
        screen.blit(text, (imgx+20,imgy-2))
        s1= "Maru Express"
        s2=str(d1.time())
        text2=font.render(s2,1,white)
        text1 = font.render(s1,1,white)
        screen.blit(text1, (353,503))
        screen.blit(text2, (502,503))
#_____________________________________________________________________________________________________________________________________DOWN
    if img6x<=1050 and img6x>900:
        img6x-=pixmov
        screen.blit(img6,(img6x,img6y))
        font  = pygame.font.Font(None , 30)
        s= "ABC Express"
        s2=str(d1.time())
        text2=font.render(s2,1,white)
        text = font.render(s,1,white)
        screen.blit(text, (img6x+20,img6y-2))
        screen.blit(text, (55,575))
        screen.blit(text2, (202,575))
        ''' if imgx<=900:
        
        n = first_avail_plat("DOWN")
        if n==6:
            imgy=202
            p1=n
        elif n==7:
            imgy=242
            p1=n
        elif n==8:
            imgy=272
            p1=n
        elif n==9:
            imgy=302
            p1=n
        elif n==10:
            imgy=332
            p1=n'''
    if img6x<=900 and img6x>=400:
        img6x-=pixmov
        screen.blit(img6,(img6x,img6y))
        font  = pygame.font.Font(None , 30)
        s= "ABC Express"
        text = font.render(s,1,white)
        screen.blit(text, (img6x+20,img6y-2))
        s1= "ABC Express"
        s2=str(d1.time())
        text2=font.render(s2,1,white)
        text1 = font.render(s1,1,white)
        screen.blit(text1, (55,575))
        screen.blit(text2, (202,575))
        cont=0
    elif img6x<=400 and img6x>395:
        screen.blit(img6,(img6x,img6y))
        font  = pygame.font.Font(None , 30)
        s= "ABC Express"
        text = font.render(s,1,white)
        screen.blit(text, (img6x+20,img6y-2))
        cont+=1
        s1= "ABC Express"
        s2=str(d1.time())
        text2=font.render(s2,1,white)
        text1 = font.render(s1,1,white)
        screen.blit(text1, (55,575))
        screen.blit(text2, (202,575))
    if count>500 and img6x>250:
        img6x-=pixmov
        screen.blit(img6,(img6x,img6y))
        font  = pygame.font.Font(None , 30)
        s= "ABC Express"
        text = font.render(s,1,white)
        screen.blit(text, (img6x+20,img6y-2))
        s1= "ABC Express"
        s2=str(d1.time())
        text2=font.render(s2,1,white)
        text1 = font.render(s1,1,white)
        screen.blit(text1, (353,575))
        screen.blit(text2, (502,575))
    if img6x<=250 and img6x>=-250 :
        img6x-=pixmov
        screen.blit(img6,(img6x,img6y))
        font  = pygame.font.Font(None , 30)
        s= "ABC Express"
        text = font.render(s,1,white)
        screen.blit(text, (img6x+20,img6y-2))
        s1= "ABC Express"
        s2=str(d1.time())
        text2=font.render(s2,1,white)
        text1 = font.render(s1,1,white)
        screen.blit(text1, (353,575))
        screen.blit(text2, (502,575))
        
            
#_____________________________________________________________________________________________________________________________________            
    if count>300:
        if img1x>=0 and img1x<=100:
            img1x+=pixmov
            screen.blit(img1,(img1x,img1y))
            font  = pygame.font.Font(None , 30)
            s= "Mandor Express"
            text = font.render(s,1,white)
            screen.blit(text, (img1x+20,img1y-2))
            s1= "Mandor Exp"
            s2=str(d1.time())
            text2=font.render(s2,1,white)
            text1 = font.render(s1,1,white)
            screen.blit(text1, (55,520))
            screen.blit(text2, (202,520))
    if img1x>=80:
        img1y=132
    if img1x>=80 and img1x<=400:
        img1x+=pixmov
        screen.blit(img1,(img1x,img1y))
        font  = pygame.font.Font(None , 30)
        s= "Mandor Express"
        text = font.render(s,1,white)
        screen.blit(text, (img1x+20,img1y-2))
        s1= "Mandor Exp"
        s2=str(d1.time())
        text2=font.render(s2,1,white)
        text1 = font.render(s1,1,white)
        screen.blit(text1, (55,520))
        screen.blit(text2, (202,520))
    if img1x>400 and img1x<405:
        screen.blit(img1,(img1x,img1y))
        font  = pygame.font.Font(None , 30)
        s= "Mandor Express"
        text = font.render(s,1,white)
        screen.blit(text, (img1x+20,img1y-2))
        s1= "Mandor Exp"
        s2=str(d1.time())
        text2=font.render(s2,1,white)
        text1 = font.render(s1,1,white)
        screen.blit(text1, (55,520))
        screen.blit(text2, (202,520))
    if count>=840 and img1x<750:
        img1x+=pixmov
        screen.blit(img1,(img1x,img1y))
        font  = pygame.font.Font(None , 30)
        s= "Mandor Express"
        text = font.render(s,1,white)
        screen.blit(text, (img1x+20,img1y-2))
        s1= "Mandor Exp"
        s2=str(d1.time())
        text2=font.render(s2,1,white)
        text1 = font.render(s1,1,white)
        screen.blit(text1, (353,515))
        screen.blit(text2, (502,515))
    if img1x>=750 and img1x<1100:
        img1y=162
        img1x+=pixmov
        screen.blit(img1,(img1x,img1y))
        font  = pygame.font.Font(None , 30)
        s= "Mandor Express"
        text = font.render(s,1,white)
        screen.blit(text, (img1x+20,img1y-2))
        s1= "Mandor Expr"
        s2=str(d1.time())
        text2=font.render(s2,1,white)
        text1 = font.render(s1,1,white)
        screen.blit(text1, (353,515))
        screen.blit(text2, (502,515))
#_______________________________________________________________________________________________________________________________________
    if count>300:
        if img7x<=1050 and img7x>900:
            img7x-=pixmov
            screen.blit(img7,(img7x,img7y))
            font  = pygame.font.Font(None , 30)
            s= "DEF Express"
            s2=str(d1.time())
            text2=font.render(s2,1,white)
            text = font.render(s,1,white)
            screen.blit(text, (img7x+20,img7y-2))
            screen.blit(text, (55,595))
            screen.blit(text2, (202,595))
    if img7x<900:
        img7y=242
    if img7x<=900 and img7x>=400:
        img7x-=pixmov
        screen.blit(img7,(img7x,img7y))
        font  = pygame.font.Font(None , 30)
        s= "DEF Express"
        text = font.render(s,1,white)
        screen.blit(text, (img7x+20,img7y-2))
        s1= "DEF Express"
        s2=str(d1.time())
        text2=font.render(s2,1,white)
        text1 = font.render(s1,1,white)
        screen.blit(text1, (55,595))
        screen.blit(text2, (202,595))
        cont=0
    elif img7x<=400 and img7x>395:
        screen.blit(img7,(img7x,img7y))
        font  = pygame.font.Font(None , 30)
        s= "DEF Express"
        text = font.render(s,1,white)
        screen.blit(text, (img7x+20,img7y-2))
        cont+=1
        s1= "DEF Express"
        s2=str(d1.time())
        text2=font.render(s2,1,white)
        text1 = font.render(s1,1,white)
        screen.blit(text1, (55,575))
        screen.blit(text2, (202,575))
    if count>790 and img7x>150:
        img7x-=pixmov
        screen.blit(img7,(img7x,img7y))
        font  = pygame.font.Font(None , 30)
        s= "DEF Express"
        text = font.render(s,1,white)
        screen.blit(text, (img7x+20,img7y-2))
        s1= "DEF Express"
        s2=str(d1.time())
        text2=font.render(s2,1,white)
        text1 = font.render(s1,1,white)
        screen.blit(text1, (353,575))
        screen.blit(text2, (502,575))
    if img7x<=150:
        img7y=202
    if img7x<=250 and img7x>=-250 :
        img7x-=pixmov
        screen.blit(img7,(img7x,img7y))
        font  = pygame.font.Font(None , 30)
        s= "DEF Express"
        text = font.render(s,1,white)
        screen.blit(text, (img7x+20,img7y-2))
        s1= "ABC Express"
        s2=str(d1.time())
        text2=font.render(s2,1,white)
        text1 = font.render(s1,1,white)
        screen.blit(text1, (353,575))
        screen.blit(text2, (502,575))
       
        

#____________________________________________________________________________________________________________________________________       
    if count>600:
        if img2x>=0 and img2x<=80:
            img2x+=pixmov
            screen.blit(img2,(img2x,img2y))
            font  = pygame.font.Font(None , 30)
            s= "Muri Express"
            text = font.render(s,1,white)
            screen.blit(text, (img2x+20,img2y-2))
            s1= "Muri Exp"
            s2=str(d1.time())
            text2=font.render(s2,1,white)
            text1 = font.render(s1,1,white)
            screen.blit(text1, (53,535))
            screen.blit(text2, (202,535))
    if img2x>=80:
        img2y=102
    if img2x>=80 and img2x<=400:
        img2x+=pixmov
        screen.blit(img2,(img2x,img2y))
        font  = pygame.font.Font(None , 30)
        s= "Muri Express"
        text = font.render(s,1,white)
        screen.blit(text, (img2x+20,img2y-2))
        s1= "Muri Exp"
        s2=str(d1.time())
        text2=font.render(s2,1,white)
        text1 = font.render(s1,1,white)
        screen.blit(text1, (53,535))
        screen.blit(text2, (202,535))
    if img2x>400 and img2x<405:
        screen.blit(img2,(img2x,img2y))
        font  = pygame.font.Font(None , 30)
        s= "Muri Express"
        text = font.render(s,1,white)
        screen.blit(text, (img2x+20,img2y-2))
        s1= "Muri Exp"
        s2=str(d1.time())
        text2=font.render(s2,1,white)
        text1 = font.render(s1,1,white)
        screen.blit(text1, (53,535))
        screen.blit(text2, (202,535))
    if count>=1100 and img2x<750:
        img2x+=pixmov
        screen.blit(img2,(img2x,img2y))
        font  = pygame.font.Font(None , 30)
        s= "Muri Express"
        text = font.render(s,1,white)
        screen.blit(text, (img2x+20,img2y-2))
        s1= "Muri Exp"
        s2=str(d1.time())
        text2=font.render(s2,1,white)
        text1 = font.render(s1,1,white)
        screen.blit(text1, (353,535))
        screen.blit(text2, (502,535))
    if img2x>=750 and img2x<1100:
        img2y=162
        img2x+=pixmov
        screen.blit(img2,(img2x,img2y))
        font  = pygame.font.Font(None , 30)
        s= "Muri Express"
        text = font.render(s,1,white)
        screen.blit(text, (img2x+20,img2y-2))
        s1= "Muri Exp"
        s2=str(d1.time())
        text2=font.render(s2,1,white)
        text1 = font.render(s1,1,white)
        screen.blit(text1, (353,535))
        screen.blit(text2, (502,535))
#____________________________________________________________________________________________________________________________________________
    if count>1200:
        if img4x>=0 and img4x<=100:
            img4x+=pixmov
            screen.blit(img4,(img4x,img4y))
            font  = pygame.font.Font(None , 30)
            s= "Puri Express"
            text = font.render(s,1,white)
            screen.blit(text, (img4x+20,img4y-2))
            s1= "Puri Exp"
            s2=str(d1.time())
            text2=font.render(s2,1,white)
            text1 = font.render(s1,1,white)
            screen.blit(text1, (55,555))
            screen.blit(text2, (202,555))
    if img4x>=80:
        img4y=132
    if img4x>=80 and img4x<=400:
        img4x+=pixmov
        screen.blit(img4,(img4x,img4y))
        font  = pygame.font.Font(None , 30)
        s= "Puri Express"
        text = font.render(s,1,white)
        screen.blit(text, (img4x+20,img4y-2))
        s1= "Puri Exp"
        s2=str(d1.time())
        text2=font.render(s2,1,white)
        text1 = font.render(s1,1,white)
        screen.blit(text1, (55,555))
        screen.blit(text2, (202,555))
    if img4x>400 and img4x<405:
        screen.blit(img4,(img4x,img4y))
        font  = pygame.font.Font(None , 30)
        s= "Puri Express"
        text = font.render(s,1,white)
        screen.blit(text, (img4x+20,img4y-2))
        s1= "Puri Exp"
        s2=str(d1.time())
        text2=font.render(s2,1,white)
        text1 = font.render(s1,1,white)
        screen.blit(text1, (55,555))
        screen.blit(text2, (202,555))
    if count>=1700 and img4x<750:
        img4x+=pixmov
        screen.blit(img4,(img4x,img4y))
        font  = pygame.font.Font(None , 30)
        s= "Puri Express"
        text = font.render(s,1,white)
        screen.blit(text, (img4x+20,img4y-2))
        s1= "Puri Exp"
        s2=str(d1.time())
        text2=font.render(s2,1,white)
        text1 = font.render(s1,1,white)
        screen.blit(text1, (353,555))
        screen.blit(text2, (502,555))
    if img4x>=750 and img4x<1100:
        img4y=162
        img4x+=pixmov
        screen.blit(img4,(img4x,img4y))
        font  = pygame.font.Font(None , 30)
        s= "Puri Express"
        text = font.render(s,1,white)
        screen.blit(text, (img4x+20,img4y-2))
        s1= "Puri Expr"
        s2=str(d1.time())
        text2=font.render(s2,1,white)
        text1 = font.render(s1,1,white)
        screen.blit(text1, (353,555))
        screen.blit(text2, (502,555))
#______________________________________________________________________________________________________________________________________
    if count>1400:
        if img8x<=1050 and img8x>900:
            img8x-=pixmov-1
            screen.blit(img8,(img8x,img8y))
            font  = pygame.font.Font(None , 30)
            s= "Yamuna Bridge P."
            s2=str(d1.time())
            text2=font.render(s2,1,white)
            text = font.render(s,1,white)
            screen.blit(text, (img8x+20,img8y-2))
            screen.blit(text, (55,595))
            screen.blit(text2, (202,595))
    if img8x<900:
        img8y=242
    if img8x<=900 and img8x>=400:
        img8x-=pixmov-1
        screen.blit(img8,(img8x,img8y))
        font  = pygame.font.Font(None , 30)
        s= "Yamuna Bridge P."
        text = font.render(s,1,white)
        screen.blit(text, (img8x+20,img8y-2))
        s1= "Yamuna Bridge "
        s2=str(d1.time())
        text2=font.render(s2,1,white)
        text1 = font.render(s1,1,white)
        screen.blit(text1, (55,595))
        screen.blit(text2, (202,595))
        cont=0
    elif img8x<=400 and img8x>395:
        screen.blit(img8,(img8x,img8y))
        font  = pygame.font.Font(None , 30)
        s= "Yamuna Bridge P."
        text = font.render(s,1,white)
        screen.blit(text, (img8x+20,img8y-2))
        cont+=1
        s1= "Yamuna Bridge "
        s2=str(d1.time())
        text2=font.render(s2,1,white)
        text1 = font.render(s1,1,white)
        screen.blit(text1, (55,575))
        screen.blit(text2, (202,575))
    if count>2200 and img8x>150:
        img8x-=pixmov-1
        screen.blit(img8,(img8x,img8y))
        font  = pygame.font.Font(None , 30)
        s= "Yamuna Bridge P."
        text = font.render(s,1,white)
        screen.blit(text, (img8x+20,img8y-2))
        s1= "Yamuna Bridge "
        s2=str(d1.time())
        text2=font.render(s2,1,white)
        text1 = font.render(s1,1,white)
        screen.blit(text1, (353,575))
        screen.blit(text2, (502,575))
    if img8x<=150:
        img8y=202
    if img8x<=250 and img8x>=-250 :
        img8x-=pixmov-1
        screen.blit(img8,(img8x,img8y))
        font  = pygame.font.Font(None , 30)
        s= "Yamuna Bridge P."
        text = font.render(s,1,white)
        screen.blit(text, (img8x+20,img8y-2))
        s1= "Yamuna Bridge "
        s2=str(d1.time())
        text2=font.render(s2,1,white)
        text1 = font.render(s1,1,white)
        screen.blit(text1, (353,575))
        screen.blit(text2, (502,575))
    if count>1400 and count<1800:
        font = pygame.font.Font(None , 30)
        s="Move Yamuna Bridge P. on plat 6 To   "
        s1="available Outer Track"
        text= font.render(s,1,red)
        text1= font.render(s1,1,red)
        screen.blit(text,(653,502))
        screen.blit(text1,(653,525))
#___________________________________________________________________________________________________________________________________________
    if count >1650:
        
        
        if img9x<=1050 and img9x>-250:
            
            img9x-=(pixmov+2)
            screen.blit(img9,(img9x,img9y))
            font  = pygame.font.Font(None , 30)
            s= "PQR SF Exp"
            s2=str(d1.time())
            text2=font.render(s2,1,white)
            text = font.render(s,1,white)
            screen.blit(text, (img9x+20,img9y-2))
            screen.blit(text, (353,615))
            screen.blit(text2, (502,615))
            
        
    
    
    
    
        
    print count  
    count+=1
    pygame.display.update()
    fpsTime.tick(100)
    
