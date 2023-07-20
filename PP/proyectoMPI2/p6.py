##Comunicaciones punto a punto
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

print("El proceso %d comienza" %rank)
if rank == 0:
  msg = "Este es el mensaje"
  rec = 1
  comm.send(msg, dest=rec)
  print("El proceso 0 envía: %s " %msg + "a %d" %rec)
if rank == 1:
  source = 0
  msg = comm.recv(source=0)
  print("El proceso 1 recibe: %s " %msg + "desde %d" %source)  
