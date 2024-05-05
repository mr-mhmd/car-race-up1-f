import pgzrun
import os
#................................
TITLE = 'race game'
WIDTH = 610
HIGHT = 417
os.environ["SDL_VIDEO_CENTERED"] = '1'
#...............................





gameMap = Actor("back")
icons = Actor("icons",(320,520))
car1 = Actor("car1",(355,320))
car2 = Actor("car2",(345,350))
start = Actor("start")
menu = Actor("menu",(580,40))
#----------------
pointPic1 = Actor("point",(457,169))
pointPic2 = Actor("point",(427,134))
pointPic3 = Actor("point",(458,62))
pointPic4 = Actor("point",(501,25))
pointPic5 = Actor("point",(267,139))
pointPic6 = Actor("point",(244,170))
pointPic7 = Actor("point",(272,286))
pointPic8 = Actor("point",(241,394))
pointPic9 = Actor("point",(170,396))
pointPic10 = Actor("point",(91,360))
pointPic11 = Actor("point",(310,568))
pointPic12 = Actor("point",(132,540))
#----------------





car1Nfs = True
car2Nfs = True
gameMenu = False
car1Score = 0 #yellow
car2Score = 0 #white
#---------
car11 = True
car12 = True
car13 = True
car14 = True
car15 = True
car16 = True
car17 = True
car18 = True
car19 = True
car110 = True
car111 = True
car112 = True
#--------
car21 = True
car22 = True
car23 = True
car24 = True
car25 = True
car26 = True
car27 = True
car28 = True
car29 = True
car210 = True
car211 = True
car212 = True













def draw():
    global gameMenu
    screen.clear()
    start.draw()
    icons.draw()
    menu.draw()
    if gameMenu == True :
        screen.clear()
        gameMap.draw()
        car1.draw()
        car2.draw()
        pointPic1.draw()
        pointPic2.draw()
        pointPic3.draw()
        pointPic4.draw()
        pointPic5.draw()
        pointPic6.draw()
        pointPic7.draw()
        pointPic8.draw()
        pointPic9.draw()
        pointPic10.draw()
        pointPic11.draw()
        pointPic12.draw()
        screen.draw.text(f"white car score : {car1Score}",(0,0),fontsize = 40 ,color = "red")
        screen.draw.text(f"yellow car score : {car2Score}",(0,27),fontsize = 40 ,color = "red")

def update():
    global car1Nfs , car2Nfs , car1Score , car2Score 
    global car11,car12,car13,car14,car15,car16,car17,car18,car19,car110,car111,car112
    global car21,car22,car23,car24,car25,car26,car27,car28,car29,car210,car211,car212
    if keyboard.up :
        car1.y -= 2
    if keyboard.down :
        car1.y += 2
    if keyboard.left :
        car1.x -= 2
    if keyboard.right :
        car1.x += 2
    if keyboard.p and car1Nfs != False :
        car1.y -= 50
        car1Nfs = False
    

    if keyboard.w :
        car2.y -= 2
    if keyboard.s :
        car2.y += 2
    if keyboard.a :
        car2.x -= 2
    if keyboard.d :
        car2.x += 2
    if keyboard.z and car2Nfs != False :
        car2.y -= 50
        car2Nfs = False

#--car 1--
    if car1.colliderect(pointPic1) and car11==True :
        car1Score += 2
        car11 = False
    if car1.colliderect(pointPic2) and car12==True :
        car1Score += 2
        car12 = False
    if car1.colliderect(pointPic3) and car13==True :
        car1Score += 2
        car13 = False
    if car1.colliderect(pointPic4) and car14==True :
        car1Score += 2
        car14 = False
    if car1.colliderect(pointPic5) and car15==True :
        car1Score += 2
        car15 = False
    if car1.colliderect(pointPic6) and car16==True :
        car1Score += 2
        car16 = False
    if car1.colliderect(pointPic7) and car17==True :
        car1Score += 2
        car17 = False
    if car1.colliderect(pointPic8) and car18==True :
        car1Score += 2
        car18 = False
    if car1.colliderect(pointPic9) and car19==True :
        car1Score += 2
        car19 = False
    if car1.colliderect(pointPic10) and car110==True :
        car1Score += 2
        car110 = False
    if car1.colliderect(pointPic11) and car111==True :
        car1Score += 2
        car111 = False
    if car1.colliderect(pointPic12) and car112==True :
        car1Score += 2
        car112 = False
#--car 2--
    if car2.colliderect(pointPic1) and car21==True :
        car2Score += 2
        car21 = False
    if car2.colliderect(pointPic2) and car22==True :
        car2Score += 2
        car22 = False
    if car2.colliderect(pointPic3) and car23==True :
        car2Score += 2
        car23 = False
    if car2.colliderect(pointPic4) and car24==True :
        car2Score += 2
        car24 = False
    if car2.colliderect(pointPic5) and car25==True :
        car2Score += 2
        car25 = False
    if car2.colliderect(pointPic6) and car26==True :
        car2Score += 2
        car26 = False
    if car2.colliderect(pointPic7) and car27==True :
        car2Score += 2
        car27 = False
    if car2.colliderect(pointPic8) and car28==True :
        car2Score += 2
        car28 = False
    if car2.colliderect(pointPic9) and car29==True :
        car2Score += 2
        car29 = False
    if car2.colliderect(pointPic10) and car210==True :
        car2Score += 2
        car210 = False
    if car2.colliderect(pointPic11) and car211==True :
        car2Score += 2
        car211 = False
    if car2.colliderect(pointPic12) and car212==True :
        car2Score += 2
        car212 = False  




















def on_mouse_down(pos,button) :
    global gameMenu
    if icons.collidepoint(pos) and button == mouse.LEFT :
        gameMenu = True
    print(pos)



pgzrun.go()
