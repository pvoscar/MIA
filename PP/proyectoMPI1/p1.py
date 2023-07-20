#%%writefile p1.py

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.rank
print("El proceso %d comenzó " %rank)


#Para ejecutar el código
#mpiexec --allow-run-as-root --oversubscribe -np 4 python3 p1.py
