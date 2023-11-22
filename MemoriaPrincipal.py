from Quadro import *
from TabelaDePaginas import *
from Interface_funções import *

class MemoriaPrincipal:
    
    def __init__(self, bits_size, bits_frame):
        if bits_size < bits_frame:
            erro("Tamanho da memória principal é menor que o de um quadro;O arquivo de entrada está correto?")
            #Evita o caso de o tamanho de enderecos do quadro for maior que o tamanho da MP, sendo assim, o quadro pode ser no maximo igual a MP

        self.bits_frame = bits_frame
        self.bits_size = bits_size
        self.tam_quadro = 2**bits_frame
        self.quadros = []

        self.constroi_memoria()

    #bits_size = n (Tamanho total da memoria)
    # bits_frame = m (Tamanho do quadro) 
    def constroi_memoria(self):#Inicializacao da paginacao da memoria
        for i in range(int((2**self.bits_size)/(2**self.bits_frame))):
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
