class Quadro:
    pagina = None#Tem a referida pagina (e serve como bit de presenca)
    def __init___(self):
        self.last_update = 0
    
    def consulta_quadro(self):
        return self.pagina#Retorna a pagina que esta alocada, ou None se nao ha nada

    def aloca_pagina(self, pagina):
        self.pagina = pagina#Usado para guardar pagina traga da memoria secundaria
    
    def desaloca_pagina(self):
        self.pagina = None#Libera o quadro para entrada de outra pagina

    def atualiza_clock(self):
        self.last_update += 1#Vai incrementando o tempo do ultimo acesso da memoria
    
    def acessado(self):
        self.last_update = 0#Seta o tempo como zero, pois foi usado a pagina recentemente