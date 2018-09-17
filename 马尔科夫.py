import numpy as np


matrixP = np.matrix([[0.2,0.4,0.4],[0.2,0.7,0.1],[0.25,0.25,0.5]], dtype=float)
matrix = np.matrix([[0.9,0.075,0.025],[0.2,0.7,0.1],[0.25,0.25,0.5]], dtype=float)
for i in range(100):
    matrixP = matrixP*matrix
    print("Current round:" , i+1)
    print(matrixP)