import sys#WHY WONT YOU FUCKING WORK
sys.path.append(r"C:\Program Files\LLNL\VisIt 3.0.0\lib\site-packages")
import visit
visit.Launch()
print("Hello")
visit.OpenDatabase(r"C:\Users\Herbert Turner\Documents\SparcCode\MeshtalParser\Parsely\bin\output2.txt")
print("FUCKING WORK")
visit.AddPlot("Scatter",["var00","var01","var02","var03"])
p = ScatterAttributes()
p.colorTableName = "hot"
p.opacity = 0.5
SetPlotOptions(p)
print("Checkpoint3")
DrawPlots()
