# Ethan Coomber
#
# To run in terminal type: python3 Game.py

import random
import sys
import time
import graphicsPlus as gr
import physics_objects as pho
import collision as coll

def main():
	# creates a GraphWin
	#Here is where all of the text that appears on the homescreen will be.
	win = gr.GraphWin('Ball Game', 500, 500, False)

	txt = gr.Text( gr.Point( 250, 50 ), 'Instructions:' )
	txt.setSize( 30 )
	txt.draw( win )

	txt1 = gr.Text( gr.Point( 250, 100 ), 'This is a game where Balls are going to fall from the tope of the window' )
	txt1.setSize( 16 )
	txt1.draw( win )

	txt2 = gr.Text( gr.Point( 250, 150 ), 'You want to avoid these balls. For each ball you avoid you gain a point.' )
	txt2.setSize( 16 )
	txt2.draw( win )

	txt3 = gr.Text( gr.Point( 250, 200 ), 'More and more balls will fall over time. Good Luck!' )
	txt3.setSize( 16 )
	txt3.draw( win )

	txt4 = gr.Text( gr.Point( 250, 250 ), '**Use the left and right arrows to move.**' )
	txt4.setSize( 16 )
	txt4.draw( win )

	txt5 = gr.Text( gr.Point( 250, 300 ), 'Click over these words window to begin the game.' )
	txt5.setSize( 16 )
	txt5.draw( win )

	# update the window so we can see the balls
	win.update()

	# wait for a mouse click
	win.getMouse()

	txt.undraw()
	txt1.undraw()
	txt2.undraw()
	txt3.undraw()
	txt4.undraw()
	txt5.undraw()

        #Initializes the ball
	ball = pho.Ball( win, 20, color = "green")
	ball.setPosition([250, 100])
	ball.draw()

	'''Sets the initial velocity and acceleration to 0'''
	ball.setVelocity([0, 0])

	ball.setAcceleration([0, 0])

	ballRadius = []
	for i in range(10):  # this is the max number of balls to drop
		ballRadius.append(random.randint(10,20))

	obstacles = []
	#We randomly assign sizes to the balls that will be dropping
	for i in ballRadius:
		rand0 = random.randint(0,500)
		rand1 = random.randint( -50, 50)
		obstacles.append(pho.Ball( win, i, pos = [rand0 , 500], vel = [rand1,0], acc = [0,-100]))

	dt = .02
	n = 0 # no balls in play to start
	dodged = 0

        #Draws the first ball
	obstacles[n].draw()
	# increment n
	n += 1



	# starts an infinite loop
	while True:
		# breaks if the user types the letter q
		key = win.checkKey()
		if key == 'q':
			break

		''' Re-positions the ball if it goes out of bounds where the user clicks'''
		pos = ball.getPosition()
		p = ball.getPosition()
		movit1 = False
		movit2 = False
		if p[0] < 0:
			p[0] += win.getWidth()
			movit1 = True
		elif p[0] > win.getWidth():
			p[0] -= win.getWidth()
			movit1 = True

		if movit1:
				ball.setPosition(p)
		 # call update on all of the visible obstacles (first n obstacles are in play)
		for i in range(n):
			obstacles[i].update(dt)

            # get location and velocity of this obstacle
			location = obstacles[i].getPosition()
			vel = obstacles[i].getVelocity()

                        #If the balls are goin out of bounds, they bounce off the side of the window
			if location[1] < 0:
				location[1] += win.getHeight()
				location[0] = random.randint(0,500)
				obstacles[i].setVelocity([0, -50])
				dodged += 1
				movit2 = True
			if location[0] < 0:
				obstacles[i].setVelocity([-vel[0], vel[1]])
				obstacles[i].setPosition( [0, location[1]] )

			elif location[0] > win.getWidth():
				obstacles[i].setVelocity([-vel[0], vel[1]])
				obstacles[i].setPosition( [win.getWidth(), location[1]] )


			if movit2:
				obstacles[i].setPosition(location)

		# decide whether to put a ball into play
		if random.random() < .01 and n < len(obstacles):
			obstacles[n].draw()
			n += 1

		current = ball.getVelocity()
		'''Tests for user interaction'''
		if key =='Left':
			ball.setVelocity([current[0]-50, current[1]])
		if key == 'Right':
			ball.setVelocity([current[0]+50, current[1]])

		'''Tests if the ball has collided with anything'''
		collided = False

		for item in obstacles:
                        #If the balls collide with the user ball, we see the end screen
			if coll.collision( ball, item, dt ) == True:
				collided = True
				ball.undraw()
				for i in obstacles:
					i.undraw()
				txtF = gr.Text( gr.Point( 250, 100 ), 'Nice Job, You received a score of...' )
				txtF.setSize( 16 )
				txtF.draw( win )
				txt4 = gr.Text( gr.Point( 250, 200 ), dodged )
				txt4.setSize( 16 )
				txt4.draw( win )
				txt5 = gr.Text( gr.Point( 250, 300 ), 'Click the mouse to quit' )
				txt5.setSize( 16 )
				txt5.draw( win )
		if collided:
			break
			
		if not collided:
			ball.update(dt)

		if not collided:
			# calls the update method of the ball with dt as the time step
			ball.update(dt)

		# calls win.update()
		win.update()
	win.getMouse()
	# closes the window
	win.close()

if __name__ == "__main__":
	main()
