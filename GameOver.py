from Button import Button

class GameOver:
    
    #Constants
    BTN_WIDTH = 300
    BTN_HEIGHT = 75
    GAME_OVER_SIZE = 48
    GAME_OVER_COLOR = "#ffffff"
    SCORE_SIZE = 24
    SCORE_COLOR = "#ffffff"
    
    #Variables
    tryAgainBtn = None
    backBtn = None
    
    score = 0
    
    def __init__(self, score):
        self.score = score
        self.tryAgainBtn = Button("Try Again", 350, 350, self.BTN_WIDTH, self.BTN_HEIGHT)
        self.backBtn = Button("Back", 350, 450, self.BTN_WIDTH, self.BTN_HEIGHT)
        
        
    def drawSelf(self):
        textSize(self.SCORE_SIZE)
        fill(self.SCORE_COLOR)
        text("Score: %.2f seconds" % self.score, 350, 275)
        textSize(self.GAME_OVER_SIZE)
        fill(self.GAME_OVER_COLOR)
        text("Game Over", 300, 200)
        self.tryAgainBtn.drawBtn()
        self.backBtn.drawBtn()
    
        
    def pressed(self, x, y):
            clicked = self.tryAgainBtn.checkClicked(x, y)
            if(clicked == None):
                clicked = self.backBtn.checkClicked(x,y)
            return clicked    
        
    def pressedBtn(self, btn):
        if(btn == "Try Again"):
            self.tryAgainBtn.highlightBtn(True)   
        if(btn == "Back"):
            self.backBtn.highlightBtn(True)     
            
    def release(self):
            self.tryAgainBtn.highlightBtn(False)   
            self.backBtn.highlightBtn(False)             
              