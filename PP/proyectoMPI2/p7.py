#Comunicaciones broadcast
from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
rank = comm.rank
print("El proceso %d comienza" %rank)
if rank == 0:
    data = random.randint(1,10)
else:
    data = None
data = comm.bcast(data, root = 0)    
if rank == 1:
    print("El cuadrado de %d es %d " %(data, data * data))
if rank == 2:
    print("La mitad de %d es %d " %(data, data / 2))
if rank == 3:
    print("El doble de %d es %d " %(data, data * 2))      