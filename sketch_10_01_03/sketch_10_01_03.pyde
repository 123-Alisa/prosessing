x = 50

def setup():
    size(500,500)
    
def draw():
    global x
    background
    ellipse(250,250,x,x)
    
def keyPressed():
    global x 
    background
    if key == CODED:
        if keyCode == RIGHT: 
            x = x + 1 
        elif keyCode == LEFT:
            x = x - 1 
