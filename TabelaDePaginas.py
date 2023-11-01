class TabelaDePaginas:

    registros = []
    id = -1

    def __init__(self, id, numPags):
        self.id = id
        self.registros = [Registro()] * numPags

class Registro:

    p = False
    m = False
    numQuadro = -1

    def __init__(self) -> None:
        pass