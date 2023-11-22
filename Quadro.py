class Quadro:

    pagina = None

    def __init___(self):
        self.last_update = 0
        self.presenca = False
        self.pagina = None#Tem a referida pagina
    


    #Consulta, alocacao e remocao da pagina no quadro
    def consulta_quadro(self):
        self.acessado()
        return self.pagina#Retorna a pagina que esta alocada

    def aloca_pagina(self, pagina):
        self.pagina = pagina#Usado para guardar pagina traga da memoria secundaria
        self.presenca = True
        self.acessado()
    
    def desaloca_pagina(self):
        self.pagina = None#Libera o quadro para entrada de outra pagina
        self.presenca = False



    #Verificacao de presenca e atualizacao do clock nos quadros e acessos
    def consulta_disponivel(self):
        return self.presenca

    def atualiza_clock(self):
        self.last_update += 1#Vai incrementando o tempo do ultimo acesso da memoria
    
    def acessado(self):
        self.last_update = 0#Seta o tempo como zero, pois foi usado a pagina recentemente