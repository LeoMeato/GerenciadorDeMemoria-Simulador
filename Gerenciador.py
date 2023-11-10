#   O arquivo contém a classe responsável pelo gerenciamento
#   da memória do sistema e dos componentes associados

from Swapper import *
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
    def __init__(self, bits_mp, bits_ms, bits_log, arq_entrada):
        
        #   A variável clock é usada como indicação de tempo para a implementação de políticas
        #   do gerenciador e coleta de dados de execução
        self.clock = 0

        self.bits_mp = bits_mp
        self.bits_ms = bits_ms
        self.bits_log = bits_log

        self.arq_entrada = arq_entrada

        self.MP = MemoriaPrincipal(bits_mp, bits_log)
        self.MS = MemoriaSecundaria(bits_ms)
        self.TP = []

    
    def cria_processo(size):
        pass