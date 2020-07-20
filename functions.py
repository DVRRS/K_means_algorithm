import random
import math
import matplotlib.pyplot as plt
from point import * 

def generatePoints (points, max_x=50, max_y=50): 
	"""
	This function generates a number of random points. 
	:param points: int
	:param max_x: int
	:param max_y: int
	:returns: set
	"""
	p = set()

	for _ in range (points): 
		x = random.randint (0, max_x)
		y = random.randint (0, max_y)
		p.add (Point(x, y))

	return p

def generateCentroids (k, max_x=50, max_y=50): 
	"""
	This function generates k random centroids. 
	:param k: int
	:param max_x: int
	:param max_y: int
	:returns: list
	"""
	c = []

	for _ in range (k): 
		x = random.randint (0, max_x)
		y = random.randint (0, max_y)
		c.append (Centroid(x, y))

	return c

def getDistance (point, centroid): 
	"""
	This function returns the euclidean distance between a point and a centroid. 
	:param poinr: point.Point
	:param centroid: point.Centroid
	:returns: float
	"""
	return math.sqrt (abs(point.x - centroid.x)**2 + abs(point.y - centroid.y)**2)

def getUserInt (message): 
	"""
	This function gets an integer input from the user. 
	:param message: String	
	"""
	while True: 
		try: 
			number = int (input (f"{message}: \n> "))
			break
		except: 
			continue

	return number

def recalculateCentroid (pointSet): 
	"""
	This function get the mean point of all the points associated with a centroid
	in order to update the centroid coordenate. 
	:param pointSet: set of point.Point
	:returns: Centroid
	"""
	if len (pointSet) == 0: 
		return None

	x = 0
	y = 0
	for p in pointSet: 
		x += p.x
		y += p.y

	newCentroid = Centroid (x//len(pointSet), y//len(pointSet))
	return newCentroid

def printResults (dictionary): 
	for centorid, point in dictionary.items(): 
		print ("Centroids: ")
		print (centorid)
		print ("Points: ")
		ps = ""
		for p in point: 
			ps += p.__str__()
			ps += "  "
		print (ps)
		print ()

def compareCentroids (oldCentroids, newCentroids): 
	"""
	This function compares the new centroids with the old centroids,
	if the centroids are the same, returns True, else returns false. 
	:param oldCentroids: list of point.Centroid
	:param newCentroids: lit of point.Centroid
	"""
	for old, new in zip (oldCentroids, newCentroids): 
		if old.x == new.x and old.y == new.y: 
			pass
		else: 
			return False

	return True

def plot (data): 
	"""
	This function plots all the data in a scatterplot. 
	:param data: dictionary
	"""
	fig = plt.figure() 
	ax = fig.add_axes ([0, 0, 1, 1])
	for key, value in data.items(): 
		pointsX = []
		pointsY = []

		for point in value: 
			pointsX.append (point.x)
			pointsY.append (point.y)

		centroidX = key.x
		centroidY = key.y

		ax.scatter (pointsX, pointsY)
		ax.scatter (centroidX, centroidY, marker='x')

	plt.show()