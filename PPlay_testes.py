from PPlay.window import *
from PPlay.sprite import *
from Processo import *
from Pagina import *

class Grupo(Sprite):
     
     # Classe que estende Sprite e tem como função reunir um sprite de label e seu conteúdo (texto),
     # bem como acoplar seus desenhos na tela.

     def __init__(self, agrupamento, frames=1):
         
         super().__init__(agrupamento.label, frames)
         self.txt = agrupamento.content
    
     def draw(self):
         super().draw()
         janela.draw_text(self.txt, self.x + 40, self.y + 25, 25, (0, 0, 0), "Candara")


class Reta:
     
     # Classe que empilha sprites na tela (ou, como deve ser usada na maior parte das vezes, empilha Grupos)
     
     def __init__(self, x, y) -> None:
        self.array = []
        self.x = x
        self.y = y
    
     def draw(self):
        for s in self.array:
            s.draw()
    
     def add(self, sprite):
        # adiciona um sprite no fim da reta
        pass
     
     def pop(self, pos):
        # deleta o sprite da posição pos e reorganiza a reta
        pass
    
     def absoluteMove(self, x, y):
        # movimenta a reta inteira como se fosse um único sprite para a posição (x, y)
        array = []
        for s in self.array:
            array.append(s)
        self.array = []
        self.x = x
        self.y = y
        for s in array:
            self.add(s)
     
     def relativeMove(self, x, y):
         # translada a reta inteira por x pixels no eixo x e y pixels no eixo y
         for s in self.array:
             s.x += x
             s.y += y
         self.x += x
         self.y += y
    
     def remove(self, pos):
         # remove o sprite da posição pos, sem reorganizar a fila (o que ocorre na verdade é que
         # o sprite é substituído por um png vazio no array)
         self.array[pos] = Sprite("Sprites/Vazio_Label.png")

     def overwrite(self, pos, sprite):
         # insere na posição pos o sprite sprite, por cima do que estiver lá, seja um sprite funcional ou vazio.
         pass


class Coluna(Reta):

    def add(self, sprite):
        if self.array == []:
            sprite.set_position(self.x, self.y)
        else:
            var = self.array[-1]
            sprite.set_position(var.x, var.y + var.height)
        self.array.append(sprite)

    def pop(self, pos):
         
         y = self.array[pos].height
         self.array.pop(pos)
         for i in range (pos, len(self.array)):
             self.array[i].y -= y
    
    def overwrite(self, pos, sprite):
        if sprite in self.array:
            self.array.remove(sprite)
        self.array[pos] = sprite
        var = self.array[pos - 1]
        self.array[pos].set_position(var.x, var.y + var.height)
             

class Linha(Reta):

    def add(self, sprite):
        if self.array == []:
            sprite.set_position(self.x, self.y)
        else:
            var = self.array[-1]
            sprite.set_position(var.x + var.width, var.y)
        self.array.append(sprite)
    
    def pop(self, pos):
         
         x = self.array[pos].width
         self.array.pop(pos)
         for i in range (pos, len(self.array)):
             self.array[i].x -= x
    
    def overwrite(self, pos, sprite):
        if sprite in self.array:
            self.array.remove(sprite)
        self.array[pos] = sprite
        var = self.array[pos - 1]
        self.array[pos].set_position(var.x + var.width, var.y)

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

p1 = Processo(4, 0)
p2 = Processo(4, 1)
p3 = Processo(4, 2)
p4 = Processo(4, 3)

g1 = Grupo(p1)
g2 = Grupo(p2)
g3 = Grupo(p3)
g4 = Grupo(p4)

coluna.add(g1)
coluna.add(g2)
coluna.add(g3)
coluna.add(g4)

coluna.add(Grupo(Pagina(10)))

coluna.remove(1)
coluna.overwrite(1, g2)

while True:
    janela.set_background_color([255, 255, 255])
    coluna.draw()
    janela.update()


