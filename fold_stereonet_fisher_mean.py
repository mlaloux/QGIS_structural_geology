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
    print "ok", layer.selectedFeatureCount()
    g= Group([Vec3(Fol(elem.attributes()[dipdir],elem.attributes()[dip])) for elem in layer.selectedFeatures()],name='plis')
else:
    g= Group([Vec3(Fol(elem.attributes()[dipdir],elem.attributes()[dip])) for elem in layer.getFeatures()],name='plis')



# mean vector
resultat= "mean vector: " + str(int(round(g.R.aslin.dd[1]))) + " - " + str(int(round(g.R.aslin.dd[0])))
s = StereoNet()
s.line(g.aslin, 'b.',markersize=18)
s.line(g.R.aslin,'g^',markersize=18)
s.cone(g.R.aslin, g.fisher_stats['a95'], 'r')  
s.cone(g.R.aslin, g.fisher_stats['csd'], 'k')
a = s.ax
a.set_title(resultat, y=1.06, size=14, color='g')
s.show()



