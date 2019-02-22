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
    MAX_AXIS_VALUE = int(SIZE_OF_GRAPH/2)
    BOX_SIZE = 5
    NUM_OF_BOXES = int((SIZE_OF_GRAPH/BOX_SIZE)*2)
    NUM_OF_CHANNELS = [0] * 32

    #Max size of graph if size=10 is 20x20 because the walk can put you at 20
    #if no walk it is 10x10
    random_x = []
    random_y = []
    box_array = []
    # max_x = SIZE_OF_GRAPH
    # max_y = SIZE_OF_GRAPH
    box_name = 'box'
    x1 = -SIZE_OF_GRAPH
    y1 = -SIZE_OF_GRAPH
    x2 = x1+BOX_SIZE
    y2 = y1+BOX_SIZE

    createBoxes(x1,x2,y1,y2,box_array,SIZE_OF_GRAPH,BOX_SIZE,NUM_OF_BOXES)
    createGraph1(random_x,random_y,MAX_AXIS_VALUE,box_array)
    graphWalk(random_x,random_y,MAX_AXIS_VALUE)
    # for x in range(0,len(box_array)):
    #     print(box_array[x])

def createBoxes(x1,x2,y1,y2,box_array,SIZE_OF_GRAPH,BOX_SIZE,NUM_OF_BOXES):
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


def createGraph1(random_x,random_y,MAX_AXIS_VALUE,box_array):
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

def graphWalk(random_x,random_y, MAX_AXIS_VALUE):
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


    #first trace
    data2 = [trace2]
    #this makes the file name random so that the file isnt overwritten 
    #each time this program runs
    randFileName2 = np.random.randn()
    nameOfFile2 = "scatterWALK"+ str(randFileName2)

    # Plot and embed in ipython notebook!
    py.plot(data2, filename=nameOfFile2)

main()