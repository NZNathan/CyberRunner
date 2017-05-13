


class Button:
    add_library('minim')
    
    #Constants
    BTN_COLOR = "#000000"
    BTN_HIGHLIGHT = "#000000"
    BTN_STROKE = "#cb602b"
    TEXT_COLOR = "#ffffff"
    BTN_STROKEHIGH = "#185797"
    BTN_WIDTH = 300
    BTN_HEIGHT = 75
        
    #Variables
    name = ""
    x = 0
    y = 0
    btnWidth = 0
    btnHeight = 0
    highlight = False
    
    def __init__(self, name, x, y, btnWidth = BTN_WIDTH, btnHeight = BTN_HEIGHT):
        self.x = x
        self.y = y
        self.name = name
        self.btnWidth = btnWidth
        self.btnHeight = btnHeight
    
            
    def drawBtn(self):
        pushMatrix()
        gap = (len(self.name) * 24)/3.5
        if(self.highlight):
            stroke(self.BTN_STROKEHIGH)
            fill(self.BTN_HIGHLIGHT)
        else:
            stroke(self.BTN_STROKE)
            fill(self.BTN_COLOR)
       
        strokeWeight(3)
        rect(self.x, self.y, self.btnWidth, self.btnHeight)
        fill(self.TEXT_COLOR)
        textSize(24)
        text(self.name, self.x+self.btnWidth/2-gap,self.y+self.btnHeight/2+6)
        popMatrix()
     
           
    def checkClicked(self, x, y):
        if(x > self.x and x < self.x + self.btnWidth):
            if(y > self.y and y < self.y + self.btnHeight):
                return self.name  
        return None 
    
     
    def highlightBtn(self, h):
        self.highlight = h                