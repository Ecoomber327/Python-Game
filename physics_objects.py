# physics_objects.py
#
# Ethan Coomber
# 
# To run in the terminal: python3 physics_objects.py

import graphicsPlus as gr
import random
import time
import math

'''The parent function that is used in all other classes'''
class Thing:
		def __init__(self, win, the_type, pos = [0,0], vel = [0,0], acc = [0,0], elasticity = .95, color="purple"):
				self.the_type = the_type
				self.win = win
				self.pos = pos[:]
				self.vel = vel[:]
				self.acc = acc[:]
				self.shapes = []
				self.elasticity = elasticity
				self.win = win
				self.drawn = False
				self.color = color
		# Gets the position
		def getPosition(self):
				return self.pos[:]
		
		# Gets the Type
		def getType(self):
				return self.the_type
		
		# Gets the Elasticity
		def getElasticity(self):
				return self.elasticity
		
		# Gets the Velocity
		def getVelocity(self):
				return self.vel[:]
		
		# Gets the Acceleration
		def getAcceleration(self):
				return self.acc[:]
		
		# Gets the Color
		def getColor(self):
				return self.color
		
		# Sets the Velocity 
		def setVelocity( self, vel ):
				self.vel[0] = vel[0]
				self.vel[1] = vel[1]
		
		# Sets the Acceleration
		def setAcceleration( self, acc ):
				self.acc[0] = acc[0]
				self.acc[1] = acc[1]
		
		# Sets the Position
		def setPosition( self, pos ):
				# saves the current x and y positions to local variables
				x = self.pos[0]
				y = self.pos[1] 
				# updates the object_list position to be the new x and y values in pos
				self.pos[0] = pos[0]
				self.pos[1] = pos[1]
				# calculates the difference between the new and old positions to get dx and dy
				dx = self.pos[0] - x 
				dy = self.pos[1] - y
				# loops over the graphics objects and move them by dx and dy
				for shape in self.shapes: 
						shape.move( dx, -dy )
		
		# Sets the Color
		def setColor( self, c ):
				self.color = c
		
		# Sets the Elasticity
		def setElasticity( self, color ):
				self.elasticity = elasticity
		
		# Draws the thing
		def draw(self):
				# Draws the Zelle graphics shapes into the window if the objects are not drawn
				for item in self.shapes:
						item.draw(self.win)
				# sets the drawn field to True
				self.drawn = True
		
		# Un-draws the thing
		def undraw(self):
				# if the objects are not drawn, draws the Zelle graphics shapes into the window
				for item in self.shapes:
						item.undraw()
				# sets the drawn field to True
				self.drawn = False
		
		'''Updates the position of the thing using parabolic trajectories 
		and physics equations'''
		def update( self, dt ):
				# compute how much the object moves using the laws of physics
				delta_x = self.vel[0] * dt + 0.5 * self.acc[0] * dt * dt
				delta_y = self.vel[1] * dt + 0.5 * self.acc[1] * dt * dt
		
				# update the object's position
				self.pos[0] = self.pos[0] + delta_x
				self.pos[1] = self.pos[1] + delta_y
		
				# update the object's velocity
				delta_velx = self.acc[0] * dt
				delta_vely = self.acc[1] * dt
				self.vel[0] = self.vel[0] + delta_velx
				self.vel[1] = self.vel[1] + delta_vely
		
				# loop over the graphics objects and move them by how much the object moved
				for shape in self.shapes: 
						shape.move( delta_x, -delta_y )
		def getWin(self):
			return self.win

class Ball(Thing):
		def __init__(self, win, radius, pos = [0,0], vel = [0,0], acc = [0,0], elasticity = .95, color = "purple"):
			#Passes in the parameters that were already defined in thing
			Thing.__init__(self, win, 'ball', pos, vel, acc, elasticity, color )
			#These are the new parameters
			self.radius = radius
			self.render()
		
		'''Essentially ball the object in the field'''
		def render(self):
			# Assign the drawn field to a local variable
			Drawn = self.drawn		# assignments go left to right
			# if the ball is drawn
			if Drawn == True: 
			# call the ball's undraw method (e.g. self.undraw()
				self.undraw()
			# create a new Zelle Circle object using the appropriate position and radius 
			ball = gr.Circle(gr.Point(self.pos[0],self.win.getHeight() - self.pos[1]), self.radius)
			# set the Circle object's color using the color field
			ball.setFill( self.color )
			self.shapes = [ball]
			if Drawn == True:
				self.draw()
		'''gets the radius'''
		def getRadius(self):
			return self.radius
		
		'''sets the radius'''
		def setRadius( self, rad ):
			# code here: update the ball's radius information then call ball_render
			self.radius = rad
			self.render()

class Block(Thing):
		def __init__(self, win, width, height, pos = [0,0], vel = [0,0], acc = [0,0], elasticity = .95, color = 'Yellow'):
			#Passes in the parameters that were already defined in thing
			Thing.__init__(self, win, 'block', pos, vel, acc, elasticity, color )
			#These are the new parameters
			self.width = width
			self.height = height
			#self.win = getWin(self)
			
			self.render()
		
		'''Essentially block the object in the field'''
		def render(self):
			Drawn = self.drawn 
			if Drawn == True: 
				self.undraw()
			block = gr.Rectangle(gr.Point(self.pos[0] - self.width/2, self.win.getHeight() - ((self.pos[1] - self.height/2)) ), gr.Point(self.pos[0] + self.width/2, self.win.getHeight() - ((self.pos[1] + self.height/2))	 ) )
			block.setFill( self.color )
			self.shapes = [block]
			# if the ball is drawn
			if Drawn == True:
					# call the ball's draw method
					self.draw()
		
		'''Gets the height'''
		def getHeight(self):
				return self.height
		
		'''Gets the width'''
		def getWidth(self):
				return self.width
		
		'''Sets the height'''
		def setHeight( self, height ):
				# code here: update the ball's radius information then call ball_render
				self.height = height
				self.render()
		
		'''sets the width'''
		def setWidth( self, width ):
				# code here: update the ball's radius information then call ball_render
				self.width = width
				self.render()
		
		'''sets the color'''
		def setColor( self, color ):
				self.color = color

class Triangle(Thing):
		def __init__(self, win, point1 = [0, 0], point2 = [4, 0], point3 = [2, 2], pos = [0,0], vel = [0,0], acc = [0,0], elasticity = .95, color = 'Yellow'):
			#Passes in the parameters that were already defined in thing
			Thing.__init__(self, win, 'triangle', pos, vel, acc, elasticity, color )
			#These are the new parameters
			self.point1 = point1[:]
			self.point2 = point2[:]
			self.point3 = point3[:]
			
			self.render()
		
		'''Essentially triangle the object in the field'''
		def render(self):
			Drawn = self.drawn 
			if Drawn == True: 
				self.undraw()
			triangle = gr.Polygon([gr.Point(self.pos[0] + self.point1[0], self.win.getHeight() - (self.pos[1] + self.point1[1])), gr.Point(self.pos[0] + self.point2[0], self.win.getHeight() - (self.pos[1] + self.point2[1])), gr.Point(self.pos[0] + self.point3[0], self.win.getHeight() - (self.pos[1] + self.point3[1]))])
			triangle.setFill( self.color )
			self.shapes = [triangle]
			# if the ball is drawn
			if Drawn == True:
					# call the ball's draw method
					self.draw()
		
		'''Gets the points that make up the triangle'''
		def getPoint1(self):
			return self.point1
		
		def getPoint2(self):
			return self.point2
		
		def getPoint3(self):
			return self.point3
		
		'''This code is not necessary'''
		def getHeight(self):
			y = abs(self.point1[1] + self.point2[1])/2
			return y
		
		def setHeight(self, h):
			y = abs(self.point1[1] + self.point2[1])/2
			difference = abs(h - y)
			change = difference / 2
			self.point1[1] = self.point1[1] - change
			self.point2[1] = self.point1[1] - change
			self.point3[1] = self.point1[1] + change
			self.render
		
		def getWidth(self):
			x = abs(self.point1[0] + self.point2[0])/2
			return x
		
		def setWidth(self, w):
			x = abs(self.point1[0] + self.point2[0])/2
			difference = abs(w - x)
			change = difference / 2
			self.point1[0] = self.point1[0] - change
			self.point2[0] = self.point1[0] + change
			self.render
		
		
		def setPoint1( self, pos ):
				# save the current x and y positions to local variables
				x = self.pos[0]
				y = self.pos[1] 
				# update the object_list position to be the new x and y values in pos
				self.point1[0] = pos[0]
				self.point1[1] = pos[1]
				# calculate the difference between the new and old positions to get dx and dy
				dx = self.pos[0] - x 
				dy = self.pos[1] - y
				# loop over the graphics objects and move them by dx and dy
				for point in self.point1: 
						point.move( dx, -dy )
		
		def setPoint2( self, pos ):
				# save the current x and y positions to local variables
				x = self.pos[0]
				y = self.pos[1] 
				# update the object_list position to be the new x and y values in pos
				self.point2[0] = pos[0]
				self.point2[1] = pos[1]
				# calculate the difference between the new and old positions to get dx and dy
				dx = self.pos[0] - x 
				dy = self.pos[1] - y
				# loop over the graphics objects and move them by dx and dy
				for point in self.point2: 
						point.move( dx, -dy )
		
		def setPoint3( self, pos ):
				# save the current x and y positions to local variables
				x = self.pos[0]
				y = self.pos[1] 
				# update the object_list position to be the new x and y values in pos
				self.point3[0] = pos[0]
				self.point3[1] = pos[1]
				# calculate the difference between the new and old positions to get dx and dy
				dx = self.pos[0] - x 
				dy = self.pos[1] - y
				# loop over the graphics objects and move them by dx and dy
				for point in self.point3: 
						point.move( dx, -dy )
	 
			
			
class Oval(Thing):
		def __init__(self, win, point1 = [0, 0], point2 = [4, 0], pos = [0,0], vel = [0,0], acc = [0,0], elasticity = .95, color = 'Yellow'):
			Thing.__init__(self, win, 'triangle', pos, vel, acc, elasticity, color )
			self.point1 = point1[:]
			self.point2 = point2[:]
			
			self.render()
		
		'''Essentially oval the object in the field'''
		def render(self):
			# Assign the drawn field to a local variable
			Drawn = self.drawn		# assignments go left to right
			# if the ball is drawn
			if Drawn == True: 
			# call the ball's undraw method (e.g. self.undraw()
				self.undraw()
			# create a new Zelle Circle object using the appropriate position and radius 
			oval = gr.Oval(gr.Point(self.pos[0] + self.point1[0], self.win.getHeight() - (self.pos[1] + self.point1[1])), gr.Point(self.pos[0] + self.point2[0], self.win.getHeight() - (self.pos[1] + self.point2[1])))
			oval.setFill( self.color )
			self.shapes = [oval]
			if Drawn == True:
				self.draw()
		
		'''Gets the points that make up the oval'''
		def getPoint1(self):
			return self.point1
		
		def getPoint2(self):
			return self.point2
		
		'''Sets the points that make up the oval'''
		def setPoint1( self, pos ):
				# save the current x and y positions to local variables
				x = self.pos[0]
				y = self.pos[1] 
				# update the object_list position to be the new x and y values in pos
				self.point1[0] = pos[0]
				self.point1[1] = pos[1]
				# calculate the difference between the new and old positions to get dx and dy
				dx = self.pos[0] - x 
				dy = self.pos[1] - y
				# loop over the graphics objects and move them by dx and dy
				for point in self.point1: 
						point.move( dx, -dy )
		
		def setPoint2( self, pos ):
				# save the current x and y positions to local variables
				x = self.pos[0]
				y = self.pos[1] 
				# update the object_list position to be the new x and y values in pos
				self.point2[0] = pos[0]
				self.point2[1] = pos[1]
				# calculate the difference between the new and old positions to get dx and dy
				dx = self.pos[0] - x 
				dy = self.pos[1] - y
				# loop over the graphics objects and move them by dx and dy
				for point in self.point2: 
						point.move( dx, -dy )
		
		'''Gets and sets both height and width
		Not sure if this is necessary'''
		def getHeight(self):
			y = abs(self.point1[1] - self.point2[1])
			return y
		
		def setHeight(self, h):
			y = abs(self.point1[1] - self.point2[1])/2
			difference = abs(h - y)
			change = difference / 2
			self.point1[1] = self.point1[1] - change
			self.point2[1] = self.point1[1] + change
			
		
		def getWidth(self):
			x = abs(self.point1[0] - self.point2[0])
			return x
		
		def setWidth(self, w):
			x = abs(self.point1[0] - self.point2[0])/2
			difference = abs(w - x)
			change = difference / 2
			self.point1[0] = self.point1[0] - change
			self.point2[0] = self.point1[0] + change

class RotatingBlock(Thing):
	def __init__(self, win, width, height, pos=[0,0], color = 'red', anchor = None):
		Thing.__init__(self, win, 'rotating block', pos, color = color)
		self.width = width
		self.height = height
		self.points = [(-width/2, -height/2), (width/2, -height/2), (width/2, height/2), (-width/2, height/2)]
		
		'''from lab'''
		if anchor == None:
			self.anchor = pos[:]
		else:
			self.anchor = anchor[:]
		self.angle = 0.0
		self.rvel = 0.0
		self.drawn = False
			
		self.render()
	'''Gets the angle'''
	def getAngle(self):
			return self.angle
			
	'''Gets the anchor'''
	def getAnchor(self):
			return self.anchor
	
	'''Gets the rotational velocity'''
	def getRotVelocity(self):
			return self.rvel
	
	'''Gets the width'''		
	def getWidth(self):
			return self.width
	
	'''Gets the height'''
	def getHeight(self):
			return self.height
	
	'''Sets the angle'''
	def setAngle(self, angle):
			self.angle = angle
			self.render()
			
	'''Sets the anchor'''
	def setAnchor(self, anchor):
			self.anchor[0] = anchor[0]
			self.anchor[1] = anchor[1]
			self.render()
	
	'''Sets the rotational velocity'''
	def setRotVelocity(self, vel):
			self.rvel = vel
			self.render()
	
	'''Sets the width'''
	def setWidth(self, width):
			self.width = width
			self.render()
	
	'''Sets the height'''
	def setHeight(self, height):
			self.height = height
			self.render()
	
	'''rotates the block'''		
	def rotate(self, da):
			self.angle = self.angle + da
			self.render()
	
	'''renders the object'''
	def render(self):
			# assigns to a local variable (e.g. drawn) the value in self.drawn
			drawn = self.drawn
			# if drawn
			if drawn == True:
			# calls the undraw method 
				self.undraw()
			
			# assign to self.points a list with two 2-element sublists that
			self.points = [(-self.width/2, -self.height/2), (self.width/2, -self.height/2), (self.width/2, self.height/2), (-self.width/2, self.height/2)]
			
			# assigns to theta the result of converting self.angle from degrees to radians
			theta = (((self.angle)*math.pi)/180.0)
			# assigns to cth the cosine of theta
			cth = math.cos(theta)
			# assigns to sth the sine of theta
			sth = math.sin(theta)
			# assigns to pts the empty list
			pts = []
		
		
			# for each vertex in self.points
			for vertex in self.points:
			# (2 lines of code): assign to x and y the result of adding the vertex to self.pos and subtracting self.anchor
				x = vertex[0] + self.pos[0] - self.anchor[0]
				y = vertex[1] + self.pos[1] - self.anchor[1]
			
				# assign to xt the calculation x * cos(theta) - y * sin(theta) using your precomputed cos/sin values above
				xt = x * math.cos(theta) - y * math.sin(theta)
				# assign to yt the calculation x * sin(theta) + y * cos(theta)
				yt = x * math.sin(theta) + y * math.cos(theta)
				
				# (2 lines of code): assign to x and y the result of adding xt and yt to self.anchor
				x = xt + self.anchor[0]
				y = yt + self.anchor[1]
				
				# append to pts a Point object with coordinates (x, self.win.getHeight() - y)
				pts.append(gr.Point(x, self.win.getHeight() - y))
			#creates the shape
			polygon = gr.Polygon(pts[0],pts[1], pts[2], pts[3])
			polygon.setFill(self.color)
			# assign to self.shapes a list containing a Zelle graphics Line object using the Point objects in pts
			self.shapes = [ polygon ]
			
			# if drawn
			if drawn == True:
			# call the draw method 
				self.draw()
	
	'''This function updates the rotation of the block'''
	def update( self, dt ):
			#gets the revolutions
			da = self.rvel * dt
			#rotates the block
			if da >= 0:
				self.rotate(da)
			Thing.update( self, dt )
			
		
		
