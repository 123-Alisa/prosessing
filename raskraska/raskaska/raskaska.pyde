x=0
y=0
z=0
w=1

def setup():
    size(600,600)
    background(220)
    
    

        
        
def draw():
    global x
    global y
    global z
    global w
    #background(220)
    noStroke()
    fill(169, 169, 169)
    rect(0,0,70,600)
    strokeWeight(3)
    stroke(0,0,0)
    fill(255)
    rect(5,10,60,35)
    line(5,90,65,90)
    strokeWeight(5)
    line(5,102,65,102)
    strokeWeight(6)
    line(5,115,65,115)
    strokeWeight(2)
    fill(255,0,0)
    rect(10,150,50,30)
    fill(255, 255, 0)
    rect(10,200,50,30)
    fill(0,255,0)
    rect(10,250,50,30)
    fill(0, 255, 255)
    rect(10,300,50,30)
    fill(0, 0, 255)
    rect(10,350,50,30)
    fill(255, 0, 255)
    rect(10,400,50,30)
    fill(255, 255, 255)
    rect(10,450,50,30)
    fill(0, 0, 0)
    rect(10,500,50,30)
    stroke(x,y,z)
    if mousePressed:
        strokeWeight(w)
        line(mouseX, mouseY, pmouseX, pmouseY)

def mouseClicked():
        global x
        global y
        global z
        global w
        if mouseX > 5 and mouseX < 65 and mouseY > 10 and mouseY < 45:
            background(220)
        if mouseX > 5 and mouseX < 65 and mouseY > 88.5 and mouseY < 91.5:
            w = 3
        if mouseX > 5 and mouseX < 65 and mouseY > 99.5 and mouseY < 104.5:
            w = 5
        if mouseX > 5 and mouseX < 65 and mouseY > 112 and mouseY < 118:
            w = 6
        if mouseX > 10 and mouseX < 60 and mouseY > 150 and mouseY < 180:
            x = 255
            y = 0
            z = 0
            stroke(x,y,z)
        if mouseX > 10 and mouseX < 60 and mouseY > 200 and mouseY < 230:
            x = 255 
            y = 255
            z = 0
            stroke(x,y,z)
        if mouseX > 10 and mouseX < 60 and mouseY > 250 and mouseY < 280:
            x = 0 
            y = 255
            z = 0
            stroke(x,y,z)
        if mouseX > 10 and mouseX < 60 and mouseY > 300 and mouseY < 330:
            x = 0
            y = 255
            z = 255
            stroke(x,y,z)
        if mouseX > 10 and mouseX < 60 and mouseY > 350 and mouseY < 380:
            x = 0 
            y = 0
            z = 255
            stroke(x,y,z)
        if mouseX > 10 and mouseX < 60 and mouseY > 400 and mouseY < 430:
            x = 255
            y = 0
            z = 255
        if mouseX > 10 and mouseX < 60 and mouseY > 450 and mouseY < 480:
            x = 255
            y = 255
            z = 255
        if mouseX > 10 and mouseX < 60 and mouseY > 500 and mouseY < 530:
            x = 0
            y = 0
            z = 0
