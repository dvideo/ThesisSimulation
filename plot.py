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
    MAX_AXIS_VALUE = int(SIZE_OF_GRAPH/4) #for SIZE_OF_GRAPH of 20, this would be 10x10 to allowe the additional 10x10 on the walk
    BOX_SIZE = 5  #length and width of boxes on graph
    NUM_OF_BOXES = int((SIZE_OF_GRAPH/BOX_SIZE)*2) #number of boxes in 1 row of graph (to get all boxes, square this number)
    NUM_OF_CHANNELS = 32 #number of channels per box
    NUM_OF_WALKS = 5
    CLUSTER_SIZE = 10

    #Max size of graph if size=10 is 20x20 because the walk can put you at 20
    #if no walk, graph size is 10x10
    random_x = [] #initialization of list for x values for graph
    random_y = [] #initialization of list for y values for graph
    box_list = [] #initialization of list for all coordinates for all boxes on graphs
    node_in_box_list = [] #initialization of list for the boxes that the nodes generated are in
    ask_clusters_unique = [] #array used for one walker node, that node wants to know if any nodes have been to these boxes
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
        print("cluster: ", i , " ",len(cluster_dictionary[i].nodes_in_cluster), "  Head: ",cluster_dictionary[i].cluster_head.node_num)
   

    # create_graph(random_x,random_y,MAX_AXIS_VALUE,box_list)
    
    create_channels(NUM_OF_CHANNELS,NUM_OF_BOXES,all_channels)

    #find out what boxes the nodes are in
    for i in range (0,len(nodes_dictionary)):
        node_in_box(box_list,nodes_dictionary,i,all_channels,NUM_OF_CHANNELS)

    # for i in range(0,len(nodes_dictionary)):
    #     print(i, " ",nodes_dictionary[i].x_val, " ", nodes_dictionary[i].y_val, " ",nodes_dictionary[i].boxes_passed)
   

    #print the boxes that nodes are in, and the channels in those boxes
    # print("node in box 1" ,node_in_box_list)
    # for i in range(len(node_in_box_list)):
    #     print("all channels at i: ",all_channels[node_in_box_list[i]], "i: " ,i)

    # node_in_box_list = [] #make the list empty again so you can add new channels and display them
    
    #let nodes move on the graph
    graph_walk(random_x,random_y, MAX_AXIS_VALUE, BOX_SIZE, NUM_OF_WALKS,box_list,nodes_dictionary,all_channels,NUM_OF_CHANNELS)

    get_trajectory(nodes_dictionary)

    send_queries(nodes_dictionary,box_list)

    for i in range(0,len(nodes_dictionary)):
        # print(i, " ", nodes_dictionary[i].coordinates, " ",nodes_dictionary[i].boxes_passed , " ", nodes_dictionary[i].x_walk , " ",nodes_dictionary[i].y_walk )
        print(i, " ", nodes_dictionary[i].coordinates, " ",nodes_dictionary[i].boxes_passed , " want to go to box: ", nodes_dictionary[i].want_to_go)
        for j in nodes_dictionary[i].channels:
            print("channels from node perspective: ",j, " ",nodes_dictionary[i].channels[j])
        for j in range (0,len(nodes_dictionary[i].boxes_passed)):
            print('channels: ',nodes_dictionary[i].boxes_passed[j], " ", all_channels[nodes_dictionary[i].boxes_passed[j]])
    #find out what boxes the nodes that have walked are in
    # node_in_box(random_x,random_y,box_list,node_in_box_list)

    #print the boxes that nodes are in, and the channels in those boxes
    # print("node_in_box_list after walk: ", node_in_box_list)
    # for i in range(len(node_in_box_list)):
    #     print("all channesl at i: " ,all_channels[node_in_box_list[i]], "i: " ,i)
    walker_node(SIZE_OF_GRAPH,box_list,ask_clusters_unique)

    cluster_aggregation(ask_clusters_unique, cluster_dictionary)

    print("boxNum: ", NUM_OF_BOXES*NUM_OF_BOXES)
    

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
        # print(i," box_list ", box_list[i])


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

def graph_walk(random_x,random_y, MAX_AXIS_VALUE,BOX_SIZE,NUM_OF_WALKS,box_list,nodes_dictionary,all_channels,NUM_OF_CHANNELS):
    #For all the nodes
    for j in range(len(random_x)):
        x_move_val = round(np.random.uniform(-MAX_AXIS_VALUE, MAX_AXIS_VALUE),2) #Get the value where x will end
        y_move_val = round(np.random.uniform(-MAX_AXIS_VALUE, MAX_AXIS_VALUE),2) #Get the value where y will end
        x_distance = random_x[j] - x_move_val #Get the distance between where x currently is and where x will end up
        y_distance = random_y[j] - y_move_val #Get the distance between where y currently is and where y will end up
        x_walk = round(x_distance/NUM_OF_WALKS,2) #The distance x will move per walk
        y_walk = round(y_distance/NUM_OF_WALKS,2) #The distance y will move per walk
        for i in range (0,NUM_OF_WALKS): 
            nodes_dictionary[j].x_val += x_walk
            nodes_dictionary[j].y_val += y_walk
            nodes_dictionary[j].x_walk = x_walk
            nodes_dictionary[j].y_walk = y_walk
            # node_in_box()
            #Add the new values to existing values to get new x,y
           
           
            # print("x: ",x)

            node_in_box(box_list,nodes_dictionary,j,all_channels,NUM_OF_CHANNELS)
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

def get_trajectory(nodes_dictionary):
    for i in range(len(nodes_dictionary)):
        # print("new x val",nodes_dictionary[i].coordinates[len(nodes_dictionary[i].coordinates)-1][0] + nodes_dictionary[i].x_walk)
        new_x = round(nodes_dictionary[i].coordinates[len(nodes_dictionary[i].coordinates)-1][0] + nodes_dictionary[i].x_walk,2)
        new_y = round(nodes_dictionary[i].coordinates[len(nodes_dictionary[i].coordinates)-1][1] + nodes_dictionary[i].y_walk,2)
        # print("new y val",nodes_dictionary[i].coordinates[len(nodes_dictionary[i].coordinates)-1][1] + nodes_dictionary[i].y_walk)
        nodes_dictionary[i].coordinates.append([new_x,new_y])

def send_queries(nodes_dictionary,box_list): 
    for i in range(0,len(nodes_dictionary)):
        # nodes_dictionary[i].coordinates(len(nodes_dictionary[i].coordinates)-1)
        # node_in_box()
        # node_num=i
        ask_ahead(box_list,nodes_dictionary,i)

def create_channels(NUM_OF_CHANNELS,NUM_OF_BOXES,all_channels):
    for i in range (NUM_OF_BOXES*NUM_OF_BOXES):
        for j in range (NUM_OF_CHANNELS):
            #10 percent chance that the channel is sensed wrong
            # error_check = np.random.randint(1,11)
            # if(error_check==10):
                #3 becaue 0,1,2 are all usable channel answers, 3 now means wrong answer
                # all_channels[i][j] = 3
            # else:
            all_channels[i][j] = np.random.randint(0,3) # 0,2 because we want 2 possible states for the channels, 0-off, 1-on
        # print(all_channels)

# def refresh_channels():

#can delete this, dont need
def distance(nodes_dictionary, MAX_AXIS_VALUE):
    for i in range (len(nodes_dictionary)):
        print("n in d i: " , i , " " ,nodes_dictionary[i].x_val, " ", nodes_dictionary[i].y_val)
        tempx = round(np.random.uniform(-MAX_AXIS_VALUE, MAX_AXIS_VALUE),2)
        tempy = round(np.random.uniform(-MAX_AXIS_VALUE, MAX_AXIS_VALUE),2)
        distancex = round(nodes_dictionary[i].x_val - tempx,2)
        distancey = round(nodes_dictionary[i].y_val - tempy,2)
        divide3 = round(distancex/3,2)
        print("n in d i: " , i , " " ,tempx, " ", tempy, " distancex: ", distancex, " distancey: ", distancey, " divided by 3x: ",distancex/3, " y: ", distancey/3)


def node_in_box(box_list, nodes_dictionary,node_num,all_channels,NUM_OF_CHANNELS):
    # for i in range (len(random_x)):
    temp_node = nodes_dictionary[node_num]
    for j in range(len(box_list)):
        #check a node lands within a boxes x,y pairs, save that box to an array
        if(temp_node.x_val>=box_list[j][0] and temp_node.x_val<=box_list[j][2] and temp_node.y_val<=box_list[j][1] and temp_node.y_val>=box_list[j][5]):
          temp_node.coordinates.append([round(temp_node.x_val,2),round(temp_node.y_val,2)])
          temp_node.boxes_passed.append(j)
          if j not in temp_node.channels:
              temp_node.channels[j] = []
              for i in range (0,NUM_OF_CHANNELS):
                check = np.random.randint(1,11)
                if(check==10):
                    temp_node.channels[j].append(3)
                else:
                    temp_node.channels[j].append(all_channels[j][i])

def ask_ahead(box_list, nodes_dictionary,node_num):
    # x = nodes_dictionary[node_num].coordinates[len(nodes_dictionary[node_num].coordinates)-1][0]
    # print("this ",x)
    temp_node = nodes_dictionary[node_num]
    temp_node_x = nodes_dictionary[node_num].coordinates[len(nodes_dictionary[node_num].coordinates)-1][0]
    temp_node_y = nodes_dictionary[node_num].coordinates[len(nodes_dictionary[node_num].coordinates)-1][1]
    for j in range(len(box_list)):
        # check a node lands within a boxes x,y pairs, save that box to an array
        if(temp_node_x>=box_list[j][0] and temp_node_x<=box_list[j][2] and temp_node_y<=box_list[j][1] and temp_node_y>=box_list[j][5]):
            temp_node.want_to_go = j
          # temp_node.boxes_passed.append(j)   #uncomment this to add the box to the boxes passed array

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
        nodes_dictionary[i] = nc.Node(random_x[i],random_y[i],i)


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
                cluster_dictionary[j].nodes_in_cluster.append(nodes_dictionary[count])
                count+=1
        else:
            for i in range(CLUSTER_SIZE):
                # index = (j*CLUSTER_SIZE)+i
                cluster_dictionary[j].nodes_in_cluster.append(nodes_dictionary[count])
                count+=1
        cluster_dictionary[j].cluster_head = cluster_dictionary[j].nodes_in_cluster[0]

def walker_node(SIZE_OF_GRAPH,box_list,ask_clusters_unique):
    ask_clusters_temp = []
    val = SIZE_OF_GRAPH/2
    x1 = round(np.random.uniform(-val, val),2) #get a random float number within given range
    y1 = round(np.random.uniform(-val, val),2)
    x2 = round(np.random.uniform(-val, val),2) #get a random float number within given range
    y2 = round(np.random.uniform(-val, val),2)

    x_distance = round(x1-x2,2)
    y_distance = round(y1-y2,2) 

    # print("distance: ", x_distance, " " , y_distance)
    print("start x,y (",x1,",",y1,") ending x,y (",x2,",",y2,")")

    x_walk = round(x_distance/10,2)
    y_walk = round(y_distance/10,2)

    for j in range(len(box_list)):
        # check a node lands within a boxes x,y pairs, save that box to an array
            if(x2>=box_list[j][0] and x2<=box_list[j][2] and y2<=box_list[j][1] and y2>=box_list[j][5]):
                final_box = j
    
    done=1
    while(done!=0):
        for j in range(len(box_list)):
        # check a node lands within a boxes x,y pairs, save that box to an array
            if(x1>=box_list[j][0] and x1<=box_list[j][2] and y1<=box_list[j][1] and y1>=box_list[j][5]):
                ask_clusters_temp.append(j)
                if(j==final_box):
                    done=0

        x1-=x_walk
        x1 = round(x1,2)
        y1-=y_walk
        y1 = round(y1,2)

    # ask_clusters_unique = [] 
    for box in ask_clusters_temp: 
        if box not in ask_clusters_unique: 
            ask_clusters_unique.append(box)
    ask_clusters_unique.sort() 
    print('boxes: ', ask_clusters_unique, ' ', len(ask_clusters_unique))

def cluster_aggregation(ask_clusters_unique, cluster_dictionary):
    report = []
    cluster_report={}
    # print("uni: ",ask_clusters_unique)
    #for each cluster
    for i in range (0,len(cluster_dictionary)):
        #for all the nodes in that cluster
        for j in range(0,len(cluster_dictionary[i].nodes_in_cluster)):
            # print("node: ",cluster_dictionary[i].nodes_in_cluster[j].boxes_passed, "in cluster: ",i)
            #for all the boxes that the node of that cluster passed
            for k in range(0,len(cluster_dictionary[i].nodes_in_cluster[j].boxes_passed)):
                #for all the boxes that the walker node wants to know about
                for l in range(0,len(ask_clusters_unique)):
                    # cluster_report[ask_clusters_unique[l]]=[]
                    if(cluster_dictionary[i].nodes_in_cluster[j].boxes_passed[k]==ask_clusters_unique[l]):
                        report.append(ask_clusters_unique[l])
                        #at the box that we found a match of, append the nodes perspective of channels, do this for all nodes in the cluster that have seen the box
                        # cluster_report[ask_clusters_unique[l]]=cluster_dictionary[i].nodes_in_cluster[j].channels[k]


    fused_report = [] 
    for box in report: 
        if box not in fused_report: 
            fused_report.append(box) 

    fused_report.sort()
    print('report: ', fused_report," ", len(fused_report)) 



main()