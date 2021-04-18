

def setup():
    size(600,400)
    frameRate(5)
def draw():
   
    if keyPressed:
        if key == CODED:
            if keyCode == UP:
                fill(0, 255, 0)
            if keyCode == RIGHT:
                fill(255,0,0)
            if keyCode == LEFT:
                fill(0,0,255)
            if keyCode == DOWN:
                fill(255,255,255)
        
          
    rect(random(0,600),random(0,400),30,30)
    
