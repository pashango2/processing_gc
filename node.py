from easing import *
import math



class NodePosTable:
    SPACE = 70
    ROW_COUNT = 6

    def __init__(self, w):
        self.padding_x = int((w - (self.SPACE * self.ROW_COUNT)) / 2)
        self.nodes = []

        self._table = []
        xnum = 1
        for y in range(4):
            width = self.SPACE * (xnum - 1)
            xx = w / 2 - width / 2
            yy = 140 + self.SPACE * y


            for x in range(xnum):
                self._table.append([
                    (xx, yy), [1, 2],
                ])
                self.nodes.append(Node(xx, yy))
                xx += self.SPACE
                
            xnum += 2


        self._leaf = [0]

    def put(self, idx=None):
        if not self._leaf:
            return

        if idx is None:
            idx = self._leaf[0]

        node = Node(*self._table[idx][0])



        pass

    def fixed(self, idx):
        if idx == 0:
            return self.padding_x + (self.SPACE / 2) + self.SPACE, 110
        if idx == 1:
            return self.padding_x + (self.SPACE / 2) + (self.SPACE * 4), 110


class Node:
    SIZE = 40

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.number = 0
        self.links = []

    def link(self, node):
        self.links.append(Link(self, node))
        node.number += 1

    def draw(self, scale_value=1.0):
        pushMatrix()

        translate(self.x, self.y)
        scale(scale_value)

        noFill()
        stroke(255)
        strokeWeight(3)
        ellipse(0, 0, self.SIZE, self.SIZE)
        
        fill(255)
        textSize(25)
        textAlign(CENTER, CENTER)
        text(str(self.number), 0, -3)

        popMatrix()

        for link in self.links:
            link.draw()

class RootNode(Node):
    pass


class Link:
    ARROW_SIZE = 10

    def __init__(self, node1, node2):
        self.begin = node1
        self.end = node2

    def draw(self):
        s = 0.4
        s = 0
        rad = math.atan2(
            self.end.y - self.begin.y,
            self.end.x - self.begin.x,
        )
        _x = math.cos(rad) * (Node.SIZE / 2)
        _y = math.sin(rad) * (Node.SIZE / 2)
        sx = _x + self.begin.x
        sy = _y + self.begin.y
        ex = -_x + self.end.x
        ey = -_y + self.end.y

        stroke(255)
        strokeWeight(3)
        strokeCap(SQUARE)
        line(sx, sy, ex, ey)
        # dx = ex - sx
        # dy = ey - sy
        # if dx < dy:
        #     dx = 0
        # else:
        #     dy = 0
        #
        # noFill()
        # bezier(
        #     sx, sy,
        #     sx + dx * s, sy + dy * s,
        #     ex - dx * 0, ey - dy * 0,
        #     ex, ey
        # )
        # pass

        pushMatrix()
        translate(ex, ey)
        rotate(rad)

        fill(255)
        noStroke()
        triangle(
            0, 0,
            -self.ARROW_SIZE, self.ARROW_SIZE * 0.7,
            -self.ARROW_SIZE, -self.ARROW_SIZE * 0.7)
        popMatrix()