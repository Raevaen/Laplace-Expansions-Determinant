#Laplace rule to calculate determinant of a matrix bigger than 3x3

import numpy as np

def _laplace(m=np.array([[0,0], [0,0]])):
	e = np.zeros((m.shape[0], m.shape[1]))
	for i in range(0, m.shape[0]):
		for j in range(0, m.shape[1]):
			p = (-1)**(i+j)
			n = np.delete(m, i, 1)
			n = np.delete(n, i, 0)
	        e[i][j] = p*m[i][j]*np.linalg.det(n)   
	
	print np.sum(e)


