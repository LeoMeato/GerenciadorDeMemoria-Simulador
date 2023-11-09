from Pagina import Pagina
from TabelaDePaginas import *
#from collections import deque


class Processo:

    def __init__(self, tam, id) -> None:
        self.paginas = [Pagina(id)] * tam
        self.pcb = Pcb()
        self.id = id
    
class Pcb:

    def __init__(self) -> None:
        self.estado = "novo"
        self.suspenso = False

    def setPronto(self):
        self.estado = "pronto"
    
    def setBloqueado(self):
        self.estado = "bloqueado"
    
    def setExecutando(self):
        self.estado = "executando"

    def setFinalizado(self):
        self.estado = "finalizado"
    
    def setSuspensoTrue(self):
        self.suspenso = True

    def setSuspensoFalse(self):
        self.suspenso = False
    

class FilaDeProcessos:

    def __init__(self, maxLength=None) -> None:
        self.fila = []

    def adicionar(self, processo):
        self.fila.append(processo)

    def remover(self):
        processo = self.fila[0]
        self.fila.pop(0)
        return processo