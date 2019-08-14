import sys
import argparse
import time
sys.path.append(r"C:\Program Files\LLNL\VisIt 3.0.0\lib\site-packages")
sys.path.append('..')
from Parsely import plotter as plt
#####################
#Python 2.7         #
#####################
def main():
    parser = argparse.ArgumentParser(description=
    'Pseudocolor and Isosurface plots of data')
    parser.add_argument("-f",help="Specify the data file to be read")
    # parser.add_argument("-e",help="Specify txt files for region numbers")
    # parser.add_argument("-o",help="Specify output file name",default="output.txt")
    args = parser.parse_args()
    time1 = time.clock()
    plot = plt.Plotter(args.f) #Example:r"C:\Users\Herbert Turner\Documents\SparcCode\MeshtalParser\Examples\split2.3D"
    img1 = plot.scatterPlot(["X","Y","Z","Heat"],"hot",5,False)
    img2 = plot.surfacePlot(stay=True)
    print("The process took " + str(time.clock()-time1) + " " + "seconds")
    print(img1)
    print(img2)

if __name__ == '__main__':
    main()
