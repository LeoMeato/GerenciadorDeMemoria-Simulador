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



class Coluna(Reta):

    def add(self, sprite):
        if self.array == []:
            sprite.set_position(self.x, self.y)
        else:
            var = self.array[-1]
            sprite.set_position(var.x, var.y + var.height)
        self.array.append(sprite)

class Linha(Reta):

    def add(self, sprite):
        if self.array == []:
            sprite.set_position(self.x, self.y)
        else:
            var = self.array[-1]
            sprite.set_position(var.x + var.width, var.y)
        self.array.append(sprite)

janela = Window(1280, 720)
janela.set_title("Gerenciador de Memória")
Mouse = janela.get_mouse()
teclado = janela.get_keyboard()

coluna = Coluna(50, 50)

for i in range(10):
    coluna.add(Sprite("Sprites/label_01.png"))

while True:
    janela.set_background_color([255, 255, 255])
    coluna.draw()
    janela.update()


