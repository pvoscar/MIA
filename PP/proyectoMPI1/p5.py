#Eficiencia basada en el número de núcleos o procesadores

import time
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.rank
	
print("El proceso %d comienza " %rank)
n = 0
for i in range(100000000):   #Llegar hasta 100000000 ciclos
  n += 1
print("El proceso %d concluye " %rank)