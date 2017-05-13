from Button import Button

class Documentation:
    
    TEXT_SIZE = 20
    HEADING_SIZE = 48
    TEXT_COLOR = "#ffffff"
    
    backBtn = None
    tronImage = None
    
    def __init__(self):
        self.backBtn = Button("Back", 350, 550)
        self.tronImage = loadImage("tron.jpg")
        
        
    def drawSelf(self):
        textSize(self.HEADING_SIZE)
        fill(self.TEXT_COLOR)
        #Game Concepts:
        text("Documentation", 200, 150)   
        #Design Precedents
        textSize(self.TEXT_SIZE)
        #Design motivation 
        text("I always liked the approuch Tron took to represent cyber space.\nThe design and colors are simple and easy to differentiate, and \nI found this was a great fit for my game, both in design and in \nsetting. That is why I have choosen this design for my game.", 50, 390)
        text("My game is an endless runner based on games like: The Impossible game, \nbut with my own flavour. Runners are quite popular on mobile devices, \nand I thought it'd be fun to make one so this is why I chose this game \ngenre. I always enjoyed challenging games, and so I made this game \nintentionally difficult to help build some tension while playing, I want \npeople to fail at this game before getting it.", 50, 200)
        text("Music credits: Synapsis, http://freemusicarchive.org/music/Synapsis/", 50, 530)
        self.backBtn.drawBtn() 
        tint(255, 255)
        fill(0)
        stroke("#cb602b")
        rect(850, 120, 308, 204)
        image(self.tronImage,855,125)
        fill(255)
        text("Tron inspiration",900, 370)
        
    
    def pressed(self, x, y):
            clicked = self.backBtn.checkClicked(x, y)
            return clicked    
        
    def pressedBtn(self, btn):  
        if(btn == "Back"):
            self.backBtn.highlightBtn(True)     
            
    def release(self):
            self.backBtn.highlightBtn(False)        