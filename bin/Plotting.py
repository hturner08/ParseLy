import sys
sys.path.append('..')
from .. import plotter
def main():
    parser = argparse.ArgumentParser(description=
    'Pseudocolor and Isosurface plots of data')
    parser.add_argument("-f",help="Specify the data file to be read")
    # parser.add_argument("-e",help="Specify txt files for region numbers")
    # parser.add_argument("-o",help="Specify output file name",default="output.txt")
    args = parser.parse_args()
    time1 = time.perf_counter()
    plot = Plotter(args.f) #Example:r"C:\Users\Herbert Turner\Documents\SparcCode\MeshtalParser\Examples\split2.3D"
    plot.scatterPlot([0,1,2,3],"hot",5,True)
    plot.surfacePlot(True)
    print("The process took " + str(time.perf_counter()-time1) + " " + "seconds")

if __name__ == '__main__':
    main()
