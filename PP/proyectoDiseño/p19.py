#Peña Valerio Oscar Luis

from __future__ import division
import numpy as np
from numpy.fft import fft2, ifft2
from math import ceil, fabs
from mpi4py import MPI

size = 10000
iter = 20
comm = MPI.COMM_WORLD

print("-------------------------------------------------------------------------")
print('  Ejecutando %d procesos MPI en paralelo' %comm.size)

my_size = size   // comm.size
size = comm.size * my_size
my_ofs = comm.rank * my_size

vec = np.zeros(size)
vec[0] = 1.0

my_M = np.zeros((my_size, size))
for i in range(my_size):
    j = (my_ofs + i - 1) % size
    my_M[i,j] = 1.0

comm.Barrier()
t_start = MPI.Wtime()

for t in range( iter ):
    my_new_vec = np.inner(my_M, vec)

    comm.Allgather(
        [my_new_vec, MPI.DOUBLE],
        [vec, MPI.DOUBLE]
    )
comm.Barrier()
t_diff = MPI.Wtime() - t_start

if fabs(vec[iter] - 1.0 > 0.01):
    print("Resultdo incorrecto ")

print(" %d iteraciones de tamaño %d en %5.2fs: %5.2f iteraciones por segundo" %(iter, size, t_diff, iter/t_diff))

print("-------------------------------------------------------------------------")