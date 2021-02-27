i=25
mode="вправо"
def setup():
    size(600,400)
    frameRate(150)
    
    
def draw():
    global i 
    global mode
    background(200)
    
    if mousePressed and (mouseButton == RIGHT):
        fill(255, 0, 0)
    if mousePressed and (mouseButton == LEFT):
        fill(0, 0, 255)
    if mousePressed and (mouseButton == CENTER):
        fill(0, 255, 0)
    ellipse(300,i,50,50)
    if mode == "вправо":
        i = i + 1
    if mode == "влево":
        i = i - 1
    if i <= 25:
        mode="вправо"
    if i >= 375:
        mode="влево"
  
        
