#Peña Valerio Oscar Luis

import pyopencl as cl

for platform in cl.get_platforms():
    print("Plataforma: %s" %platform.name)
    print("  Vendedor: %s" %platform.vendor)
    print("    Versón: %s" %platform.version)

for device in platform.get_devices():
    print("        Dispositivo: %s"     %device.name)
    print("    Velocidad reloj: %s"     %device.max_clock_frequency)
    print("Unidades de cómputo: %s"     %device.max_compute_units)
    print("      Memoria local: %s  KB" %(int(device.local_mem_size/1024)))
    print("     Memoria global: %s  GB" %(round(device.global_mem_size/1073741824.0,2)))
