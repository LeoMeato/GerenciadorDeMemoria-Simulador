#   O arquivo contém a classe responsável pelo gerenciamento
#   da memória do sistema e dos componentes associados
from math import *
from Swapper import *
from Processo import *
from FilaDeProcessos import *
from MemoriaPrincipal import *
from MemoriaSecundaria import *

#   Classe: Gerenciador de Memória
#   
#   Responsável por receber e interpretar as instruções de entrada
class Gerenciador:

    #   Construtor
    #
    #   Inicializa o gerenciador explicitando os tamanhos dos vários componentes da memória
    #   Todos os métodos de classes internas retornam mensagens para serem empilhadas e exibidas lentamente pela
    #   interface, indicando com mais detalhes as ações feitas pelo sistema
    #   Tamanhos são recebidos no formato log2(tamanho desejado) por padrão
    #   n_residente_inicial se refere ao tamanho do conjunto residente alocado na criação de um processo
    #   que passa pela transição (novo, pronto)
    def __init__(self, bits_mp, bits_ms, bits_frame, bits_log, n_residente, arq_entrada):
        
        #   A variável clock é usada como indicação de tempo para a implementação de políticas
        #   do gerenciador e coleta de dados de execução
        self.clock = 0
        self.page_faults = 0
        self.mem_waste = 0

        self.bits_mp = bits_mp
        self.bits_ms = bits_ms
        self.bits_log = bits_log
        self.n_resident = n_residente

        self.frame_size = 2**bits_frame
        self.arq_entrada = arq_entrada

        self.MP = MemoriaPrincipal(bits_mp, bits_log)
        self.MS = MemoriaSecundaria(bits_ms)
        self.TP = []

        self.executando = None
        self.emIO = None

        self.tabela_de_processos = []
        self.fila_de_processos = FilaDeProcessos()


    #   Método responsável por alocar as estruturas necessárias para administrar um novo processo
    def cria_processo(self, pid, size):


        p = Processo(size, self.frame_size, pid)
        self.fila_de_processos.novo.adicionar(p)

        n_paginas = ceil(size/self.frame_size)
        tp = TabelaDePaginas(pid, n_paginas)
        self.TP.append(tp)

        self.tabela_de_processos.append(p)



    #   Método responsável por carregar a imagem de um processo sem nenhuma página na MP para a mesma
    #   O número de quadros carregados é decidido por uma configuração
    def carrega_imagem(self, processo):
            
            pass
    

    #   Método implementa a polítical de substituição de páginas do sistema
    def add_LRU(self, pagina):
        pass

    #   Método utilizado para marcar a passagem do tempo dentro do sistema
    #   Necessário para a implementação da política LRU de substituição de páginas
    #   e para a chamada do swapper
    def atualizaClock(self):

        self.clock += 1
        self.MP.atualiza_clock_quadros()
    

    #   Método utilizado para suspender um processo, que será escolhido pelo swapper
    #   Deve ser chamado quando a taxa de falta de páginas atingir um número inaceitável
    def callSwapOut(self):
        
        pass

    #   Método utilizado para cancelar a suspensão de um processo escolhido pelo swapper
    def unsuspend(self, pid):
        
        pass

    #   Os métodos a seguir representam requisições básicas feitas por processos
    #   Comumente resultam em faltas de páginas, visto que acessam a MP
    #   Recebem as identificações dos processos e endereços lógicos (quando aplicável)
    def CPUinstruction(self, pid, end):

        pass
    
    def IOinstruction(self, pid):

        #Ver amanhã se eu posso roubar com uma lista de processos. Até lá assumir que p existe
        p = Processo("LEMBRAR DE REMOVER ISSO")

        p.pcb.setBloqueado()
        self.fila_de_processos.transita(pid, "pronto", "bloqueado")

        pass

    def MPread(self, p, end):

        pass

    def MPwrite(self, p, end):

        pass

    #   Método utilizado para desalocar as estruturas associadas a um processo após o seu fim
    def terminateProcess(self, p):


        pass