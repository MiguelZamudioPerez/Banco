import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class Banco(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Banco.ui",self)

        self.addRegister.setEnabled(False) # Establece como no clickable el boton addRegister
        self.mostrarTabla.clicked.connect(self.fnActivar) # Conectamos con la funcion al clickar
        self.addRegister.clicked.connect(self.fnDesactivar)
        
    def fnActivar(self):    
        self.addRegister.setEnabled(True)
        self.mostrarTabla.setEnabled(False)

    def fnDesactivar(self):    
        self.mostrarTabla.setEnabled(True)
        self.addRegister.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    banco = Banco()
    banco.show()
    sys.exit(app.exec_())


# self.mostrarTabla.isEnabled()  # Te devuelve True si esta activo o False si no