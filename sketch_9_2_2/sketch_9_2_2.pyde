x = 400
y = 300

def setup():
    size(800,600)
    background(220)    
    
def draw():
    global x 
    global y 
    background(220)
    fill(255)
    rect(290,550,40,40)
    rect(350,550,40,40)
    rect(410,550,40,40)
    rect(470,550,40,40)
    fill(0, 255, 255)
    triangle(310,555,295,585,325,585)
    triangle(355,555,385,555,370,585)
    triangle(415,555,415,585,445,570)
    triangle(505,555,505,585,475,570)
    
    fill(255)
    ellipse(x,y,50,50)    
    
    if mousePressed:
        if mouseX > 290 and mouseX < 330 and mouseY > 550 and mouseY < 590:
            y = y - 2
        if mouseX > 350 and mouseX < 390 and mouseY > 550 and mouseY < 590:
            y = y + 2
        if mouseX > 410 and mouseX < 450 and mouseY > 550 and mouseY < 590:
            x = x + 2
        if mouseX > 470 and mouseX < 510 and mouseY > 550 and mouseY < 590:
            x = x - 2
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
