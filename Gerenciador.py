#   O arquivo contém a classe responsável pelo gerenciamento
#   da memória do sistema e dos componentes associados

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
    #   Tamanhos são recebidos no formato log2(tamanho desejado) por padrão
    #   n_residente_inicial se refere ao tamanho do conjunto residente alocado na criação de um processo
    #   que passa pela transição (novo, pronto)
    def __init__(self, bits_mp, bits_ms, bits_log, n_residente, arq_entrada):
        
        #   A variável clock é usada como indicação de tempo para a implementação de políticas
        #   do gerenciador e coleta de dados de execução
        self.clock = 0

        self.bits_mp = bits_mp
        self.bits_ms = bits_ms
        self.bits_log = bits_log

        self.n_resident = n_residente

        self.arq_entrada = arq_entrada

        self.MP = MemoriaPrincipal(bits_mp, bits_log)
        self.MS = MemoriaSecundaria(bits_ms)
        self.TP = []

        #self.tabela_de_processos = [] Isso é válido?

        self.fila_de_processos = FilaDeProcessos()


    #   Método responsável por alocar as estruturas necessárias para administrar um novo processo
    def cria_processo(self, pid, size):

        p = Processo(size, self.MP.tam_quadro, pid)
        self.fila_de_processos.novo.adicionar(p)

    #   Método responsável por carregar a imagem de um processo novo para a MP
    #   O número de quadros carregados é decidido por uma configuração
    # def carrega_imagem(self, pid):

    #     tabela = None

    #     for i in range(len(self.TP)):
    #         if self.TP[i].id == pid:
    #             tabela = self.TP[i]

    #     for i in range(self.n_resident):

    #         self.MP.add_LRU(tabela.registros[i])
    #         tabela.registros[i].p = True
    

    #   Método utilizado para marcar a passagem do tempo dentro do sistema
    #   Necessário para a implementação da política LRU de substituição de páginas
    #   e para a chamda do swapper
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

    #   Método utilizado para indicar um erro fatal para a execução do programa
    #   Chamado em situações absurdas como a submissão de um processo com tamanho maior
    #   que o endereço lógico, falta de espaço para swap, acesso à um endereço inválido, etc
    def erro_fatal(msg):

        pass

    #   Os métodos a seguir representam requisições básicas feitas por processos
    #   Comumente resultam em faltas de páginas, visto que acessam a MP
    #   Recebem as identificações dos processos e endereços lógicos (quando aplicável)
    def adquireCPU(self, pid, end):

        pass
    
    def IOinstruction(self, pid):

        #Ver amanhã se eu posso roubar com uma lista de processos. Até lá assumir que p existe
        p = Processo("LEMBRAR DE REMOVER ISSO")

        p.pcb.setBloqueado()
        self.fila_de_processos.transita(pid, "pronto", "bloqueado")

        pass

    def leituraMP(self, pid, end):

        pass

    def escritaMP(self, pid, end):

        pass

    #   Método utilizado para desalocar as estruturas associadas a um processo após o seu fim
    def terminateProcess(self, pid):
        pass