# Load libraries

import csv
import random
import math
import matplotlib

import numpy as np

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

class IrisData():
 def __init__(self, filename):
  with open(filename, "r") as f_input:
   csv_input = csv.reader(f_input)
   self.details = list(csv_input)

 def get_col_row(self, col, row):
  return self.details[row-1][col-1] 
  # Python index starts from 0 so we have to substract by 1

data = IrisData("irisk2.csv")


sepall=[]
sepalw=[]
petall=[]
petalw=[]
category1=[]
category2=[]


for x in range(0,150):
	sepall.append(float(data.get_col_row(1,x)))
	sepalw.append(float(data.get_col_row(2,x)))
	petall.append(float(data.get_col_row(3,x)))
	petalw.append(float(data.get_col_row(4,x)))

	category1.append(float(data.get_col_row(6,x)))
	category2.append(float(data.get_col_row(7,x)))


the1=random.uniform(0,1)
the2=random.uniform(0,1)
the3=random.uniform(0,1)
the4=random.uniform(0,1)
bias1=random.uniform(0,1)

the5=random.uniform(0,1)
the6=random.uniform(0,1)
the7=random.uniform(0,1)
the8=random.uniform(0,1)
bias2=random.uniform(0,1)

the1H=random.uniform(0,1)
the2H=random.uniform(0,1)
the3H=random.uniform(0,1)
the4H=random.uniform(0,1)
bias1H=random.uniform(0,1)
bias2H=random.uniform(0,1)



target1=0
target2=0
sigmoid1=0
sigmoid2=0
eror1=0
eror2=0
lrate=0.1
totalerror1=0
totalerror2=0
accurate=0

sigmoid1H=0
sigmoid2H=0
target1H=0
target2H=0



for y in range (0,200):
	print('epoch-',y)
	
	for x in range (0,150):
		target1=float(the1*sepall[x]+the2*sepalw[x]+the3*petall[x]+the4*petalw[x]+bias1)
		target2=float(the5*sepall[x]+the6*sepalw[x]+the7*petall[x]+the8*petalw[x]+bias2)

		sigmoid1=float(1/(1+math.exp(-target1)))
		sigmoid2=float(1/(1+math.exp(-target2)))

		target1H=float(the1H*sigmoid1+the3H*sigmoid2+bias1H)
		target2H=float(the2H*sigmoid1+the4H*sigmoid2+bias2H)
		
		sigmoid1H=float(1/(1+math.exp(-target1H)))
		sigmoid2H=float(1/(1+math.exp(-target2H)))

		print(sigmoid1H,sigmoid2H,category1[x],category2[x])


		if sigmoid1H > 0.5:
			prediction1=1.0
		else:
			prediction1=0.0

		if sigmoid2H > 0.5:
			prediction2=1.0
		else:
			prediction2=0.0
			
		if (category1[x] == prediction1 and category2[x] == prediction2):
			accurate=accurate+1
			print(accurate)


		
		eror1=float(((abs(sigmoid1H-category1[x]))**2)/2)
		eror2=float(((abs(sigmoid2H-category2[x]))**2)/2)

		totalerror1=totalerror1+eror1
		totalerror2=totalerror2+eror2

		temp1=float((sigmoid1-category1[x])*(1-sigmoid1)*sigmoid1)
		temp2=float((sigmoid2-category2[x])*(1-sigmoid2)*sigmoid2)

		temp3=float(temp1+the1H*temp2+the2H)*sigmoid1*(1-sigmoid1)
		temp4=float(temp1+the3H*temp2+the4H)*sigmoid2*(1-sigmoid2)



		dthe1H=sigmoid1*temp1
		dthe2H=sigmoid1*temp2
		dthe3H=sigmoid2*temp1
		dthe4H=sigmoid2*temp2
		dbias1H=temp1
		dbias2H=temp2

		dthe1=temp3*sepall[x]
		dthe2=temp3*sepalw[x]
		dthe3=temp3*petall[x]
		dthe4=temp3*petalw[x]
		dbias1=temp3*1
		dthe5=temp4*sepall[x]
		dthe6=temp4*sepalw[x]
		dthe7=temp4*petall[x]
		dthe8=temp4*petalw[x]
		dbias2=temp4*1



		the1=the1-lrate*dthe1
		the2=the2-lrate*dthe2
		the3=the3-lrate*dthe3
		the4=the4-lrate*dthe4
		bias1=bias1-lrate*dbias1
		the5=the5-lrate*dthe5
		the6=the6-lrate*dthe6
		the7=the7-lrate*dthe7
		the8=the8-lrate*dthe8
		bias2=bias2-lrate*dbias2

		the1H=the1H-lrate*dthe1H
		the2H=the2H-lrate*dthe2H
		the3H=the3H-lrate*dthe3H
		the4H=the4H-lrate*dthe4H
		bias1H=bias1H-lrate*bias1H
		bias2H=bias2H-lrate*bias1H

		
		
		
	erorav1=totalerror1/150
	eroeav2=totalerror2/150
	accuav=accurate/150
	totalerror1=0
	totalerror2=0
	accurate=0

	

	
	print('Eror1 : ',erorav1)
	print('Eror2 : ',eroeav2)
	print('Accuracy : ',accuav)

	y=y+1

	plt.figure('Eror1')
	plt.plot(y,erorav1,'-o')
	plt.figure('Eror2')
	plt.plot(y,eroeav2,'-o')
	plt.figure('Accurate')
	plt.plot(y,accuav,'-o')

	
	
plt.show()



