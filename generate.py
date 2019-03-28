import numpy as np
import nodeClass as nc
def main():
	SIZE_OF_GRAPH = 50  #this value and max axis value must be divisible with a remainder of 0
	MAX_AXIS_VALUE = int(SIZE_OF_GRAPH/2) #for SIZE_OF_GRAPH of 20, this would be 10x10 to allowe the additional 10x10 on the walk
	random_x = [] #initialization of list for x values for graph
	random_y = [] #initialization of list for y values for graph
	dictionary = {}

	generate_nodes(random_x,random_y,MAX_AXIS_VALUE)
	file = open('axisValues.txt','w') 
	for i in range(0,len(random_x)):
		file.write(str(random_x[i]))
		file.write('\n')
		file.write(str(random_y[i]))
		file.write('\n')
		

	file.close()
	random_x = []
	random_y = []
	readFile(random_x,random_y)
	# print(random_x)
	# print(random_y)

	node_object(random_x,random_y,dictionary)
	for i in dictionary:
		print(i, " ", dictionary[i].x_val, " ", dictionary[i].y_val, " ")
	# print(dictionary[9].x_val,dictionary[9].y_val)
	# for i in range (0,len(obj_array)):
		# print(obj_array[i].x_val," ", obj_array[i].y_val, " ",obj_array[i].node_num," ")

def generate_nodes(random_x,random_y,MAX_AXIS_VALUE):
    node_number = int(input("How many nodes would you like to run this simulation with? "))
    #print("Nodes: ",N)
    for i in range (node_number):
        random_x.append(round(np.random.uniform(-MAX_AXIS_VALUE, MAX_AXIS_VALUE),2)) #get a random float number within given range
        random_y.append(round(np.random.uniform(-MAX_AXIS_VALUE, MAX_AXIS_VALUE),2)) #get a random float number within given range
    # print("random x:",random_x,"\nrandom y:",random_y)




def readFile(random_x,random_y):
    file = open('axisValues.txt','r')
    # file = file.readline()
    # file = string.split(numbers)
    count = 0
    for line in file:
        line = line.rstrip('\n')
        if count%2==0:
            random_x.append(float(line))
        else:
            random_y.append(float(line))
        #print("hi")
        count+=1
        # print(line)
    file.close()
    print("random_x ", random_x, "\nrandom_y ",random_y)


def node_object(random_x,random_y,dictionary):
	#create node obj for the nodes and store those in a dictionary
	for i in range(0,len(random_x)):
		dictionary[i] = nc.Node(random_x[i],random_y[i],i)


main()