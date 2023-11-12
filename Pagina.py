class Agrupavel:
    label = ''
    content = ''

class Pagina(Agrupavel):

    label = "Sprites/Pagina_Label.jpg"
    content = "Página X"

    #deve haver um metodo que entregue uma copia dela mesma
    def __init__(self, tam) -> None:

        # A página não precisa conhecer o id do próprio processo, certo? -Arthur
        self.tam = tam
        self.conteudo = []