#Definition of inputs and outputs
#==================================
##[Mes scripts GEOL]=group
##strati=vector
##dip_dir=field strati
##dip=field strati
##schisto=vector
##dip_dir2=field schisto
##dip2=field schisto
#Algorithm body
from qgis.core import *
from apsg import *


layer = processing.getObject(strati)
dipdir = layer.fieldNameIndex(dip_dir)
dip = layer.fieldNameIndex(dip)

if layer.selectedFeatureCount():
    g= Group([Vec3(Fol(elem.attributes()[dipdir],elem.attributes()[dip])) for elem in layer.selectedFeatures()],name='plis')
else:
    g= Group([Vec3(Fol(elem.attributes()[dipdir],elem.attributes()[dip])) for elem in layer.getFeatures()],name='plis')
    
    
print g

layer2 = processing.getObject(schisto)
dipdir2 = layer2.fieldNameIndex(dip_dir2)
dip2 = layer2.fieldNameIndex(dip2)

if layer2.selectedFeatureCount():
    g2= Group([Vec3(Fol(elem.attributes()[dipdir2],elem.attributes()[dip2])) for elem in layer2.selectedFeatures()],name='schisto')
else:
    g2= Group([Vec3(Fol(elem.attributes()[dipdir2],elem.attributes()[dip2])) for elem in layer2.getFeatures()],name='schisto')
    
print g2

#intersection

inters =  (g.R ** g2.R)
print inters.aslin.dd

resultat= "intersection: " + str(int(round(inters.aslin.dd[1]))) + " -> " + str(int(round(inters.aslin.dd[0])))
s = StereoNet()
a = s.ax

s.line(g.aslin, 'b.',markersize=18)
s.line(Ortensor(g).eigenlins.data[2],'r.',markersize=18)
s.plane(Ortensor(g).eigenfols.data[2],'r')
s.plane(g2.asfol)
s.line(g2.aslin, 'c.',markersize=18)
s.line(inters.aslin, markersize=20)
a.set_title(resultat, y=1.06, size=14, color='red')
s.show()
