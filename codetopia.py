from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

'''
Versie 15
Kaart:

+--------------------------------------------------* Hoekpunt 127.7, 127.7 (x,z)
|................|................|................|
|................|................|................|
|................|................|................|
|................|................|................|
|................|................|................|
|................|................|................|
|................|................|................|
+--------------------------------------------------+
|................|................|................|
|................|................|................|
|................|................|................|         |Q7,Q8,Q9
|................|....CoderTopia..|................|         |Q4,Q5,Q6
|................|.StevePi..raket.|................|        x|Q1,Q2,Q3
|................|................|Bloem...........|         |________
|................|..Bieb....Altaar|Hondje..........|            z
+--------------------------------------------------+
|................|................|................|
|................|................|................|       90 bij 90
|................|...Zwembad?.....|................|
|................|................|................|
|................|................|................|
|................|................|................|
|................|................|................|
+--------------------------------------------------* hoekpunt -127.7,127.7(x,z)

'''

def resetSpeelveld():
    mc.postToChat("Dit gaat even duren...")
    time.sleep(0.5)
    #Zorg ervoor dat de speler geen aanpassingen meer kan maken
    mc.setting("world_immutable", True)
    #maak het speelveld leeg
    mc.setBlocks(-127.7       ,-0 ,-127.7        ,
                      127.7       ,100 , 127.7        , 0)
    #Maak een stuk land
    mc.setBlocks(-127.7 +  90 ,-1 ,-127.7 +  90  ,
                     -127.7 + 180 ,  0 ,-127.7 + 180  , 2) #Toplaag gras Q5

    mc.setBlocks(-127.7 +  90 ,-10 ,-127.7 +  90  ,
                     -127.7 + 180 ,  -1 ,-127.7 + 180  , 3) #bodemlaag Dirt Q5
    
    mc.setBlocks(-127.7 +  90 ,-10 ,-127.7 + 180  ,
                     -127.7 + 180 ,  0 ,-127.7 + 270  ,12) #zand Q6
    
    mc.setBlocks(-127.7,-10 ,-127.7 +90 ,
                     -127.7 + 90 ,  0 ,-127.7 + 180  ,12) #obsidian Q2
    
    mc.setBlocks(-127.7,-10 ,-127.7 ,
                     -127.7 +  89,  0 ,-127.7 + 89  ,9) #Water Q1
    
    #breng speler naar het midden van het scherm
    mc.player.setPos(8 ,1 ,23)

def checkPositie(x ,y ,z):
    checkx ,checky ,checkz = mc.player.getPos()
    if (x > checkx-2 and x < checkx +2) and (y > checky-2 and y < checky+2) and (z > checkz-2 and z<checkz + 2):
        return True
    else:
        return False

def codetopia():
        X = 41 #goud


        C = [[0,X,X,X,0,0,0,X,X,X,0,0,X,X,X,X,0,0,X,X,X,X,X,0,X,X,X,X,X,0,0,X,X,X,0,0,X,X,X,X,0,0,0,0,X,0,0,0,0,0,X,0,0],
                [X,0,0,0,X,0,X,0,0,0,X,0,X,0,0,0,X,0,X,0,0,0,0,0,0,0,X,0,0,0,X,0,0,0,X,0,X,0,0,0,X,0,0,0,X,0,0,0,0,X,0,X,0],
                [X,0,0,0,0,0,X,0,0,0,X,0,X,0,0,0,X,0,X,0,0,0,0,0,0,0,X,0,0,0,X,0,0,0,X,0,X,0,0,0,X,0,0,0,X,0,0,0,X,0,0,0,X],
                [X,0,0,0,0,0,X,0,0,0,X,0,X,0,0,0,X,0,X,X,X,0,0,0,0,0,X,0,0,0,X,0,0,0,X,0,X,X,X,X,0,0,0,0,X,0,0,0,X,0,0,0,X],
                [X,0,0,0,0,0,X,0,0,0,X,0,X,0,0,0,X,0,X,0,0,0,0,0,0,0,X,0,0,0,X,0,0,0,X,0,X,0,0,0,0,0,0,0,X,0,0,0,X,X,X,X,X],
                [X,0,0,0,X,0,X,0,0,0,X,0,X,0,0,0,X,0,X,0,0,0,0,0,0,0,X,0,0,0,X,0,0,0,X,0,X,0,0,0,0,0,0,0,X,0,0,0,X,0,0,0,X],
                [0,X,X,X,0,0,0,X,X,X,0,0,X,X,X,X,0,0,X,X,X,X,X,0,0,0,X,0,0,0,0,X,X,X,0,0,X,0,0,0,0,0,0,0,X,0,0,0,X,0,0,0,X]]

        x= -15
        startx = x
        y = 15
        z = -10
        for rij in reversed(C):
                for kleur in rij:
                        mc.setBlock(x, y, z,kleur)
                        x += 1
                y +=1
                x = startx
def HuisTom():
    x1 =20
    y1 =0
    z1 =-64
    x2 =53
    y2 =8
    z2 =-32
    block=45 #id 45 is eenbaksteen.
    mc.setBlocks(x1,y1,z1,x2,y2,z2,block)
    #De binnenkant van het huis moet leeg zijn.
    mc.setBlocks(x1+1,y1+1,z1+1,x2-1,y2-1,z2-1,0) #Het blockID 0 is lucht, oftewel niets!
    #Zet een boekenkast in het huis neer.
    mc.setBlocks(21,1,-63,21,7,-58,47)
    mc.setBlocks(21,1,-63,26,7,-63,47)
    mc.setBlocks(52,1,-63,47,7,-63,47)
    mc.setBlocks(52,1,-63,52,7,-58,47)  
##  #Zet een kist in het huis neer.
##  mc.setBlock(x,y,z,54)
    #Zet een tafel in het huis neer.
    mc.setBlock(52,1,-33,58)
    mc.setBlock(21,1,-33,58)
 #light gefent dak
    block=89
    mc.setBlocks(x1,y2,z1,x2,y2,z2,block)

    #een deur
    mc.setBlocks(36,1,-32,35,2,-32,0)
    #een deur
    mc.setBlock(36,1,-32,64,1)
    mc.setBlock(36,2,-32,64,8)
    mc.setBlock(35,1,-32,64,4)
    mc.setBlock(35,2,-32,64,8)

    #een raaam
    mc.setBlocks(40,3,-32,47,6,-32,20)


        #EEN RAAM
    mc.setBlocks(31,3,-32,24,6,-32,20)
    #Typ hier onder het volgende: Huis()
    mc.setBlock(71,5,-9,58)

        #een vloer
    block=5
    mc.setBlocks(x1,y1,z1,x2,y1,z2,block)

    #Boekenkasten
    mc.setBlocks(24,1,-36,30,3,-36,47)
    mc.setBlocks(24,1,-39,30,3,-39,47)
    mc.setBlocks(24,1,-42,30,3,-42,47)
    mc.setBlocks(24,1,-45,30,3,-45,47)
    mc.setBlocks(24,1,-48,30,3,-48,47)
    mc.setBlocks(44,1,-36,50,3,-36,47)
    mc.setBlocks(44,1,-39,50,3,-39,47)
    mc.setBlocks(44,1,-42,50,3,-42,47)
    mc.setBlocks(44,1,-45,50,3,-45,47)
    mc.setBlocks(44,1,-48,50,3,-48,47)
def HuisChristian():
    Steen=57
    fakkel=50
    Lucht=0
    mc.setBlocks(-10, 0, -30, -15, 4, -24, Steen)      #vervang de argumenten x1,y1,z1 etc. door jouw getallen. 
    #De binnenkant moet eruit
    mc.setBlocks(-10-1, 1, -30+1, -15+1, 4-1, -24-1, Lucht) #vervang de argumenten x1,y1,z1 etc. door jouw getallen.

    #Deur
    mc.setBlock(-13,2,-24,Lucht)
    mc.setBlock(-13,1,-24,64,0)#Deur
    mc.setBlock(-13,2,-24,64,8)#Deur
    ##mc.setBlock(2,2,4,64,8)#Deur2)
    #twee fakkels
    mc.setBlock(-11,2,-29,fakkel)
    mc.setBlock(-14,2,-29,fakkel)

def Skelet():
        #Opdracht, hoe zorg je ervoor dat de andere kant van Sans ook wordt geplaatst?
        Q = 35,3 #Lichtblauw
        V = 35,11 #Blauw
        I = 35,15 #Zwart
        B = 35,0 #Wit
        C = [[0,0,0,0,0,0,I,I,I,I,I],
        [0,0,0,0,I,I,B,B,B,B,B],
        [0,0,0,I,B,B,B,B,B,B,B],
        [0,0,0,I,B,B,B,B,B,B,B],
        [0,0,I,B,B,I,I,B,B,B,B],
        [0,0,I,B,B,I,I,B,B,B,B],
        [0,0,I,B,B,B,B,B,B,B,I],
        [0,0,0,I,B,B,B,B,B,I,I],
        [0,0,0,I,B,I,B,B,B,B,B],
        [0,0,I,B,B,I,I,I,I,I,I],
        [0,0,I,B,B,B,I,B,I,B,I],
        [0,0,I,B,B,B,B,I,I,I,I],
        [0,0,0,I,I,B,B,B,B,B,B],
        [0,0,0,I,I,I,I,I,I,I,I],
        [0,0,I,V,I,V,V,V,V,I,Q],
        [0,I,V,V,V,I,V,V,V,I,Q],
        [0,I,V,I,I,V,I,I,V,I,Q],
        [I,V,V,V,V,I,V,V,V,I,Q],
        [I,V,V,V,V,V,I,V,V,I,Q],
        [I,V,V,V,V,I,V,V,V,I,Q],
        [0,I,V,V,V,I,V,V,V,I,Q],
        [0,0,I,V,V,I,V,V,V,I,Q],
        [0,0,0,I,I,I,V,V,V,I,Q],
        [0,0,0,I,I,I,I,I,I,I,Q],
        [0,0,0,I,I,I,I,I,I,I,I],
        [0,0,I,I,I,I,I,I,I,I,I],
        [0,0,I,I,I,I,I,I,I,I,0],
        [0,0,0,I,I,I,I,I,I,0,0],
        [0,I,I,I,B,B,B,B,I,0,0],
        [0,I,B,B,B,B,B,B,I,0,0],
        [0,0,I,I,I,I,I,I,0,0,0,]]
        x= -19
        startx = x
        y = 1
        z = 52
        for rij in reversed(C):
                 for kleur in rij:
                         mc.setBlock(x, y, z,kleur)
                         x += 1
                 y +=1
                 x = startx
        C = [[0,0,0,0,0,0,I,I,I,I,I],
        [0,0,0,0,I,I,B,B,B,B,B],
        [0,0,0,I,B,B,B,B,B,B,B],
        [0,0,0,I,B,B,B,B,B,B,B],
        [0,0,I,B,B,I,I,B,B,B,B],
        [0,0,I,B,B,I,I,B,B,B,B],
        [0,0,I,B,B,B,B,B,B,B,I],
        [0,0,0,I,B,B,B,B,B,I,I],
        [0,0,0,I,B,I,B,B,B,B,B],
        [0,0,I,B,B,I,I,I,I,I,I],
        [0,0,I,B,B,B,I,B,I,B,I],
        [0,0,I,B,B,B,B,I,I,I,I],
        [0,0,0,I,I,B,B,B,B,B,B],
        [0,0,0,I,I,I,I,I,I,I,I],
        [0,0,I,V,I,V,V,V,V,I,Q],
        [0,I,V,V,V,I,V,V,V,I,Q],
        [0,I,V,I,I,V,I,I,V,I,Q],
        [I,V,V,V,V,I,V,V,V,I,Q],
        [I,V,V,V,V,V,I,V,V,I,Q],
        [I,V,V,V,V,I,V,V,V,I,Q],
        [0,I,V,V,V,I,V,V,V,I,Q],
        [0,0,I,V,V,I,V,V,V,I,Q],
        [0,0,0,I,I,I,V,V,V,I,Q],
        [0,0,0,I,I,I,I,I,I,I,Q],
        [0,0,0,I,I,I,I,I,I,I,I],
        [0,0,I,I,I,I,I,I,I,I,I],
        [0,0,I,I,I,I,I,I,I,I,0],
        [0,0,0,I,I,I,I,I,I,0,0],
        [0,I,I,I,B,B,B,B,I,0,0],
        [0,I,B,B,B,B,B,B,I,0,0],
        [0,0,I,I,I,I,I,I,0,0,0,]]
        x= -9
        startx = x
        y = 1
        z = 52
        for rij in reversed(C):
                 for kleur in reversed(rij):
                         mc.setBlock(x, y, z,kleur)
                         x += 1
                 y +=1
                 x = startx

def portaal(x,y,z):
        mc.setBlocks(x   ,y  ,z  ,x + 2  ,y + 3  ,z   ,247)
        mc.setBlocks(x+1 ,y  ,z  ,x + 1  ,y + 2  ,z   , 0)

def hond():
        B = 35,0
        I = 35,15
        C = [[0,0,I,0,I,I,I,I,0,I,0,0,0,0,0,0,0,0,0,0],
                [0,I,B,I,B,B,B,B,I,B,I,0,0,0,0,0,0,0,0,0],
                [0,I,B,B,B,B,B,B,B,B,I,0,0,0,0,0,0,0,0,0],
                [0,I,B,B,B,B,B,B,B,B,B,I,0,0,0,0,0,0,I,0],
                [I,B,B,I,B,B,I,B,B,B,B,I,I,0,0,0,0,I,B,I],
                [I,B,B,B,B,B,B,B,B,B,B,B,B,I,I,0,0,I,B,I],
                [I,B,B,B,I,I,B,B,B,B,B,B,B,B,B,I,I,I,B,I],
                [I,B,I,B,I,B,B,I,B,B,B,B,B,B,B,B,B,B,B,I],
                [I,B,B,I,I,I,I,B,B,B,B,B,B,B,B,B,B,B,B,I],
                [I,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,I],
                [I,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,I],
                [I,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,I],
                [I,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,I],
                [I,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,I,0],
                [0,I,B,B,B,B,B,B,I,I,I,I,B,B,B,B,B,B,I,0],
                [0,I,B,B,I,I,B,B,I,0,0,I,B,B,I,I,B,B,I,0],
                [0,I,B,B,I,I,B,B,I,0,0,I,B,B,I,I,B,B,I,0],
                [0,I,B,I,0,I,B,I,0,0,0,I,B,I,0,I,B,I,0,0],
                [0,0,I,0,0,0,I,0,0,0,0,0,I,0,0,0,I,0,0,0]]
        x= -34
        startx = x
        y = 1
        z = -34
        for rij in reversed(C):
                for kleur in rij:
                        mc.setBlock(x, y, z,kleur)
                        x += 1
                y +=1
                x = startx

def Mario():
        B = 35,11
        R = 35,14
        P = 35,6
        S = 35,12
        W = 35,0
        C = [[0,0,R,R,R,R,0,0],
                [0,0,R,R,R,W,R,0],
                [0,0,P,B,P,B,0,0],
                [0,0,P,P,S,S,0,0],
                [P,R,B,R,R,B,R,P],
                [0,0,B,B,B,B,0,0],
                [0,0,B,B,B,B,0,0],
                [0,0,B,B,B,B,0,0],
                [0,0,S,0,0,S,0,0]]
        x= -12
        startx = x
        y = 5
        z = -27
        for rij in reversed(C):
                for kleur in rij:
                        mc.setBlock(x, y, z,kleur)
                        x += 1
                y +=1
                x = startx

def StevePi():
    #Gemaakt door Merijn.
    x = -17
    y = 1
    z = 0
    #GOUD
    goud = 57
    #informatieblokje
    mc.setBlock(x+1,0,z+3,89)
    #voeten
    mc.setBlock(x+0,y+0,z,goud)
    mc.setBlock(x+1,y+0,z,goud)
    mc.setBlock(x+2,y+0,z,goud)

    mc.setBlock(x+0,y+1,z,goud)
    mc.setBlock(x+1,y+1,z,goud)
    mc.setBlock(x+2,y+1,z,goud)

    mc.setBlock(x+0,y+2,z,goud)
    mc.setBlock(x+1,y+2,z,goud)
    mc.setBlock(x+2,y+2,z,goud)

    mc.setBlock(x+0,y+3,z,goud)
    mc.setBlock(x+1,y+3,z,goud)
    mc.setBlock(x+2,y+3,z,goud)

    mc.setBlock(x+0,y+4,z,goud)
    mc.setBlock(x+1,y+4,z,goud)
    mc.setBlock(x+2,y+4,z,goud)

    mc.setBlock(x+0,y+5,z,goud)
    mc.setBlock(x+1,y+5,z,goud)
    mc.setBlock(x+2,y+5,z,goud)

    mc.setBlock(x+0,y+6,z,35,6)
    mc.setBlock(x+1,y+6,z,35,6)
    mc.setBlock(x+2,y+6,z,35,6)

    #HOOFD
    mc.setBlock(x+0,y+7,z,goud)
    mc.setBlock(x+1,y+7,z,35,14)
    mc.setBlock(x+2,y+7,z,goud)

    mc.setBlock(x+0,y+8,z,35,5)
    mc.setBlock(x+1,y+8,z,goud)
    mc.setBlock(x+2,y+8,z,35,5)

    mc.setBlock(x+0,y+9,z,35,12)
    mc.setBlock(x+1,y+9,z,35,12)
    mc.setBlock(x+2,y+9,z,35,12)
    #Arm links
    mc.setBlock(x-1,y+4,z,goud)
    mc.setBlock(x-2,y+4,z,goud)
    mc.setBlock(x-1,y+5,z,goud)
    mc.setBlock(x-2,y+5,z,goud)
    mc.setBlock(x-1,y+6,z,goud)
    mc.setBlock(x-2,y+6,z,goud)
    #Hand links

    #Arm rechts
    mc.setBlock(x+3,y+4,z,goud)
    mc.setBlock(x+4,y+4,z,goud)
    mc.setBlock(x+3,y+5,z,goud)
    mc.setBlock(x+4,y+5,z,goud)
    mc.setBlock(x+3,y+6,z,goud)
    mc.setBlock(x+4,y+6,z,goud)

def Raket(hoehoog=0):
    mc.setBlocks(2,-8+hoehoog,2,8,2+hoehoog,8,0)
    mc.setBlocks(3,-7+hoehoog,5,7,-4+hoehoog,5,98,98)
    mc.setBlocks(5,-8+hoehoog,4,5,-5+hoehoog,6,35,15)
    mc.setBlocks(3,-5+hoehoog,3,7,-4+hoehoog,7,35,7)
    mc.setBlocks(4,-3+hoehoog,4,6,0+hoehoog,6,35,8)
    mc.setBlocks(4,-3+hoehoog,5,6,0+hoehoog,6,35,30)
    mc.setBlock(5,1+hoehoog,5,35,14)
    mc.setBlock(5,2+hoehoog,5,50)#35,6 is de kleur rood!

    #lanceerblokje
    mc.setBlock(5,0,12,89)
def zwembad():
    #Gemaakt door Noa
    x=33
    y=0
    z=8
    x2=38
    y2=-2
    z2=-1
    steen=82
    mc.setBlocks(x,y,z,x2,y2,z2,steen)
    x=33+1
    y=0
    z=8-1
    x2=38-1
    y2=-1
    z2=-1+1
    water=8
    mc.setBlocks(x,y,z,x2,y2,z2,water)

    duikplank=44,0
    trap=67,1
    mc.setBlock(38,1,2,trap)
    mc.setBlock(37,2,2,duikplank)
    #De hoge duikplank
    paal=1
    mc.setBlock(39,1,4,paal)
    mc.setBlock(39,2,4,paal)
    mc.setBlock(39,3,4,paal)
    mc.setBlock(39,4,4,paal)
    mc.setBlock(39,5,4,paal)
    mc.setBlock(39,6,4,paal)
    mc.setBlock(38,7,4,duikplank)
    mc.setBlock(37,7,4,duikplank)
    mc.setBlock(36,7,4,duikplank)
    #ladder
    mc.setBlock(40,1,4,65,5)
    mc.setBlock(40,2,4,65,5)
    mc.setBlock(40,3,4,65,5)
    mc.setBlock(40,4,4,65,5)
    mc.setBlock(40,5,4,65,5)
    mc.setBlock(40,6,4,65,5)
def Bloem():
        Q = 35,5
        V = 35,4
        I = 35,15
        B = 35,0
        C = [[0,0,0,0,0,0,I,I,I,0,0,0,I,I,I,0,0,0,0,0,0],
                [0,0,0,0,0,I,V,V,V,I,I,I,V,V,V,I,0,0,0,0,0],
                [0,0,0,0,I,V,V,I,I,B,B,B,I,I,V,V,I,0,0,0,0],
                [0,0,I,I,I,I,I,B,B,B,B,B,B,B,I,I,I,I,I,I,0],
                [0,I,V,V,V,I,B,B,B,I,B,I,B,B,B,I,V,V,V,I,0],
                [I,V,V,V,V,I,B,B,B,B,B,B,B,B,B,I,V,V,V,V,I],
                [0,I,V,V,V,I,B,B,I,B,B,B,I,B,B,I,V,V,V,I,0],
                [0,0,I,I,I,V,I,B,B,I,I,I,B,B,I,V,I,I,I,0,0],
                [0,0,0,I,V,V,V,I,B,B,B,B,B,I,V,V,V,I,0,0,0],
                [0,0,I,V,V,V,V,V,I,I,I,I,I,V,V,V,V,V,I,0,0],
                [0,0,I,V,V,V,V,V,V,I,Q,I,V,V,V,V,V,V,I,0,0],
                [0,0,0,I,V,V,V,I,I,Q,Q,I,I,I,V,V,V,I,0,0,0],
                [0,0,0,0,I,I,I,0,I,Q,Q,I,0,0,I,I,I,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,I,Q,Q,I,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,I,Q,I,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,I,Q,Q,I,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,I,Q,I,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,I,Q,Q,I,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,I,Q,Q,I,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,I,Q,Q,Q,I,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,I,I,I,0,0,0,0,0,0,0,0,0]]
        x= -54
        startx = x
        y = 1
        z = -36
        for rij in reversed(C):
                 for kleur in rij:
                         mc.setBlock(x, y, z,kleur)
                         x += 1
                 y +=1
                 x = startx
def mijnMijn():
    #gemaakt door nesheira
    x      =5
    y      =0
    z      =30


    #Geef de afmetigen van de balk op
    breedte=12        #getal
    hoogte =12        #getal
    lengte =12        #getal
    bloknr =42       #Irom Block


    #Zet de blokken neer
    mc.setBlocks(x,y,z,x+breedte,y+hoogte,z+lengte,bloknr)

    #Geef de afmetigen van de balk op
    breedte=10        #gatal
    hoogte =10        #getal
    lengte =10        #getal
    bloknr =0        #LUCHT


    #Zet de blokken neer
    mc.setBlocks(x+1,y+1,z+1,x+1+breedte,y+1+hoogte,z+1+lengte,bloknr)
    #-5,1,22
    glas=20
    for i in range(0,6):
        mc.setBlock(10-i,1+i,42,glas)
        mc.setBlock(5,1+i,37+i,glas)
        mc.setBlock(12+i ,1+i,30,glas)
    for i in range(0,7):
        mc.setBlock(x,2+i,36-i,glas)
        mc.setBlock(12-i ,1+i,30,glas)
        mc.setBlock(10+i ,1+i,42,glas)
        mc.setBlock(17,2+i,36+i,glas)
    for i in range(0,5):  
        mc.setBlock(17 ,1+i,35-i,glas)
    #deur
    mc.setBlock(7,1,30,0) #0 is lucht!
    mc.setBlock(7,2,30,0) #0 is lucht!
    HoogBankje= 5 #Een heel blokje van hout!
    LaagBankje=44,2 #Een half blokje van hout!
    Leuning=53 #Een trapvormig blokje van hout!
    #Nesheira mag haar huis zelf inrichten!
    mc.setBlock(11,1,36,HoogBankje)
    mc.setBlock(12,1,36,LaagBankje)
    mc.setBlock(13,1,36,Leuning)


    mc.setBlock(6,1,29,37)#Gele bloem
    mc.setBlock(8,1,29,38) #Roze bloem

def kasteel():
        '''We gaan een kasteel bouwen, te beginnen met 4 muren
        Daarna een slotgracht, een binnenplein, een loopbrug en een poort
        Daarnaast willen we hier en daar nog wat bomen, wie helpt daarmee?'''
        #Bouw 4 muren.
        block = 98 #Steen
        mc.setBlocks( 70 , 0 , -67 ,72 ,5 , -82 ,block)
        mc.setBlocks( 69, 0 , -66 ,54 ,5 ,-68 ,block)
        mc.setBlocks(53 , 0 ,-65 , 51 ,5 ,-82 ,block)
        mc.setBlocks( 72 , 0 , -82, 51 ,5 , -84 ,block)
        #Maak een poort
        block = 85 #iron bars
        mc.setBlocks(63 ,0 , -67 , 60 ,4 ,-67 ,block)
        mc.setBlocks(63,0,-68,60,3,-68,0)
        mc.setBlocks(63,0,-66,60,3,-66,0)


        mc.setBlock(59,0,-71,5)
        mc.setBlock(57,1,-71,5)
        mc.setBlock(55,2,-72,5)
        mc.setBlock(54,2,-75,85)
        mc.setBlock(54,2,-74,85)
        mc.setBlock(56,3,-76,5)
        mc.setBlock(58,4,-75,57)
        mc.setBlock(58,5,-78,57)
        mc.setBlock(58,4,-77,65)
        mc.setBlock(58,4,-81,57)
        mc.setBlock(57,6,-77,57)
        mc.setBlock(57,5,-77,57)
        mc.setBlocks(64,5,-78,65,5,-79,57)
        mc.setBlocks(64,4,-73,65,4,-75,57)
        mc.setBlocks(69,4,-68,69,4,-69,57)
        mc.setBlock(67,5,-70,57)
        mc.setBlock(65,4,-70,57)

def Smilie():
    x=-1
    y=1
    z=-26
    blokken = [[0,0,22,22,22,22,0,0],
             [0,22,35,35,35,35,22,0],
             [22,35,22,35,35,22,35,22],
             [22,35,35,35,35,35,35,22],
             [22,35,22,35,35,22,35,22],
             [22,35,35,22,22,35,35,22],
             [0,22,35,35,35,35,22,0],
             [0,0,22,22,22,22,0,0]]

    for rij in reversed(blokken):
        for blok in rij:
            mc.setBlock(x,y,z,blok)
            x += 1
        y += 1
        x = -1
    y=1
    time.sleep(6)
    B=35,14
    blokken = [[0,0,22,22,22,22,0,0],
             [0,22,35,35,35,35,22,0],
             [22,35,B,35,35,B,35,22],
             [22,35,35,35,35,35,35,22],
             [22,35,35,B,B,35,35,22],
             [22,35,B,35,35,B,35,22],
             [0,22,22,35,35,22,22,0],
             [0,0,22,22,22,22,0,0]]

    for rij in reversed(blokken):
        for blok in rij:
            mc.setBlock(x,y,z,blok)
            x += 1
        y += 1
        x = -1
    y=1
    time.sleep(6)
    B=35,14
    blokken = [[0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],  
             [0,0,0,0,0,0,0,0]]

    for rij in reversed(blokken):
        for blok in rij:
            mc.setBlock(x,y,z,blok)
            x += 1
        y += 1
        x = -1
'''Vanaf hier gaan we programmeren!'''
resetSpeelveld()
codetopia()
HuisTom()
hond()
portaal(11.6,1,-9)
portaal(4.9,1,-9.3)
portaal(-1.9,1,-9.5)
portaal(36.8,1,-62.6)
portaal(21,1,-10)
portaal(60,6,-67)
portaal(16,1,-10)

mc.setBlock(5.5, 5, -9.6, 37) #naar de Bloem/Hond
mc.setBlock(12.6, 5, -8.7, 47) #naar de Bieb
mc.setBlock(22, 5, -10, 98) #naar het kasteel
mc.setBlock(-1, 5, -10, 35,14) #naar het Altaar
StevePi()
Raket()
Bloem()
HuisChristian()
Mario()
kasteel()
mijnMijn()
zwembad()
Skelet()
mc.setBlock(1,0,-22,41)
'''Hier staan alle dingen die bewegen en actief zijn'''
stevepi=0
raket=0
altaar=0
gezwommen=0
while True:
    if checkPositie(11.6,1,-9):
        x=36
        y=1
        z=-33
        mc.player.setTilePos(x,y,z)
        mc.postToChat("welkom in de bibliotheek!")

    if checkPositie(61,5,-67):
        x=13
        y=1
        z=15
        mc.player.setTilePos(x,y,z)
        mc.postToChat("doei :-) !")
    if checkPositie(1,1,-22):
        Smilie()

    if checkPositie(17,1,-9.7):
        x=7
        y=1
        z=19
        mc.player.setTilePos(x,y,z)
        mc.postToChat("welkom bij het huis")


    if checkPositie(5,1,-10):
        x=-26
        y=1
        z=-20
        mc.player.setTilePos(x,y,z)
        mc.postToChat("welkom bij de HOND en de BLOEM")
    if checkPositie(21.4,1,-9.6):
        x=61.7
        y=0
        z=-64.5

        mc.player.setTilePos(x,y,z)
        mc.postToChat("welkom in HET KASTEEL!")
    if checkPositie(36.8,1,-62.6):
        x=5.7
        y=1
        z=-1
        mc.player.setTilePos(x,y,z)
        mc.postToChat("doei :-)!")

    if checkPositie(-0.5,1,-9.3):
        x=-12.5,
        y=1
        z=-15.6
        mc.player.setTilePos(x,y,z)
        mc.postToChat("welkom bij het mario altaar :-)")
    if checkPositie(-16,1,3) and stevepi==0:
        mc.postToChat("Dit is een standbeeld voor StevePi!")
        stevepi=1
    if checkPositie(-13,1,-27) and altaar==0:
        mc.postToChat("Hier is het Altaar van Mario")
        altaar=1
    if checkPositie(36,0,4) and gezwommen==0:
        mc.postToChat("Plons")
        gezwommen=1
    while checkPositie(5,1,12) and raket==0:
        mc.postToChat("Klaar voor lancering?")
        time.sleep(2)
        for i in range(3,1,-1):
            mc.postToChat("Nog "+str(i)+" seconden voor de lancering")
            time.sleep(1)
        mc.postToChat("Nog 1 seconde")
        time.sleep(1)
        mc.postToChat("We have a lift off")
        for i in range(0,50):
            Raket(i)
            time.sleep(0.3)
            mc.setBlocks(2,-8+i,2,8,2+i,8,0) #Alles weer weghalen    
            if (i <10):
                mc.setBlock(5,-8+i,5,11)
        raket=1
    #spelletje in de bieb
    x,y,z=mc.player.getPos()
    while (46>x>27) and (2>y>0) and (-33>z>-53):
        for i in range(0,20):
            mc.setBlock(28+i,1,-46,11) #Laat een blokje lava vliegen
            mc.setBlock(50-i,1,-43,11) #Laat een blokje lava vliegen
            mc.setBlock(45-i,1,-40,11) #Laat een blokje lava vliegen
            mc.setBlock(24+i,1,-41,11) #Laat een blokje lava vliegen
            mc.setBlock(47-i,1,-37,11)

            time.sleep(0.4)
            mc.setBlock(28+i,1,-46,0)#Haal het blokje weer weg
            mc.setBlock(50-i,1,-43,0)#Haal het blokje weer weg
            mc.setBlock(45-i,1,-40,0)#Haal het blokje weer weg
            mc.setBlock(24+i,1,-41,0)#Haal het blokje weer weg
            mc.setBlock(47-i,1,-37,0)
            x,y,z=mc.player.getPos()
    #Controleer of de speler voor de poort staat
    if checkPositie(63 , 0 ,-68) or checkPositie(63,0,-63):
        #Zo ja, open de poort
        block = 0 #air
        mc.setBlocks(63 ,0,-67 ,60 ,0 ,-67 ,block)
        time.sleep(0.5)
        mc.setBlocks(63 ,1 ,-67 ,60 ,1 ,-67 ,block)
        time.sleep(0.5)
        mc.setBlocks(63 ,2 ,-67 ,60 ,2 ,-67 ,block)
        time.sleep(0.5)
        mc.setBlocks(63 ,3 ,-67 ,60 ,3 ,-67 ,block)
    else:
        #Zo nee, doe de poort dicht.
        block=85 #hekwerk
        mc.setBlocks(63 ,3 ,-67 ,60 ,3 ,-67 ,block)
        time.sleep(0.5)
        mc.setBlocks(63 ,2 ,-67 ,60 ,2 ,-67 ,block)
        time.sleep(0.5)
        mc.setBlocks(63 ,1 ,-67 ,60 ,1 ,-67 ,block)
        time.sleep(0.5)
        mc.setBlocks(63 ,0 ,-67 ,60 ,0 ,-67 ,block)