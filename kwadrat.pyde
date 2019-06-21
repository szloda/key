def setup():
    size(500, 500)
    global krotka_kolorow
    krotka_kolorow = ((0,50,0), (0,100,250),(70,0,80))
    krotka_kolorow[0]
    frameRate(100)
    rectMode(CENTER)
    global x 
    x = 50
    global y 
    y = 50
    fill(0,100,150)
    strokeWeight(3)
    stroke(*krotka_kolorow[0])
    
    
    

def draw():
    global x 
    x = x + 1
    global y
    y = y + 1
    
    figura = rect(x,y, 100,100)
    
    global krotka_kolorow
    
    if x > 150:
        stroke(*krotka_kolorow[1])
        fill(50,50,55)
        
    if x > 300:
        stroke(*krotka_kolorow[2])
        fill(10,190,200)
    
    if x > 450:
        exit()
    
def mousePressed():
    pass
