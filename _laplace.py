#Laplace expansions for the determinant of a matrix nxn

import numpy as np

def _laplace(M = np.array([[0,0], [0,0]])): #Initialize a void matrix with the same dimension of matrix M
	e = np.zeros((M.shape[0], M.shape[1]))
	for i in range(0, M.shape[0]): #Scroll with indexes (i,j) lines and columns of the matrix
		for j in range(0, M.shape[1]):
			p = (-1)**(i+j) # p is the parameter associated to the matrix value sign 
			m = np.delete(M, i, 1) # m is the reduced matrix with (n-1)x(n-1)dimensions
			m = np.delete(m, i, 0)
	        e[i][j] = p*M[i][j]*np.linalg.det(m) #Fill the matrix e   
	
	print np.sum(e) #sum(e) does the sum of all the values stored in e


