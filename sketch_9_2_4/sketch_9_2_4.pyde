das = 1
#fig = 1


def setup():
    size(600,400)
    background(220)
    
def draw():
    #frameRate(1)
    global das
    #global fig
    background(220)
    ellipse(300,200,das,das)
    das = das + 1
    #fig = fig + 1 
    
    if mousePressed:
        xDif = 300 - mouseX
        yDif = 200 - mouseY
        if sqrt(xDif*xDif + yDif*yDif) < das:
            background(255,0,0)
            das = 1 
            
    if das >= 400:
        background(255,0,0)
        das = 1 
        
    #if das <= 200:
      #  background(220)
