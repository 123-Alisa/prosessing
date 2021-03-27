das = 1
r = 255
g = 255
b = 255

def setup():
    size(600,400)
    background(220)
    
def draw():
    #frameRate(1)
    global das
    global r
    global g 
    global b
    background(220)
    fill(r,g,b)
    ellipse(300,200,das,das)
    das = das + 1
    #r = r + 1
    g = g - 1 
    b = b - 1
    
    if mousePressed:
        xDif = 300 - mouseX
        yDif = 200 - mouseY
        if sqrt(xDif*xDif + yDif*yDif) < das:
            background(255,0,0)
            das = 1 
            r = 255 
            g = 255
            b = 255
            
    if das >= 400:
        background(255,0,0)
        das = 1 
        r = 255 
        g = 255
        b = 255
        
    #if das <= 200:
      #  background(220)
