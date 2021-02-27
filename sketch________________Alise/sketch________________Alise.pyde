i = 25
s="больше"
def setup():
    size(600,400)
    
def draw():
    global i
    global s
    if mousePressed == True:
       background(200)
       ellipse(300,200,i,i)
       if i <= 25:
         s = "больше"
       if i >= 40:
         s = "меньше"
       if s == "больше":
         i = i + 1
       if s == "меньше":
         i = i - 1
       
    else:
       background(200)
        
        
        
        
        
        
        
        
