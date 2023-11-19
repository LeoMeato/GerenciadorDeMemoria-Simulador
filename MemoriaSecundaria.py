#   O arquivo contém todas as classes e métodos necessários para a 
#   manipulação da representação escolhida para memória secundária
 
#   Representa a parte disponível para swap em um sistema que implementa memória virtual
#   Deve ser inicializada pelo gerenciador geral e manipulada apenas pelo swapper
class MemoriaSecundaria:
    
    #   O valor bits_size é esperado na forma log2(tamamho desejado), como no resto do sistema
    def __init__(self, bits_size):

        self.size = self.free_space = 2**bits_size
        self.images = []


    #   Procedimento realizado na inserção de uma página qualquer na MS
    #   Explode o programa em caso de falha
    def swap_out(self, idProcesso, numPagina, pagina) -> bool:

        if (pagina.size > self.free_space):

            #print("Falta de memória secundária")
            return False
        
        self.free_space += pagina.size
        self.registros.append(RegistroMS(idProcesso, numPagina, pagina))
        return True


    #   Procedimento realizado no swap in de uma página para a MP
    #   Retorna uma cópia da página e libera o espaço adequado na MS em um fluxo normal
    #   Retorna falha caso as informações recebidas não façam sentido
    def swap_in(self, idProcesso, numPagina):

        for i in range(len(self.registros)):
            
            r = self.registros[i]

            if (r.idProcesso == idProcesso and r.numPagina == numPagina):

                pagina = r.copy()

                self.free_space += pagina.size
                self.registros.pop(i)
                return pagina

        return False
    

#   Garante a organização das páginas armazenadas por swap out
#   Não deve existir fora da classe MS
class RegistroMS:

    def __init__(self, pid, numPagina, pagina):

        self.pid = pid
        self.numPagina = numPagina
        self.pagina = pagina