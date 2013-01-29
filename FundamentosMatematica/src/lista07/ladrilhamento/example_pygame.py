# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
 
from lista07.ladrilhamento import ladrilhamento_matriz
import pygame
import random

# CRIA A MATRIZ.

def escolher_cor(column, row, valor):
    #return random.randint(1,1000) % 5 #isso faz piscar!
    return valor % 5

matriz = ladrilhamento_matriz.executar(5, (23,13))
#matriz = ladrilhamento_matriz.executar(4, (11,8))

tam_matriz = len(matriz) 
 
# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
blue     = (   0,   0, 255)
yellow   = ( 255, 255,   0)
pink     = ( 255, 192, 203)
 
# This sets the width and height of each grid location
lado=20
width=lado
height=lado
 
# This sets the margin between each cell
margin=2
 
## Create a 2 dimensional array. A two dimesional
## array is simply a list of lists.
#grid=[]
#for row in range(10):
#    # Add an empty array that will hold each cell
#    # in this row
#    grid.append([])
#    for column in range(10):
#        grid[row].append(0) # Append a cell
 
## Set row 1, cell 5 to one. (Remember rows and
## column numbers start at zero.)
#grid[1][5] = 1

 
# Initialize pygame
pygame.init()
  
# Set the height and width of the screen
size=[lado*(tam_matriz+margin+1),lado*(tam_matriz+margin+1)]
screen=pygame.display.set_mode(size)
 
# Set title of screen
pygame.display.set_caption("Ladrilhamento!")
 
#Loop until the user clicks the close button.
done=False
 
# Used to manage how fast the screen updates
clock=pygame.time.Clock()

# -------- Main Program Loop -----------
while done==False:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        if event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column=pos[0] // (width+margin)
            row=pos[1] // (height+margin)
            # Sete t hat location to zero
            #grid[row][column]=1
            #print("Click ",pos,"Grid coordinates: ",row,column)
            pygame.display.set_caption("Coord:(%s,%s) - Cor: %s"%(row,column,matriz[row,column]))
    # Set the screen background
    screen.fill(black)
 
    # Draw the grid
    #for row in range(10):
    for row in range(tam_matriz):
        #for column in range(10):
        for column in range(tam_matriz):
            color = white
            #if grid[row][column] == 1:
            #    color = green
            valor = matriz[row,column]
            if matriz[row,column] == ladrilhamento_matriz.BILL:
                color = black
            elif escolher_cor(column, row, valor) == 0:
                color = white
            elif escolher_cor(column, row, valor) == 1:
                color = green
            elif escolher_cor(column, row, valor) == 2:
                color = red
            elif escolher_cor(column, row, valor) == 3:
                color = blue
            elif escolher_cor(column, row, valor) == 4:
                color = yellow
            pygame.draw.rect(screen,color,[(margin+width)*column+margin,(margin+height)*row+margin,width,height])
     
    # Limit to 20 frames per second
    clock.tick(20)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit ()