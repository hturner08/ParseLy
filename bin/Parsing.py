import argparse
import numpy as np
import pandas as pd
import math
import time
import csv
import sys
sys.path.append('..')
from Parsely.MParser import *
#####################
#Python 2.7         #
#####################
def main():
    parser = argparse.ArgumentParser(description=
    'Convert meshtal file to format readable by VisIT')
    parser.add_argument("-f",help="Specify path to file you want to convert")
    parser.add_argument("-e",help="Specify txt files for region numbers")
    parser.add_argument("-o",help="Specify output file name",default="output.txt")
    args = parser.parse_args()
    time1 = time.clock()
    parser = MParser(args.f)
    for region in parser.data_frame["Region"].unique():
        print("Region:" + " "+ region)
        print(parser.data_frame.loc[parser.data_frame["Region"]==region].describe())
    if args.e:
        parser.data_frame[parser.data_frame['Region'].isin(get_options(args.e))].to_csv(args.o,sep = ' ', index=False, header=False)
    else:
        parser.data_frame.to_csv(args.o,sep = ' ', index=False, header=False)
    print("The process took " + str(time.clock()-time1) + " " + "seconds")

if __name__ == '__main__':
    main()
