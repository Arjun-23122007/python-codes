import numpy as np 
# Define two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
# Matrix addition
print("\nAddition of A and B:") 
print(A + B)
# Matrix multiplication 
print("\nMultiplication of A and B:") 
print(np.dot(A, B)) 
# Transpose
print("\nTranspose of A:")
print(A.T) 
# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("\nEigenvalues of A:")
print(eigenvalues)
print("\nEigenvectors of A:") 
print(eigenvectors) 
# Eigenvalue decomposition
P = eigenvectors
D = np.diag(eigenvalues)
print("\nDiagonal Matrix D:")
print(D)
 # QR Deomposition
Q, R = np.linalg.qr(A)
print("\nQR Decomposition - Q:")
print(Q) 
print("\nQR Decomposition - R:")
print(R)