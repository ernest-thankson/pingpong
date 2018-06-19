#This the first python project I ever worked on. We decided to use tkinter to create a ping pong game. At the time
#I and my group felt quite proud of ourselves. On looking at it now, however, I feel there is a lot that could be improved
#I would have modified this program but decided not to on considering that we used a module whose main purpose is
#not creating games to create a game.
import turtle
import math
import random

wn=turtle.Screen()
wn.bgcolor("tan")

writerturt=turtle.Turtle()                   #creation of scorekeeper and general informer
writerturt.hideturtle()
writerturt.up()
writerturt.setpos(-300,-300)                #moving writerturt to a position where he can begin drawing ping pong court
writerturt.down()
for i in range(4):                          #drawing of ping pong court
    writerturt.forward(600)
    writerturt.left(90)
def writescore(turt,text):                  #function that writes a string of text when passed a turtle and the text
    turt.undo()
    turt.write(text,font=("Algerian",12,"bold"))

p1scorekeeper=turtle.Turtle()            #creation of turtle to write score for player 1
p1scorekeeper.hideturtle()
p1scorekeeper.up()
p1scorekeeper.goto(320,290)              #moving player 1 score keeper to position where its to write scores
p1scorekeeper.down()
p1scorekeeper.write("Player 1 Score:0",font=("Algerian",12,"bold"))   #initializing player 1 score display

p2scorekeeper=turtle.Turtle()           #creation of turtle to write score for player 2
p2scorekeeper.hideturtle()
p2scorekeeper.up()
p2scorekeeper.goto(320,270)             #moving player 2 score keeper to position where its to write scores
p2scorekeeper.down()
p2scorekeeper.write("Player 2 Score:0",font=("Algerian",12,"bold")) #initializing player 2 score display
    


player1=turtle.Turtle()                       #Creation of player 1 (controlled by human)
player1.speed(10)
player1.shape("square")
player1.color("green")
player1.shapesize(1,4)
player1.up()
player1.setpos(0,-290)                      #moving player 1 to start position
#player1 methods
def p1right():                              #defining callback functions for player 1
    if player1.xcor()<250:
        player1.forward(30) #BOTH PLAYERS KEEP DEFAULT HEADING. TO MOVE THEM RIGHT, WE USE THE FORWARD METHOD OF THE TURTLE AND VICE VERSA.
def p1left():
    if player1.xcor()>-250:            
        player1.backward(30)
wn.onkey(p1right,"Right")
wn.onkey(p1left,"Left")
wn.listen()




bspeed=10       #defining distance moved by ball for each iteration of while loop below
ball=turtle.Turtle()           #creation of ball and movement to start position
ball.shape("circle")
ball.color("black")
ball.up()
ball.setpos(0,-270)
ball.setheading(random.randint(20,160))    #initializing ball heading







player2=turtle.Turtle()        #creation of player2, controlled by program
player2.shape("square")
player2.color("green")
player2.shapesize(1,4)
player2.up()
player2.setpos(0,290)
#player2 methods
def p2right(dist):
        player2.forward(dist)


def play():
    p1score=0  #initializing player 1 score
    p2score=0  #initializing player 2 score
    while True:
        if p1score>=5:    #check if player 1 score is five
            writerturt.up()
            writerturt.goto(-60,0) 
            writerturt.down()
            writerturt.write("GAME OVER\n",font=("Algerian",25,"bold"))  #display gameover and break loop
            writerturt.write("YOU WIN",font=("Algerian",25,"bold"))
            wn.exitonclick()
            break                     
        if p2score>=5:      #check if player 2 score is five
            writerturt.up()
            writerturt.goto(-60,0)
            writerturt.down()
            writerturt.write("GAME OVER\n",font=("Algerian",25,"bold"))    #display gameover and break loop
            writerturt.write("YOU LOSE",font=("Algerian",25,"bold"))
            wn.exitonclick()
            break
        
        if ball.ycor()<-350:                   #check if ball has crossed player 1 line, increase 
            p2score=p2score+1                  #increase player 2 score 
            writescore(p2scorekeeper,"Player 2 Score: "+str(p2score)) #display new score on screen
            ball.setpos(player1.xcor(),-270)
            ball.setheading(random.randint(30,150))
            player2.goto(ball.xcor(),290)
        if ball.ycor()>350:                 #check if ball has crossed player 2 line, increase 
            p1score+=1                          #increase player 2 score
            writescore(p1scorekeeper,"Player 1 Score: "+str(p1score))     #display new score on screen
            ball.setpos(player2.xcor(),270)
            ball.setheading(random.randint(210,330))
            
      #right and left boundaries
        if ball.xcor()<=-290:       #check if ball is on or is about crossing left ping pong court boundary
            if ball.heading()>90 and ball.heading()<180:   #if ball is coming from player 1
                angle=ball.heading()-90         #turn ball heading towards player 2 according to laws of reflection
                ball.right(2*angle)
                ball.forward(30)   #move ball forward 30 pixels to get it out of boundary range
            elif ball.xcor()<-325:        # if ball by any chance has gone too far past left boundary
                ball.setpos(player1.xcor(),-270)  #return ball to player 1 
                ball.setheading(random.randint(15,165))
            else:                      #if ball is coming from player 2
                angle=ball.heading()-180   #turn ball heading towards player 1 according to laws of reflection
                ball.left(180-2*angle)
                ball.forward(30)       #move ball forward 30 pixels to get it out of boundary range
                                         
        if ball.xcor()>=290:           #if ball is on or is about crossing right ping pong court boundary                     
            if ball.heading()>0 and ball.heading()<90:  #if ball is coming from player 1
                angle=ball.heading()          #turn ball heading towards player 2 according to laws of reflection
                ball.left(180-2*angle)
                ball.forward(30)     #move ball forward 30 pixels to get it out of boundary range
            elif ball.xcor()>325:     # if ball by any chance has gone too far past right boundary
                ball.setpos(player2.xcor(),270)             #return ball to player 2
                ball.setheading(random.randint(195,340))
            else:                     #if ball is coming from player 2
                angle=ball.heading()-270
                ball.right(2*angle)      #turn ball heading towards player 1 according to laws of reflection
                ball.forward(30)        #move ball forward 30 pixels to get it out of boundary range
                
        oldPosX=ball.xcor()         #record current ball position  
        ball.forward(bspeed)        #move ball forward
        changeX=ball.xcor()-oldPosX   #evaluate change in x-coordinates of ball
        p2right(changeX)              #move player 2 accordingly

        p1dist=math.sqrt((player1.xcor()-ball.xcor())**2+(player1.ycor()-ball.ycor())**2) #evaluate distance between player 1 and ball
        p2dist=math.sqrt((player2.xcor()-ball.xcor())**2+(player2.ycor()-ball.ycor())**2)  #evaluate distance between player 2 and ball     
        #<p1dist condition>
        fdist=50    #distance moved by ball after hitting a player in order to get out of player range
        if p1dist<=27:         #if distance between player 1 and ball is less than 27 pixels
            if ball.heading()>180 and ball.heading()<270:  #and ball is coming towards player 1 from the right
                angle=ball.heading()-180   
                ball.right(2*angle)      #turm ball according to laws of reflection
                ball.forward(fdist)       
            elif ball.heading()>270 and ball.heading()<360:#if ball is coming towards player 1 from the left
                angle=ball.heading()-270
                ball.left(180-2*angle)    #turn ball according to laws of reflection
                ball.forward(fdist)
            elif ball.heading()==270:     #if ball is coming vertically at player 1
                ball.right(random.randint(110,160))  #turn ball to face in a random opposite direction to the left
                ball.forward(fdist)
                
            else:         
                pass
        #</p1dist condition>


        #<p2dist condition>
        if p2dist<=27:     #if distance between player 1 and ball is less than 27 pixels, ie the ball is getting
                                        #close to player2
            if ball.heading()>0 and ball.heading()<90: #and ball is coming towards player 2 from the left 
                angle=ball.heading()
                ball.right(2*angle)   #turn ball according to laws of reflection
                ball.forward(fdist)
            elif ball.heading()>90 and ball.heading()<180:  #if ball is coming towards player 2 from the right
                angle=ball.heading()-90
                ball.left(180-2*angle)    #turn ball according to laws of reflection
                ball.forward(fdist)
            elif ball.heading()==90:      #if ball is coming vertically at player 2
                ball.setheading(random.randint(190,260))    #turn ball to face in a random opposite direction to the right
                ball.forward(fdist)
            else:
                pass

play()          #games begin  

