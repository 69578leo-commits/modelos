from PyQt5 import QtWidgets,uic
from load.load_ventana_modelos_basicos import Load_ventana_modelos_basicos

class Load_ventana_menu(QtWidgets.QMainWindow):
    def init(self):
        super()._init_()
        uic.loadUi("interfaces_ventana_menu.ui",self)
        self.showMaximized()

        self.acrionBasico.triggered.connect(self.abrirVentanaBasicos)
        self.actionLangchain.triggered.connect(self.abrirVentanaLangchain)
        self.actionSalir.triggered.connect(self.cerrarVentana)

    def abrirVentanaBasicos(self):
        self.basicos=Load_ventana_modelos_basicos()
        self.basicos.exec_()
    def abrirVentanaLangchain(self):
        pass
    def cerrarVentana(self):
        self.close()