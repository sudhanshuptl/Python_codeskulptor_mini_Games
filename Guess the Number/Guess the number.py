# Guess The Number
        #     Sudhanshu Patel
        #      NIT Rourkela

import simplegui
import random
import math


# initialize global variables used in your code

num_range = 100
attempt = 7
Number = 0


# helper function to start and restart the game
def new_game():
    print ""
    print "New game. Range is from 0 to",num_range
    print "Number of remaining guesses is ",attempt

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range,attempt,Number
    num_range = 100
    attempt = 7
    Number = random.randint(0,100)
    new_game()
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range,attempt,Number
    num_range = 1000
    attempt = 10
    Number = random.randint(0,1000)
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global attempt
    attempt-=1
  
    print ""
    print "Guess was",guess
    print "number of remaining guesses is",attempt
    
    if(Number > int(guess)):
        print "Higher!"   
    elif(Number < int(guess)):
        print "Lower!"   
    else:
        print "Correct!"
        
    if(attempt == 0):
        if(num_range == 100):
            range100()
        else:
            range1000()

    
# create frame
f= simplegui.create_frame("Guess The Number",200,200)

# register event handlers for control elements

f.add_button("0 to 100",range100,100)
f.add_button("0 to 1000",range1000,100)
f.add_input("Enter your guess",input_guess,100)

# call new_game and start frame

f.start()
range100()