#Create graphs with plotly
import plotly.plotly as py
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np
def main():
    SIZE_OF_GRAPH = 20  #this value and max axis value must be divisible with a remainder of 0
    MAX_AXIS_VALUE = int(SIZE_OF_GRAPH/2) #for SIZE_OF_GRAPH of 20, this would be 10x10 to allowe the additional 10x10 on the walk
    BOX_SIZE = 5 #length and width of boxes on graph
    NUM_OF_BOXES = int((SIZE_OF_GRAPH/BOX_SIZE)*2) #number of boxes in 1 row of graph (to get all boxes, square this number)
    NUM_OF_CHANNELS = 32 #number of channels per box

    #Max size of graph if size=10 is 20x20 because the walk can put you at 20
    #if no walk, graph size is 10x10
    random_x = [] #initialization of list for x values for graph
    random_y = [] #initialization of list for y values for graph
    box_list = [] #initialization of list for all coordinates for all boxes on graphs
    node_in_box_list = [] #initialization of list for the boxes that the nodes generated are in

    w, h = NUM_OF_CHANNELS,NUM_OF_BOXES*NUM_OF_BOXES; #width and height of all_channels (2d list/matrix). 
                                                          #Num of channels is squared beacuse num of channels only gives you the length in one row of boxes, across the graph
    all_channels = [[0 for x in range(w)] for y in range(h)] # initialize the all_channels with all 0's
    x1 = -SIZE_OF_GRAPH
    y1 = -SIZE_OF_GRAPH
    x2 = x1+BOX_SIZE
    y2 = y1+BOX_SIZE

    #create the graph, the boxes on the graph, and the channels for the boxes
    create_boxes(x1,x2,y1,y2,box_list,SIZE_OF_GRAPH,BOX_SIZE,NUM_OF_BOXES)
    create_graph(random_x,random_y,MAX_AXIS_VALUE,box_list)
    create_channels(NUM_OF_CHANNELS,NUM_OF_BOXES,all_channels)

    #find out what boxes the nodes are in
    node_in_box(random_x,random_y,box_list,node_in_box_list)

    #print the boxes that nodes are in, and the channels in those boxes
    print("node in box 1" ,node_in_box_list)
    for i in range(len(node_in_box_list)):
        print("all channels at i: ",all_channels[node_in_box_list[i]], "i: " ,i)

    node_in_box_list = [] #make the list empty again so you can add new channels and display them
    
    #let nodes move on the graph
    graph_walk(random_x,random_y,MAX_AXIS_VALUE)

    #find out what boxes the nodes that have walked are in
    node_in_box(random_x,random_y,box_list,node_in_box_list)

    #print the boxes that nodes are in, and the channels in those boxes
    print("node_in_box_list after walk: ", node_in_box_list)
    for i in range(len(node_in_box_list)):
        print("all channesl at i: " ,all_channels[node_in_box_list[i]], "i: " ,i)
    

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
    node_number = int(input("How many nodes would you like to run this simulation with? "))
    #print("Nodes: ",N)
    for i in range (node_number):
        random_x.append(np.random.uniform(-MAX_AXIS_VALUE, MAX_AXIS_VALUE)) #get a random float number within given range
        random_y.append(np.random.uniform(-MAX_AXIS_VALUE, MAX_AXIS_VALUE)) #get a random float number within given range
        # for j in range(0,len(box_list)): #check what box each of the x,y vgvalues lands in
        #     if(random_x[i]>=box_list[j][0] and random_x[i]<=box_list[j][2] and random_y[i]<=box_list[j][1] and random_y[i]>=box_list[j][5]):
        #         print("j",j)
        #         print("j in array",box_list[j])
    print("random x:",random_x,"\nrandom y:",random_y)
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

def graph_walk(random_x,random_y, MAX_AXIS_VALUE):
    #Modify the x and y value
    for x in range(len(random_x)):
        movex = np.random.uniform(-MAX_AXIS_VALUE, MAX_AXIS_VALUE) #get a random float number within given range
        movey = np.random.uniform(-MAX_AXIS_VALUE, MAX_AXIS_VALUE) #get a random float number within given range
        #Add the new values to existing values to get new nooe x,y
        random_x[x] += movex
        random_y[x] += movey

    #second trace
    trace2 = go.Scatter(
        x = random_x,
        y = random_y,
        mode = 'markers'
    )

    print("random x:",random_x,"\nrandom y:",random_y)
    #second trace
    data2 = [trace2]
    #this makes the file name random so that the file isnt overwritten 
    #each time this program runs
    randFileName2 = np.random.randn()
    nameOfFile2 = "scatterWALK"+ str(randFileName2)

    # Plot and embed in ipython notebook!
    py.plot(data2, filename=nameOfFile2)

def create_channels(NUM_OF_CHANNELS,NUM_OF_BOXES,all_channels):
    for i in range (NUM_OF_BOXES*NUM_OF_BOXES):
        for j in range (NUM_OF_CHANNELS):
            all_channels[i][j] = np.random.randint(0,2) # 0,2 because we want 2 possible states for the channels, 0-off, 1-on
        # print(all_channels)


def node_in_box(random_x,random_y,box_list,node_in_box_list):
    for i in range (len(random_x)):
        for j in range(len(box_list)):
            #check a node lands within a boxes x,y pairs, save that box to an array
            if(random_x[i]>=box_list[j][0] and random_x[i]<=box_list[j][2] and random_y[i]<=box_list[j][1] and random_y[i]>=box_list[j][5]):
              # print("j",j,"i",i)
              node_in_box_list.append(j)
              # print(box_list[j])
              # print(random_x[i])
              # print(random_y[i])
              # print(box_list[j][0])
              # print(box_list[j][2])
              # print(box_list[j][1])
              # print(box_list[j][5])
              # print("\n")

main()