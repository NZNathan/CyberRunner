

class BG:
    
    BG_COLOR = "#000000" #"#5CA277"
    BG_DARK = "#407153"
    BG_SIZE = 20
    BG_IMAGE = None
    
    x = 0
    borderSize = 0
    scrollSpeed = 0
    tintBg = False
    
    def __init__(self, bs):
        background(self.BG_COLOR)
        self.borderSize = bs
        self.BG_IMAGE = loadImage("BG.png")
        
        
    def drawBG(self):
        clear()
        background(self.BG_COLOR)
        if(self.tintBg):
            tint(255, 50)
        else:
            tint(255, 255)    
        image(self.BG_IMAGE,self.x,100)
        self.x -= self.scrollSpeed
        if(self.x + width < 0):
            self.x = 0
            
            
    def turnTint(self):
        if(self.tintBg):
            self.tintBg = False
        else:
            self.tintBg = True            