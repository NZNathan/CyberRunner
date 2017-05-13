from Collision import Collision 

class Obstacle:
    
    #Constants
    OBS_COLOR = ["#000000"] #"#407153"
    OBS_STROKE = "#cb602b"
    
    #Variables
    obsWidth = 0
    obsHeight = 0
    obsX = 0
    obsY = 0
    collider = None
    obsColor = None
    
    def __init__(self, obsX, obsY, obsWidth, obsHeight):
        self.obsX = obsX
        self.obsY = obsY
        self.obsWidth = obsWidth
        self.obsHeight = obsHeight
        self.collider = Collision(self.obsX, self.obsY, self.obsWidth, self.obsHeight)
        self.obsColor = self.OBS_COLOR[int(random(0,len(self.OBS_COLOR) ) )]
      
    def drawSelf(self):
        pushMatrix()
        rectMode(CENTER)
        fill(self.obsColor) 
        strokeWeight(3)
        stroke(self.OBS_STROKE)
        rect(self.obsX, self.obsY, self.obsWidth, self.obsHeight)
        self.collider = Collision(self.obsX, self.obsY, self.obsWidth, self.obsHeight)
        popMatrix()    