try:
    import pygame
    import random
    import os
    #get input
    color1=input("color 1:random 2:choose")
    #--------------------------------------
    #color:random 1
    if color1 == "1":
        colorall=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    #--------------------------------------------------------------------------------
    #color:user input 2
    if color1 == "2":
        color1=input("rgb red: (0,225)")
        color2=input("rgb green: (0,225)")
        color3=input("rgb blue: (0,225)")
        color1=int(color1)
        color2=int(color2)
        color3=int(color3)
        colorall=(color1,color2,color3)
    #------------------------------------
    #else
    else:
        print("error: 3 is not allowed")
        exit()
    #-------------------------------------
    #input
    dis1=input("display 1:random 2:choose")
    #-------------------------------------
    #display:random 1
    if dis1=="1":
        dis1=random.randint(100,900)
        dis2=random.randint(100,900)
    #-------------------------------------
    #display:user input 2
    if dis1=="2":
        dis1=input("display 1: (number only)")
        dis2=input("display 2: (number only)")
        dis1=int(dis1)
        dis2=int(dis2)
    #-------------------------------------
    #else
    else:
        print("error: 3 is not allowed")
        exit()
    #-------------------------------------
    #input caption or title (whatever)
    cap=input("caption:")
    #-------------------------------------
    #start
    pygame.init()
    #-------------------------------------
    #display
    win=pygame.display.set_mode((dis1,dis2))
    #---------------------------------------
    #caption or title (whatever)
    pygame.display.set_caption(cap)
    #---------------------------------------
    #run or "un"run
    run=True
    while run:
        for ev in pygame.event.get():
            if ev.type==pygame.QUIT:
                run=False
    #----------------------------------------
    #color
        win.fill(colorall)
        pygame.display.flip()
    #----------------------------------------
    #exit
    pygame.quit()
    #-----------------------------------------------------
    #i made this for no reason at all
    if run==False:
        with open("you made pygame window.txt","w") as e:
            e.write("yay!!")
    #----------------------------------------------------
#error
except:
    print('error something is wrong')
#--------------------------------------------
