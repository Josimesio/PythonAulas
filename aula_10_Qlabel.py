import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication,QMainWindow,QLabel 


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    
        self.setWindowTitle("QLabel")
        self.setFixedSize(QSize(600,400))

        self.lbl =QLabel('Meu Programa')
        #self.lbl.setText("Teste") 
        font =self.lbl.font()
        font.setPointSize(35)
        self.lbl.setFont(font)
        self.lbl.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
 
        self.setCentralWidget(self.lbl)

       
app = QApplication(sys.argv)
w =MainWindow()
w.show()
app.exec()


