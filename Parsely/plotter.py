import sys#WHY WONT YOU FUCKING WORK
sys.path.append(r"C:\Program Files\LLNL\VisIt 3.0.0\lib\site-packages")
import visit
visit.Launch()
print("Hello")
visit.OpenDatabase(r"C:\Users\Herbert Turner\Documents\SparcCode\MeshtalParser\Parsely\bin\output2.txt")
plot = visit.AddPlot("Scatter","var00")
p = visit.ScatterAttributes()
# Variables
p.var2="var01"
p.var3="var02"
p.var4="var03"
#Role
p.var1Role="Coordinate0"
p.var2Role="Coordinate1"
p.var3Role = "Coordinate2"
p.var4Role = "Color"
#Other Attributes
# p.colorType = "ColorByColorTable"
# p.var4Scaling = "Log"
p.pointSizePixels = 5
p.colorTableName = "hot"
v = visit.GetView3D()
v.viewNormal = (-0.571619, 0.405393, 0.713378)
v.viewUp = (0.308049, 0.911853, -0.271346)
visit.SetPlotOptions(p)
visit.SetView3D(v)
visit.DrawPlots()
while(True):
    a = 1
