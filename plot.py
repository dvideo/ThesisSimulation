#Create graphs with plotly
import plotly.plotly as py
import plotly.graph_objs as go

#Create random data with numpy
import numpy as np

#Node object file
import nodeClass as nc

#Cluster object file
import clusters as cl

def main():
    SIZE_OF_GRAPH = 100  #this value and max axis value must be divisible with a remainder of 0
    MAX_AXIS_VALUE = int(SIZE_OF_GRAPH/2) #for SIZE_OF_GRAPH of 20, this would be 10x10 to allowe the additional 10x10 on the walk
    BOX_SIZE = 5 #length and width of boxes on graph
    NUM_OF_BOXES = int((SIZE_OF_GRAPH/BOX_SIZE)*2) #number of boxes in 1 row of graph (to get all boxes, square this number)
    NUM_OF_CHANNELS = 32 #number of channels per box
    NUM_OF_WALKS = 2
    CLUSTER_SIZE = 3

    #Max size of graph if size=10 is 20x20 because the walk can put you at 20
    #if no walk, graph size is 10x10
    random_x = [] #initialization of list for x values for graph
    random_y = [] #initialization of list for y values for graph
    box_list = [] #initialization of list for all coordinates for all boxes on graphs
    node_in_box_list = [] #initialization of list for the boxes that the nodes generated are in
    nodes_dictionary = {}
    cluster_dictionary = {}

    w, h = NUM_OF_CHANNELS,NUM_OF_BOXES*NUM_OF_BOXES; #width and height of all_channels (2d list/matrix). 
                                                          #Num of channels is squared beacuse num of channels only gives you the length in one row of boxes, across the graph
    all_channels = [[0 for x in range(w)] for y in range(h)] # initialize the all_channels with all 0's
    x1 = -SIZE_OF_GRAPH
    y1 = -SIZE_OF_GRAPH
    x2 = x1+BOX_SIZE
    y2 = y1+BOX_SIZE


    # test = nc.Node(-2,3,[1,2])
    # print(test.x_val)

    #create the graph, the boxes on the graph, and the channels for the boxes
    create_boxes(x1,x2,y1,y2,box_list,SIZE_OF_GRAPH,BOX_SIZE,NUM_OF_BOXES)

    readFile(random_x,random_y)

    nodes_in_dictionary(random_x,random_y,nodes_dictionary)

    clustering(CLUSTER_SIZE,nodes_dictionary,cluster_dictionary)

    # distance(nodes_dictionary, MAX_AXIS_VALUE)

    for i in range (0,len(cluster_dictionary)):
        print("cluster: ", i , " ",cluster_dictionary[i].nodes_in_cluster, "  Head: ",cluster_dictionary[i].cluster_head)
   

    # create_graph(random_x,random_y,MAX_AXIS_VALUE,box_list)
    
    create_channels(NUM_OF_CHANNELS,NUM_OF_BOXES,all_channels)

    #find out what boxes the nodes are in
    for i in range (0,len(nodes_dictionary)):
        node_in_box(box_list,nodes_dictionary,i)

    # for i in range(0,len(nodes_dictionary)):
    #     print(i, " ",nodes_dictionary[i].x_val, " ", nodes_dictionary[i].y_val, " ",nodes_dictionary[i].boxes_passed)
   

    #print the boxes that nodes are in, and the channels in those boxes
    # print("node in box 1" ,node_in_box_list)
    # for i in range(len(node_in_box_list)):
    #     print("all channels at i: ",all_channels[node_in_box_list[i]], "i: " ,i)

    # node_in_box_list = [] #make the list empty again so you can add new channels and display them
    
    #let nodes move on the graph
    graph_walk(random_x,random_y, MAX_AXIS_VALUE, BOX_SIZE, NUM_OF_WALKS,box_list,nodes_dictionary)

    send_queries(nodes_dictionary)

    for i in range(0,len(nodes_dictionary)):
        print(i, " ", nodes_dictionary[i].coordinates, " ",nodes_dictionary[i].boxes_passed , " ", nodes_dictionary[i].x_walk , " ",nodes_dictionary[i].y_walk )
        for j in range (0,len(nodes_dictionary[i].boxes_passed)):
            print('channels: ', all_channels[nodes_dictionary[i].boxes_passed[j]])
    #find out what boxes the nodes that have walked are in
    # node_in_box(random_x,random_y,box_list,node_in_box_list)

    #print the boxes that nodes are in, and the channels in those boxes
    # print("node_in_box_list after walk: ", node_in_box_list)
    # for i in range(len(node_in_box_list)):
    #     print("all channesl at i: " ,all_channels[node_in_box_list[i]], "i: " ,i)
    

def create_boxes(x1,x2,y1,y2,box_list,SIZE_OF_GRAPH,BOX_SIZE,NUM_OF_BOXES):
    for i in range(NUM_OF_BOXES):
        x1 = -SIZE_OF_GRAPH
        x2 = x1+BOX_SIZE
        for p in range(NUM_OF_BOXES):
            box_list.append([x1,-y1,
                                x2,-y1,
                                x1,-y2,
                                x2,-y2])
            x1+=BOX_SIZE
            x2+=BOX_SIZE
        y1+=BOX_SIZE
        y2+=BOX_SIZE

    #uncomment this to see coordinates and numbers of all boxes
    # for i in range (len(box_list)):
    #     print(i," box_list ", box_list[i])


def create_graph(random_x,random_y,MAX_AXIS_VALUE,box_list):
    # Create a trace
    trace = go.Scatter(
        x = random_x,
        y = random_y,
        mode = 'markers'
    )
    #first trace
    data = [trace]
    #this makes the file name random so that the file isnt overwritten 
    #each time this program runs
    randFileName = np.random.randn()
    nameOfFile = "scatter"+ str(randFileName)

    # Plot and embed in ipython notebook!
    py.plot(data, filename=nameOfFile)

    # or plot with: plot_url = py.plot(data, filename='basic-line')

def graph_walk(random_x,random_y, MAX_AXIS_VALUE,BOX_SIZE,NUM_OF_WALKS,box_list,nodes_dictionary):
    #For all the nodes
    for j in range(len(random_x)):
        x_move_val = np.random.uniform(-MAX_AXIS_VALUE, MAX_AXIS_VALUE) #Get the value where x will end
        y_move_val = np.random.uniform(-MAX_AXIS_VALUE, MAX_AXIS_VALUE) #Get the value where y will end
        x_distance = random_x[j] - x_move_val #Get the distance between where x currently is and where x will end up
        y_distance = random_y[j] - y_move_val #Get the distance between where y currently is and where y will end up
        x_walk = x_distance/NUM_OF_WALKS #The distance x will move per walk
        y_walk = y_distance/NUM_OF_WALKS #The distance y will move per walk
        for i in range (0,NUM_OF_WALKS): 
            nodes_dictionary[j].x_val += x_walk
            nodes_dictionary[j].y_val += y_walk
            nodes_dictionary[j].x_walk = x_walk
            nodes_dictionary[j].y_walk = y_walk
            # node_in_box()
            #Add the new values to existing values to get new x,y
           
           
            # print("x: ",x)

            node_in_box(box_list,nodes_dictionary,j)
            # print("if ",i)
            #this removes channel the oldest channel every loop after the 2nd walk
            # if(i>=1):  bring this back for "forgetting nodes"
                # print("hi")
                # for j in range(0,len(nodes_dictionary)):
                # nodes_dictionary[x].boxes_passed.pop(0) bring this back for "forgetting nodes"

    #second trace
    # trace2 = go.Scatter(
    #     x = random_x,
    #     y = random_y,
    #     mode = 'markers'
    # )

    # print("random x:",random_x,"\nrandom y:",random_y)
    #second trace
    # data2 = [trace2]
    #this makes the file name random so that the file isnt overwritten 
    #each time this program runs
    # randFileName2 = np.random.randn()
    # nameOfFile2 = "scatterWALK"+ str(randFileName2)

    # Plot and embed in ipython notebook!
    # py.plot(data2, filename=nameOfFile2)

def send_queries(nodes_dictionary):
    for i in range(len(nodes_dictionary)):
        print("new x val",nodes_dictionary[i].coordinates[len(nodes_dictionary[i].coordinates)-1][0] + nodes_dictionary[i].x_walk)
        print("new y val",nodes_dictionary[i].coordinates[len(nodes_dictionary[i].coordinates)-1][1] + nodes_dictionary[i].y_walk)


def create_channels(NUM_OF_CHANNELS,NUM_OF_BOXES,all_channels):
    for i in range (NUM_OF_BOXES*NUM_OF_BOXES):
        for j in range (NUM_OF_CHANNELS):
            all_channels[i][j] = np.random.randint(0,3) # 0,2 because we want 2 possible states for the channels, 0-off, 1-on
        # print(all_channels)

# def refresh_channels():

def distance(nodes_dictionary, MAX_AXIS_VALUE):
    for i in range (len(nodes_dictionary)):
        print("n in d i: " , i , " " ,nodes_dictionary[i].x_val, " ", nodes_dictionary[i].y_val)
        tempx = np.random.uniform(-MAX_AXIS_VALUE, MAX_AXIS_VALUE)
        tempy = np.random.uniform(-MAX_AXIS_VALUE, MAX_AXIS_VALUE)
        distancex = nodes_dictionary[i].x_val - tempx
        distancey = nodes_dictionary[i].y_val - tempy
        divide3 = distancex/3
        print("n in d i: " , i , " " ,tempx, " ", tempy, " distancex: ", distancex, " distancey: ", distancey, " divided by 3x: ",distancex/3, " y: ", distancey/3)


def node_in_box(box_list, nodes_dictionary,nodeNum):
    # for i in range (len(random_x)):
    temp_node = nodes_dictionary[nodeNum]
    # print(temp_node.x_val, " ", temp_node.y_val, " ", x)
    for j in range(len(box_list)):
        #check a node lands within a boxes x,y pairs, save that box to an array
        if(temp_node.x_val>=box_list[j][0] and temp_node.x_val<=box_list[j][2] and temp_node.y_val<=box_list[j][1] and temp_node.y_val>=box_list[j][5]):
          # print("j",j,"i",i)
          # node_in_box_list.append(j)
          temp_node.coordinates.append([temp_node.x_val,temp_node.y_val])
          temp_node.boxes_passed.append(j)
          # print(box_list[j])
          # print(random_x[i])
          # print(random_y[i])
          # print(box_list[j][0])
          # print(box_list[j][2])
          # print(box_list[j][1])
          # print(box_list[j][5])
          # print("\n")


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

def nodes_in_dictionary(random_x,random_y,nodes_dictionary):
    #create node obj for the nodes and store those in a dictionary
    for i in range(0,len(random_x)):
        nodes_dictionary[i] = nc.Node(random_x[i],random_y[i])

def clustering(CLUSTER_SIZE,nodes_dictionary,cluster_dictionary):
    num_of_clusters = len(nodes_dictionary)//CLUSTER_SIZE
    left_overs = len(nodes_dictionary)%CLUSTER_SIZE
    count = 0
    for j in range(num_of_clusters):
        cluster_dictionary[j] = cl.Cluster()
        #Run this if there are left over nodes and we are on the last cluster that will be bigger than the rest
        if j == num_of_clusters-1 and left_overs>0:
            for i in range(CLUSTER_SIZE+left_overs):
                # index = (j*CLUSTER_SIZE)+i
                cluster_dictionary[j].nodes_in_cluster.append(count)
                count+=1
        else:
            for i in range(CLUSTER_SIZE):
                # index = (j*CLUSTER_SIZE)+i
                cluster_dictionary[j].nodes_in_cluster.append(count)
                count+=1
        cluster_dictionary[j].cluster_head = cluster_dictionary[j].nodes_in_cluster[0]

main()