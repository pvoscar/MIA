#Peña Valerio Oscar Luis

import numpy as np

n = 3
a = np.random.randint(10, size = (n * n))
b = np.random.randint(10, size = (n * n))
c = np.zeros((n*n), dtype= np.float32)
a = a.astype( np.float32)
b = b.astype( np.float32)

def matmul(n, A, B, C):
    for i in range (n):
        for j in range (n):
            temp = 0.0
            for k in range ( n ):
                temp +=  A[i * n + k] * B[k * n + j]
            C[i * n + j] = temp


matmul(n, a, b, c)
print("Matriz A: ")
print(a.reshape(n,n))
print("Matriz B: ")
print(b.reshape(n,n))
print("Matriz C: ")
print(c.reshape(n,n))

