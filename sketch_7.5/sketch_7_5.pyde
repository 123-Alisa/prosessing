i = 0
s = "вправо"

def setup():
    size(400,400)
    
    
def draw():
    global i
    global s
    #background(200)
    fill(random(0,220))
    
    rectMode(CENTER)
    
    rect(i,i,random(0,50),random(0,50))
   
    if s == "вправо":
        i = i + 1
    if s == "влево":
        i = i - 1
    if i >= 375:
        s = "влево"
    if i <= 25:
        s = "вправо"    
    if i >= 375:
        background(200)
    if i <= 25:
        background(200)
