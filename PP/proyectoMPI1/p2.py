from mpi4py import MPI
import time

def main():
    comm = MPI.COMM_WORLD
    id = comm.Get_rank()			#Número de procesos ejecutando el código
    numProcesses = comm.Get_size()		#Total de procesos en ejecución
    myHostName = MPI.Get_processor_name()	#Máquina donde se ejecuta el código
	
    print("Saludos desde el proceso {} of {} on {}"\
    .format(id, numProcesses, myHostName))
	
main()

#Para ejecutar el código
#mpiexec --allow-run-as-root --oversubscribe -np 6 python3 p2.py

#mpiexec –n x python3 mpy4py p2.py

#mpiexec --oversubscribe -np 6 python3 p2.py	
