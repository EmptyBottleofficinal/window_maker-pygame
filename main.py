try:
    import pygame
    import random
    import os
    color1=input("color 1:random 2:choose")
    if color1 == "1":
        colorall=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    if color1 == "2":
        color1=input("rgb red:")
        color2=input("rgb green:")
        color3=input("rgb blue:")
        color1=int(color1)
        color2=int(color2)
        color3=int(color3)
        colorall=(color1,color2,color3)
    dis1=input("display 1:random 2:choose")
    if dis1=="1":
        dis1=random.randint(100,900)
        dis2=random.randint(100,900)
    if dis1=="2":
        dis1=input("display 1:")
        dis2=input("display 2:")
        dis1=int(dis1)
        dis2=int(dis2)
    cap=input("caption:")
    pygame.init()
    win=pygame.display.set_mode((dis1,dis2))
    pygame.display.set_caption(cap)
    run=True
    while run:
        for ev in pygame.event.get():
            if ev.type==pygame.QUIT:
                run=False
        win.fill(colorall)
        pygame.display.flip()
    pygame.quit()
    if run==False:
        with open("r.txt","w") as e:
            e.write("hello")
except:
    print('error something is wrong')