#Definition of inputs and outputs
#==================================
##[Mes scripts GEOL]=group
##entree=vector
##dip=field entree
##angle=number 10

#Algorithm body
#==================================
from qgis.core import *

layer = processing.getObject(entree)
field1_index = layer.fieldNameIndex(dip)
if layer.selectedFeatureCount():
    nb = len(layer.selectedFeatures())
    T = [elem.attributes()[field1_index] for elem in layer.selectedFeatures()]
else:
    nb = layer.featureCount()
    T = [elem.attributes()[field1_index] for elem in layer.getFeatures()]


#T = [right_angle(i) for i in T]
print T
from matplotlib.projections import PolarAxes, register_projection
from matplotlib.transforms import Affine2D, Bbox, IdentityTransform
import numpy as np
import matplotlib.pyplot as plt

#angle = 5
nsection = 360 / angle + 1
direction = np.linspace(0, 360, nsection, False) / 180 * np.pi
frequency = [0] * (nsection)
dipangle = [0] * (nsection)


for i in range(len(T)):
    tmp = int((T[i] - T[i] % angle) / angle)
    frequency[tmp] = frequency[tmp] + 1
    dipangle[tmp] = dipangle[tmp] + T[i]

for i in range(nsection):
	if frequency[i] > 0:
		dipangle[i] = dipangle[i] / frequency[i]
        
width = angle / 180.0 * np.pi * np.ones(nsection)
print width 

ax = plt.subplot(1, 1, 1, projection = 'polar')
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
bars = ax.bar(direction, dipangle, width=width, bottom=0.0)
for r,bar in zip(frequency, bars):
    bar.set_facecolor(plt.cm.jet(0.8))
    bar.set_edgecolor('grey')
    bar.set_alpha(0.8)
    
titre = "pendages: "+ str(nb)+ " valeurs"
ax.set_title(titre, y=1.06, size=14, color='red')
plt.show()

