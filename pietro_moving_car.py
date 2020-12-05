#Pietro Stabile, Quarter 2 Project 2020
#A car with a color of the user's choice moves across a landscape
#Sources: w3schools.com, stackoverflow.com, Dr. Patankar
from graphics import * #imports the graphics module
import time #imports the time module
def main(): #defines the main function
    win = GraphWin("My Window",500,500) #establishes drawing window

    def drawRectangle(x1,y1,x2,y2,r,g,b): #defines the repetitive rectangle-drawing process
        rect = Rectangle(Point(x1,y1),Point(x2,y2)) #uses x1 and y1 for one rectangle point, and x2 and y2 for the opposite point
        rect.setFill(color_rgb(r,g,b)) #sets the color according to input
        rect.draw(win) #draws the rectangle
        return rect #returns the rectangle so it can be stored as a variable (useful for moving the car body)

    def drawCircle(x,y,radius,r,g,b): #defines the repetitive circle-drawing process
        circ = Circle(Point(x,y),radius) #uses x and y for the center of the circle, and plugs in the radius
        circ.setFill(color_rgb(r,g,b)) #sets the color according to input
        circ.draw(win) #draws the circle
        return circ #returns the circle so it can be stored as a variable (useful for moving the car wheels)

    def drawTree(x,y): #tree drawing function, using x and y as the center of the circle on top
        drawRectangle(x-5,y+10,x+5,y+40,94,60,4) #the first four numbers define the tree trunk's location in relation to the top circle, and the last three numbers color it brown
        drawCircle(x,y,15,8,87,7) #x and y are the coordinates of the top circle's center, 15 is the radius, and the last three numbers color it dark green
    
    drawRectangle(0,0,500,500,34,139,34) #draws the background as a rectangle and colors it light green
    drawRectangle(10,200,40,300,0,0,0) #draws the starting point as a rectangle at the left of the scene and colors it black
    drawRectangle(490,200,460,300,0,0,0) #draws the ending point as a rectangle at the right of the scene and colors it black
    drawRectangle(40,230,460,270,128,128,128) #draws the road as a rectangle stretching from the start to the end and colors it grey

    #draws six trees across the scene

    coordinateList = [(125,100),(250,100),(375,100),(125,400),(250,400),(375,400)]
    for i in range(len(coordinateList)):
        drawTree(coordinateList[i[0]],coordinateList[i[1]])

    textLine1 = Text(Point(225,25),50) #locates a question for the user at the top of the screen
    textLine1.setText("Would you like the car to be red or blue (r for red, b for blue)?") #sets the question text, asking the user for input on car color
    textLine1.draw(win) #draws the question

    textLine2 = Text(Point(225,50),25) #locates another line of text under the question
    textLine2.setText("Click anywhere to enter.") #instructs the user to click anywhere on the screen when they are done entering input
    textLine2.draw(win) #draws the second line of text
    
    choice = Entry(Point(470,25),5) #designates a user input box at the top right of the scene
    choice.draw(win) #draws the input box
    while(True): #infinite loop which repeats until the user enters r or b
        win.getMouse() #waits for mouse click
        color = choice.getText() #stores the user's input
        choice.setText("") #clears the entry box
        if(color == "r" or color == "R"): #if the user picked red
            #then draw a red car, wheels first so the body is shown on top
            wheel1 = drawCircle(65,240,5,0,0,0)
            wheel2 = drawCircle(85,240,5,0,0,0)
            wheel3 = drawCircle(65,260,5,0,0,0)
            wheel4 = drawCircle(85,260,5,0,0,0)
            
            carBack = drawCircle(60,250,10,255,0,0)
            carFront = drawCircle(90,250,10,255,0,0)
            carBody = drawRectangle(60,240,90,260,255,0,0)
            
            break #exit the loop and continue the program
        elif(color == "b" or color == "B"): #if the user picked blue
            #then draw a blue car, wheels first so the body is shown on top
            wheel1 = drawCircle(65,240,5,0,0,0)
            wheel2 = drawCircle(85,240,5,0,0,0)
            wheel3 = drawCircle(65,260,5,0,0,0)
            wheel4 = drawCircle(85,260,5,0,0,0)
            
            carBack = drawCircle(60,250,10,0,0,255)
            carFront = drawCircle(90,250,10,0,0,255)
            carBody = drawRectangle(60,240,90,260,0,0,255)
            
            break #exit the loop and continue the program
        else: #if the user did not pick red or blue
            textLine1.setText("Please enter r for red or b for blue.") #then tell them to pick red or blue and restart the loop

    for i in range(0,175): #this loop runs 175 times
        #moves the entire car two pixels at a time
        wheel1.move(2,0)
        wheel2.move(2,0)
        wheel3.move(2,0)
        wheel4.move(2,0)
        carBack.move(2,0)
        carFront.move(2,0)
        carBody.move(2,0)

        time.sleep(0.01) #pauses slightly to appear as if the car is moving smoothly

    textLine1.setText("Would you like to go in reverse (y for yes, anything else to exit)?") #asks the user whether they would like to go backwards or exit
    win.getMouse() #waits for mouse click
    goBack = choice.getText() #stores the user's input
    choice.setText("") #clears the entry box
    if(goBack == "y" or goBack == "Y"): #if the user wants to go in reverse
        for i in range(0,175): #then repeat this code 175 times
            #moves the entire car backwards, two pixels at a time
            wheel1.move(-2,0)
            wheel2.move(-2,0)
            wheel3.move(-2,0)
            wheel4.move(-2,0)
            carBack.move(-2,0)
            carFront.move(-2,0)
            carBody.move(-2,0)
            
            time.sleep(0.01) #pauses slightly to appear as if the car is moving smoothly
    textLine2.setText("Goodbye!") #says goodbye to the user, whether or not they went in reverse
    #prints a 3-2-1 countdown to IDLE
    print("Shutting down in 3... ")
    time.sleep(1)
    print("2... ")
    time.sleep(1)
    print("1... ")
    time.sleep(1)
    os._exit(0) #exits the program without a confirmation window
main() #runs the main function, which contains all the code
