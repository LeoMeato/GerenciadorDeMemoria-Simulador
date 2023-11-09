from Quadro import *
from Swapper import *
from TabelaDePaginas import *

class MemoriaPrincipal:
    quadros = []            #Quadros alocados em MP
    tabelas_de_paginas = [] #Tabela de Paginas mantida
    
    
    def __init__(self, bits_size, bits_log):
        if bits_size < bits_log:
            bits_log = bits_size

        self.num_bit = bits_log
        self.bits_size = bits_size
        self.tam_quadro = 2**bits_size

        self.quadros = self.mp_constroi_memoria(bits_log, bits_size)

            
    def mp_constroi_memoria(self, bits_log, bits_size):#Inicializacao da paginacao da memoria
        for i in range((2**bits_size)/(2**bits_log)):
            self.quadros.append(Quadro(0))


    def mp_retira_pagina(self, index_quadro):#recebo do swapper a pagina calculada a ser retirada
        self.quadros[index_quadro] = None

    def mp_aloca_pagina(self, index_quadro, pagina):
        self.quadros[index_quadro] = pagina

    def mp_consulta_pagina(self, index_quadro):#Obtem a pagina para swapper analisar, ou para devida manipulacao como swapp-in
        return self.quadros[index_quadro]