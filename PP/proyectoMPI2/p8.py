#Comunicaciones scattering

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.rank

if rank == 0:
    array = ['AAA', 'BBB', 'CCC', 'DDD']
else:
    array = None

data = comm.scatter(array, root = 0)
print("El proceso %d está trabajando en el elemento %s " %(rank, data))        