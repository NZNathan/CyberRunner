from Collision import Collision 

class Player:
    
    #Constants
    PLAYER_COLOR = "#ffffff"#"#3659B7"
    PLAYER_STROKE = "#185797"
    PLAYER_SIZE = 50
    
    #Variables
    playerY = 0
    playerX = 0
    playerYTop = 0
    playerYBot = 0
    collider = None
    
    #Remain variables
    xVariance = 0
    yVariance = 0
    dir = 1

    
    def __init__(self, playerX, playerY, borderSize, playerSize = PLAYER_SIZE):
        self.xVariance = random(0, 4)
        self.yVariance = random(0, 4)
        self.PLAYER_SIZE = playerSize
        self.playerX = playerX - self.PLAYER_SIZE/2
        self.playerY = playerY - self.PLAYER_SIZE/2
        self.playerYBot = height-borderSize-self.PLAYER_SIZE/2
        self.playerYTop = borderSize+self.PLAYER_SIZE/2
        self.collider = Collision(self.playerX, self.playerY, self.PLAYER_SIZE, self.PLAYER_SIZE)
        
    def drawPlayer(self):
        pushMatrix()
        fill(self.PLAYER_COLOR)
        strokeWeight(3)
        if(self.PLAYER_SIZE == 50):
            stroke(self.PLAYER_STROKE)
        else:
            noStroke()    
        self.collider = Collision(self.playerX, self.playerY, self.PLAYER_SIZE, self.PLAYER_SIZE)
        rect(self.playerX, self.playerY, self.PLAYER_SIZE, self.PLAYER_SIZE)  
        popMatrix()  