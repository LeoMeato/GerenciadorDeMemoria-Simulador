from Pagina import Pagina
from TabelaDePaginas import *
#from collections import deque


class Processo:

    # IMPORTANTE: Refazer a geração das páginas do processo baseado no tamanho real

    def __init__(self, tam, id) -> None:
        self.paginas = [Pagina(id)]
        self.pcb = Pcb(id, tam)

    
class Pcb:

    def __init__(self, id, tam) -> None:
        
        self.tam = tam
        self.id = id
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
    
