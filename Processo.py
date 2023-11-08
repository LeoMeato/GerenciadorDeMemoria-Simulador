from TabelaDePaginas import *
from collections import deque


class Pagina:

    pass

class FilaDeProcessos:

    def __init__(self, maxLength=None) -> None:
        self.fila = []

    def adicionar(self, processo):
        self.fila.append(processo)

    def remover(self):
        processo = self.fila[0]
        self.fila.pop(0)
        return processo