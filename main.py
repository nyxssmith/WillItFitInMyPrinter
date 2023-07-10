
import pymesh
import numpy as np
import sys
import os
import math

from multiprocessing import Pool
# Function to find distance
def calc_distance(point_a, point_b):
      
    d = math.sqrt(math.pow(point_b[0] - point_a[0], 2) +
                math.pow(point_b[1] - point_a[1], 2) +
                math.pow(point_b[2] - point_a[2], 2)* 1.0)
    return d
    

def do_mesh(mesh_path):
    mesh = pymesh.load_mesh(mesh_path)

    heights_in_mesh = []
    height_dict = dict()

    for vertice in mesh.vertices:
        # get the Z which is height
        
        heights_in_mesh.append(list(vertice)[2])

        if list(vertice)[2] not in list(height_dict.keys()):
            height_dict[list(vertice)[2]] = []
        height_dict[list(vertice)[2]].append(vertice)

    max_max_distance = 0
    # check keys    
    for key in height_dict.keys():
        #print(len(height_dict[key]))
        # get list of points
        points = height_dict[key]
        # max distance counter
        max_distance = 0
        # for each point as a starting point
        for point_a in points:
            # iterate to all
            # its not fastest but is easiest
            for point_b in points:
                #distance  = math.dist(point_a,point_b)
                distance  = calc_distance(point_a,point_b)
                if distance > max_distance:
                    max_distance = distance
        # update global
        if max_distance > max_max_distance:
            max_max_distance = max_distance

    return max_max_distance

# start

#print(os.listdir("/local"))

files_list = []

for root,d_names,f_names in os.walk("/local"):
    #print (root, f_names)
    for f in f_names:
        #print(f)
        file_path = os.path.join(root,f)
        #print(file_path)
        if "stl" in file_path:
            files_list.append(file_path)

i = 0
total = len(files_list)


outputs = ""

for file_path in files_list:
    max_dist = do_mesh(file_path)
    fraction = str(i)+"/"+str(total)
    percent = int(i/total*100)
    status = str(percent)+"% : "+str(max_dist) +" "+file_path
    print(status)
    outputs += status+"\n"
    i+=1
    #if i > 2:
    #    break

with open("/local/analysis.txt","w") as o:
    o.write(outputs)