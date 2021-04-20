x = 300
y = 300

def setup():
    size(600,600)
    background(220) 
def draw():
    global x 
    global y 
    ellipse(x,y,50,50)
   # background(220) 
def keyPressed():
    global x 
    global y 
    background(220)
    if key == CODED:
        if keyCode == UP:
            y = y - 3
        if keyCode == DOWN:
            y = y + 3
        if keyCode == RIGHT:
            x = x + 3 
        if keyCode == LEFT:
            x = x - 3
            
