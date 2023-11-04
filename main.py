from TabelaDePaginas import *
from Processo import *
from Memorias import *

t = TabelaDePaginas(1, 10)
f = FilaDeProcessos(5)

for c in range(5):
    f.adicionar(c)
for c in range(3):
    f.remover()

print(t.id, t.registros[6].numQuadro)
print(f.fila)
