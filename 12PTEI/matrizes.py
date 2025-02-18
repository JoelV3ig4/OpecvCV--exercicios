'''
    Programador.....:Joel Veiga
    Data............: 17/02/2025
    Observação......:Matriz
'''

import numpy

print("Análise de matrizes")
matriz1D = np.array([1, 2, 3, 4])
print(matriz1D)
print(matriz1D.dtype)
resultadoSoma = np.sum(matriz1D)
print(resultadoSoma)


matriz2D = np.arry([[0, 0, 1], [1, 1, 0] [1, 1, 1]])
print(matriz2D)
print(matriz2D.dtype)
resultadoSoma = np.sum(matriz2D, axis=0)
print(resultadoSoma)

image = np.zeros((800, 600))
print(image)