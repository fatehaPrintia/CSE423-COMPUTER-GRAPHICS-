from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_points(x, y):
    glPointSize(2) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glColor3f(1.5, 1.5, 1.0)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()
def Circlepoints(x, y, x0, y0):
    draw_points(x + x0, y + y0)
    draw_points(y + x0, x + y0)
    draw_points(y + x0, -x + y0)
    draw_points(x + x0, -y + y0)
    draw_points(-x + x0, -y + y0)
    draw_points(-y + x0, -x + y0)
    draw_points(-y + x0, x + y0)
    draw_points(-x + x0, y + y0)
def allCircle(x,y,r):
    glColor3f(0.0, 0, 1.0)
    midPointCircleAlgorithm(x,y,r)
    glColor3f(0.0, 1.0, 0.0)
    midPointCircleAlgorithm(x,y+r/2,r/2)
    glColor3f(1.0, 1.0, 0.0)
    midPointCircleAlgorithm(x,y-r/2,r/2)
    glColor3f(0.0, 1.0, 1.0)
    midPointCircleAlgorithm(x+r/2,y,r/2)
    glColor3f(1.0, 0.0, 0.0)
    midPointCircleAlgorithm(x-r/2,y,r/2)

    glColor3f(1.0, 1.0, 0.0)
    midPointCircleAlgorithm(x+r/2.85,x+r/2.85,r/2)
    glColor3f(1.0, 1.0, 0.0)
    midPointCircleAlgorithm(x+r/2.85,x-r/2.85,r/2)
    glColor3f(1.0, 1.0, 0.0)
    midPointCircleAlgorithm(x-r/2.85,x+r/2.85,r/2)
    glColor3f(1.0, 1.0, 0.0)
    midPointCircleAlgorithm(x-r/2.85,x-r/2.85,r/2)
  
def midPointCircleAlgorithm(x0, y0, radius):
    # Initial d
    d = 1 - radius
    x = 0
    y = radius
    Circlepoints(x,y,x0,y0)

    while (x < y):

        if d < 0:
            # IF EAST
            d += 2 * x + 3
            x = x + 1
        else:
            # IF SOUTH
            d += 2 * x - 2 * y + 5
            x = x + 1
            y = y - 1
        Circlepoints(x,y,x0,y0)

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    allCircle(250,250,200)
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()

