from TabelaDePaginas import *
from Processo import *
from MemoriaPrincipal import *
from Quadro import *

print("Informe numero de bits da pagina, e numero de bits dos quadros")
tam_pag, tam_qua = input().split()
tam_pag = int(tam_pag)
tam_qua = int(tam_qua)
memoria = MemoriaPrincipal(tam_pag, tam_qua) #Memoria Principal inicializada





t = TabelaDePaginas(1, 10)
f = FilaDeProcessos(5)

for c in range(5):
    f.adicionar(c)
for c in range(3):
    f.remover()

print(t.id, t.registros[6].numQuadro)
print(f.fila)
