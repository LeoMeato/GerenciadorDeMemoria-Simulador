from Pagina import *
from TabelaDePaginas import *
#from collections import deque

#   Responsável por representar os processos recebidos de um escalonador imaginário
class Processo(Agrupamento):

    label = "Sprites/Processo_Label.jpg"
    content = ""

    #   Fugindo do padrão, aqui os tamanhos são esperados como decimais para facilitar a coelta de informações do gerenciador
    def __init__(self, tam, tam_quadro, id) -> None:

        self.id = id #id é redundado por limitações da interface, mas não é necessário para a lógica
        self.content = "Processo {}".format(id)

        self.paginas = []

        #IMPORTANTE: Lembra de revisar essa palhaçada Arthur
        for i in range(tam//tam_quadro):

            self.paginas.append(Pagina(tam_quadro, self.id, i))
        self.paginas.append(Pagina(tam % tam_quadro, self.id, tam//tam_quadro))

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
    
