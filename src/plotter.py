import sys#WHY WONT YOU FUCKING WORK
#sys.path.append(r"C:\Program Files\LLNL\VisIt 3.0.0\lib\site-packages")
import visit
import time
class Plotter:
    def __init__(self,paths):
        visit.Launch()
        if isinstance(paths,list):
            try: #Preventing crashing of scripts because only 1/100 files didn't open
                for path in paths:
                    visit.OpenDatabase(path)
            except:
                print("Invalid file path")
        else:
            visit.OpenDatabase(paths)
    def scatterPlot(self,coords=["var00","var01","var02","var03"],colorTable="hot",pixelSize = 5,stay=False):
        if len(visit.ListPlots()) > 0:
            visit.SetActivePlots(0)
            visit.HideActivePlots()
        plot = visit.AddPlot("Scatter", coords[0])
        p = visit.ScatterAttributes()
        # Variables
        if coords[1]:
            p.var2= coords[1]
        if coords[2]:
            p.var3= coords[2]
        if coords[3]:
            p.var4=coords[3]
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
        time.sleep(5)
        return visit.SaveWindow()
        return visit.SaveWindow()
    def surfacePlot(self,stay=False,samples = 100, contours=50):
        returned = []
        if len(visit.ListPlots()) > 0:
            visit.SetActivePlots(0)
            visit.HideActivePlots()
        p = visit.PseudocolorAttributes()
        q=visit.ResampleAttributes()
        r = visit.IsosurfaceAttributes()
        q.samplesX = samples
        q.samplesY = samples
        q.samplesZ = samples
        r.contourNLevels = contours
        plot = visit.AddPlot("Pseudocolor","Heat")
        visit.AddOperator("Resample")
        # visit.AddOperator("Isosurface")
        visit.SetOperatorOptions(q)
        visit.SetOperatorOptions(r)
        visit.SetPlotOptions(p)
        visit.DrawPlots()
        returned.append(visit.SaveWindow())
        count = 0
        visit.AddOperator("Isosurface")
        visit.DrawPlots()
        time.sleep(60)
        returned.append(visit.SaveWindow())
        return returned


def main():
    plot = Plotter(r"C:\Users\Herbert Turner\Documents\SparcCode\MeshtalParser\Examples\split2.3D")
    plot.scatterPlot(["X","Y","Z","Heat"],"hot",5,True)
    plot.surfacePlot(True)
if __name__ == '__main__':
    main()
