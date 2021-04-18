

def setup():
    size(600,400)
    frameRate(5)
def draw():
   
    if keyPressed == True:
        fill(0,0,0)
    else:
        fill(255,0,255)
        
          
    rect(random(0,600),random(0,400),30,30)
    
