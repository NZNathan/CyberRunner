

class Timer:
    
    #Constants
    TIMER_TEXTSIZE = 24
    TIMER_TEXTCOLOR = "#ffffff"
    
    #Variables
    startTime = 0
    secTime = 0
    millisTime = 0
    stopTime = False
    time = 0
    
    def __init__(self):
        self.startTime = float(millis()/1000)
        self.updateTime()
        
    def updateTime(self):
       if(not self.stopTime):
           self.secTime = int(millis()/1000) - self.startTime
           self.millisTime = float(millis()/10) - self.startTime - self.secTime
           self.time = self.secTime + (self.millisTime%100)/100
       textSize(self.TIMER_TEXTSIZE)
       fill(self.TIMER_TEXTCOLOR)
       text("%.2f" % self.time, 100, height-40)
       
    def getTime(self):
       time = self.secTime + (self.millisTime%100)/100
       return time    