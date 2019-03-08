#Create graphs with plotly
import plotly.plotly as py
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np

import nodeClass as nc
def main():
    SIZE_OF_GRAPH = 20  #this value and max axis value must be divisible with a remainder of 0
    MAX_AXIS_VALUE = int(SIZE_OF_GRAPH/2) #for SIZE_OF_GRAPH of 20, this would be 10x10 to allowe the additional 10x10 on the walk
    BOX_SIZE = 5 #length and width of boxes on graph
    NUM_OF_BOXES = int((SIZE_OF_GRAPH/BOX_SIZE)*2) #number of boxes in 1 row of graph (to get all boxes, square this number)
    NUM_OF_CHANNELS = 32 #number of channels per box
    NUM_OF_WALKS = 2

    #Max size of graph if size=10 is 20x20 because the walk can put you at 20
    #if no walk, graph size is 10x10
    random_x = [] #initialization of list for x values for graph
    random_y = [] #initialization of list for y values for graph
    box_list = [] #initialization of list for all coordinates for all boxes on graphs
    node_in_box_list = [] #initialization of list for the boxes that the nodes generated are in
    nodes_dictionary = {}

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

    for i in range(0,len(nodes_dictionary)):
        print(i, " ",nodes_dictionary[i].x_val, " ", nodes_dictionary[i].y_val, " ",nodes_dictionary[i].boxes_passed)
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
    #Modify the x and y value
    for x in range(len(random_x)):
        for i in range (0,NUM_OF_WALKS): #here
            movex = np.random.uniform(-BOX_SIZE, BOX_SIZE) #get a random float number within given range
            movey = np.random.uniform(-BOX_SIZE, BOX_SIZE) #get a random float number within given range
            # node_in_box()
            #Add the new values to existing values to get new x,y
            nodes_dictionary[x].x_val += movex
            nodes_dictionary[x].y_val += movey
            # print("x: ",x)

            node_in_box(box_list,nodes_dictionary,x)
            # print("if ",i)
            #this removes channel the oldest channel every loop after the 2nd walk
            if(i>=1):
                # print("hi")
                # for j in range(0,len(nodes_dictionary)):
                nodes_dictionary[x].boxes_passed.pop(0)

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

def create_channels(NUM_OF_CHANNELS,NUM_OF_BOXES,all_channels):
    for i in range (NUM_OF_BOXES*NUM_OF_BOXES):
        for j in range (NUM_OF_CHANNELS):
            all_channels[i][j] = np.random.randint(0,2) # 0,2 because we want 2 possible states for the channels, 0-off, 1-on
        # print(all_channels)

# def refresh_channels():

def node_in_box(box_list, nodes_dictionary,x):
    # for i in range (len(random_x)):
    temp_node = nodes_dictionary[x]
    # print(temp_node.x_val, " ", temp_node.y_val, " ", x)
    for j in range(len(box_list)):
        #check a node lands within a boxes x,y pairs, save that box to an array
        if(temp_node.x_val>=box_list[j][0] and temp_node.x_val<=box_list[j][2] and temp_node.y_val<=box_list[j][1] and temp_node.y_val>=box_list[j][5]):
          # print("j",j,"i",i)
          # node_in_box_list.append(j)
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


main()