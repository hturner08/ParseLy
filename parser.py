import argparse

def main():
    parser = argparse.ArgumentParser(description=
    'Convert meshtal file to format readable by VisIT')
    parser.add_argument("file",help="Specify path to file you want to convert")
    parser.add_argument("type",help="Specify output file type(.csv,.silo,.txt)",
    action="store_const",const=str, default=".csv")
    args = parser.parse_args()
    meshtalFile = open(args.file,"r")
if __name__ == '__main__':
    main()
