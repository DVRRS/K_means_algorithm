class Point: 

	def __init__ (self, x, y): 
		self.x = x 
		self.y = y

	def getCoordenates (self): 
		return (self.x, self.y)

	def __str__ (self): 
		return f"({self.x}, {self.y})"


class Centroid (Point): 

	def __init__ (self, x, y): 
		super().__init__ (x, y)