from Quadro import *
from Swapper import *
from TabelaDePaginas import *

class MemoriaPrincipal:
    
    def __init__(self, bits_size, bits_log):
        if bits_size < bits_log:
            bits_log = bits_size
            #Evita o caso de o tamanho de enderecos do quadro for maior que o tamanho da MP, sendo assim, o quadro pode ser no maximo igual a MP

        self.bits_log= bits_log
        self.bits_size = bits_size
        self.tam_quadro = 2**bits_log
        self.quadros = []

        self.constroi_memoria()

    #bits_size = n (Tamanho total da memoria)
    # bits_log = m (Tamanho do quadro) 
    def constroi_memoria(self):#Inicializacao da paginacao da memoria
        for i in range(int((2**self.bits_size)/(2**self.bits_log))):
            self.quadros.append(Quadro())#Setando o tempo de ultimo acesso como 0



    #Consultas de paginas, alocacao e remocao
    def retira_pagina(self, index_quadro):#recebo do swapper a pagina calculada a ser retirada
        self.quadros[index_quadro].desaloca_pagina()

    def aloca_pagina(self, index_quadro, pagina):
        self.quadros[index_quadro].aloca_pagina(pagina)

    def consulta_pagina(self, index_quadro):
        return self.quadros[index_quadro].consulta_quadro() #Retorna a pagina requisitada, e ja zera o last_update
    


    #Verificacao de presenca e atualizacao para a LRU
    def consulta_quadro_disponivel(self, index_quadro):
        return self.quadros[index_quadro].consulta_disponivel() #Retorna False se o quadro estiver vazio
    
    def atualiza_clock_quadros(self):
        for i in self.quadros:
            i.atualiza_clock()
