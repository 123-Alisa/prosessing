bg = 0
x = 255
y = 255
z = 255
mode = "игра"
def setup():
    size(600,400)
    frameRate(60)
    
def draw():
    global bg
    global x 
    global y 
    global z 
    global mode
    background(220)
    if mode == "игра":
        fill(x,y,z)
        rect(250,150,100,100)
        textSize(20)
        fill(0)
        textAlign(CENTER,CENTER)
        text(bg,200,300)
        text(frameCount,20,20)
        if bg == 30:
                x = 255
                y = 0
                z = 0
                mode = "победа"
        if frameCount == 1800:
            mode = "поражение"
    elif mode == "победа":
        background(255, 228, 225)
        textSize(20)
        fill(0)
        textAlign(CENTER,CENTER)
        text(u"Победа",50,20)
    else :
        textSize(20)
        fill(0)
        textAlign(CENTER,CENTER)
        text(u"Поражение",50,20)
def mouseClicked():
        global bg
        global x 
        global y 
        global z 
        global mode        
        if mouseX > 250 and mouseX < 350 and mouseY > 150 and mouseY < 250 and mode == "игра":
            bg = bg + 1
        
    
