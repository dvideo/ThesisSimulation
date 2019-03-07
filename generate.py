import numpy as np

def main():
	SIZE_OF_GRAPH = 20  #this value and max axis value must be divisible with a remainder of 0
	MAX_AXIS_VALUE = int(SIZE_OF_GRAPH/2) #for SIZE_OF_GRAPH of 20, this would be 10x10 to allowe the additional 10x10 on the walk
	random_x = [] #initialization of list for x values for graph
	random_y = [] #initialization of list for y values for graph

	create_graph(random_x,random_y,MAX_AXIS_VALUE)
	file = open('axisValues.txt','w') 
	for i in range(0,len(random_x)):
		file.write(str(random_x[i]))
		file.write('\n')
		file.write(str(random_y[i]))
		file.write('\n')
		

	file.close()
	# read(random_x,random_y)
	# print(random_x)
	# print(random_y)

def create_graph(random_x,random_y,MAX_AXIS_VALUE):
    node_number = int(input("How many nodes would you like to run this simulation with? "))
    #print("Nodes: ",N)
    for i in range (node_number):
        random_x.append(np.random.uniform(-MAX_AXIS_VALUE, MAX_AXIS_VALUE)) #get a random float number within given range
        random_y.append(np.random.uniform(-MAX_AXIS_VALUE, MAX_AXIS_VALUE)) #get a random float number within given range
    print("random x:",random_x,"\nrandom y:",random_y)




# def read(random_x,random_y):
# 	file = open('axisValues.txt','r')
# 	# file = file.readline()
# 	# file = string.split(numbers)
# 	count = 0
# 	for line in file:
# 		line = line.rstrip('\n')
# 		if count%2==0:
# 			random_x.append(line)
# 		else:
# 			random_y.append(line)
# 		#print("hi")
# 		count+=1
# 		# print(line)

main()