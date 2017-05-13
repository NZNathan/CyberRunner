

class Collision:
    
    bounds = None
    position = None
    
    def __init__(self, x, y, w, h):
        self.position = PVector(x,y)
        self.bounds = PVector(w, h)
        
    def isTouching(self, collider): 
        if ((abs(self.position.x - collider.position.x) <= self.bounds.x/2 + collider.bounds.x/2)
        and (abs(self.position.y - collider.position.y) <= self.bounds.y/2 + collider.bounds.y/2)) :
            return True
        return False