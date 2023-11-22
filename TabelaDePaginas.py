class TabelaDePaginas:

    def __init__(self, id, numPags):
        self.id = id
        self.registros = [Registro()] * numPags



    #Consulta, alocacao e desalocacao
    def consulta_entrada(self, numRegistro):
        if self.registros[numRegistro].p == False:
            return None
        return self.registros[numRegistro].numQuadro
    
    def aloca_entrada(self, numRegistro, numQuadro):
        self.registros[numRegistro].aloca_registro(numQuadro)

    def desaloca_entrada(self, numRegistro):
        self.registros[numRegistro].desaloca_registro()
        

class Registro:

    p = False
    m = False
    numQuadro = -1

    def __init__(self) -> None:
        pass
    

    #Alocacao e desalocacao dos registros
    def aloca_registro(self, numQuadro):
        self.p = True
        self.m = False
        self.numQuadro = numQuadro

    def desaloca_registro(self):
        self.p = False
        self.m = False
        self.numQuadro = -1