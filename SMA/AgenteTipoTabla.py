class AgenteTabla:
    """Agente racional de tipo tabla."""

    def __init__(self, acciones):
        self.acciones = acciones
        self.percepciones = ""

    def actuar(self, percepcion, accion_basica=""):
        """Actua según la percepción, devolviendo una acción."""
        if not percepcion:
            return accion_basica
        if len(self.percepciones) != 0:
            self.percepciones += ','
        self.percepciones += percepcion
        if self.percepciones in self.acciones.keys():
            return self.acciones[self.percepciones]
        self.percepciones = ""
        return accion_basica   

if __name__ == "__main__":

    ACCIONES = {'moneda': 'pedir-codigo',
                'moneda,a1': 'servir-bebida1',
                'moneda,a2': 'servir-bebida2',
                'moneda,a3': 'servir-bebida3',
                'moneda,a1,moneda': 'pedir-codigo',
                'moneda,a2,moneda': 'pedir-codigo',
                'moneda,a3,moneda': 'pedir-codigo',
                'moneda,a1,moneda,a1': 'servir-bebida1',
                'moneda,a1,moneda,a2': 'servir-bebida2',
                'moneda,a1,moneda,a3': 'servir-bebida3',
                'moneda,a2,moneda,a1': 'servir-bebida1',
                'moneda,a2,moneda,a2': 'servir-bebida2',
                'moneda,a2,moneda,a3': 'servir-bebida3',
                'moneda,a3,moneda,a1': 'servir-bebida1',
                'moneda,a3,moneda,a2': 'servir-bebida2',
                'moneda,a3,moneda,a3': 'servir-bebida3'}

    print("-- Agente Tabla: Máquina Expendedora -- ")
    expendedora = AgenteTabla(ACCIONES)
    PERCEPCION = input("Indicar Percepcion: ")
    while PERCEPCION:
        ACCION = expendedora.actuar(PERCEPCION, 'esperar')
        print(ACCION)
        PERCEPCION = input("Indicar Percepcion: ")