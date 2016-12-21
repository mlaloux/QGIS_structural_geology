#Definition of inputs and outputs
#==================================
##[Mes scripts GEOL]=group
##entree=vector
##dip_dir=field entree
##dip=field entree

#Algorithm body
#==================================
from qgis.core import *
from apsg import *


layer = processing.getObject(entree)
dipdir = layer.fieldNameIndex(dip_dir)
dip = layer.fieldNameIndex(dip)


if layer.selectedFeatureCount():
    g= Group([Vec3(Fol(elem.attributes()[dipdir],elem.attributes()[dip])) for elem in layer.selectedFeatures()],name='plis')
else:
    g= Group([Vec3(Fol(elem.attributes()[dipdir],elem.attributes()[dip])) for elem in layer.getFeatures()],name='plis')





resultat= "fold plunge: : " + str(int(round(Ortensor(g).eigenlins.data[2].dd[1]))) + " -> " + str(int(round(Ortensor(g).eigenlins.data[2].dd[0])))

s = StereoNet()
a = s.ax
s.line(g.aslin, 'b.',markersize=18)
s.line(Ortensor(g).eigenlins.data[0],'g.',markersize=18)
s.plane(Ortensor(g).eigenfols.data[0],'g')
s.line(Ortensor(g).eigenlins.data[1],'c.',markersize=18)
s.plane(Ortensor(g).eigenfols.data[1],'c')
s.line(Ortensor(g).eigenlins.data[2],'r.',markersize=18)
s.plane(Ortensor(g).eigenfols.data[2],'r')
a.set_title(resultat, y=1.06, size=14, color='red')
s.show()
