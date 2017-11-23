'''
Read the Geolife file and save as python data file format
'''

import os
import os.path
import numpy as np
import datetime


def read_geolife_file(filepath):
    i = 0
    data = []
    for dirpath, dirnames, filenames in os.walk(filepath):
        for filename in [f for f in filenames if f.endswith(".plt")]:
            inputfile = os.path.join(dirpath, filename)
            print(inputfile) ## for progress monitering
            i = i+1
            data.append(np.genfromtxt(inputfile,dtype= None, names=['Lat','Lon','Allzero','Altitude','Days','Date','Time'], delimiter=',', skip_header=6))
    np.save("geolife.npy", data)
    return True
    
    
def generate_one_day_trajectory(date, length_data):
    traj = []
    for i in range(length_data):
        path  = []
        if data[i][0][5] == date:
            
            for trajectory in data[i]:
                path.append((trajectory[0],trajectory[1]))
            traj.append(path)
    return traj

filepath = r"C:\Users\b6liu\Documents\dataset\Geolife Trajectories 1.3\Data" # change this path to your own location
read_geolife_file(filepath)

data = np.load("geolife.npy")
date = b"2009-05-12"
traj = generate_one_day_trajectory(date, len(data))

