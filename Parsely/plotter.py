import sys#WHY WONT YOU FUCKING WORK
sys.path.append(r"C:\Program Files\LLNL\VisIt 3.0.0\lib\site-packages")
import visit
visit.Launch(r"C:\Program Files\LLNL\VisIt 3.0.0")
print("Hello")
visit.OpenDatabase(r"C:\Users\Herbert Turner\Documents\SparcCode\MeshtalParser\Parsely\bin\output.txt")
print("FUCKING WORK")
visit.AddPlot("Scatter", "u")
p = ScatterPlotAttributes()
p.colorTableName = "hot"
p.opacity = 0.5
SetPlotOptions(p)
DrawPlots()
