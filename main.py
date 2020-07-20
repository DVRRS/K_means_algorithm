from functions import * 
from point import * 

def main (): 
	# Get user input
	pointsCant = getUserInt ("Number of points")
	centroidsCant = getUserInt ("Number of centrois")

	# Generate random points and centroids (in a list)
	points = generatePoints (pointsCant)
	centroids = generateCentroids (centroidsCant)

	# Mainloop
	run = True 
	while run:

		# Clusters 
		clusters = {}
		for cent in centroids: 
			a = set()
			clusters[cent] = a

		for p in points: 
			nearestCentroid = centroids[0]

			# Compare the distance of each centorid and get the nearest
			for index, c in enumerate(centroids): 
				distance = getDistance (p, c)
				if distance < getDistance (p, nearestCentroid):
					nearestCentroid = centroids[index]

			s = clusters[nearestCentroid]
			s.add (p)
			clusters[nearestCentroid] = s

		# Print clustering result
		# print ("###############################")
		# printResults (clusters)
		# print ("###############################")
		# Ploting step by step
		# It has the centroids unuploaded (uses the old centroid)
		plot (clusters)

		# Recalculate centroids
		newCentroids = []
		for cantroid, pointSet in clusters.items(): 
			newCentroid = recalculateCentroid (pointSet)

			if newCentroid == None: 
				newCentroids.append (cantroid)
			else: 
				newCentroids.append (newCentroid)

		res = compareCentroids (centroids, newCentroids)
		
		if res:
			# Found the result 
			run = False
			return clusters
		
		else: 
			# Continue clustering
			centroids = newCentroids

		# It has the centroids uploaded (uses the new centroid)
		plot (clusters)


if __name__ == '__main__':

	result = main()

	print("\n\n")
	print ("***** Final result ******")
	printResults (result)
	plot (result)

# https://www.tutorialspoint.com/matplotlib/matplotlib_scatter_plot.htm#:~:text=Scatter%20plots%20are%20used%20to,the%20X%20and%20Y%20axes.