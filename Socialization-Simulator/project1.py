import pygame, sys, random, time
import students
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 1000
WINDOWHEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('자구')
basicFont0 = pygame.font.Font('H2GTRE.ttf', 20)
basicFont4 = pygame.font.Font('H2GTRE.ttf', 30)
basicFont1 = pygame.font.Font('H2GTRE.ttf', 40)
basicFont2 = pygame.font.Font('H2GTRE.ttf', 50)
basicFont3 = pygame.font.Font('H2GTRE.ttf', 120)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (66, 108, 188)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)

SPEED = 50
Bookheight = 156
Bookwidth = 281
Book2height = 110
Book2width = 244
Book = pygame.image.load('Book3.png')
Bookimage = pygame.transform.scale(Book, (Bookwidth, Bookheight))
Book2 = pygame.image.load('Book.png')
Book2image = pygame.transform.scale(Book2, (Book2width, Book2height))
bookleft = WINDOWWIDTH/2 - Bookwidth/2
booktop = WINDOWHEIGHT/3*2 - Bookheight/2 +50
book2left = WINDOWWIDTH/2 - Book2width/2
book2top = WINDOWHEIGHT/3*2 - Book2height/2 +50
bookplace = (bookleft, booktop)
book2place = (book2left, book2top)
Calheight = 150
Calwidth = 150
Cal2height = 180
Cal2width = 180
Cal = pygame.image.load('Cal.png')
Calimage = pygame.transform.scale(Cal, (Calwidth, Calheight))
Cal2 = pygame.image.load('Cal2.png')
Cal2image = pygame.transform.scale(Cal2, (Cal2width, Cal2height))
calleft = WINDOWWIDTH/4 - Calwidth/2 + 100
caltop = WINDOWHEIGHT/5*2 - Calheight/2 + 80
cal2left = WINDOWWIDTH/4 - Cal2width/2 + 100
cal2top = WINDOWHEIGHT/5*2 - Cal2height/2 + 80
calplace = (calleft, caltop)
cal2place = (cal2left, cal2top)
Eventhappenheight = 270
Eventhappenwidth = 250
Eventhappen = pygame.image.load('Eventhappen.png')
Eventhappenimage = pygame.transform.scale(Eventhappen, (Eventhappenwidth, Eventhappenheight))
eventhappenleft = WINDOWWIDTH/7 - Eventhappenwidth/2
eventhappentop = WINDOWHEIGHT/4*3 - Eventhappenheight/2
eventhappenplace = (eventhappenleft, eventhappentop)
Studyheight = 450
Studywidth = 800
Study = pygame.image.load('Study.jpg')
Studyimage = pygame.transform.scale(Study, (Studywidth, Studyheight))
studyleft = WINDOWWIDTH/2 - Studywidth/2
studytop = WINDOWHEIGHT/2 - Studyheight/2
studyplace = (studyleft, studytop)
Graphbackheight = 450
Graphbackwidth = 800
Graphback = pygame.image.load('Graphback.png')
Graphbackimage = pygame.transform.scale(Graphback, (Graphbackwidth, Graphbackheight))
graphbackleft = WINDOWWIDTH/2 - Graphbackwidth/2
graphbacktop = WINDOWHEIGHT/2 - Graphbackheight/2
graphbackplace = (graphbackleft, graphbacktop)
Dalyukheight = 566
Dalyukwidth = 800
Dalyuk = pygame.image.load('Dalyuk.png')
Dalyukimage = pygame.transform.scale(Dalyuk, (Dalyukwidth, Dalyukheight))
dalyukleft = WINDOWWIDTH/2 - Dalyukwidth/2
dalyuktop = WINDOWHEIGHT/2 - Dalyukheight/2
dalyukplace = (dalyukleft, dalyuktop)
Helpheight = 70
Helpwidth = 130
Help2height = 70
Help2width = 130
Help = pygame.image.load('Help.png')
Helpimage = pygame.transform.scale(Help, (Helpwidth, Helpheight))
Help2 = pygame.image.load('Help2.png')
Help2image = pygame.transform.scale(Help2, (Help2width, Help2height))
helpleft = WINDOWWIDTH/5*4 - Helpwidth/2
helptop = WINDOWHEIGHT/5*2 - Helpheight/2
help2left = WINDOWWIDTH/5*4 - Help2width/2
help2top = WINDOWHEIGHT/5*2 - Help2height/2
helpplace = (helpleft, helptop)
help2place = (help2left, help2top)
Phoneheight = 200
Phonewidth = 225
Phone2height = 215
Phone2width = 240
Phone = pygame.image.load('Phone.png')
Phoneimage = pygame.transform.scale(Phone, (Phonewidth, Phoneheight))
Phone2 = pygame.image.load('Phone2.png')
Phone2image = pygame.transform.scale(Phone2, (Phone2width, Phone2height))
phoneleft = WINDOWWIDTH/4*3 - Phonewidth/2
phonetop = WINDOWHEIGHT/5*4 - Phoneheight/2
phone2left = WINDOWWIDTH/4*3 - Phone2width/2
phone2top = WINDOWHEIGHT/5*4 - Phone2height/2
phoneplace = (phoneleft, phonetop)
phone2place = (phone2left, phone2top)
Phonescreenheight = 600
Phonescreenwidth = 370
Phonescreen = pygame.image.load('Phonescreen.png')
Phonescreenimage = pygame.transform.scale(Phonescreen, (Phonescreenwidth, Phonescreenheight))
phonescreenleft = WINDOWWIDTH/2 - Phonescreenwidth/2
phonescreentop = WINDOWHEIGHT/2 - Phonescreenheight/2
phonescreenplace = (phonescreenleft, phonescreentop)
Makefriendheight = 600
Makefriendwidth = 370
Makefriend = pygame.image.load('Makefriend.png')
Makefriendimage = pygame.transform.scale(Makefriend, (Makefriendwidth, Makefriendheight))
makefriendleft = WINDOWWIDTH/2 - Makefriendwidth/2
makefriendtop = WINDOWHEIGHT/2 - Makefriendheight/2
makefriendplace = (makefriendleft, makefriendtop)
Phonemessengerheight = 600
Phonemessengerwidth = 370
Phonemessenger = pygame.image.load('Phonemessenger.png')
Phonemessengerimage = pygame.transform.scale(Phonemessenger, (Phonemessengerwidth, Phonemessengerheight))
phonemessengerleft = WINDOWWIDTH/2 - Phonemessengerwidth/2
phonemessengertop = WINDOWHEIGHT/2 - Phonemessengerheight/2
phonemessengerplace = (phonemessengerleft, phonemessengertop)
Messengertopfriendheight = 600
Messengertopfriendwidth = 370
Messengertopfriend = pygame.image.load('Messengertopfriend.png')
Messengertopfriendimage = pygame.transform.scale(Messengertopfriend, (Messengertopfriendwidth, Messengertopfriendheight))
messengertopfriendleft = WINDOWWIDTH/2 - Messengertopfriendwidth/2
messengertopfriendtop = WINDOWHEIGHT/2 - Messengertopfriendheight/2
messengertopfriendplace = (messengertopfriendleft, messengertopfriendtop)
Phonebackgroundheight = 534
Phonebackgroundwidth = 330
Phonebackground = pygame.image.load('Phonebackground.png')
Phonebackgroundimage = pygame.transform.scale(Phonebackground, (Phonebackgroundwidth, Phonebackgroundheight))
phonebackgroundleft = WINDOWWIDTH/2 - Phonebackgroundwidth/2
phonebackgroundtop = WINDOWHEIGHT/2 - Phonebackgroundheight/2
phonebackgroundplace = (phonebackgroundleft, phonebackgroundtop)
Facebookheight = 70
Facebookwidth = 70
Facebook = pygame.image.load('Facebook.png')
Facebookimage = pygame.transform.scale(Facebook, (Facebookwidth, Facebookheight))
facebookleft = WINDOWWIDTH/2 - Facebookwidth/2
facebooktop = WINDOWHEIGHT/5*2 - Facebookheight/2
facebookplace = (facebookleft, facebooktop)
Facebook2height = 80
Facebook2width = 80
Facebook2 = pygame.image.load('Facebook2.png')
Facebook2image = pygame.transform.scale(Facebook2, (Facebook2width, Facebook2height))
facebook2left = WINDOWWIDTH/2 - Facebook2width/2
facebook2top = WINDOWHEIGHT/5*2 - Facebook2height/2
facebook2place = (facebook2left, facebook2top)
Cookieheight = 70
Cookiewidth = 70
Cookie = pygame.image.load('cookie.png')
Cookieimage = pygame.transform.scale(Cookie, (Cookiewidth, Cookieheight))
cookieleft = WINDOWWIDTH/2 - Cookiewidth/2
cookietop = WINDOWHEIGHT/5 - Cookieheight/2
cookieplace = (cookieleft, cookietop)
Cookie2height = 80
Cookie2width = 80
Cookie2 = pygame.image.load('cookie2.png')
Cookie2image = pygame.transform.scale(Cookie2, (Cookie2width, Cookie2height))
cookie2left = WINDOWWIDTH/2 - Cookie2width/2
cookie2top = WINDOWHEIGHT/5 - Cookie2height/2
cookie2place = (cookie2left, cookie2top)
Messengerheight = 70
Messengerwidth = 80
Messenger = pygame.image.load('Messenger.png')
Messengerimage = pygame.transform.scale(Messenger, (Messengerwidth, Messengerheight))
messengerleft = WINDOWWIDTH/2 - Messengerwidth/2
messengertop = WINDOWHEIGHT/5*3 - Messengerheight/2
messengerplace = (messengerleft, messengertop)
Messenger2height = 90
Messenger2width = 100
Messenger2 = pygame.image.load('Messenger2.png')
Messenger2image = pygame.transform.scale(Messenger2, (Messenger2width, Messenger2height))
messenger2left = WINDOWWIDTH/2 - Messenger2width/2
messenger2top = WINDOWHEIGHT/5*3 - Messenger2height/2
messenger2place = (messenger2left, messenger2top)
Phonebackheight = 40
Phonebackwidth = 40
Phoneback = pygame.image.load('Phoneback.png')
Phonebackimage = pygame.transform.scale(Phoneback, (Phonebackwidth, Phonebackheight))
phonebackleft = WINDOWWIDTH/2 - Phonebackwidth/2
phonebacktop = WINDOWHEIGHT/4*3 - Phonebackheight/2
phonebackplace = (phonebackleft, phonebacktop)
Calbackheight = 40
Calbackwidth = 40
Calback = pygame.image.load('Phoneback.png')
Calbackimage = pygame.transform.scale(Calback, (Calbackwidth, Calbackheight))
calbackleft = WINDOWWIDTH/13*12 - Calbackwidth/2
calbacktop = WINDOWHEIGHT/10*9 - Calbackheight/2
calbackplace = (calbackleft, calbacktop)
Facebackheight = 40
Facebackwidth = 40
Faceback = pygame.image.load('Faceback.png')
Facebackimage = pygame.transform.scale(Faceback, (Facebackwidth, Facebackheight))
facebackleft = WINDOWWIDTH/5*3 - Facebackwidth/2
facebacktop = WINDOWHEIGHT/15*14 - Facebackheight/2
facebackplace = (facebackleft, facebacktop)
Deskheight = WINDOWHEIGHT
Deskwidth = WINDOWWIDTH
Desk = pygame.image.load('Table.jpg')
Deskimage = pygame.transform.scale(Desk, (Deskwidth, Deskheight))
deskleft = WINDOWWIDTH/2 - Deskwidth/2
desktop = WINDOWHEIGHT/2 - Deskheight/2
deskplace = (deskleft, desktop)
Classtableheight = 500
Classtablewidth = 850 
Classtable = pygame.image.load('Classtable.png')
Classtableimage = pygame.transform.scale(Classtable, (Classtablewidth, Classtableheight))
classtableleft = WINDOWWIDTH/2 - Classtablewidth/2
classtabletop = WINDOWHEIGHT/2 - Classtableheight/2 +20
classtableplace = (classtableleft, classtabletop)
Inclassheight = WINDOWHEIGHT
Inclasswidth = WINDOWWIDTH
Inclass = pygame.image.load('Inclass.jpg')
Inclassimage = pygame.transform.scale(Inclass, (Inclasswidth, Inclassheight))
inclassleft = WINDOWWIDTH/2 - Inclasswidth/2
inclasstop = WINDOWHEIGHT/2 - Inclassheight/2
inclassplace = (inclassleft, inclasstop)
Messengerbackheight = 500
Messengerbackwidth = 350
Messengerback = pygame.image.load('Messengerback.png')
Messengerbackimage = pygame.transform.scale(Messengerback, (Messengerbackwidth, Messengerbackheight))
messengerbackleft = WINDOWWIDTH/2 - Messengerbackwidth/2
messengerbacktop = WINDOWHEIGHT/2 - Messengerbackheight/2
messengerbackplace = (messengerbackleft, messengerbacktop)
Helpbackheight = 40
Helpbackwidth = 40
Helpback = pygame.image.load('Faceback.png')
Helpbackimage = pygame.transform.scale(Helpback, (Helpbackwidth, Helpbackheight))
helpbackleft = WINDOWWIDTH/7*6 - Helpbackwidth/2
helpbacktop = WINDOWHEIGHT/6*5- Helpbackheight/2
helpbackplace = (helpbackleft, helpbacktop)
Faceupheight = 50
Faceupwidth = 25
Faceup = pygame.image.load('Faceup.png')
Faceupimage = pygame.transform.scale(Faceup, (Faceupwidth, Faceupheight))
faceupleft = WINDOWWIDTH/10*6 - Faceupwidth/2 + 40
faceuptop = WINDOWHEIGHT/5 - Faceupheight/2 + 20
faceupplace = (faceupleft, faceuptop)
Facedownheight = 50
Facedownwidth = 25
Facedown = pygame.image.load('Facedown.png')
Facedownimage = pygame.transform.scale(Facedown, (Facedownwidth, Facedownheight))
facedownleft = WINDOWWIDTH/10*6 - Facedownwidth/2 + 40
facedowntop = WINDOWHEIGHT/5*4 - Facedownheight/2 + 20
facedownplace = (facedownleft, facedowntop)
Letsbefriendheight = 40
Letsbefriendwidth = 120
Letsbefriend = pygame.image.load('Letsbefriend.png')
Letsbefriendimage = pygame.transform.scale(Letsbefriend, (Letsbefriendwidth, Letsbefriendheight))
letsbefriendleft = WINDOWWIDTH/10*6 - Letsbefriendwidth/2 - 50
letsbefriendtop = WINDOWHEIGHT/5*4 - Letsbefriendheight/2
letsbefriendplace = (letsbefriendleft, letsbefriendtop)
Sendedheight = 40
Sendedwidth = 120
Sended = pygame.image.load('Sended.png')
Sendedimage = pygame.transform.scale(Sended, (Sendedwidth, Sendedheight))
sendedleft = WINDOWWIDTH/10*6 - Sendedwidth/2 - 50
sendedtop = WINDOWHEIGHT/5*4 - Sendedheight/2
sendedplace = (sendedleft, sendedtop)
Becomefriendheight = 40
Becomefriendwidth = 120
Becomefriend = pygame.image.load('Becomefriend.png')
Becomefriendimage = pygame.transform.scale(Becomefriend, (Becomefriendwidth, Becomefriendheight))
becomefriendleft = WINDOWWIDTH/10*6 - Becomefriendwidth/2 - 50
becomefriendtop = WINDOWHEIGHT/5*4 - Becomefriendheight/2
becomefriendplace = (becomefriendleft, becomefriendtop)
Letstalkheight = 40
Letstalkwidth = 120
Letstalk = pygame.image.load('Letstalk.png')
Letstalkimage = pygame.transform.scale(Letstalk, (Letstalkwidth, Letstalkheight))
letstalkleft = WINDOWWIDTH/10*6 - Letstalkwidth/2 - 50
letstalktop = WINDOWHEIGHT/5*4 - Letstalkheight/2
letstalkplace = (letstalkleft, letstalktop)
Talkanythingheight = 80
Talkanythingwidth = 240
Talkanything = pygame.image.load('Talkanything.png')
Talkanythingimage = pygame.transform.scale(Talkanything, (Talkanythingwidth, Talkanythingheight))
talkanythingleft = WINDOWWIDTH/2 - Talkanythingwidth/2 
talkanythingtop = WINDOWHEIGHT/5*4 - Talkanythingheight/2
talkanythingplace = (talkanythingleft, talkanythingtop)
Talkanything2height = 80
Talkanything2width = 240
Talkanything2 = pygame.image.load('Talkanything2.png')
Talkanything2image = pygame.transform.scale(Talkanything2, (Talkanything2width, Talkanything2height))
talkanything2left = WINDOWWIDTH/2 - Talkanything2width/2 
talkanything2top = WINDOWHEIGHT/5*4 - Talkanything2height/2
talkanything2place = (talkanything2left, talkanything2top)
namelist = ["JYH","JWY","JDW","LSJ","MSM","SJB","OKJ","KMJ","JIH","LJS","YJH","JJJ","KJH","SYS","KHJ"]
Peopleheight = 800
Peoplewidth = 500
peopleleft = WINDOWWIDTH/2 - Peoplewidth/2 
peopletop = WINDOWHEIGHT/2 - Peopleheight/2
peopleplace = (peopleleft, peopletop)
People = []
Peopleimage = []
for i in range(15):
    People.append(pygame.image.load(namelist[i]+'_1.png'))
    Peopleimage.append(pygame.transform.scale(People[len(People)-1], (Peoplewidth, Peopleheight)))
mousex = 0
mousey = 0
Book = 0
Cal = 0
Phone = 0
Facebook = 0
Cookie = 0
Help = 0
Messenger = 0
studyclock = 0
gameclock = 0
Gamestart = 0
friendmss = [0,0,0,0,0,0,0,2,0,0,2,0,0,1,0,0]
friendplace = [[0,0],[17.1, 2.8],[10.8, 4.1],[15,27.3],[9.6,17],[12.9,11.2],[17.1,9.3],[1.5,14.7],[2.3,6.8],[8.6,10.2],[9.8,25.8],[5.2,5.5],[2.7,21],[6.1,15],[4.6,28],[17.2,19.9]]
classplace = [[2.6,2.6],[6.8, 2.6],[10.7, 2.6],[14.7,2.6],[18.7,2.6],[22.8,2.6],[26.8,2.6],[26.8,6.6],[26.8,11],[26.8,15.2],[26.8,19.4],[22.8,19.4],[18.7,19.4],[14.7,19.4],[10.7,19.4],[6.8,19.4],[2.6,19.4]]
Heartbreak = 10
grade = 300
Instudyroom = 0
Inclassroom = 1
Talk = 0
Talktowhom = 0
Day = 1
friendtalk = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
friends = [students.KJS,students.JYH,students.JWY,students.JDW,students.LSJ,students.MSM,students.SJB,students.OKJ,students.KMJ,students.JIH,students.LJS,students.YJH,students.JJJ,students.KJH,students.SYS,students.KHJ]
studytime = 0
a = 'B+'
stop1 = 0
stop1time = 0
n11=0
n12=0
stop2 = 0
stop2time = 0
n21=0
n22=0
right1 = 0
left1 = 0
right2 = 0
left2 = 0

def getevent():
    mousex = 0
    mousey = 0
    mousedown = 0
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == MOUSEBUTTONDOWN:
                mousedown = 1
    pos = pygame.mouse.get_pos()
    mousex = pos[0]
    mousey = pos[1]
    return mousex, mousey, mousedown
    
while True:
    studytime = 0
    while Gamestart:
        windowSurface.fill(WHITE)
        mousex, mousey, mousedown = getevent()
        pygame.display.update()
        mainClock.tick(SPEED)
    while Instudyroom:
        studytime += 1
        if studytime == 15*SPEED:
            Instudyroom = 0
            Inclassroom = 1
        if grade>=480:
            a = 'A+'
        elif grade>=420:
            a = 'A0'
        elif grade>=360:
            a = 'A-'
        elif grade>=300:
            a = 'B+'
        elif grade>=240:
            a = 'B0'
        elif grade>=180:
            a = 'B-'
        elif grade>=120:
            a = 'C+'
        elif grade>=60:
            a = 'C0'
        elif grade>=0:
            a = 'C-'
        windowSurface.fill(WHITE)
        windowSurface.blit(Deskimage, deskplace)
        mousex, mousey, mousedown = getevent()
        if mousex > bookleft and mousex < bookleft+Bookwidth and mousey > booktop and mousey < booktop+Bookheight:
            if mousedown == 1:
                Book = 1
            windowSurface.blit(Bookimage, bookplace)
        else:
            windowSurface.blit(Book2image, book2place)
        if mousex > calleft and mousex < calleft+Calwidth and mousey > caltop and mousey < caltop+Calheight:
            if mousedown == 1:
                Cal = 1
            windowSurface.blit(Cal2image, cal2place)
        else:
            windowSurface.blit(Calimage, calplace)
        if mousex > phoneleft and mousex < phoneleft+Phonewidth and mousey > phonetop and mousey < phonetop+Phoneheight:
            windowSurface.blit(Phone2image, phone2place)
            if mousedown == 1:
                Phone = 1
        else:
            windowSurface.blit(Phoneimage, phoneplace)
        if mousex > helpleft and mousex < helpleft+Helpwidth and mousey > helptop and mousey < helptop+Helpheight:
            windowSurface.blit(Help2image, help2place)
            if mousedown == 1:
                Help = 1
        else:
            windowSurface.blit(Helpimage, helpplace)
        windowSurface.blit(Eventhappenimage, eventhappenplace)
        texthelp = basicFont1.render('마음의 상처', True, WHITE)
        texthelpRect = texthelp.get_rect()
        texthelpRect.centerx = WINDOWWIDTH/20*4 - 20
        texthelpRect.centery = WINDOWHEIGHT/20+3 
        textheart = basicFont4.render('도와줘!', True, BLACK)
        textheartRect = textheart.get_rect()
        textheartRect.centerx = helpleft + Helpwidth/2
        textheartRect.centery = helptop + Helpheight/2
        textday = basicFont1.render(str(Day)+'일차', True, WHITE)
        textdayRect = textday.get_rect()
        textdayRect.centerx = WINDOWWIDTH/20*19 - 40
        textdayRect.centery = WINDOWHEIGHT/20+3
        textgrade = basicFont1.render('받을 학점', True, WHITE)
        textgradeRect = textgrade.get_rect()
        textgradeRect.centerx = WINDOWWIDTH/20*4
        textgradeRect.centery = WINDOWHEIGHT/20*3+3
        textgrade2 = basicFont1.render(a, True, WHITE)
        textgrade2Rect = textgrade2.get_rect()
        textgrade2Rect.centerx = WINDOWWIDTH/20*19
        textgrade2Rect.centery = WINDOWHEIGHT/20*3+3
        pygame.draw.rect(windowSurface, BLACK, (WINDOWWIDTH/20*6-2, WINDOWHEIGHT/20-2, 542, 14))
        pygame.draw.rect(windowSurface, RED, (WINDOWWIDTH/20*6, WINDOWHEIGHT/20, Heartbreak, 10))
        pygame.draw.rect(windowSurface, BLACK, (WINDOWWIDTH/20*6-2, WINDOWHEIGHT/20*3-2, 542, 14))
        pygame.draw.rect(windowSurface, RED, (WINDOWWIDTH/20*6, WINDOWHEIGHT/20*3, grade, 10))
        windowSurface.blit(textheart, textheartRect)
        windowSurface.blit(texthelp, texthelpRect)
        windowSurface.blit(textgrade, textgradeRect)
        windowSurface.blit(textgrade2, textgrade2Rect)
        windowSurface.blit(textday, textdayRect)
        pygame.draw.rect(windowSurface, BLACK, (WINDOWWIDTH/20*19-2-25, WINDOWHEIGHT/20-2, 14, WINDOWHEIGHT/10*9+4))
        pygame.draw.rect(windowSurface, YELLOW, (WINDOWWIDTH/20*19-25, WINDOWHEIGHT/20, 10, studytime*540/SPEED/15))
        while Help:
            mousex, mousey, mousedown = getevent()
            studytime += 1
            if studytime == 15*SPEED:
                Instudyroom = 0
                Inclassroom = 1
            windowSurface.fill(WHITE)
            windowSurface.blit(Deskimage, deskplace)
            windowSurface.blit(Graphbackimage, graphbackplace)
            windowSurface.blit(Helpbackimage, helpbackplace)
            pygame.draw.rect(windowSurface, BLACK, (WINDOWWIDTH/20*19-2-25, WINDOWHEIGHT/20-2, 14, WINDOWHEIGHT/10*9+4))
            pygame.draw.rect(windowSurface, YELLOW, (WINDOWWIDTH/20*19-25, WINDOWHEIGHT/20, 10, studytime*540/SPEED/15))
            if mousex > helpbackleft and mousex < helpbackleft+Helpbackwidth and mousey > helpbacktop and mousey < helpbacktop+Helpbackheight and mousedown:
                Help = 0
            for i in range (1, 16):
                textname = basicFont1.render(students.students[i].name, True, WHITE)
                textnameRect = textname.get_rect()
                textnameRect.centerx = WINDOWWIDTH/2 - Graphbackwidth/2 + Graphbackwidth*friendplace[i][1]/34 
                textnameRect.centery = WINDOWHEIGHT/2 - Graphbackheight/2 + Graphbackheight*friendplace[i][0]/19 
                windowSurface.blit(textname, textnameRect)
            for i in range (1,16):
                for j in range(1,16):
                    if students.checkfriend(friends[i],friends[j]):
                        placex1 = WINDOWWIDTH/2 - Graphbackwidth/2 + Graphbackwidth*friendplace[i][1]/34
                        placey1 = WINDOWWIDTH/2 - Graphbackwidth/2 + Graphbackwidth*friendplace[i][0]/34 -25
                        placex2 = WINDOWWIDTH/2 - Graphbackwidth/2 + Graphbackwidth*friendplace[j][1]/34
                        placey2 = WINDOWWIDTH/2 - Graphbackwidth/2 + Graphbackwidth*friendplace[j][0]/34 - 25
                        pygame.draw.line(windowSurface, YELLOW, (placex1, placey1),(placex2, placey2), 2)
            pygame.display.update()
            mainClock.tick(SPEED)
        while Cal:
            studytime += 1
            if studytime == 15*SPEED:
                Instudyroom = 0
                Inclassroom = 1
            windowSurface.fill(WHITE)
            windowSurface.blit(Deskimage, deskplace)
            mousex, mousey, mousedown = getevent()
            windowSurface.blit(Dalyukimage, dalyukplace)
            windowSurface.blit(Calbackimage, calbackplace)
            pygame.draw.rect(windowSurface, BLACK, (WINDOWWIDTH/20*19-2-25, WINDOWHEIGHT/20-2, 14, WINDOWHEIGHT/10*9+4))
            pygame.draw.rect(windowSurface, YELLOW, (WINDOWWIDTH/20*19-25, WINDOWHEIGHT/20, 10, studytime*540/SPEED/15))
            if mousex > calbackleft and mousex < calbackleft+Calbackwidth and mousey > calbacktop and mousey < calbacktop+Calbackheight and mousedown:
                Cal = 0
            pygame.display.update()
            mainClock.tick(SPEED)
        while Book:
            studytime += 1
            if studytime == 15*SPEED:
                Instudyroom = 0
                Book = 0
                Inclassroom = 1
            windowSurface.fill(WHITE)
            windowSurface.blit(Deskimage, deskplace)
            mousex, mousey, mousedown = getevent()
            windowSurface.blit(Studyimage, studyplace)
            pygame.draw.rect(windowSurface, BLACK, (WINDOWWIDTH/20*19-2-25, WINDOWHEIGHT/20-2, 14, WINDOWHEIGHT/10*9+4))
            pygame.draw.rect(windowSurface, YELLOW, (WINDOWWIDTH/20*19-25, WINDOWHEIGHT/20, 10, studytime*540/SPEED/15))
            studyclock += 1
            if studyclock == 5*SPEED:
                Book = 0
            textstudy = basicFont3.render('공부중....', True, WHITE)
            pygame.draw.rect(windowSurface, BLACK, (WINDOWWIDTH/20*5-1, WINDOWHEIGHT/20*19-1, 5*SPEED*2, 7))
            pygame.draw.rect(windowSurface, RED, (WINDOWWIDTH/20*5, WINDOWHEIGHT/20*19, studyclock*2, 5))
            textstudyRect = textstudy.get_rect()
            textstudyRect.centerx = WINDOWWIDTH/2
            textstudyRect.centery = WINDOWHEIGHT/2
            windowSurface.blit(textstudy, textstudyRect)
            grade += 1/5
            pygame.display.update()
            mainClock.tick(SPEED)
        studyclock = 0
        while Phone:
            studytime += 1
            if studytime == 15*SPEED:
                Instudyroom = 0
                Phone = 0
                Inclassroom = 1
            windowSurface.fill(WHITE)
            mousex, mousey, mousedown = getevent()
            windowSurface.blit(Deskimage, deskplace)
            windowSurface.blit(Phonescreenimage, phonescreenplace)
            windowSurface.blit(Phonebackgroundimage, phonebackgroundplace)
            if mousex > facebookleft and mousex < facebookleft+Facebookwidth and mousey > facebooktop and mousey < facebooktop+Facebookheight:
                windowSurface.blit(Facebook2image, facebook2place)
                if mousedown == 1:
                    Facebook = 1 
            else:
                windowSurface.blit(Facebookimage, facebookplace)
            if mousex > cookieleft and mousex < cookieleft+Cookiewidth and mousey > cookietop and mousey < cookietop+Cookieheight:
                windowSurface.blit(Cookie2image, cookie2place)
                if mousedown == 1:
                    Cookie = 1
            else:
                windowSurface.blit(Cookieimage, cookieplace)
            if mousex > messengerleft and mousex < messengerleft+Messengerwidth and mousey > messengertop and mousey < messengertop+Messengerheight:
                windowSurface.blit(Messenger2image, messenger2place)
                if mousedown == 1:
                    Messenger = 1
            else:
                windowSurface.blit(Messengerimage, messengerplace)
            windowSurface.blit(Phonebackimage, phonebackplace)
            if mousex > phonebackleft and mousex < phonebackleft+Phonebackwidth and mousey > phonebacktop and mousey < phonebacktop+Phonebackheight and mousedown:
                Phone = 0
            i = random.randint(1,6)
            Cookiebackwidth = 711
            Cookiebackheight = 400
            Cookieback = pygame.image.load('cookierun'+str(i)+'.jpg')
            Cookiebackimage = pygame.transform.scale(Cookieback, (Cookiebackwidth, Cookiebackheight))
            cookiebackleft = WINDOWWIDTH/2 - Cookiebackwidth/2
            cookiebacktop = WINDOWHEIGHT/2 - Cookiebackheight/2
            cookiebackplace = (cookiebackleft, cookiebacktop)
            pygame.draw.rect(windowSurface, BLACK, (WINDOWWIDTH/20*19-2-25, WINDOWHEIGHT/20-2, 14, WINDOWHEIGHT/10*9+4))
            pygame.draw.rect(windowSurface, YELLOW, (WINDOWWIDTH/20*19-25, WINDOWHEIGHT/20, 10, studytime*540/SPEED/15))
            while Cookie:
                studytime += 1
                if studytime == 15*SPEED:
                    Instudyroom = 0
                    Cookie = 0
                    Phone = 0
                    Inclassroom = 1
                windowSurface.fill(WHITE)
                windowSurface.blit(Deskimage, deskplace)
                mousex, mousey, mousedown = getevent()
                windowSurface.blit(Cookiebackimage, cookiebackplace)
                gameclock += 1
                if gameclock == 5*SPEED:
                    Cookie = 0
                textgame = basicFont3.render('게임중....', True, WHITE)
                textgameRect = textgame.get_rect()
                textgameRect.centerx = WINDOWWIDTH/2
                textgameRect.centery = WINDOWHEIGHT/2
                pygame.draw.rect(windowSurface, BLACK, (WINDOWWIDTH/20*5-1, WINDOWHEIGHT/20*19-1, 5*SPEED*2, 7))
                pygame.draw.rect(windowSurface, RED, (WINDOWWIDTH/20*5, WINDOWHEIGHT/20*19, gameclock*2, 5))
                windowSurface.blit(textgame, textgameRect)
                pygame.draw.rect(windowSurface, BLACK, (WINDOWWIDTH/20*19-2-25, WINDOWHEIGHT/20-2, 14, WINDOWHEIGHT/10*9+4))
                pygame.draw.rect(windowSurface, YELLOW, (WINDOWWIDTH/20*19-25, WINDOWHEIGHT/20, 10, studytime*540/SPEED/15))
                grade -= 2/5
                pygame.display.update()
                mainClock.tick(SPEED)
            gameclock = 0
            upbarleft = 630
            upbarup = 200
            Messengerfriendheight = 740
            Messengerfriendwidth = 140
            Messengerfriend = pygame.image.load('Messengerfriend.png')
            Messengerfriendimage = pygame.transform.scale(Messengerfriend, (Messengerfriendwidth, Messengerfriendheight))
            messengerfriendleft = WINDOWWIDTH/2 - Messengerfriendwidth/2 - 70
            messengerfriendtop = WINDOWHEIGHT/2 - Messengerfriendheight/2
            messengerfriendplace = (messengerfriendleft, messengerfriendtop)
            while Facebook:
                studytime += 1
                if studytime == 15*SPEED:
                    Instudyroom = 0
                    Facebook = 0
                    Phone = 0
                    Inclassroom = 1
                top = messengerfriendtop
                windowSurface.fill(WHITE)
                windowSurface.blit(Deskimage, deskplace)
                mousex, mousey, mousedown = getevent()
                messengerfriendplace = (messengerfriendleft, messengerfriendtop)
                windowSurface.blit(Messengerbackimage, messengerbackplace)
                for i in range (0,16):
                    if friendmss[i] == 0:
                        letsbefriendplace = (letsbefriendleft, top)
                        windowSurface.blit(Letsbefriendimage, letsbefriendplace)
                    if friendmss[i] == 1:
                        sendedplace = (sendedleft, top)
                        windowSurface.blit(Sendedimage, sendedplace)
                    if friendmss[i] == 2:
                        becomefriendplace = (becomefriendleft, top)
                        windowSurface.blit(Becomefriendimage, becomefriendplace)
                    top += 45.2
                top = messengerfriendtop
                windowSurface.blit(Messengerfriendimage, messengerfriendplace)
                windowSurface.blit(Makefriendimage, makefriendplace)
                windowSurface.blit(Facebackimage, facebackplace)
                windowSurface.blit(Faceupimage, faceupplace)
                windowSurface.blit(Facedownimage, facedownplace)
                if mousex > facebackleft and mousex < facebackleft+Facebackwidth and mousey > facebacktop and mousey < facebacktop+Facebackheight and mousedown:
                    Facebook = 0
                if mousex > faceupleft and mousex < faceupleft+Faceupwidth and mousey > faceuptop and mousey < faceuptop+Faceupheight and mousedown:
                    messengerfriendtop += 50
                    if messengerfriendtop > 140:
                        messengerfriendtop -= 50
                if mousex > facedownleft and mousex < facedownleft+Facedownwidth and mousey > facedowntop and mousey < facedowntop+Facedownheight and mousedown:
                    messengerfriendtop -= 50
                    if messengerfriendtop + Messengerfriendheight < 550:
                        messengerfriendtop += 50
                for i in range (0, 16):
                    if mousex > letsbefriendleft and mousex < letsbefriendleft+Letsbefriendwidth and mousey > top and mousey < top+Letsbefriendheight and mousedown and friendmss[i] == 0:
                        friendmss[i] = 1
                    top += 45.2
                pygame.draw.rect(windowSurface, BLACK, (WINDOWWIDTH/20*19-2-25, WINDOWHEIGHT/20-2, 14, WINDOWHEIGHT/10*9+4))
                pygame.draw.rect(windowSurface, YELLOW, (WINDOWWIDTH/20*19-25, WINDOWHEIGHT/20, 10, studytime*540/SPEED/15))
                pygame.display.update()
                mainClock.tick(SPEED)
            while Messenger:
                studytime += 1
                if studytime == 15*SPEED:
                    Instudyroom = 0
                    Messenger = 0
                    Phone = 0
                    Inclassroom = 1
                top = messengerfriendtop
                windowSurface.fill(WHITE)
                windowSurface.blit(Deskimage, deskplace)
                messengerfriendplace = (messengerfriendleft, messengerfriendtop)
                mousex, mousey, mousedown = getevent()
                windowSurface.blit(Messengerbackimage, messengerbackplace)
                pygame.draw.rect(windowSurface, BLACK, (WINDOWWIDTH/20*19-2-25, WINDOWHEIGHT/20-2, 14, WINDOWHEIGHT/10*9+4))
                pygame.draw.rect(windowSurface, YELLOW, (WINDOWWIDTH/20*19-25, WINDOWHEIGHT/20, 10, studytime*540/SPEED/15))
                for i in range (0,16):
                    if friendmss[i] == 2:
                        letstalkplace = (letstalkleft, top)
                        windowSurface.blit(Letstalkimage, letstalkplace)
                    top += 45.2
                top = messengerfriendtop
                windowSurface.blit(Messengerfriendimage, messengerfriendplace)
                windowSurface.blit(Phonemessengerimage, phonemessengerplace)
                windowSurface.blit(Facebackimage, facebackplace)
                windowSurface.blit(Faceupimage, faceupplace)
                windowSurface.blit(Facedownimage, facedownplace)
                if mousex > facebackleft and mousex < facebackleft+Facebackwidth and mousey > facebacktop and mousey < facebacktop+Facebackheight and mousedown:
                    Messenger = 0
                if mousex > faceupleft and mousex < faceupleft+Faceupwidth and mousey > faceuptop and mousey < faceuptop+Faceupheight and mousedown:
                    messengerfriendtop += 50
                    if messengerfriendtop > 140:
                        messengerfriendtop -= 50
                if mousex > facedownleft and mousex < facedownleft+Facedownwidth and mousey > facedowntop and mousey < facedowntop+Facedownheight and mousedown:
                    messengerfriendtop -= 50
                    if messengerfriendtop + Messengerfriendheight < 550:
                        messengerfriendtop += 50
                for i in range (0,16):
                    if mousex > letstalkleft and mousex < letstalkleft+Letstalkwidth and mousey > top and mousey < top+Letstalkheight and mousedown and friendmss[i] == 2:
                        Talk = 1
                        Talktowhom = i
                        break
                    top += 45.2
                while Talk:
                    studytime += 1
                    if studytime == 15*SPEED:
                        Instudyroom = 0
                        Talk = 0
                        Phone = 0
                        Inclassroom = 1
                    windowSurface.fill(WHITE)
                    windowSurface.blit(Deskimage, deskplace)
                    mousex, mousey, mousedown = getevent()
                    windowSurface.blit(Messengerbackimage, messengerbackplace)
                    texthitop = [WINDOWHEIGHT/5*3]
                    for n in range (1, len(friendtalk[i])):
                        texthitop.append(texthitop[n-1] + 50)
                    for n in range (0, len(friendtalk[i])):
                        texthitop[n] -= 50*(len(friendtalk[i])-1)
                    for n in range (0, len(friendtalk[i])):
                        texthi = basicFont1.render(talking[friendtalk[i][n]], True, BLACK)
                        texthiRect = textany.get_rect()
                        texthiRect.centerx = WINDOWWIDTH/5*3
                        texthiRect.centery = texthitop[n]
                        windowSurface.blit(texthi, texthiRect)
                    windowSurface.blit(Messengertopfriendimage, messengertopfriendplace)
                    textname = basicFont0.render(students.students[i].name, True, WHITE)
                    textnameRect = textname.get_rect()
                    textnameRect.centerx = WINDOWWIDTH/2
                    textnameRect.centery = WINDOWHEIGHT/10+19
                    windowSurface.blit(textname, textnameRect)
                    windowSurface.blit(Facebackimage, facebackplace)
                    textany = basicFont1.render('아무 말 하기', True, BLACK)
                    textanyRect = textany.get_rect()
                    textanyRect.centerx = WINDOWWIDTH/2
                    textanyRect.centery = WINDOWHEIGHT/5*4
                    if mousex > facebackleft and mousex < facebackleft+Facebackwidth and mousey > facebacktop and mousey < facebacktop+Facebackheight and mousedown:
                        Talk = 0
                    if mousex > talkanythingleft and mousex < talkanythingleft+Talkanythingwidth and mousey > talkanythingtop and mousey < talkanythingtop+Talkanythingheight:
                        windowSurface.blit(Talkanything2image, talkanything2place)
                        if mousedown:
                            p = random.randint(0,len(friends[i].talking))
                            friendtalk[i].append(p)
                    else:
                        windowSurface.blit(Talkanythingimage, talkanythingplace)
                    windowSurface.blit(textany, textanyRect)
                    pygame.draw.rect(windowSurface, BLACK, (WINDOWWIDTH/20*19-2-25, WINDOWHEIGHT/20-2, 14, WINDOWHEIGHT/10*9+4))
                    pygame.draw.rect(windowSurface, YELLOW, (WINDOWWIDTH/20*19-25, WINDOWHEIGHT/20, 10, studytime*540/SPEED/15))
                    pygame.display.update()
                    mainClock.tick(SPEED)
                pygame.display.update()
                mainClock.tick(SPEED)
            pygame.display.update()
            mainClock.tick(SPEED)
        pygame.display.update()
        mainClock.tick(SPEED)
        
    pnum=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    pnum1 = random.choice(pnum)
    pnum.remove(pnum1)
    pnum2 = random.choice(pnum)
    pnum.remove(pnum2)
    pnum3 = 0
    if pnum1 > pnum2:
        pnum3 = pnum1
        pnum1 = pnum2
        pnum2 = pnum3
    snum=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    for i in range(0, 14):
        if friends[i].retired:
            snum.remove(i)
    random.shuffle(snum)
    while Inclassroom:
        windowSurface.fill(WHITE)
        mousex, mousey, mousedown = getevent()
        windowSurface.blit(Inclassimage, inclassplace)
        windowSurface.blit(Classtableimage, classtableplace)
        texthelp = basicFont1.render('마음의 상처', True, WHITE)
        texthelpRect = texthelp.get_rect()
        texthelpRect.centerx = WINDOWWIDTH/20*4 - 20
        texthelpRect.centery = WINDOWHEIGHT/20+3
        textgrade2 = basicFont1.render('남은 자리 중 하나를 골라 앉으세요', True, WHITE)
        textgrade2Rect = textgrade2.get_rect()
        textgrade2Rect.centerx = WINDOWWIDTH/2 - 60
        textgrade2Rect.centery = WINDOWHEIGHT/2
        windowSurface.blit(textgrade2, textgrade2Rect)
        windowSurface.blit(texthelp, texthelpRect)
        for i in range(0,15):
            textany = basicFont0.render(friends[snum[i]].name, True, BLACK)
            textanyRect = textany.get_rect()
            textanyRect.centerx = WINDOWWIDTH/2 - Classtablewidth/2 + Classtablewidth*classplace[pnum[i]][0]/28 -25
            textanyRect.centery = WINDOWHEIGHT/2 - Classtableheight/2 + Classtableheight*classplace[pnum[i]][1]/21 +5
            windowSurface.blit(textany, textanyRect)
        Oneseatheight = 100
        Oneseatwidth = 120
        Oneseat = pygame.image.load('Oneseat.png')
        Oneseatimage = pygame.transform.scale(Oneseat, (Oneseatwidth, Oneseatheight))
        oneseatleft = WINDOWWIDTH/2 - Classtablewidth/2 + Classtablewidth*classplace[pnum1][0]/28 - Oneseatwidth/2 -20
        oneseattop = WINDOWHEIGHT/2 - Classtableheight/2 + Classtableheight*classplace[pnum1][1]/21 - Oneseatheight/2 +12
        oneseatplace = (oneseatleft, oneseattop)
        Oneseat2height = 100
        Oneseat2width = 120
        Oneseat2 = pygame.image.load('Oneseat.png')
        Oneseat2image = pygame.transform.scale(Oneseat2, (Oneseat2width, Oneseat2height))
        oneseat2left = WINDOWWIDTH/2 - Classtablewidth/2 + Classtablewidth*classplace[pnum2][0]/28 - Oneseat2width/2 - 20
        oneseat2top = WINDOWHEIGHT/2 - Classtableheight/2 + Classtableheight*classplace[pnum2][1]/21 - Oneseat2height/2 +12
        oneseat2place = (oneseat2left, oneseat2top)
        if mousex > oneseatleft and mousex < oneseatleft+Oneseatwidth and mousey > oneseattop and mousey < oneseattop+Oneseatheight:
            windowSurface.blit(Oneseatimage, oneseatplace)
            if mousedown and pnum1 != 0:
                n11=snum[pnum1-1]
                stop1 = 1
                right1 = 1
            if mousedown and pnum1 != 0 and pnum2 != pnum1+1:
                n12=snum[pnum1]
                stop1 = 1
                left1 = 1
        if stop1:
            if right1:
                peopleleft = WINDOWWIDTH/4 - Peoplewidth/2
                peopleplace = (peopleleft, peopletop)
                windowSurface.blit(Peopleimage[n11-1], peopleplace)
            if left1:
                peopleleft = WINDOWWIDTH/4*3 - Peoplewidth/2
                peopleplace = (peopleleft, peopletop)
                windowSurface.blit(Peopleimage[n12-1], peopleplace)
            stop1time += 1
            if stop1time >= SPEED:
                stop1 = 0
                left1 = 0
                right1 = 0
        if mousex > oneseat2left and mousex < oneseat2left+Oneseat2width and mousey > oneseat2top and mousey < oneseat2top+Oneseat2height:
            windowSurface.blit(Oneseat2image, oneseat2place)
            if mousedown and pnum2 != 0 and pnum2 != pnum2-1:
                n21=snum[pnum2-2]
                stop2 = 1
                right2 = 1
            if mousedown and pnum2 != 0:
                n22=snum[pnum2-1]
                stop2 = 1
                left2 = 1
        if stop2:
            if right2:
                peopleleft = WINDOWWIDTH/4 - Peoplewidth/2
                peopleplace = (peopleleft, peopletop)
                windowSurface.blit(Peopleimage[n21-1], peopleplace)
            if left2:
                peopleleft = WINDOWWIDTH/4*3 - Peoplewidth/2
                peopleplace = (peopleleft, peopletop)
                windowSurface.blit(Peopleimage[n22-1], peopleplace)
            stop2time += 1
            if stop2time >= SPEED:
                stop2 = 0
                left2 = 0
                right2 = 0
        pygame.draw.rect(windowSurface, BLACK, (WINDOWWIDTH/20*6-2, WINDOWHEIGHT/20-2, 542, 14))
        pygame.draw.rect(windowSurface, RED, (WINDOWWIDTH/20*6, WINDOWHEIGHT/20, Heartbreak, 10))
        pygame.display.update()
        mainClock.tick(SPEED)
    Day += 1
    for i in range (0, 16):
        if friendmss[i] ==1 and students.allowfriend(friends[i]):
            friendmss[i] = 2
    Instudyroom = 1
    Inclassroom = 1
    students.endoftheday()
    pygame.display.update()
    mainClock.tick(SPEED)
