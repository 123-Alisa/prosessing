i = 0
s = "вправо"
def setup():
    size(800,400)
    frameRate(160)
    
def draw():
    global s
    global i
    
    background(200)
    ellipse(i,200,50,50)
    if mousePressed == True:
        fill(random(0,220),random(0,250),random(0,222))
        
        if s == "вправо":
            i = i + 1
        if i >= 800:
            s = "влево"
        if s == "влево":
            i = i - 1
        if i <= 0:
            s = "вправо"
