from Interface_funções import *
from TabelaDePaginas import *
from Processo import *
from MemoriaPrincipal import *
from Quadro import *
from FilaDeProcessos import *
from Interface_classes import *
from Pagina import Agrupamento
from Gerenciador import *
from time import sleep

janela = Window(1920, 1080)
janela.set_title("Gerenciador de Memória")
Mouse = janela.get_mouse()
teclado = janela.get_keyboard()
pressed = False

global gm
global arquivo

# Nota: toda a lógica do gerenciador está implementada na classe Gerenciador. A maior parte das estruturas manipuladas na main que não envolvem gm são relativas à interface.

gm = Gerenciador(6, 8, 2, 5, 2, "caso_simples.txt")
# gm.cria_processo(2, 16)
# gm.fila_de_processos.transita(2, "novo", "pronto")
# gm.ganha_CPU(2)

arquivo = open(gm.arq_entrada, "r")


global podeExecutar

global tam_mp
global tfp
global mdpf
global nfp

global ms
global mp
global cpu

global filas
global tps

global sleepTime

podeExecutarPorPausa = True
podeExecutarPorTempo = False
tam_mp = int(2**(gm.bits_mp - gm.bits_frame))
tfp = 0
mdpf = 0
nfp = 0

ms = Coluna(1475, 50, "MS")
mp = Coluna(1650, 50, "MP")
cpu = Container("Sprites/Cpu_Label.jpg", "CPU"); cpu.set_position(1250, 500)
dma = Container("Sprites/Dma_Label.jpg", "DMA"); dma.set_position(1250, 630)

sleepTime = 0.2

finalizado = False

def atualiza():
        # função que faz a conexão da interface com os dados do gerenciador
        
        global tfp
        global mdpf
        global nfp
        ms.delete()
        for v in mp.array:
            v.popContent()
        for v in filas:
            v.delete()
        for v in tps:
            v.coluna.delete()
            v.list = []

        
        for i, q in enumerate(gm.MP.quadros):
            if q.pagina != None:
                mp.array[i].setContent(Grupo(q.pagina, janela))
        for p in gm.MS.images:
            ms.add(Grupo(p, janela))

        cpu_tmp = gm.executando
        if cpu_tmp == None:
            cpu.popContent()
        else:
            cpu.setContent(Grupo(cpu_tmp, janela))
        
        dma_tmp = gm.emIO
        if dma_tmp == None:
            dma.popContent()
        else:
            dma.setContent(Grupo(dma_tmp, janela))
        
        for p in gm.fila_de_processos.novo.fila:
            filas[0].add(Grupo(p, janela))
        for p in gm.fila_de_processos.pronto.fila:
            filas[1].add(Grupo(p, janela))
        for p in gm.fila_de_processos.bloqueado_page_fault.fila:
            filas[2].add(Grupo(p, janela))
        for p in gm.fila_de_processos.bloqueado_IO.fila:
            filas[3].add(Grupo(p, janela))
        for p in gm.fila_de_processos.sus_pronto.fila:
            filas[4].add(Grupo(p, janela))
        for p in gm.fila_de_processos.sus_bloqueado.fila:
            filas[5].add(Grupo(p, janela))
        
        tfp = gm.fault_rate
        mdpf = gm.mem_waste
        nfp = gm.page_faults

        for i, t in enumerate(gm.TP):
            for r in t.registros:
                if r.p == True:
                    P = 1
                else:
                    P = 0
                if r.m == True:
                    M = 1
                else:
                    M = 0
                tps[i].add((P, M, r.numQuadro))

def executar():
    # função que de fato chama o gerenciador
    global finalizado
    if gm.msgs != []:
        messageBox.newMessage(gm.msgs[0])
        gm.msgs.pop(0)
    else:
        line = arquivo.readline()
        if line != "":
            pieces = line.split()
            pid = int(pieces[0].split("P")[1])
            inst = pieces[1]
            end = pieces[2]
            print(line)
            if inst == "P":

                p = gm.process_by_pid(pid)
                if p.pcb.suspenso:
                    gm.unsuspend(pid)

                gm.CPUinstruction(pid, end)

            elif inst == "I":

                p = gm.process_by_pid(pid)
                if p.pcb.suspenso:
                    gm.unsuspend(pid)
                gm.begin_IO_instruction(pid)

            elif inst == "R":

                p = gm.process_by_pid(pid)
                if p.pcb.suspenso:
                    gm.unsuspend(pid)

                gm.MPread(pid, end)

            elif inst == "W":

                p = gm.process_by_pid(pid)
                if p.pcb.suspenso:
                    gm.unsuspend(pid)

                gm.MPwrite(pid, end, write=True)

            elif inst == "C":
                
                size = binario_decimal(end)
                gm.cria_processo(pid, size)
                gm.fila_de_processos.transita(pid, "novo", "pronto")
                
            elif inst == "T":
                gm.terminateProcess(pid)
            elif inst == "E":
                gm.end_IO_instruction(pid)
        elif not finalizado:
            gm.msgs = [" ", " ", "Alunos:", "Arthur Sodré", "Fábio Gabriel", "Leonardo Meato", "Thiago Thomaz"]
            finalizado = True
        else:
            pass

# criação da interface da mp
for i in range(tam_mp):
    mp.add(Container("Sprites/Quadro_Label.jpg"))

# criação da interface das filas
nomesDasFilas = ("Novo", "Pronto", "Bloq. Page Fault", "Bloq. por E/S", "Pronto-Suspenso", "Bloq.-Suspenso")
filas = []
for i in range (6):
    filas.append(Coluna(20 + i * 170, 610, nomesDasFilas[i]))

# criação da interface das tabelas de páginas
tps = [None]*3
tps[0] = TabelaDePaginasUI(janela, [], "TP - Processo 0")
tps[1] = TabelaDePaginasUI(janela, [], "TP - Processo 1", 300)
tps[2] = TabelaDePaginasUI(janela, [], "TP - Processo 2", 550)

for i in range(7):
    tps.append(TabelaDePaginasUI(janela, [], f"TP - Processo {i + 3}", 85 + i*250, 100))

for i in range(7):
    tps.append(TabelaDePaginasUI(janela, [], f"TP - Processo {i + 10}", 85 + i*250, 600))


messageBox = MessageBox(12, 850, 30, janela)

pauseButton = Sprite("Sprites/Botao_Pausa.png")
pauseButton.set_position(1275, 750)

page = 1

tempo = 0

# loop da interface
while True:

    janela.set_background_color([255, 255, 255])

    tempo += janela.delta_time()
    if tempo > sleepTime:
        podeExecutarPorTempo = True

    if podeExecutarPorPausa and podeExecutarPorTempo:
        executar()
        atualiza()
        podeExecutarPorTempo = False
        tempo = 0
    
    if teclado.key_pressed("1"):
        page = 1
    elif teclado.key_pressed("2"):
        page = 2
    if page == 1:
        messageBox.draw()
        ms.draw()
        mp.draw()
        ms.draw_text(janela)
        mp.draw_text(janela)
        cpu.draw()
        cpu.draw_text(janela)
        dma.draw()
        dma.draw_text(janela)
        pauseButton.draw()
        tps[0].draw()
        tps[1].draw()
        tps[2].draw()
        for i in filas:
            i.draw()
            i.draw_text(janela)
        tfp_show = tfp
        if tfp < 0:
            tfp_show = 0
        write(janela, f"Taxa de falta de páginas: {tfp_show:.2f}                                Número de falta de páginas: {nfp};;Memória desperdiçada por fragmentação: {mdpf}", 50, 50, 20)

        if not pressed and Mouse.is_button_pressed(1):
            pressed = True
            if Mouse.is_over_area((pauseButton.x, pauseButton.y), (pauseButton.x + pauseButton.width, pauseButton.y + pauseButton.height)):
                if podeExecutarPorPausa == True:
                    podeExecutarPorPausa = False
                elif podeExecutarPorPausa == False:
                    podeExecutarPorPausa = True

        if not Mouse.is_button_pressed(1):
            pressed = False
    elif page == 2:
        for i in range(3, len(tps)):
            tps[i].draw()
    else:
        pass
    
    


    janela.update()