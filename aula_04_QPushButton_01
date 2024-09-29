import sys
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Meu primeiro programa")

        button = QPushButton("clique aqui")
        self.setCentralWidget(button)
        
        button.setCheckable(True)
        button.clicked.connect(self.imprimir)
        button.clicked.connect(self.clicado)
 
        self.setFixedSize(QSize(600,400))


    def imprimir(self):
        print( "testando botão")

    def clicado(self,s):
        print("clicado", s)   
            
app = QApplication(sys.argv)
w =MainWindow()
w.show()
app.exec()