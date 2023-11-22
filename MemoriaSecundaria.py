from Interface_funções import *
#   O arquivo contém todas as classes e métodos necessários para a 
#   manipulação da representação escolhida para memória secundária
 
#   Representa a parte disponível para swap em um sistema que implementa memória virtual
#   Deve ser inicializada pelo gerenciador geral e manipulada apenas por ele e o swapper
class MemoriaSecundaria:
    
    #   O valor bits_size é esperado na forma log2(tamamho desejado), como no resto do sistema
    def __init__(self, bits_size):

        self.size = self.free_space = 2**bits_size
        self.images = []


    #   Procedimento realizado na criação de um novo processo
    #   Adiciona sua imagem na memória secundária e explode se
    #   não houver mais espaço
    def load_image(self, processo):

        if (processo in self.images): 
            erro("Processo duplicado na MS :(;O arquivo de entrada está correto?")

        if (self.free_space < processo.pcb.tam):
            erro("MS explodiu :(; Espaço de swap excedido")

        self.images.append(processo)
        self.free_space -= processo.pcb.tam


    #   Procedimento chamado no término de um processo
    #   Libera espaço de swap para as próximas execuções
    def remove_image(self, processo):

        if (not processo in self.images):
            erro("Processo " + processo.pcb.pi + " não pôde ser retirado da MS :(;Verifique a lógica do gerenciador;O arquivo de entrada está correto?")

        self.images.remove(processo)
        self.free_space += processo.pcb.tam


    #   Procedimento realizado no swap out de uma página da MP para MS
    #   Chamado quando a página foi alterada para preservar a consistência das informações
    def swap_out(self, pid, numPagina, pagina) -> bool:
        
        p = None
        for i in self.images:
            if (i.pcb.id == pid):
                p = i
                break
        
        p.paginas[numPagina] = pagina


    #   Procedimento realizado no swap in de uma página para a MP
    #   Retorna uma cópia da página solicitada
    def swap_in(self, pid, numPagina):

        for p in self.images:
            if (p.pcb.id == pid):
                return p.paginas[numPagina]
    