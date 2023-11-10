#   O arquivo contém todas as classes e métodos necessários para a 
#   manipulação da representação escolhida para memória secundária


#   Classe: Memória Secundária
#   
#   Representa a parte disponível para swap em um sistema que implementa memória virtual
#   Deve ser inicializada pelo gerenciador geral e manipulada apenas pelo swapper
class MemoriaSecundaria:
    
    #   Construtor
    #
    #   O valor bits_size é esperado na forma log2(tamamho desejado), como no resto do sistema
    def __init__(self, bits_size):

        self.size = self.free_space = 2**bits_size
        self.registros = None


    #   Procedimento realizado no swap out de uma página qualquer da MP
    #   Recebe os valores adequados para representar uma página na MS
    #   Explode o programa em caso de falha
    def swap_out(self, idProcesso, numPagina, pagina) -> bool:

        if (pagina.size > self.free_space):

            print("Falta de memória secundária")
            exit(1)
            return False
        
        self.free_space += pagina.size
        self.registros.append(RegistroMS(idProcesso, numPagina, pagina))
        return True


    #   Procedimento realizado no swap in de uma página para a MP
    #   Recebe os identificadores da página desejada
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
    

#   Classe interna: Registro da MS
#   Garante a organização das páginas armazenadas por swap out
#   Não deve existir fora da classe MS
class RegistroMS:

    def __init__(self, idProcesso, numPagina, pagina):

        self.idProcesso = idProcesso
        self.numPagina = numPagina
        #self.pagina = pagina.copy() Aguardado implementação da classe Página