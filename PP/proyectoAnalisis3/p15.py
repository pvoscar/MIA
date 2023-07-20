#Peña Valerio Oscar Luis

import sys 
import numpy as np
from mpi4py import MPI
import random

ENVIOINICIAL = 1
ENVIOFINAL = 2

def initialize(t):
    print("Vector ")
    m = np.random.rand(t)
    print(m)
    return m

def send_data(a, t, al, t1, myid, numprocs):
    tammin = int(t / numprocs) 
    if myid == 0:
        pos = t1
        for i in range(1, numprocs):
            tam = tammin
            x = t % numprocs
            if t % numprocs > i:
                tam = tammin + 1
            comm.send(a[pos], dest = i, tag = ENVIOINICIAL)  
            pos += tam 
        al[:t1] = a[:t1]
    else:
        data = comm.recv(source = 0, tag = ENVIOINICIAL)    
        al[:t1] = data  

def sumarray(a, t, myid, numprocs):
    s = np.sum(a)
    if myid == 0:
        for i in range(1, numprocs):
            s1 = comm.recv(source = i, tag = ENVIOFINAL)
            s += s1
    else:
        comm.send(s, dest = 0, tag = ENVIOFINAL)         
    
    return s    

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    numprocs = comm.Get_size()
    myid = comm.Get_rank()
    a = 0.0
    startwtime = 0
    iN = int(sys.argv[1])
    fN = int(sys.argv[2])
    incN = int(sys.argv[3])

    for t in range(iN, fN + 1, incN):
        t1 = int(t / numprocs)
        if t % numprocs > myid:
            t1 += 1
        if myid == 0:
            a = initialize(t)
        al = np.zeros(t1)
        comm.Barrier()
        startwtime = MPI.Wtime()
        send_data(a, t, al, t1, myid, numprocs)  
        comm.Barrier()
        endwtime = MPI.Wtime()   

        if myid == 0:
            tx = endwtime - startwtime
            print("Procesadores {}, suma de {} números \n tiempo de envío = {}" .format(numprocs, t, tx))

        comm.Barrier()
        startwtime = MPI.Wtime()
        s = sumarray(al, t1, myid, numprocs)      
        comm.Barrier()
        endwtime = MPI.Wtime()
        totaltime = endwtime - startwtime

        if myid == 0:
            Cmflops = t / totaltime / 1000000
            PorNodo = t / totaltime / 1000000 / numprocs
            print("Suma: {}, tiempo de suma = {}, Mflops {}, Mflops/nodo {}" .format(s, totaltime, Cmflops, PorNodo))

MPI.Finalize()            
