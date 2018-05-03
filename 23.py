import numpy as np
import matplotlib.pyplot as plt

datos=[1.2, 2.5, 2.8, 5.0]

def f(x, l):
	a=(1.0/l)*(np.exp(-x/l))
	return a

valores=[]

for i in datos:
	s=f(i, 2)
	valores.append(s)



