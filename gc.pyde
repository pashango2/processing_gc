from node import Node, RootNode, NodePosTable
from easing import EasingInOutCubic

python_logo = None

node_pos_table = NodePosTable(640)

def setup():
    global python_logo
    size(640, 480)
    frameRate(60) 
    
    python_logo = loadShape("python.svg")




def draw():
    background(93, 71, 188)
    
    if frameCount < 30:
        t = EasingInOutCubic.get(float(frameCount) / 30)
    else:
        t = 1.0

    for node in node_pos_table.nodes:
        node.draw(t)
    
    # rect.rotate(0.1)
    # rect.rotateX(0.1)
    # rect.translate(10, 100)
    # shapeMode(CENTER)
    # rect.scale(1.01)
    # shape(s, 0, 0, 640, 480)
    shapeMode(CENTER)
    shape(python_logo, 320, 50)