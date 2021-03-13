x=0
y=0
z=0


def setup():
    size(600,600)
    background(220)
    
    

        
        
def draw():
    global x
    global y
    global z
    #background(220)
    noStroke()
    fill(169, 169, 169)
    rect(0,0,70,600)
    strokeWeight(3)
    stroke(0,0,0)
    fill(255)
    rect(5,10,60,35)
    #line(5,90,65,90)
    #strokeWeight(5)
    #line(5,102,65,102)
    #strokeWeight(6)
    #line(5,115,65,115)
    strokeWeight(2)
    fill(255,0,0)
    rect(10,150,50,30)
    #fill(255, 255, 0)
    #rect(10,200,50,30)
    #fill(0,255,0)
    #rect(10,250,50,30)
    #fill(0, 0, 255)
    #rect(10,300,50,30)
    stroke(x,y,z)
    if mousePressed:
        line(mouseX, mouseY, pmouseX, pmouseY)

def mouseClicked():
        global x
        global y
        global z
        if mouseX > 5 and mouseX < 65 and mouseY > 10 and mouseY < 45:
            background(220)
        if mouseX > 10 and mouseX < 60 and mouseY > 150 and mouseY < 180:
            x = x + 255
            stroke(x,y,z)

    
    

    
