

def setup():
    size(600,400)
    
    
def draw():
    if mousePressed and (mouseButton == LEFT):
        ellipse(mouseX, mouseY,random(0,40),random(0,40))
    if mousePressed and (mouseButton == RIGHT):
        background(200)
