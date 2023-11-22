#   O arquivo contém a classe responsável pelo gerenciamento
#   da memória do sistema e dos componentes associados
from math import *
from Processo import *
from utilidades import *
from FilaDeProcessos import *
from MemoriaPrincipal import *
from MemoriaSecundaria import *

#   Classe: Gerenciador de Memória
#   
#   Responsável por receber e interpretar as instruções de entrada
#   Todos os métodos tem como efeito colateral adicionar uma mensagem
#   indicando o que foi realizado
#   Mensagens são recebidas e manipuladas pela interface
class Gerenciador:

    #   Construtor
    #
    #   Inicializa o gerenciador explicitando os tamanhos dos vários componentes da memória
    #   Tamanhos são recebidos no formato log2(tamanho desejado) por padrão
    #   n_residente_inicial se refere ao tamanho do conjunto residente alocado na criação de um processo
    #   que passa pela transição (novo, pronto)
    def __init__(self, bits_mp, bits_ms, bits_frame, bits_log, n_residente, arq_entrada, max_fault_rate=0.35):
        
        #   A variável clock é usada como indicação de tempo para a implementação de políticas
        #   do gerenciador e coleta de dados de execução
        self.clock = 0
        self.time_since_swap = 0
        self.faults_since_swap = 0

        #   Essas variáveis são coletadas ao longo da execução de uma instância
        #   e exibidas em uma interface
        self.page_faults = 0
        self.fault_rate = 0
        self.mem_waste = 0

        #   Mensagens é uma fila entregue à interface a cada interação para
        #   permitir que um histórico de ações relevates seja montado
        self.msgs = []

        #   Essas variáveis são todas configurações ou consequências diretas delas
        #   Todas as bits_ representam o número de bits necessário para endereçar a
        #   estrutura a qual estão associadas
        self.bits_mp = bits_mp
        self.bits_ms = bits_ms
        self.bits_log = bits_log
        self.bits_frame = bits_frame
        self.n_resident = n_residente
        self.max_fault_rate = max_fault_rate

        self.frame_size = 2**bits_frame
        self.arq_entrada = arq_entrada

        #   Estruturas manipuladas pelo gerenciador
        self.MP = MemoriaPrincipal(bits_mp, bits_frame)
        self.MS = MemoriaSecundaria(bits_ms)
        self.TP = []
        self.tabela_de_processos = []
        self.fila_de_processos = FilaDeProcessos()

        #   Informação visual para os processos que ganharam DMA e CPU
        self.executando = None
        self.emIO = None




    #   Método responsável por alocar as estruturas necessárias para administrar um novo processo
    def cria_processo(self, pid, size):


        p = Processo(size, self.frame_size, pid)
        self.fila_de_processos.novo.adicionar(p)

        n_paginas = ceil(size/self.frame_size)
        tp = TabelaDePaginas(pid, n_paginas)
        self.TP.append(tp)

        self.tabela_de_processos.append(p)

        self.MS.load_image(p)
        self.carrega_imagem_MP(p)


    #   Método responsável por carregar a imagem de um processo sem nenhuma página na MP para a mesma
    #   O número de quadros carregados é decidido por uma configuração
    def carrega_imagem_MP(self, processo):
            i = 0
            while i < self.n_resident and i < len(processo.paginas):
                pagina = self.MS.swap_in(processo.id, i)
                self.add_LRU(pagina)
                i += 1

    #   Método implementa a polítical de substituição de páginas do sistema
    #   Desculpa pelo método gigante gente
    def add_LRU(self, pagina):

        new_pid = self.pid_of_page(pagina)
        new_page_num = self.num_of_page(pagina)
        new_tp = self.TP_by_pid(new_pid) 

        lru_index = max_age = 0
        quadro = None
        for i in range(len(self.MP.quadros)):

            quadro = self.MP.quadros[i]

            if not quadro.presenca:
                self.MP.aloca_pagina(i, pagina)
                new_tp.aloca_entrada(new_page_num, i)
                return
            
            if (quadro.last_update > max_age):
                lru_index = i
                max_age = quadro.last_update


        ##### IMPORTANTE: USAR O BIT M PARA VERIFICAR SE A CHAMDA DE SWAP OUT FAZ SENTIDO

        old_pid = self.pid_of_page(quadro.pagina)
        old_page_num = self.num_of_page(quadro.pagina)
        old_tp = self.TP_by_pid(old_pid)

        if old_tp.registros[old_page_num].m:    #Se a página antiga não foi modificada, evita o swapout desnecessário
            self.MS.swap_out(old_pid, old_page_num, quadro.pagina)
        self.MP.retira_pagina(lru_index)
        old_tp.desaloca_entrada(old_page_num)

        self.MP.aloca_pagina(lru_index, pagina)
        new_tp.aloca_entrada(new_page_num, lru_index)

        self.atualizaDados()


    #   Método que isola a abstração da busca pelo processo de uma página
    #   Perguntar os limites de implementação para a professora
    def pid_of_page(self, pagina):
        return pagina.id

    #   Idem
    def num_of_page(self, pagina):
        return pagina.num
    
    #   Métodos que existem por pura conveniência
    def process_by_pid(self, pid):

        for p in self.tabela_de_processos:
            if p.pcb.id == pid:
                return p
        return None
    
    def TP_by_pid(self, pid):

        for tp in self.TP:
            if tp.id == pid:
                return tp
        return None

    def count_page_fault(self):

        self.page_faults += 1
        self.faults_since_swap += 1

    def get_mem_waste(self):

        waste = 0
        for q in self.MP.quadros:
            waste += self.frame_size - q.pagina.tam
        return waste
    
    def ganha_CPU(self, pid):

        if self.executando != None:
            self.executando.pcb.setPronto()
            self.fila_de_processos.pronto.adicionar(self.executando)
        
        self.executando = self.fila_de_processos.pronto.remove_pid(pid)
        self.executando.pcb.setExecutando()

    #   Método utilizado para manter a consistência das informações do gerenciador
    #   Deve ser chamado ao fim de qualquer método que não seja considerado de duração nula
    def atualizaDados(self):

        self.clock += 1
        self.MP.atualiza_clock_quadros()

        self.time_since_swap += 1
        self.fault_rate = self.faults_since_swap / self.time_since_swap

        self.mem_waste = self.get_mem_waste()
        
    #   Os métodos a seguir representam requisições básicas feitas por processos
    #   Comumente resultam em faltas de páginas, visto que acessam a MP
    #   Recebem as identificações dos processos como decimais e endereços lógicos como strings binárias(quando aplicável)

    #   Método genérico que representa um acesso qualquer à memória principal
    #   Por ser um método auxiliar, é considerado tempo 0 para a chamada de atualizaDados()
    #   Supõe que pid é o id de um processo que ganhou no instante da chamada
    def MPaccess(self, pid, end):

        tp = self.TP_by_pid(pid)
        p = self.process_by_pid(pid)

        n_pag_bin = end[0 : self.bits_log-self.bits_frame]
        n_pag = binario_decimal(n_pag_bin)

        offset_bin = end[self.bits_log-self.bits_frame : ]
        offset = binario_decimal(offset_bin)

        num_quadro = tp.consulta_entrada(n_pag)
        if not num_quadro:  #Falta de páginas

            self.count_page_fault()

            self.executando = None
            p.pcb.setBloqueado()
            self.fila_de_processos.bloqueado_page_fault.adicionar(p)

            page = self.MS.swap_in(pid, n_pag)
            self.add_LRU(page)

            p.pcb.setExecutando()
            self.executando = self.fila_de_processos.bloqueado_page_fault.remove_pid(pid)

            num_quadro = tp.consulta_entrada(n_pag)

        pagina_acessada = self.MP.consulta_pagina(num_quadro)

        return pagina_acessada

    def CPUinstruction(self, pid, end):

        self.ganha_CPU(pid)
        used_page = self.MPaccess(pid, end)

        self.atualizaDados()
    
    def begin_IO_instruction(self, pid):

        self.ganha_CPU(pid)
        p = self.process_by_pid(pid)

        self.executando = None
        self.fila_de_processos.transita(pid, "pronto", "bloqueado")

        if (self.emIO == None):
            self.emIO = p
        
        self.atualizaDados()

    def end_IO_instruction(self, pid):

        p = self.emIO

        if p.pcb.suspenso:

            self.fila_de_processos.transita(pid, "sus_bloqueado", "sus_pronto")
        
        else:

            self.fila_de_processos.transita(pid, "bloqueado_IO", "pronto")
        
        self.emIO = self.fila_de_processos.bloqueado_IO.remover()

        self.atualizaDados()


    def MPread(self, pid, end):

        self.ganha_CPU(pid)
        used_page = self.MPaccess(pid, end)

        self.atualizaDados()

    def MPwrite(self, pid, end):

        self.ganha_CPU(pid)
        used_page = self.MPaccess(pid, end)

        self.atualizaDados()


    #   Método utilizado para desalocar as estruturas associadas a um processo após o seu fim
    #   seja lá qual for o motivo
    def terminateProcess(self, pid):

        tp = self.TP_by_pid(pid)

        p = self.process_by_pid(pid)
        if self.executando == p:
            self.executando = None

        elif self.emIO == p:
            self.emIO = None

        self.fila_de_processos.purge(pid)
        self.tabela_de_processos.remove(p)

        for r in tp.registros:

            if (r.p):
                self.MP.retira_pagina(r.numQuadro)

        self.MS.remove_image(p)
        self.TP.remove(tp)

        self.atualizaDados()


    #   Método utilizado para julgar se o número recente de faltas de páginas é excessivo
    #   e realizar a suspensão de um processo caso necessário
    def check_fault_rate(self):
        if self.fault_rate >= self.max_fault_rate:
            self.call_swap_out()
        

    #   Método utilizado para suspender um processo, que será escolhido pelo swapper
    #   Deve ser chamado quando a taxa de falta de páginas atingir um número inaceitável
    #   A política implementada suspende o processo que ocupa mais espaço na MP no momento
    #   da chamada
    def call_swap_out(self):

        max_use = -1
        max_use_i = 0

        for i in range(len(self.TP)):

            tp = self.TP[i]
            if self.executando != None and tp.id == self.executando.id: #Garantindo que o processo em execução não é um candidato a suspensão
                continue

            mp_use = 0

            for r in tp:

                if r.p:
                    mp_use += self.MP.quadros[r.numQuadro]
            
            if mp_use > max_use:
                 max_use = mp_use
                 max_use_i = i

        
        tp = self.TP[max_use_i]
        self.suspend(self, tp.id, tp)


    #   Método utilizado para suspender um processo
    #   No sistema implementado, só faz sentido suspender prontos e bloqueados por IO
    def suspend(self, pid, tp):

        p = self.process_by_pid(pid)

        for i in range(tp.registros):

            r = tp.registros[i]

            if r.p:

                page = self.MP.quadros[r.numQuadro].pagina

                if r.m:
                    self.MS.swap_out(pid, page.num, page)
                
                self.MP.retira_pagina(r.numQuadro)
                r.desaloca_registro()

        if p.pcb.estado == "pronto":

            self.fila_de_processos.transita(pid, p.pcb.estado, "sus_pronto")
        
        else:

            if p.pcb.estado == "bloqueado":

                self.fila_de_processos.transita(pid, "bloqueado_IO", "sus_bloqueado")

        p.pcb.setSuspensoTrue()


    #   Método utilizado para cancelar a suspensão de um processo escolhido pelo swapper
    #   É assumido que se um processo é escolhido pelo escalonador ele deve ter o estado
    #   de suspenso removido imediatamente
    def unsuspend(self, pid):
        
        p = self.process_by_pid(pid)

        if not p.pcb.suspenso:
            erro("Tentativa de remover suspensão de Processo não suspenso " + pid)

        p.pcb.setSuspensoFalse()

        if p.pcb.estado == "bloqueado":
            self.fila_de_processos.transita(pid, "sus_bloqueado", "bloqueado_IO")
        else:
            self.fila_de_processos.transita(pid, "sus_pronto", "pronto")
