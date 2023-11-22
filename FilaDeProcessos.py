from Interface_funções import *

#   O arquivo contém as classes responsáveis por gerenciar
#   os processos em suas respectivas filas, considerando o
#   diagrama de 7 estados

#   Classe: Fila de Processos
#
#   Representação estruturada das filas de novo, pronto, bloqueado, etc
class FilaDeProcessos:

    def __init__(self):

        self.novo = Fila()
        self.pronto = Fila()
        self.bloqueado_page_fault = Fila()
        self.bloqueado_IO = Fila()
        self.sus_pronto = Fila()
        self.sus_bloqueado = Fila()

        self.filas = {
            "novo": self.novo,
            "pronto": self.pronto,
            "bloqueado_page_fault": self.bloqueado_page_fault,
            "bloqueado_IO": self.bloqueado_IO,
            "sus_pronto": self.sus_pronto,
            "sus_bloqueado": self.sus_bloqueado
        }

    def transita(self, pid, fila1, fila2):

        if (fila1 == "sus_pronto" and fila2 == "sus_bloqueado"):
            erro("Transição (" + fila1 + "," + fila2 + ") não faz sentido")

        processo = self.filas[fila1].remove_pid(pid)
        if (processo == None):
            erro("Transição inválida. Processo " + pid + " não encontrado na fila " + fila1)
            
        self.filas[fila2].adicionar(processo)
    
    def purge(self, pid):
        for f in self.filas.values():
            f.remove_pid(pid)

class Fila:

    def __init__(self) -> None:
        self.fila = []

    def adicionar(self, processo):
        self.fila.append(processo)

    def remover(self):
        processo = self.fila[0]
        self.fila.pop(0)
        return processo
    
    def remove_pid(self, pid):

        for i in self.fila:

            p = i
            if (p.pcb.id == pid):
                self.fila.remove(p)
                return p
        return None