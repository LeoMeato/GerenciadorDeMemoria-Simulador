from Quadro import *
from Swapper import *
from TabelaDePaginas import *

class MemoriaPrincipal:
    quadros = []           #Quadros disponiveis e usados em MP
    tabelas_de_paginas = [] #Tabela de Paginas mantida
    
    
    def __init__(self, bits_size, bits_log):
        if bits_size < bits_log:
            bits_log = bits_size#Evita o caso de o tamanho de enderecos do quadro for maior que o tamanho da MP, sendo assim, o quadro pode ser no maximo igual a MP

        self.bits_log= bits_log
        self.bits_size = bits_size
        self.tam_quadro = 2**bits_log

        self.quadros = self.constroi_memoria()

    #bits_size = n (Tamanho total da memoria)
    # bits_log = m (Tamanho do quadro) 
    def constroi_memoria(self):#Inicializacao da paginacao da memoria
        for i in range(int((2**self.bits_size)/(2**self.bits_log))):
            self.quadros.append(Quadro())#Setando o tempo de ultimo acesso como 0


    def retira_pagina(self, index_quadro):#recebo do swapper a pagina calculada a ser retirada
        self.quadros[index_quadro] = None

    def aloca_pagina(self, index_quadro, pagina):
        self.quadros[index_quadro] = pagina#E guardado a pagina trazida da memoria

    def consulta_pagina(self, index_quadro):#Obtem a pagina para swapper analisar, ou para devida manipulacao como swapp-in
        return self.quadros[index_quadro].consulta_quadro()#Retorna None se o quadro estiver vazio
    
    def consulta_tabela(self, index_tabela, pagina):
        return self.tabelas_de_paginas[index_tabela] #Retorno a tabela de paginas para consultar qual quadro esta a pagina
    
        ################################Vai mudar aqui, no caso consultar tp, depois verificar a pagina################################
        #index_quadro = self.tabelas_de_paginas[index_tabela].consulta_quadro(pagina)
        #if index_quadro == None:
        #   return index_quadro
        #return self.consulta_pagina(index_quadro)
    
    def tamanho_do_quadro(self):
        return 2**self.bits_log#Numero de enderecos disponiveis no quadro