class Node:
	def __init__(self,x_val,y_val,node_num):
		self.node_num = node_num
		self.x_val = x_val
		self.y_val = y_val
		self.boxes_passed = []
		self.coordinates = []
		self.x_walk = None
		self.y_walk = None
		self.want_to_go = None
		self.channels={}

		



# josh = Node(1,2)
# josh.boxes_passed.append(1)

# josh.boxes_passed.append(2)
# print(len(josh.boxes_passed))

# josh = Node(1,2,3)
# print(josh)