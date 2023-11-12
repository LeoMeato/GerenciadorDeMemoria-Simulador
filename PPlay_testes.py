from PPlay.window import *
from PPlay.sprite import *

class Reta:
     
     def __init__(self, x, y) -> None:
        self.array = []
        self.x = x
        self.y = y
    
     def draw(self):
        for s in self.array:
            s.draw()
    
     def add(self, sprite):
        pass
     
     def remove(self, pos):
        pass
    
     def absoluteMove(self, x, y):
        array = []
        for s in self.array:
            array.append(s)
        self.array = []
        self.x = x
        self.y = y
        for s in array:
            self.add(s)
     
     def relativeMove(self, x, y):
         for s in self.array:
             s.x += x
             s.y += y
         self.x += x
         self.y += y


class Coluna(Reta):

    def add(self, sprite):
        if self.array == []:
            sprite.set_position(self.x, self.y)
        else:
            var = self.array[-1]
            sprite.set_position(var.x, var.y + var.height)
        self.array.append(sprite)

    def remove(self, pos):
         
         y = self.array[pos].height
         self.array.pop(pos)
         for i in range (pos, len(self.array)):
             self.array[i].y -= y
             

class Linha(Reta):

    def add(self, sprite):
        if self.array == []:
            sprite.set_position(self.x, self.y)
        else:
            var = self.array[-1]
            sprite.set_position(var.x + var.width, var.y)
        self.array.append(sprite)
    
    def remove(self, pos):
         
         x = self.array[pos].width
         self.array.pop(pos)
         for i in range (pos, len(self.array)):
             self.array[i].x -= x

janela = Window(1280, 720)
janela.set_title("Gerenciador de Memória")
Mouse = janela.get_mouse()
teclado = janela.get_keyboard()

coluna = Coluna(50, 50)

for i in range(10):
    coluna.add(Sprite("Sprites/label_01.png"))

coluna.remove(5)

coluna.absoluteMove(200, 200)
coluna.relativeMove(100, 100)

while True:
    janela.set_background_color([255, 255, 255])
    coluna.draw()
    janela.update()


