from PPlay.window import *

global janela
janela = Window(1920, 1080)

def erro(msg):
    while True:
        janela.set_background_color([0, 0, 255])
        write(janela, f"Houve um erro :(;;{msg}", 35, 25, 20, (255, 255, 255))
        janela.update()

def write(janela, txt, x, y, tam, cor=(0, 0, 0)):
    # Escreve o texto txt na tela, dando um Enter a cada ";"
    txts = txt.split(';')
    for i, t in enumerate(txts):
        janela.draw_text(t, x, y + i*tam, tam, cor)