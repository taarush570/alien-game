import pgzrun
import random

WIDTH= 600
HEIGHT= 600
TITLE= ("GoodShot Alien Game")

#variable to store the messages getting displayed on the screen
message=""


#getting the picture and making it a sprite
#Actor function for it

alien = Actor("alien picture")

def draw():
    screen.clear() #This clears the screen if anything is placed on the screen before
    #screen is a default variable

    #adding background colour for the screen
    screen.fill(color=(65,255,1))

    #adding picture on the screen which has been taken already in a vairable name
    alien.draw()

    #adding text in the screen
    screen.draw.text(message, center= (400,30), fontsize=40)


def place_alien(): #this functiom is to give random positions for the alien
    alien.x = random.randint(0,WIDTH)
    alien.y = random.randint(0,HEIGHT)


def on_mouse_down(pos):
    global message #global means making the variable global so that changes are reflected all over the code and not limited to only this function
    if alien.collidepoint(pos):
        message="Good Job!"
        place_alien()
    else:
        message="Oops... you missed it.."
    
place_alien()
pgzrun.go()