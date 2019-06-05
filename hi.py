import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np


def main():
	MAX_AXIS_VALUE = 25
	random_x = []
	random_y = []
	for i in range (100):
		random_x.append(round(np.random.uniform(-MAX_AXIS_VALUE, MAX_AXIS_VALUE),2))
		random_y.append(round(np.random.uniform(-MAX_AXIS_VALUE, MAX_AXIS_VALUE),2))
	create_graph(random_x,random_y)
	for i in range (100):
		random_x[i]+=round(np.random.uniform(-MAX_AXIS_VALUE, MAX_AXIS_VALUE),2)
		random_y[i]+=round(np.random.uniform(-MAX_AXIS_VALUE, MAX_AXIS_VALUE),2)
	create_graph2(random_x,random_y)

def create_graph(random_x,random_y):
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

def create_graph2(random_x,random_y):
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
    nameOfFile = "scatter2"+ str(randFileName)

    # Plot and embed in ipython notebook!
    py.plot(data, filename=nameOfFile)


main()