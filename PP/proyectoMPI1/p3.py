from mpi4py import MPI
import time
    
comm = MPI.COMM_WORLD
rank = comm.rank
	
print("El proceso %d comenzó " %rank)
time.sleep(10)
print("El proceso %d concluye " %rank)


#Para ejecutar el código
#time mpiexec --allow-run-as-root --oversubscribe -np 4 python3 p3.py

#mpiexec –n x python3 mpy4py p3.py

#mpiexec --oversubscribe -np 4 python3 p3.py	
