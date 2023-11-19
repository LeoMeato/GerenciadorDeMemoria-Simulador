class Agrupavel:
    label = ''
    content = ''

class Pagina(Agrupavel):

    label = "Sprites/Pagina_Label.jpg"
    content = ""

    #deve haver um metodo que entregue uma copia dela mesma
    def __init__(self, tam, id, num) -> None:

        self.id = id
        self.num = num
        self.content = f"Página {num} P{id}"
        self.tam = tam
        self.conteudo = []