from PyQt5.QtWidgets import *

global txt
txt = 0

def main():
    def onClicked():
        pass
    app = QApplication([])
    window = QWidget()
    window.setGeometry(100, 100, 200, 300)
    window.setWindowTitle("Teste")
    window2 = QWidget()
    

    layout = QVBoxLayout()
    label = QLabel("{}".format(txt))
    textbox = QTextEdit()
    button = QPushButton("Teste")
    button.clicked.connect(onClicked)

    layout.addWidget(label)
    layout.addWidget(textbox)
    layout.addWidget(button)

    window.setLayout(layout)

    window.show()
    #window2.show()
    app.exec_()

    

if __name__ == '__main__':
    main()