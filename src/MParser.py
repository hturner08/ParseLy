import pandas as pd
import math

class MParser:
    def __init__(self,files):
        if isinstance(files,list):
            for file in files:
                try:
                    self.file = open(file,"r")
                    self.get_region_data()
                except IOError:
                    print("Improper file name/type")
        else:
            try:
                self.file = open(files,"r")
            except IOError:
                print("Improper file name/type")
            self.get_region_data()

# Individual Parsing Functions
    def read_int(self,str):
        if "E" in str:
            try:
                base = float(str[:str.index("E")])
                ex = float(str[str.index("E")+1:])
            except(TypeError):
                print("Invalid string, could not read number")
                raise
            if ex is not 0:
                return base*10**ex
        return float(str)


    def read_data_line(self, str, origin, vec, system,particle):
        return_data = []
        str_data = str.split()
        shift = 0
        if particle is "photon":
            shift = 1
        for x in range(len(str_data)-shift):
            return_data.append(self.read_int(str_data[x+shift]))
        #FIX SOON
        if(system == 1):
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


# Region Functions
    def get_region_data(self):
        region_data = []
        #coordinate system conversions
        origin = [0,0,0]
        vec = [0,0,0]
        #For each loop
        current_region = 0
        system = 0 #cartesion = 0, polar = 1
        particle = "neutron"
        real_data = False
        x = []
        particles = []
        y = []
        z = []
        az = []
        heat = []
        error = []
        region_number = []
        for line in self.file.readlines():
            if "Mesh Tally Number" in line:
                current_region = line[18:].replace(" ","")
                current_region = current_region.replace("\n", "")
                origin = [0,0,0]
                real_data=False
                system=0
                particle = "neutron"
            else:
                if real_data and line:
                    parsed_data = self.read_data_line(line, origin,vec,system,particle)
                    if parsed_data is not None and len(parsed_data) > 0:
                        region_number.append(current_region)
                        particles.append(particle)
                        x.append(parsed_data[0])
                        y.append(parsed_data[1])
                        z.append(parsed_data[2])
                        az.append(math.atan(parsed_data[2]/parsed_data[0]))
                        heat.append(parsed_data[3])
                        error.append(parsed_data[4])
                elif "photon" in line:
                    particle = "photon"
                elif "origin at " in line:
                    str_coords = line.split()
                    for coord in range(3):
                        origin[coord] = self.read_int(str_coords[coord+2])
                        vec[coord] = self.read_int(str_coords[coord+13])
                elif ("X" in line) and ("Y" in line) and ("Z" in line):
                    real_data = True
                elif ("R" in line) and ("Z" in line) and ("Th" in line):
                    real_data = True
                    system = 1
        add = pd.DataFrame({'Region': region_number,
                            'Particle': particles,
                            'X': x,
                            'Y': y,
                            'Z': z,
                            'Azimuth': az,
                            'Heat': heat,
                            'Error': error})
        try:
            self.data_frame = pd.concat([self.data_frame,add]).reset_index(drop=True)
        except:
            self.data_frame = add
    def to_point3D(self,name):
        self.data_frame.to_csv(name,index=False,header=True,columns=["X","Y","Z","Heat"],sep= " ")

    def get_options(self,filename):
        options = []
        with open(filename,"r") as file:
            for line in file.readlines():
                for region in line.split():
                    options.append(region)
        return options

"""Testing"""
def main():
    parser = MParser("Para-013.mt")
    parser.data_frame.to_csv("output.txt")
    parser.to_point3D("output.3D")
    print("This should not be main.")

if __name__ == '__main__':
    main()
