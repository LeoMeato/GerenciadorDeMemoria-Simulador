#   O arquivo contém as classes responsáveis por gerenciar
#   os processos em suas respectivas filas, considerando o
#   diagrama de 7 estados

#   Classe: Fila de Processos
#
#   Representação estruturada das filas de pronto, 
#
class FilaDeProcessos:

    def __init__(self):

        self.pronto = Fila()
        self.bloqueado = Fila()
        self.sus_pronto = Fila()
        self.sus_bloqueado = Fila()
        

class Fila:

    def __init__(self, maxLength=None) -> None:
        self.fila = []

    def adicionar(self, processo):
        self.fila.append(processo)

    def remover(self):
        processo = self.fila[0]
        self.fila.pop(0)
        return processo