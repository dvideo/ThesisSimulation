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
N = int(input("How many nodes would you like to run this simulation with? "))
#print("Nodes: ",N)
random_x = np.random.randn(N)
random_y = np.random.randn(N)
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

#modify the x and y values "the random walk"
for x in range(0,len(random_x)):
    movex = np.random.randn()
    movey = np.random.randn()
    random_x[x] += movex
    random_x[x] += movey

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
