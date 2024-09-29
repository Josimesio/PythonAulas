import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Meu primeiro programa")

        button = QPushButton("clique aqui")
        self.setCentralWidget(button)
        button.clicked.connect(self.imprimir)
 
    def imprimir(self):
        print( "testando botão")
            
app = QApplication(sys.argv)
w =MainWindow()
w.show()
app.exec()