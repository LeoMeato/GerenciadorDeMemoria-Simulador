from PPlay.window import *
from PPlay.sprite import *
from Processo import *
from Pagina import *

class TabelaDePaginas:

    def __init__(self, janela, list, title, x=50, y=170) -> None:
        self.coluna = Coluna(x, y, title)
        self.janela = janela
        self.list = list
        for v in list:
            g = Grupo(Agrupamento("Sprites/Tp_Registro.jpg", f"{v[0]}    {v[1]}    {v[2]}"), self.janela)
            self.coluna.add(g)

    def add(self, tuple):
        t = tuple
        g = Grupo(Agrupamento("Sprites/Tp_Registro.jpg", f"{t[0]}    {t[1]}    {t[2]}"), self.janela)
        self.coluna.add(g)
        self.list.append(t)

    def modify(self, pos, tuple):
        t = tuple
        g = Grupo(Agrupamento("Sprites/Tp_Registro.jpg", f"{t[0]}    {t[1]}    {t[2]}"), self.janela)
        self.coluna.overwrite(pos, g)
    
    def setM(self, pos, value):
        to = self.list[pos]
        tn = (to[0], value, to[2])
        g = Grupo(Agrupamento("Sprites/Tp_Registro.jpg", f"{tn[0]}    {tn[1]}    {tn[2]}"), self.janela)
        self.coluna.overwrite(pos, g)
        self.list[pos] = tn
    
    def setAddress(self, pos, value):
        to = self.list[pos]
        tn = (to[0], to[1], value)
        g = Grupo(Agrupamento("Sprites/Tp_Registro.jpg", f"{tn[0]}    {tn[1]}    {tn[2]}"), self.janela)
        self.coluna.overwrite(pos, g)
        self.list[pos] = tn

    def draw(self):
        self.coluna.draw_text(self.janela)
        self.coluna.draw()

class Container(Sprite):
    # Classe que possui um sprite maior e um Grupo menor, o maior funcionando como um contêiner para o Grupo

    def __init__(self, image_file, title="", frames=1):
        super().__init__(image_file, frames)
        self.title = title
        self.grupo = Sprite("Sprites/Vazio_Label.png")
    
    def draw(self):
        super().draw()
        self.grupo.set_position(self.x + 12, self.y + 5)
        self.grupo.draw()
    
    def draw_text(self, janela):
         janela.draw_text(self.title, self.x, self.y - 30, 20, (0,0,0))
    
    def setContent(self, sprite):
        self.grupo = sprite
    
    def popContent(self):
        self.setContent(Sprite("Sprites/Vazio_Label.png"))

class Grupo(Sprite):
     
     # Classe que herda de Sprite e tem como função reunir um sprite de label e seu conteúdo (texto),
     # bem como acoplar seus desenhos na tela.

     def __init__(self, agrupamento, janela, ratio=14,frames=1):
         self.ratio = ratio
         super().__init__(agrupamento.label, frames)
         self.txt = agrupamento.content
         self.janela = janela
    
     def draw(self):
         super().draw()
         self.janela.draw_text(self.txt, self.x + self.width/self.ratio, self.y + self.height/self.ratio * 2, 25, (0, 0, 0), "Comic Sans")

class MessageBox:
    def __init__(self, tam, x, y, janela) -> None:
        self.coluna = Coluna(x, y)
        self.janela = janela
        for i in range(tam):
            self.coluna.add(Grupo(Agrupamento("Sprites/Caixa_De_Acao.jpg", ""), self.janela, 60))
        
    def draw(self):
        self.coluna.draw()
    
    def newMessage(self, msg):
        self.coluna.pop(0)
        self.coluna.add(Grupo(Agrupamento("Sprites/Caixa_De_Acao.jpg", msg), self.janela, 60))


class Reta: # Classe Abstrata
     # Classe que empilha sprites na tela (ou, como deve ser usada na maior parte das vezes, empilha Grupos)
     
     def __init__(self, x, y, title="") -> None:
        self.title = title
        self.array = []
        self.x = x
        self.y = y
    
     def draw(self):
        for i in range(len(self.array) - 1, -1, -1):
            self.array[i].draw()
     
     def draw_text(self, janela):
         pass
    
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

    def draw_text(self, janela):
         janela.draw_text(self.title, self.x, self.y - 30, 20, (0,0,0))

    def add(self, sprite):
        if self.array == []:
            sprite.set_position(self.x, self.y)
        else:
            var = self.array[-1]
            sprite.set_position(var.x, var.y + var.height)
        self.array.append(sprite)

    def pop(self, pos = -1):
         
         if pos == -1:
             pos = len(self.array) - 1
         
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

    def draw_text(self, janela):
         janela.draw_text(self.title, self.x - 30, self.y, 20, (0,0,0))

    def add(self, sprite):
        if self.array == []:
            sprite.set_position(self.x, self.y)
        else:
            var = self.array[-1]
            sprite.set_position(var.x + var.width, var.y)
        self.array.append(sprite)
    
    def pop(self, pos = -1):
         
         if pos == -1:
            pos = len(self.array) - 1
         
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




