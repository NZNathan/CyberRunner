from BG import BG
from Title import Title
from Player import Player
from Obstacle import Obstacle
from Collision import Collision 
from Timer import Timer
from GameOver import GameOver
from Documentation import Documentation
add_library('minim')


#Constants
BORDER_SIZE = 100
PLAYER_SPEED = 5
PLAYER_VEL = 0.5
OBSTACLE_SPEED = 8
SPEED_INCREASE = 1

#Variables
title = None
documentation = None
gameOver = None
timer = None
bg = None
song = None

obstacles = []
obstacleSpeed = OBSTACLE_SPEED
obstacleSpawnTimer = 0
obstacleSpeedTimer = 0

player = None
PlayerUpSpeed = PLAYER_SPEED
playerDownSpeed = PLAYER_SPEED
playing = False
playerRemains = []

gravity = True
spaceReleased = True
time = 0
keyPressTimer = 0
dead = False
tutorial = False
docUp = False
fadeOut = 0


def setup():
    global bg, title
    size(1200,750)
    bg = BG(BORDER_SIZE)
    frameRate(60)
    title = Title()
    
    
    
def draw():
    global playing, bg, playerDownSpeed, playerUpSpeed, time, obstacleSpeed, obstacleSpawnTimer, obstacleSpeedTimer, keyPressTimer
    
    rectMode(CORNER)
    time = (float(millis())/1000)
    bg.drawBG()
    #Border - floor and roof
    fill(0)
    stroke("#185797")
    rect(-10, 0, width+20, BORDER_SIZE)
    rect(-10, height-BORDER_SIZE, width+20, BORDER_SIZE) 
    
    #Controls moving game objects
    if(playing):
        
        rectMode(CENTER)
        if(not dead):
            movePlayer()
        else:
            moveRemains()
            fadeSong() 
            slowBG()
           
        if(not tutorial):  
            
            timer.updateTime()
                  
            #Obstacle Movement
            if(obstacleSpawnTimer < time - 0.5 and not dead):
                obstacleSpawnTimer = time
                createObstacle()
            if(obstacleSpeedTimer < time - 5):
                obstacleSpeedTimer = time
                obstacleSpeed += SPEED_INCREASE    
                bg.scrollSpeed += SPEED_INCREASE  
            moveObstacles()
            if(len(obstacles) == 0):
                playing = False
                bg.turnTint()
        
            if(time - keyPressTimer > 0.6 and keyPressTimer != -1 and not dead):
                sendObstacle()
                keyPressTimer = -1
        else: #Tutorial
            textSize(24)
            fill("#ffffff")
            text("Press Space to invert gravity", 405, height - 50)    
            text("Avoid the obstactles", 460, 50)        

    elif(dead):
        getGameOver()
    elif(docUp):
        getDoc()     
    else: #Game is not playing, player is not dead or alive and doc isn't up
        getTitle()
   

def fadeSong():
    global fadeOut, song
    
    if(fadeOut > -80):
        song.setGain(fadeOut)#song.shiftGain(fadeOut,0, 1000)
        fadeOut -= 1
    else:
        song.pause()
        

def slowBG():
    global bg
    
    if(bg.scrollSpeed > 0):
        bg.scrollSpeed -= 1
        
    else:
        bg.scrollSpeed = 0    

def moveRemains():
    global playerRemains, playerDownSpeed, playerUpSpeed
    
    for p in playerRemains:
        
        p.playerY += PLAYER_SPEED + playerDownSpeed - playerUpSpeed + p.yVariance
            
        if(p.playerY > p.playerYBot):
           p.playerY = p.playerYBot
        else:
           p.playerX += ((PLAYER_SPEED + p.xVariance) * p.dir)/2   
        p.drawPlayer()
        
    playerDownSpeed += PLAYER_VEL
    playerUpSpeed -= PLAYER_VEL
    if(playerUpSpeed < 0 ):
            playerUpSpeed = 0  
 
 
def movePlayer():
    global player, playerDownSpeed, playerUpSpeed
    
    #Player Movement
    if(gravity and player.playerYBot != player.playerY): #Moving down
        player.playerY += PLAYER_SPEED + playerDownSpeed - playerUpSpeed
        playerDownSpeed += PLAYER_VEL
        playerUpSpeed -= PLAYER_VEL
        if(playerUpSpeed < 0 ):
            playerUpSpeed = 0    
    elif(not gravity and player.playerYTop != player.playerY): #Moving Up
        player.playerY -= PLAYER_SPEED + playerUpSpeed - playerDownSpeed
        playerUpSpeed += PLAYER_VEL
        playerDownSpeed -= PLAYER_VEL
        if(playerDownSpeed < 0 ):
            playerDownSpeed = 0
            
    else:
        playerDownSpeed = 0
        playerUpSpeed = 0
            
    if(player.playerY > player.playerYBot):
           player.playerY = player.playerYBot
           playerDownSpeed = 0
                
    if(player.playerY < player.playerYTop):
           player.playerY = player.playerYTop     
           playerUpSpeed = 0               
                           
    player.drawPlayer()
 
 
def sendObstacle():
    global obstacles
    
    w = random(20,100)
    h = random(20,100)
    if(gravity):
        obs = Obstacle(width+w, height-BORDER_SIZE-h, w, h )  
    else:
        obs = Obstacle(width+w, BORDER_SIZE+h/2, w, h ) 
    obstacles.append(obs)
    
    
def createObstacle():
    global obstacles
    
    w = random(20,100)
    h = random(20,100)
    obs = Obstacle(width+w, random(BORDER_SIZE+h/2, height-BORDER_SIZE-h/2),w , h )  
    for o in obstacles:
       if(o.collider.isTouching(obs.collider)):
           obs = Obstacle(width+w, random(BORDER_SIZE+h/2, height-BORDER_SIZE-h/2),w , h )  
    obstacles.append(obs)
        

    
def moveObstacles():
    global obstacles, playing, player, dead, gravity, song, gameOver
    
    for o in obstacles:
        o.obsX -= obstacleSpeed        
        if(o.obsX < 0 - o.obsWidth*5):
            obstacles.remove(o)   
        o.drawSelf()
        if(not dead and o.collider.isTouching(player.collider)): 
                dead = True 
                gravity = True
                #song.pause()
                splitPlayer() 
                timer.stopTime = True
                gameOver = GameOver(timer.getTime()) 

    
def splitPlayer():
    global player, playerRemains
    
    splitAmount = 10
    
    for i in range(0, splitAmount):
        for j in range(0,splitAmount):
            x = player.playerX - player.PLAYER_SIZE/2 + i*player.PLAYER_SIZE/splitAmount
            y = player.playerY - player.PLAYER_SIZE/2 + j*player.PLAYER_SIZE/splitAmount
            p = Player(x,y, BORDER_SIZE, player.PLAYER_SIZE/splitAmount)
            if(i <= 1):
               p.dir = -1.3 + (i*0.3)
            if(i == 3):
                p.dir = 1.3 
            playerRemains.append(p)                                       
    player = None 
    
    
def getGameOver():
    global gameOver
    gameOver.drawSelf()      
             
def getTitle():
    global title
    title.drawSelf() 

def getDoc():
    global documentation
    documentation.drawSelf()    
  
def keyReleased():
    global spaceReleased
    if(key == ' '):
        spaceReleased = True  
  
def keyPressed(evt):
    global spaceReleased, keyPressTimer
    if(key == ' ' and spaceReleased):
        if(not dead and playing):
            spaceReleased = False
            gravitySwap()
            if(tutorial):
                startGame()
            else:    
                keyPressTimer = (float(millis())/1000) 
        elif dead and not playing:
            spaceReleased = False
            bg.turnTint()
            newGame()    
   
    
def gravitySwap():
    global gravity, playerUpSpeed, playerDownSpeed
    
    if(gravity):
        gravity = False
        playerDownSpeed -= PLAYER_VEL
        if(playerDownSpeed < 0 ):
                playerDownSpeed = 0
    else:
        gravity = True
 
        if(playerUpSpeed < 0 ):
                playerUpSpeed = 0  
          
def mousePressed(evt):
    
    if(title != None and mouseButton == LEFT):
        
       clicked = title.pressed(mouseX,mouseY)

       if(clicked != None):
           title.pressedBtn(clicked)
           
    elif(documentation != None and mouseButton == LEFT):
        
        clicked = documentation.pressed(mouseX, mouseY) 
        
        if(clicked != None):
           documentation.pressedBtn(clicked)          
           
    elif(gameOver != None and mouseButton == LEFT):
        
       clicked = gameOver.pressed(mouseX,mouseY)
       
       if(clicked != None):
           gameOver.pressedBtn(clicked)    
                      
                                                            
def mouseReleased(evt):
    global dead, playing, title, docUp, documentation
    minim = Minim(this)
    clickSE = minim.loadFile("btnSE.wav")
    
    if(title != None and mouseButton == LEFT):
        
       clicked = title.pressed(mouseX,mouseY)
       title.release()
       
       if(clicked != None):
            clickSE.play() 
       
       if(clicked == "New Game"):
           tutorialText()
       elif(clicked == "Documentation"):
           docUp = True
           bg.turnTint()   
           title = None
           documentation = Documentation() 
       elif(clicked == "Exit"):
           exit()
           
    elif(documentation != None and mouseButton == LEFT):
        
        clicked = documentation.pressed(mouseX, mouseY)
        documentation.release()
        
        if(clicked != None):
            clickSE.play() 
        
        if(clicked == "Back"):
           title = Title()
           bg.turnTint()
           documentation = None   
           docUp = False     
              
    elif(gameOver != None and mouseButton == LEFT):
        
       clicked = gameOver.pressed(mouseX,mouseY)
       gameOver.release()
       
       if(clicked != None):
           clickSE.play() 
       
       if(clicked == "Try Again"):
           bg.turnTint()
           newGame()
       if(clicked == "Back"):
           bg.turnTint()
           title = Title()
           playing = False   
           dead = False  
                  
   
               
def tutorialText():
    global player, title, playing, obstacles, gravity, song, playerRemains, timer, dead, gameOver, obstacleSpeed, tutorial    
       
    bg.scrollSpeed = 2
    dead = False
    gameOver = None
    minim = Minim(this)
    song = minim.loadFile("Synapsis_-_07_-_Pandora.mp3")
    song.play()
    title = None
    obstacles = []
    obstacleSpeed = OBSTACLE_SPEED
    playerRemains = []
    gravity = True
    player = Player(width/4, height-BORDER_SIZE, BORDER_SIZE) 
    playing = True
    tutorial = True                        
  
         
def startGame():
    global timer, tutorial
    
    timer = Timer()
    tutorial = False    
    
                                        
def newGame():
    global player, title, playing, obstacles, gravity, song, playerRemains, timer, dead, gameOver, obstacleSpeed, fadeOut
    
    bg.scrollSpeed = 2
    dead = False
    gameOver = None
    minim = Minim(this)
    song = minim.loadFile("Synapsis_-_07_-_Pandora.mp3")
    song.setGain(0) 
    song.play()
    timer = Timer()
    title = None
    obstacles = []
    obstacleSpeed = OBSTACLE_SPEED
    playerRemains = []
    gravity = True
    player = Player(width/4, height-BORDER_SIZE, BORDER_SIZE) 
    playing = True 
    fadeOut = 0    