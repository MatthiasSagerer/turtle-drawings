import math
import letters


def polygon(turtle, edges, sidelength):
    for i in range(edges):
        turtle.forward(sidelength)
        turtle.right(360 / edges)


def polygonSpiral(turtle, edges, difference, iterations, deg):
    for i in range(iterations):
        polygon(turtle, edges, difference * i)
        turtle.right(deg)


def spiralTunnel(turtle, iteration, initialsize, deg):
    rad_deg = deg * math.pi / 180
    length = initialsize
    for i in range(iteration):
        if i != 0:
            turtle.left(deg)
            dist = length * math.sin(rad_deg)
            turtle.backward(dist)
            length = length * (math.sin(rad_deg) + math.cos(rad_deg))
        polygon(turtle, 4, length)


def rainbowPolygon(turtle, edges, sidelength):
    for i in range(edges):
        turtle.pencolor(letters.colors[i % len(letters.colors)])
        turtle.forward(sidelength)
        turtle.right(360 / edges)
    turtle.pencolor((0, 0, 0))


def rainbowPolygonSpiral(turtle, edges, difference, iterations, deg):
    for i in range(iterations):
        turtle.pencolor(letters.colors[i % len(letters.colors)])
        polygon(turtle, edges, difference * i)
        turtle.right(deg)

    turtle.pencolor((0, 0, 0))


def rainbowSpiralTunnel(turtle, iteration, initialsize, deg):
    rad_deg = deg * math.pi / 180
    length = initialsize
    for i in range(iteration):
        turtle.pencolor(letters.colors[i % len(letters.colors)])
        if i != 0:
            turtle.left(deg)
            dist = length * math.sin(rad_deg)
            turtle.backward(dist)
            length = length * (math.sin(rad_deg) + math.cos(rad_deg))
        polygon(turtle, 4, length)
    turtle.pencolor((0, 0, 0))
