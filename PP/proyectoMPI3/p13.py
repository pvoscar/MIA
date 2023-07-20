#Peña Valerio Oscar Luis

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.rank
comm_3D = comm.Create_cart(dims = [3, 3, 3], periods = [False, False, False], reorder = False)
xyz = comm_3D.Get_coords(rank)
print('En esta topología, el proceso %s tiene coordenadas %s' %(rank, xyz))
