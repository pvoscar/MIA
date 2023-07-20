#Peña Valerio Oscar Luis

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.rank
comm_3D = comm.Create_cart(dims = [3, 3, 3], periods = [False, False, False], reorder = False)
xyz = comm_3D.Get_coords(rank)
if rank == 12:
    print('En esta topología, el proceso %s ha coordinado %s' %(rank, xyz))
    right, left = comm_3D.Shift(0,1)
    up, down = comm_3D.Shift(1,1)
    forward, backward = comm_3D.Shift(2,1)
    print('Vecinos (Izquierda-Derecha): %s %s' %(left, right))
    print('Vecinos (Arriba   -Abjo   ): %s %s' %(up, down))
    print('Vecinos (Adelante -Atrás  ): %s %s' %(forward, backward))