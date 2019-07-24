import argparse
import numpy as np
import pandas as pd
import math
import time
import csv

def readInt(str):
    if "E" in str:
        base = float(str[:str.index("E")])
        ex = float(str[str.index("E")+1:])
        if ex is not 0:
            return base*10**ex
        return base
    return float(str)

def read_data_line(str, origin, vec, system,particle):
    return_data = []
    str_data = str.split()
    shift = 0
    if particle is "photon":
        shift = 1
    for x in range(len(str_data)-shift):
        return_data.append(readInt(str_data[x+shift]))
    if(system == 1):
        print(return_data)
        if return_data[0] < 105 or return_data[2] > .5: #Only get larger radius
            return None
        copy = return_data[:]
        theta_0 = math.atan(vec[2]/vec[0])
        if(vec[0] < 0):
            theta_0 += math.pi
        if vec[0] < 0:
            sign = 1
        else:
            sign = -1
        return_data[0] = origin[0] + copy[0]*math.cos(sign*copy[2]*2*math.pi + theta_0)
        return_data[1] = copy[1]
        return_data[2] = origin[2] - sign * copy[0]*math.sin(sign*copy[2]*2*math.pi + theta_0)
        return_data[3] = copy[3]
        return_data[4] = copy[4]
    return return_data

def get_region_data(regions):
    region_data = []
    #columns
    region_number = []
    particles = []
    x = []
    y = []
    z = []
    az = []
    heat = []
    error = []
    #coordinate system conversions
    origin = [0,0,0]
    vec = [0,0,0]
    #For each loop
    current_region = 0
    system = 0 #cartesion = 0, polar = 1
    particle = "neutron"
    real_data= False
    for region in regions:
        origin = [0,0,0]
        for line in region:
            if real_data and line:
                parsed_data = read_data_line(line, origin,vec,system,particle)
                if parsed_data is not None:
                    region_number.append(current_region)
                    particles.append(particle)
                    x.append(parsed_data[0])
                    y.append(parsed_data[1])
                    z.append(parsed_data[2])
                    az.append(math.atan(parsed_data[2]/parsed_data[0]))
                    heat.append(parsed_data[3])
                    error.append(parsed_data[4])
            elif "Mesh Tally Number" in line:
                current_region = line[17:].replace(" ","")
            elif "photon" in line:
                particle = "photon"
            elif "origin at " in line:
                str_coords = line.split()
                for coord in range(3):
                    origin[coord] = readInt(str_coords[coord+2])
                    vec[coord] = readInt(str_coords[coord+13])
            elif ("X" in line) and ("Y" in line) and ("Z" in line):
                real_data = True
            elif ("R" in line) and ("Z" in line) and ("Th" in line):
                real_data = True
                system = 1
        real_data=False
        system=0
        particle = "neutron"
    return pd.DataFrame({'Region':region_number,
                        'Particle':particles,
                        'X':x,
                        'Y':y,
                        'Z':z,
                        'Azimuth':az,
                        'Heat':heat,
                        'Error':error})

def split_regions(file):
    current = 0
    regions = [[]]
    for line in file.readlines():
        if("Mesh Tally Number" in line):
            regions.append([line.strip()])
            current+=1
        else:
            regions[current].append(line.strip())
    return regions

def main():
    parser = argparse.ArgumentParser(description=
    'Convert meshtal file to format readable by VisIT')
    parser.add_argument("file",help="Specify path to file you want to convert")
    parser.add_argument("type",help="Specify output file type(.csv,.silo,.txt)",
    action="store_const",const=str, default=".csv")
    args = parser.parse_args()
    meshtalFile = open(args.file,"r")
    time1 = time.perf_counter()
    data_frame = get_region_data(split_regions(meshtalFile))
    data_frame.to_csv(r"output.txt",sep = ' ', index=False, header=True)
    print("The process took " + str(time.perf_counter()-time1) + " " + "seconds")
    print(data_frame.to_string())


if __name__ == '__main__':
    main()
