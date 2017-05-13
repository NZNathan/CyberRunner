from Button import Button

class Title:
    
    #Constant Variables
    BTN_WIDTH = 300
    BTN_HEIGHT = 75
    TITLE = "CYBER RUNNER"
    TITLE_SIZE = 72
    TITLE_COLOR = "#ffffff"
    
    #Variables
    newGameBtn = None
    docBtn = None
    exitBtn = None
    font = None
    
    
    def __init__(self):
        self.newGameBtn = Button("New Game", 350, 290, self.BTN_WIDTH, self.BTN_HEIGHT)
        self.docBtn = Button("Documentation", 350, 390, self.BTN_WIDTH, self.BTN_HEIGHT)
        self.exitBtn = Button("Exit", 350, 490, self.BTN_WIDTH, self.BTN_HEIGHT)
        self.font = loadFont("Videophreak-56.vlw")
         
    def drawSelf(self):
        textSize(self.TITLE_SIZE)
        textFont(self.font, 72)
        fill(self.TITLE_COLOR)
        text(self.TITLE, 300, 200) 
        self.newGameBtn.drawBtn()
        self.docBtn.drawBtn()
        self.exitBtn.drawBtn()        
                     
    def pressed(self, x, y):
            clicked = self.newGameBtn.checkClicked(x, y)
            if(clicked == None):
                clicked = self.exitBtn.checkClicked(x, y)
            if(clicked == None):
                clicked = self.docBtn.checkClicked(x, y)    
            return clicked 
        
    def pressedBtn(self, btn):
        if(btn == "New Game"):
            self.newGameBtn.highlightBtn(True)    
            
        if(btn == "Documentation"):
            self.docBtn.highlightBtn(True)    
            
        if(btn == "Exit"):
            self.exitBtn.highlightBtn(True)    
            
    def release(self):
        self.newGameBtn.highlightBtn(False)
        self.docBtn.highlightBtn(False)           
        self.exitBtn.highlightBtn(False)    