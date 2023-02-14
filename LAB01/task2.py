from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_HOME():
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_LINES)
    glVertex2f(100,50) #jekhane show korbe pixel
    glVertex2f(400,50)

    glVertex2f(100,300) #jekhane show korbe pixel
    glVertex2f(400,300)

    glVertex2f(100,50) #jekhane show korbe pixel
    glVertex2f(100,300)

    glVertex2f(400,50)
    glVertex2f(400,300)

    

    glEnd()


def ROOF():
    glPointSize(5) 
    
    glBegin(GL_TRIANGLES)
 
    glColor3f(0.1, 0.0, 0.0)
    glVertex2f(100,300)

    glColor3f(0.1, 0.0, 0.0)
    glVertex2f(250,450)

    glColor3f(1, 0.5, 0.0)
    glVertex2f(400,300)

    glEnd()


def quads():
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_QUADS)


    # DOOR
    glColor3f(1, 0.5, 0.0)
    glVertex2f(220,50)

    glColor3f(1, 0.5, 0.0)

    glVertex2f(280,50)

    glColor3f(1, 0.5, 0.0)
    glVertex2f(280,150)

    glColor3f(1, 0.5, 0.0)
    glVertex2f(220,150)


    # WINDOW1
    # glBegin(GL_QUADS)

    glColor3f(1, 0.5, 0.0)
    glVertex2f(120,200)

    glColor3f(1, 0.5, 0.0)
    glVertex2f(120,250)

    glColor3f(1, 0.0, 0.0)
    glVertex2f(170,250)

    glColor3f(1, 0.5, 0.0)
    glVertex2f(170,200)

    # WINDOW2


    glColor3f(1, 0.5, 0.0)
    glVertex2f(330,200)

    glColor3f(1, 0.0, 0.0)

    glVertex2f(330,250)

    glColor3f(1, 0.5, 0.0)
    glVertex2f(380,250)

    glColor3f(1, 0.5, 0.0)
    glVertex2f(380,200)



    
    glEnd()

def lock():
    glPointSize(5)
    glBegin(GL_POINTS)
    glColor3f(0.1, 0.0, 0.0)
    glVertex2f(270,100)
    glEnd()


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
    glColor3f(1, 0.5, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    draw_HOME()
    ROOF()
    quads()
    lock()
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()
