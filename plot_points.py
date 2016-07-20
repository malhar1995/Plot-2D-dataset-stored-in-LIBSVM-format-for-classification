# This script plots 2-D data (stored in LIBSVM format) for classification.

import numpy as np
import matplotlib.pyplot as plt
import sklearn
import sys
from sklearn import svm

file_name=sys.argv[1]
fp=open(file_name,"r")
lines=fp.readlines()	#Storing all the lines of the input file in the list "lines".

temp=[]
X1=[]
X2=[]
Y=[]
for line in lines:
	temp.append(line.split())

for item in temp:
	Y.append(item[0])
	feature1=item[1].split(":")
	X1.append(feature1[1])
	feature2=item[2].split(":")
	X2.append(feature2[1])
Y=[int(i) for i in Y]
Y=np.array(Y)
X1=[float(i) for i in X1]
X1=np.array(X1)
X2=[float(i) for i in X2]
X2=np.array(X2)
plt.scatter(X1,X2,c=Y,cmap=plt.get_cmap('Spectral'))
ax = plt.subplot()
ax.set_axis_bgcolor((0.0,0.0,0.0))

plt.savefig(file_name+"_plot")