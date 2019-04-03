add_library('pdf')
def setup():
    global i
    global nazwa
    global ext
    nazwa = "idman"
    ext = ".jpg"
    i = loadImage("id.jpg")
    size(300, 300, PDF, "id.pdf")
    print(type(i))
    imageMode(CENTER)
    
def draw():
    global i
    global nazwa
    global ext
    image(i, width/2, height/2, width, height)
    h = loadShape("hat.svg")
    shapeMode(CENTER)
    shape(h, 150, 50, width/1.8, height/1.8)
    
    z = createShape()
    beginShape()
    vertex(240, 220)
    vertex(250, 200)
    vertex(280, 180)
    vertex(255, 160)
    vertex(250, 200)
    endShape()
    
    x = createShape()
    beginShape()
    vertex(70, 220)
    vertex(60, 200)
    vertex(30, 180)
    vertex(55, 160)
    vertex(60, 200)
    endShape()
    
    print(LEFT)
    if keyPressed:
        print(keyCode)
    if keyCode == 32:
        s = loadShape("green.svg")
        shapeMode(CENTER)
        shape(s, 150, 120, width/2, height/2)
    #save(id+".edited"+ext)
