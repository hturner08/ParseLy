import sys#WHY WONT YOU FUCKING WORK
sys.path.append(r"C:\Program Files\LLNL\VisIt 3.0.0\lib\site-packages")
import visit
class Plotter:
    def __init__(self,path):
        visit.Launch()
        visit.OpenDatabase(path)
    def scatterPlot(self,coords=[0,1,2,3],colorTable="hot",pixelSize = 5,stay=False):
        plot = visit.AddPlot("Scatter","var0" + str(coords[0]))
        p = visit.ScatterAttributes()
        # Variables
        if coords[1]:
            p.var2="var0" + str(coords[1])
        if coords[2]:
            p.var3="var0" + str(coords[2])
        if coords[3]:
            p.var4="var0" + str(coords[3])
        #Role Variable Roles take intergers as inputs, not strings
        p.var1Role= 0
        p.var2Role = 1
        p.var3Role = 2
        p.var4Role = 3
        p.scaleCube = 0
        #p.colorType = "ColorByColorTable"
        p.pointSizePixels = pixelSize
        p.colorTableName = colorTable
        #p.colorScaling = "Log"
        v = visit.GetView3D()
        v.viewNormal = (-0.571619, 0.405393, 0.713378)
        v.viewUp = (0.308049, 0.911853, -0.271346)
        visit.SetPlotOptions(p)
        visit.SetView3D(v)
        visit.DrawPlots()
        count = 0
        while(stay):
            print(count)
            count+=1
    def surfacePlot(self,stay=False):
        p = visit.PseudocolorAttributes()
        q=visit.ResampleAttributes()
        r = visit.IsosurfaceAttributes()
        q.samplesX = 10
        q.samplesY = 10
        q.samplesZ = 10
        r.contourNLevels = 10
        plot = visit.AddPlot("Pseudocolor","Heat")
        visit.AddOperator("Resample")
        # visit.AddOperator("Isosurface")
        visit.SetPlotOptions(p)
        visit.DrawPlots()
        count = 0
        while(stay):
            count+=1

def main():
    plot = Plotter(r"C:\Users\Herbert Turner\Documents\SparcCode\MeshtalParser\Examples\split2.3D")
    plot.scatterPlot([0,1,2,3],"hot",5,True)
    plot.surfacePlot(True)
if __name__ == '__main__':
    main()
