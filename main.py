from Interface_funções import *
from TabelaDePaginas import *
from Processo import *
from MemoriaPrincipal import *
from Quadro import *
from FilaDeProcessos import *
from Interface_classes import *
from input import *

janela = Window(1920, 1080)
janela.set_title("Gerenciador de Memória")
Mouse = janela.get_mouse()
teclado = janela.get_keyboard()

global tam_mp
global tfp
global mdpf

global ms
global mp
global cpu

tam_mp = 16
tfp = 0
mdpf = 0

ms = Coluna(1475, 30, "MS")
mp = Coluna(1650, 30, "MP")
cpu = Coluna(1250, 30, "CPU");cpu.add(Container("Sprites/Cpu_Label.jpg"))

'''
#Leitura de Arquivo
arquivo = open("nome_arq", 'r')
instrucoes = arquivo.readlines()
arquivo.close'''
"""
processos = []
id_processos = 0
for i in range(len(instrucoes)):
    instrucoes[i][0] = binario_decimal(instrucoes[i][0]) # Transforma binario em decimal
    if instrucoes[i][1] == 'P': # instrução a ser executada pela CPU
        valido = True
    elif instrucoes[i][1] == 'I': # instrução de I/O
        valido = True

    elif instrucoes[i][1] == 'C': # criação (submissão de um processo)
        valido = True
        num_processo = instrucoes[i][0]
        tam_processo = instrucoes[i][2]
        if len(instrucoes[i]) > 3:
            unidade = instrucoes[i][3]
            if unidade == "KB":
                tam_processo = int(tam_processo) * 210
            elif unidade == "MB":
                tam_processo = int(tam_processo) * 220
            elif unidade == "GB":
                tam_processo = int(tam_processo) * 2**30
        processos.append(Grupo(Processo(tam_processo, id_processos), janela))
        coluna.add(processos[len(processos)-1])
        id_processos += 1

    elif instrucoes[i][1] == 'R': # pedido de leitura em um endereço lógico
        valido = True

    elif instrucoes[i][1] == 'W': # pedido de escrita em um endereço lógico de um dado valor
        valido = True

    elif instrucoes[i][1] == 'T': # terminação de processo
        valido = True
    else:
        print("Instrução inválido")
"""

'''for i in range(10):
    coluna.add(Sprite("Sprites/Pagina_Label.jpg"))

coluna.pop(5)

coluna.absoluteMove(20, 20)
coluna.relativeMove(10, 10)'''



processos = []
for i in range(40):
    processos.append(Processo(20, 2, i))

for i in range(tam_mp):
    mp.add(Container("Sprites/Quadro_Label.jpg"))

nomesDasFilas = ("Novo", "Pronto", "Bloq. Page Fault", "Bloq. por E/S", "Pronto-Suspenso", "Bloq.-Suspenso")
filas = []
for i in range (6):
    filas.append(Coluna(20 + i * 170, 500, nomesDasFilas[i]))
    for j in range(2):
        filas[i].add(Grupo(processos[i*2 + j], janela))

filas[3].add(Grupo(processos[14], janela))
filas[3].add(Grupo(processos[15], janela))
filas[3].add(Grupo(processos[16], janela))
filas[3].add(Grupo(processos[18], janela))
filas[3].add(Grupo(processos[19], janela))
filas[5].add(Grupo(processos[20], janela))
filas[5].add(Grupo(processos[21], janela))


'''
print("Informe numero de bits da pagina, e numero de bits dos quadros")
tam_pag, tam_qua = input().split()
tam_pag = int(tam_pag)
tam_qua = int(tam_qua)
memoria = MemoriaPrincipal(tam_pag, tam_qua) #Memoria Principal inicializada

t = TabelaDePaginas(1, 10)
f = FilaDeProcessos()

for c in range(5):
    f.pronto.adicionar(c)
for c in range(3):
    f.pronto.remover()

print(t.id, t.registros[6].numQuadro)
print(f.pronto.fila)'''


while True:
    janela.set_background_color([255, 255, 255])
    ms.draw()
    mp.draw()
    ms.draw_text(janela)
    mp.draw_text(janela)
    cpu.draw()
    cpu.draw_text(janela)
    for i in filas:
        i.draw()
        i.draw_text(janela)
    write(janela, f"Taxa de falta de páginas: {tfp};;Memória desperdiçada por fragmentação: {mdpf}", 40, 40, 20)
    janela.update()
    #erro("oops")