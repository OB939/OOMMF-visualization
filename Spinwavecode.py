
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 21:12:10 2022

@author: oscar
"""


        
import numpy as np
from mayavi.mlab import *



loadedndarray1 = np.loadtxt('f2.txt')#Load the OMF file you want to model
ymax=20 #set the dimensions of your simulation, ymax how many cells your nanowire is wide, zmax is how many cells your nanowire is thick 
zmax=1
#Here are the scale factors for the x,y and z component. The scale factor determines how much each component is divided by
sfx=1000000#scale factor for x component 
sfy=1 #scalefactor for y component 
sfz=1 #scalefactor for z component 
Clr=2 #This sets what you want the color coding to represent. 0 is x component, 1 is y component and 2 is z component of the magnetization 
Scale=1.5 #This sets by how much you want to scale your arrows by, i.e their length



index=0

for line in loadedndarray1:
    if line[0]=="#":
        continue 
    else:
        index+=1
        
#Index represents the total number of cells in the simulation

array=np.zeros((index,3))
array2=np.zeros(index)


xmax=int((index/ymax)/zmax)

o=0


for line in loadedndarray1:
    if line[1]=="#":
        continue 
    else:
        array[o][0]=line[0]
        array[o][1]=line[1]
        array[o][2]=line[2]
        array2[o]=array[o][Clr]
        #print(line)
        o+=1

   

array3=np.zeros(index)

for i in range(xmax):
    for j in range(ymax):
        for k in range(zmax):
                  array3[(i*int(index/xmax))+(j*zmax)+k]=array2[j*xmax+k*int(index/zmax)+i]

       
    
       
            
i = xmax
j = ymax
k = zmax

new_array= np.zeros((i,j,k))#Define first empty 3D array with geometry of the wire
#Bellow we add the x-components of the magnetization to their corresonding locations in the wire
for l in range(zmax):
    for s in range(ymax):
        for k in range(xmax):
                g=(((array[k+(s*xmax)+(l*int(index/zmax))][0])/sfx)**2+((array[k+(s*xmax)+(l*int(index/zmax))][1])/sfy)**2+((array[k+(s*xmax)+(l*int(index/zmax))][2])/sfz)**2)**0.5
                new_array[k][s][l]=((array[k+(s*xmax)+(l*int(index/zmax))][0])/sfx)/g#This ensures that after each row of pixels has been filled the program starts filling the next row, there are 2000 pixes in a row
                          

i2 = xmax
j2 = ymax
k2 = zmax

new_array2= np.zeros((i2,j2,k2))#Define second 3D array corresponding to y components of magnetization 

for l in range(zmax):
    for s in range(ymax):
        for k in range(xmax):
               g=(((array[k+(s*xmax)+(l*int(index/zmax))][0])/sfx)**2+((array[k+(s*xmax)+(l*int(index/zmax))][1])/sfy)**2+((array[k+(s*xmax)+(l*int(index/zmax))][2])/sfz)**2)**0.5
               new_array2[k][s][l]=((array[k+(s*xmax)+(l*int(index/zmax))][1])/sfy)/g
             
                            
i3 = xmax
j3 = ymax
k3 = zmax


new_array3= np.zeros((i3,j3,k3))
for l in range(zmax):
    for s in range(ymax):
        for k in range(xmax):
             g=(((array[k+(s*xmax)+(l*int(index/zmax))][0])/sfx)**2+((array[k+(s*xmax)+(l*int(index/zmax))][1])/sfy)**2+((array[k+(s*xmax)+(l*int(index/zmax))][2])/sfz)**2)**0.5
             new_array3[k][s][l]=((array[k+(s*xmax)+(l*int(index/zmax))][2])/sfz)/g
           
             
                
                                            

phi=array2

def test_quiver3d():
    obj = quiver3d(new_array, new_array2,new_array3,line_width=1,scale_factor=Scale, scalars=array3)
    obj.glyph.color_mode = 'color_by_scalar'
    return obj

 

print(test_quiver3d())