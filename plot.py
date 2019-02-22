#import plotly 
#plotly.tools.set_credentials_file(username='dvideo', api_key='Yz9kDPJ2CHuPrZtcVpFs')
##import plotly.plotly as py
##import plotly.graph_objs as go
##
##trace0 = go.Scatter(
##    x=[10, 15, 13, 17],
##    y=[10, 15, 13, 17]
##)
##trace1 = go.Scatter(
##    x=[1, 2, 3, 4],
##    y=[1, 2, 3, 4]
##)
##data = [trace0, trace1]
##
##py.plot(data, filename = 'basic-line2', auto_open=True)

import plotly.plotly as py
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np
def main():
    SIZE_OF_GRAPH = 20  #these numbers must be divisible with a remainder of 0
    MAX_AXIS_VALUE = int(SIZE_OF_GRAPH/2) #for SIZE_OF_GRAPH of 20, this would be 10x10 to allowe the additional 10x10 on the walk
    BOX_SIZE = 5 #length and width of boxes
    NUM_OF_BOXES = int((SIZE_OF_GRAPH/BOX_SIZE)*2) #number of total boxes that we will have in the entire graph
    NUM_OF_CHANNELS = 32 #number of channels per box

    #Max size of graph if size=10 is 20x20 because the walk can put you at 20
    #if no walk it is 10x10
    random_x = [] #initialization of array for x values for graph
    random_y = [] #initialization of array for y values for graph
    box_array = [] #initialization of array for all coordinates for all boxes on graphs
    node_in_box_array = [] #initialization of array for the boxes that the nodes generated are in

    w, h = NUM_OF_CHANNELS,NUM_OF_BOXES*NUM_OF_BOXES; #width and height of all_channels (2d array). 
                                                          #Num of channels is squared beacuse num of channels only gives you the length in one row of boxes, across the graph
    all_channels = [[0 for x in range(w)] for y in range(h)] # initialize the all_channels with all 0's
    # max_x = SIZE_OF_GRAPH
    # max_y = SIZE_OF_GRAPH
    # box_name = 'box'
    x1 = -SIZE_OF_GRAPH
    y1 = -SIZE_OF_GRAPH
    x2 = x1+BOX_SIZE
    y2 = y1+BOX_SIZE

    create_boxes(x1,x2,y1,y2,box_array,SIZE_OF_GRAPH,BOX_SIZE,NUM_OF_BOXES)
    create_graph(random_x,random_y,MAX_AXIS_VALUE,box_array)

    node_in_box(random_x,random_y,box_array,node_in_box_array)
    print(node_in_box_array)
    for i in range(0,len(node_in_box_array)):
        print(all_channels[i])

    node_in_box_array = [] #make the array empty again so you can add new channels and display them
    graph_walk(random_x,random_y,MAX_AXIS_VALUE)
    create_channels(NUM_OF_CHANNELS,NUM_OF_BOXES,all_channels)

    node_in_box(random_x,random_y,box_array,node_in_box_array)
    print(node_in_box_array)
    for i in range(0,len(node_in_box_array)):
        print(all_channels[i])
    

def create_boxes(x1,x2,y1,y2,box_array,SIZE_OF_GRAPH,BOX_SIZE,NUM_OF_BOXES):
    for i in range(0,NUM_OF_BOXES):
        x1 = -SIZE_OF_GRAPH
        x2 = x1+BOX_SIZE
        for p in range(0,NUM_OF_BOXES):
            box_array.append([x1,-y1,
                                x2,-y1,
                                x1,-y2,
                                x2,-y2])
            x1+=BOX_SIZE
            x2+=BOX_SIZE
        y1+=BOX_SIZE
        y2+=BOX_SIZE


def create_graph(random_x,random_y,MAX_AXIS_VALUE,box_array):
    import numpy as np
    N = int(input("How many nodes would you like to run this simulation with? "))
    #print("Nodes: ",N)
    for i in range (0,N):
        random_x.append(np.random.uniform(-MAX_AXIS_VALUE, MAX_AXIS_VALUE))
        random_y.append(np.random.uniform(-MAX_AXIS_VALUE, MAX_AXIS_VALUE))
        for j in range(0,len(box_array)):
            if(random_x[i]>=box_array[j][0] and random_x[i]<=box_array[j][2] and random_y[i]<=box_array[j][1] and random_y[i]>=box_array[j][5]):
                print(j)
                print(box_array[j])
    print(random_x)
    print(random_y)
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
    for x in range(0,len(random_x)):
        movex = np.random.uniform(-MAX_AXIS_VALUE, MAX_AXIS_VALUE)
        movey = np.random.uniform(-MAX_AXIS_VALUE, MAX_AXIS_VALUE)
        random_x[x] += movex
        random_y[x] += movey

    #second trace
    trace2 = go.Scatter(
        x = random_x,
        y = random_y,
        mode = 'markers'
    )


    #second trace
    data2 = [trace2]
    #this makes the file name random so that the file isnt overwritten 
    #each time this program runs
    randFileName2 = np.random.randn()
    nameOfFile2 = "scatterWALK"+ str(randFileName2)

    # Plot and embed in ipython notebook!
    py.plot(data2, filename=nameOfFile2)

def create_channels(NUM_OF_CHANNELS,NUM_OF_BOXES,all_channels):
    for i in range (0,NUM_OF_BOXES*NUM_OF_BOXES):
        for j in range (0,NUM_OF_CHANNELS):
            all_channels[i][j] = np.random.randint(0,2) # 0,2 because we want 2 possible states for the channels, 0-off, 1-on


def node_in_box(random_x,random_y,box_array,node_in_box_array):
    for i in range (0,len(random_x)):
        for j in range(0,len(box_array)):
            if(random_x[i]>=box_array[j][0] and random_x[i]<=box_array[j][2] and random_y[i]<=box_array[j][1] and random_y[i]>=box_array[j][5]):
              print(j)
              print(i)
              node_in_box_array.append(j)
              # print(box_array[j])
              # print(random_x[i])
              # print(random_y[i])
              # print(box_array[j][0])
              # print(box_array[j][2])
              # print(box_array[j][1])
              # print(box_array[j][5])
              print("\n")

main()