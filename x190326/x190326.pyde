def setup():
    size(400, 400)
    textSize(114)
    textAlign(CENTER)
def draw():
    text("J", width/2-75, (height/3*2))
    #print(mouseX, mouseY)
    print(hex(get(mouseX, mouseY)))
    print(LEFT)
    if keyPressed:
        print(keyCode)
        text("S", width/2+75, (height/3)*2)
        if keyCode == 37 or key == 'j':  # zabrakło reeakcji na klawisz z literą
            fill(800, 200, 40)
            text("J", width/2-75, (height/3)*2) 
            fill(0)
        if keyCode == 39 or key == 's':
            fill(800, 200, 40)
            text("S", width/2+75, (height/3)*2) 
            fill(0)
        
    if (mouseX >=80 and mouseX <= 170 and mouseY >= 170 and mouseY <=265):
        fill(150, 200, 40)
        text("J", width/2-75, (height/3)*2)
        fill(250)
        
    if (mouseX >=245 and mouseX <=305 and mouseY >= 275 and mouseY <=270):
        fill(150, 200, 40)
        text("S", width/2+75, (height/3)*2)
        fill(250)
    
    s = createShape()
    s.beginShape()
    s.fill(50, 55, 100, 20)
    s.noStroke()
    s.vertex(50, height/3*2)
    s.vertex(250, height/3*2-15)
    s.vertex(width/2, height/3*2+15)
    s.vertex(width-100, height/3*2)
    s.endShape(CLOSE)
    shape(s, 25, 25)
