from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# 20301357
def draw_Lines2():
    glPointSize(10) #pixel size. by default 1 thake
    glBegin(GL_LINES)
    
    
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(10,500) #jekhane show korbe pixel
    glVertex2f(60,500)

    glVertex2f(60,500)
    glVertex2f(60,450)

    glVertex2f(60,450)
    glVertex2f(10,450) 

    glVertex2f(10,450)
    glVertex2f(10,400)

    glVertex2f(10,400)
    glVertex2f(60,400)
    

    glEnd()

def draw_Lines01():
    glPointSize(10) #pixel size. by default 1 thake
    glBegin(GL_LINES)
    
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(70,500) 
    glVertex2f(120,500)

    glVertex2f(120,500)
    glVertex2f(120,400)
    

    glVertex2f(120,400)
    glVertex2f(70,400)
     #jekhane show korbe pixel
    glVertex2f(70,500) 
    glVertex2f(70,400)


 
    glEnd()
def draw_Lines31():
    glPointSize(10) #pixel size. by default 1 thake
    glBegin(GL_LINES)
    
    glColor3f(1.0,0.0, 0.0)

    glVertex2f(130,500) 
    glVertex2f(180,500)

    glVertex2f(180,400)
    glVertex2f(180,500)
    

    glVertex2f(180,450)
    glVertex2f(130,450)
   
    glVertex2f(180,400)
    glVertex2f(130,400)

    glEnd()
def draw_Lines02():
    glPointSize(10) #pixel size. by default 1 thake
    glBegin(GL_LINES)
    
    glColor3f(1.0, 0.0, 1.0)
    glVertex2f(190,500) 
    glVertex2f(240,500)

    glVertex2f(240,400)
    glVertex2f(240,500)
    

    glVertex2f(190,400)
    glVertex2f(240,400)
   
    glVertex2f(190,500)
    glVertex2f(190,400)

 
    glEnd()
def draw_Lines1():
    glPointSize(10) #pixel size. by default 1 thake
    glBegin(GL_LINES)
    
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(250,500) #jekhane show korbe pixel
    glVertex2f(250,400)
    
    glEnd()

def draw_Lines32():
    glPointSize(10) #pixel size. by default 1 thake
    glBegin(GL_LINES)
    
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(260,500) #jekhane show korbe pixel
    glVertex2f(310,500)

    glVertex2f(310,500)
    glVertex2f(310,400)

    glVertex2f(260,450)
    glVertex2f(310,450)

    glVertex2f(310,400)
    glVertex2f(260,400)

    glEnd()
def draw_Lines5():
    glPointSize(10) #pixel size. by default 1 thake
    glBegin(GL_LINES)
    
    glColor3f(0.0, 1.0, 1.0)
    glVertex2f(320,500) #jekhane show korbe pixel
    glVertex2f(370,500)

    glVertex2f(320,500)
    glVertex2f(320,450)

    glVertex2f(320,450)
    glVertex2f(370,450)

    glVertex2f(370,450)
    glVertex2f(370,400)

    glVertex2f(370,400)
    glVertex2f(320,400)

    glEnd()

def draw_Lines7():
    glPointSize(10) #pixel size. by default 1 thake
    glBegin(GL_LINES)
    
    glColor3f(0.5,0.5,0.5)
    glVertex2f(380,500) #jekhane show korbe pixel
    glVertex2f(430,500)

    glVertex2f(430,500)
    glVertex2f(380,400)
 
    glEnd()

def iterate():
    glViewport(0, 0,1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    draw_Lines2()
    draw_Lines01()
    draw_Lines31()
    draw_Lines02()
    draw_Lines1()
    draw_Lines32()
    draw_Lines5()
    draw_Lines7()
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 1000) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()
