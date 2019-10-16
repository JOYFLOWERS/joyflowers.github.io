#Joy Flowers
# Sept 2, 2019
# Python Course

import turtle

#This program creates seven stars. The first one is drawn
#and not filled. Each of the others are filled and circle the first one
my_star = turtle.Turtle()   # create a turtle
my_star.hideturtle()        # makes turtle invisible
my_star.penup()             # don't draw
my_star.goto(-70,100)       # set the starting position
my_star.showturtle()        # make the turtle visible
my_star.color('gold')       # set the outline color
my_star.pendown()           # ready to draw
my_star.left(270)           # the following lines draw the first star
my_star.forward(240)
my_star.left(144)
my_star.forward(240)
my_star.right(216)
my_star.forward(240)
my_star.right(216)
my_star.forward(240)
my_star.right(216)
my_star.forward(240)        # end of drawing the first star
my_star.fillcolor("red")    # draw red star filled
my_star.begin_fill()
for i in range(5):
   my_star.forward(150)
   my_star.right(144)
my_star.end_fill()          # end draw red star
my_star.right(300)          # position the line
my_star.forward(100)        # move to the next star
my_star.fillcolor("green")  # draw green star filled
my_star.begin_fill()
for i in range(5):
   my_star.forward(150)
   my_star.right(144)
my_star.end_fill()          # end draw green star
my_star.right(1)            # position the line
my_star.backward(325)       # move to the next star
my_star.fillcolor("purple") # draw purple star filled
my_star.begin_fill()
for i in range(5):
   my_star.forward(150)
   my_star.right(144)
my_star.end_fill()          # end draw purple star
my_star.right(270)          # position the line
my_star.forward(80)         # move to the next star
my_star.fillcolor("yellow") # draw yellow star filled
my_star.begin_fill()
for i in range(5):
   my_star.forward(150)
   my_star.right(144)
my_star.end_fill()          # end draw yellow star
my_star.right(216)          # position the line
my_star.backward(350)       # move to the next star
my_star.fillcolor("orange") # draw orange star filled
my_star.begin_fill()
for i in range(5):
   my_star.forward(150)
   my_star.right(144)
my_star.end_fill()          # end draw orange star
my_star.left(88)            # position the line
my_star.forward(160)        # move to the next star
my_star.fillcolor("blue")   # draw blue star filled
my_star.begin_fill()
for i in range(5):
   my_star.forward(150)
   my_star.right(144)
my_star.end_fill()          # end draw blue star
my_star.left(145)           # position the line
my_star.backward(225)       # complete the star circle
#x = input()            this was used for Mac OS to display output
#have fun!
