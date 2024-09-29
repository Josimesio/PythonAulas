import sys
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication,QMainWindow,QLabel 


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    
        self.setWindowTitle("Imagem")
        self.lbl =QLabel()
        self.lbl.setPixmap(QPixmap("filhotes.jpg"))
        self.lbl.setScaledContents(True)

        self.setCentralWidget(self.lbl)
        
        
 
       
app = QApplication(sys.argv)
w =MainWindow()
w.show()
app.exec()


