from Interface_funções import *
from TabelaDePaginas import *
from Processo import *
from MemoriaPrincipal import *
from Quadro import *
from FilaDeProcessos import *
from Interface_classes import *

janela = Window(1280, 720)
janela.set_title("Gerenciador de Memória")
Mouse = janela.get_mouse()
teclado = janela.get_keyboard()

coluna = Coluna(50, 50)

'''for i in range(10):
    coluna.add(Sprite("Sprites/Pagina_Label.jpg"))

coluna.pop(5)

coluna.absoluteMove(20, 20)
coluna.relativeMove(10, 10)'''

p1 = Processo(4, 4, 0)
p2 = Processo(4, 4, 1)
p3 = Processo(4, 4, 2)
p4 = Processo(4, 4, 3)

g1 = Grupo(p1, janela)
g2 = Grupo(p2, janela)
g3 = Grupo(p3, janela)
g4 = Grupo(p4, janela)

coluna.add(g1)
coluna.add(g2)
coluna.add(g3)
coluna.add(g4)

coluna.add(Grupo(Pagina(10), janela))

coluna.remove(1)
coluna.overwrite(1, g2)

g5 = Grupo(Processo(4, 4, 4), janela)
c1 = Container("Sprites/Quadro_Label.jpg")
coluna.add(c1)

c1.setContent(g5)

MP = Coluna(400, 20)
for i in range(7):
    MP.add(Container("Sprites/Quadro_Label.jpg"))

MP.array[4].setContent(g5)    
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
    coluna.draw()
    MP.draw()
    janela.update()
    erro(janela, "oops")
    '''valido = False # Será true quando o comando for válido
    processos = []
    id_processos = 0
    while (valido == False):
        comando = input().split() # array dos inputs
        print(comando)

        if comando[1] == 'P': # instrução a ser executada pela CPU
            valido = True

        elif comando[1] == 'I': # instrução de I/O
            valido = True

        elif comando[1] == 'C': # criação (submissão de um processo)
            valido = True
            num_processo = comando[0]
            tam_processo = comando[2]
            if len(comando) > 3:
                unidade = comando[3]
                if unidade == "KB":
                    tam_processo = int(tam_processo) * 2**10
                elif unidade == "MB":
                    tam_processo = int(tam_processo) * 2**20
                elif unidade == "GB":
                    tam_processo = int(tam_processo) * 2**30
            processos.append(Grupo(Processo(tam_processo, id_processos), janela))
            coluna.add(processos[len(processos)-1])
            id_processos += 1

        elif comando[1] == 'R': # pedido de leitura em um endereço lógico
            valido = True

        elif comando[1] == 'W': # pedido de escrita em um endereço lógico de um dado valor
            valido = True

        elif comando[1] == 'T': # terminação de processo
            valido = True

        else:
            print("Comando inválido")
'''