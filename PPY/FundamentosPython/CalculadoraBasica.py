from FundamentosPython import nuevoTema
# import Calc.Operaciones
import Calc.Operaciones as c  # Uso de alias para acortar el nombre

if __name__ == "__main__":
    nuevoTema("Módulos y paquetes")

    # módulo que utiliza import sin el uso de alias
    # print(Calc.Operaciones.suma(2, 3))
    # print(Calc.Operaciones.resta(20, 3))

    # módulo que utiliza import con el uso de alias
    print(c.suma(1, 2, 3, 4))
    print(c.resta(40, 30, 20, 10))
    print(c.mult(3, 4, 5))
    print(c.div(25, 3))
    
    