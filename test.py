# random_x = []
# random_y = []
# max_x = 5*2
# max_y = 5*2
# count=0
# negCount = 0
# test = "box"
# test += str(1)
# #while max_x<0 and max_y<0:
# print(test)
    


# while count<=20 and negCount>=-20:
# 	print(count)
# 	print(negCount)
# 	print("\n")
# 	count+=5
# 	negCount-=5

# print("end")
# print(count)
# print(negCount)

import numpy as np
SIZE_OF_GRAPH = 20
BOX_SIZE = 5
#Max size of graph if size=10 is 20x20 because the walk can put you at 20
#if no walk it is 10x10
random_x = []
random_y = []
box_array = [[]]
# max_x = SIZE_OF_GRAPH
# max_y = SIZE_OF_GRAPH
count=0
box_name = 'box'
x1 = -SIZE_OF_GRAPH
y1 = -SIZE_OF_GRAPH
x2 = x1+BOX_SIZE
y2 = y1+BOX_SIZE

#while max_x<0 and max_y<0: # change this to while they are both greater then -max and less than max
    #box_name+=str(count)
    #box_array[count]
#while x2!=SIZE_OF_GRAPH and y2!=0:
for i in range(0,8):
	x1 = -SIZE_OF_GRAPH
	x2 = x1+BOX_SIZE
	for p in range(0,8):
		box_array[count] = [x1,-y1,
							x2,-y1,
		                    x1,-y2,
		                    x2,-y2] #probably need 4 sets of coordinates in here 
		
		print(box_array)
		x1+=BOX_SIZE
		x2+=BOX_SIZE

	y1+=BOX_SIZE
	y2+=BOX_SIZE





    




