i = 1
#a = true

def setup():
    size(600,400)
    background(255)    
   
def draw():
    global i
    global a
    frameRate(3)
   
    stroke(0)
    translate(0,0)
    strokeWeight(1)
    fill(210, 180, 140)
    rect(0,0,70,399)
    fill(255)
    rect(5,5,60,40)
   
    strokeWeight(2)
    line(5,80,65,80)
    strokeWeight(4)
    line(5,103,65,103)
    strokeWeight(6)
    line(5,129,65,129)
   
    strokeWeight(1)
    stroke(random(0,255),random(0,100),random(0,222))
    line(random(70,600),random(0,400),random(70,600),random(0,400))
   
   
#def mouseClicked():
    if mousePressed and mouseButton:
        if mouseX > 5 and mouseX < 65 and mouseY > 5 and mouseY < 45:
            background(255)
        if mouseX > 5 and mouseX < 65 and mouseY > 126 and mouseY < 132:
           # noLoop()
            strokeWeight(6)
            stroke(random(0,255),random(0,100),random(0,222))
            line(random(70,600),random(0,400),random(70,600),random(0,400))
        if mouseX > 5 and mouseX < 65 and mouseY > 100 and mouseY < 106:
            #noLoop()
            strokeWeight(4)
            stroke(random(0,255),random(0,100),random(0,222))
            line(random(70,600),random(0,400),random(70,600),random(0,400))
        if mouseX > 5 and mouseX < 65 and mouseY > 77 and mouseY < 83:
           # noLoop()
            strokeWeight(2)
            stroke(random(0,255),random(0,100),random(0,222))
            line(random(70,600),random(0,400),random(70,600),random(0,400))
