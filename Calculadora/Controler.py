from Calculadora_Científica import Ui_CalculadoraCientifica
from Calculadora_Comum import Ui_CalculadoraComum
from Menu import Ui_Menu

from PyQt5 import QtCore, QtGui, QtWidgets
import math

class Controler():
    def __init__(self):
        self.Widgets_Menu = QtWidgets.QWidget()
        self.ui_menu = Ui_Menu()
        self.ui_menu.setupUi(self.Widgets_Menu)

        self.Widgets_Comum = QtWidgets.QWidget()
        self.ui_comum = Ui_CalculadoraComum()
        self.ui_comum.setupUi(self.Widgets_Comum)

        self.Widgets_Cientifica = QtWidgets.QWidget()
        self.ui_cientifica = Ui_CalculadoraCientifica()
        self.ui_cientifica.setupUi(self.Widgets_Cientifica)


        self.display_txt = self.ui_cientifica.display.text()

        self.ui_menu.comum.clicked.connect(self.muda_menu_comum)
        self.ui_menu.cientifica.clicked.connect(self.muda_menu_cientifica)
        self.ui_comum.voltar.clicked.connect(self.muda_comum_menu)
        self.ui_cientifica.voltar.clicked.connect(self.muda_cientifica_menu)

        self.ui_comum.um.clicked.connect(self.escreve_display)
        self.ui_comum.dois.clicked.connect(self.escreve_display)
        self.ui_comum.trez.clicked.connect(self.escreve_display)
        self.ui_comum.quatro.clicked.connect(self.escreve_display)
        self.ui_comum.cinco.clicked.connect(self.escreve_display)
        self.ui_comum.seis.clicked.connect(self.escreve_display)
        self.ui_comum.sete.clicked.connect(self.escreve_display)
        self.ui_comum.oito.clicked.connect(self.escreve_display)
        self.ui_comum.nove.clicked.connect(self.escreve_display)
        self.ui_comum.zero.clicked.connect(self.escreve_display)

        self.ui_comum.virgula.clicked.connect(self.virgula)

        self.ui_comum.apaga.clicked.connect(self.apaga_um)
        self.ui_comum.C.clicked.connect(self.apaga_C)

        self.ui_comum.raiz.clicked.connect(self.operacoes_avancada)
        self.ui_comum.divisao.clicked.connect(self.operacoes_padrao)
        self.ui_comum.vezes.clicked.connect(self.operacoes_padrao)
        self.ui_comum.menos.clicked.connect(self.operacoes_padrao)
        self.ui_comum.mais.clicked.connect(self.operacoes_padrao)

        self.ui_comum.igual.clicked.connect(self.igual)

        self.ui_cientifica.um.clicked.connect(self.escreve_display)
        self.ui_cientifica.dois.clicked.connect(self.escreve_display)
        self.ui_cientifica.tres.clicked.connect(self.escreve_display)
        self.ui_cientifica.quatro.clicked.connect(self.escreve_display)
        self.ui_cientifica.cinco.clicked.connect(self.escreve_display)
        self.ui_cientifica.seis.clicked.connect(self.escreve_display)
        self.ui_cientifica.sete.clicked.connect(self.escreve_display)
        self.ui_cientifica.oito.clicked.connect(self.escreve_display)
        self.ui_cientifica.nove.clicked.connect(self.escreve_display)
        self.ui_cientifica.zero.clicked.connect(self.escreve_display)

        self.ui_cientifica.virgula.clicked.connect(self.virgula)
        
        self.ui_cientifica.apaga.clicked.connect(self.apaga_um)
        self.ui_cientifica.C.clicked.connect(self.apaga_C)

        self.ui_cientifica.raiz.clicked.connect(self.operacoes_avancada)
        self.ui_cientifica.divisao.clicked.connect(self.operacoes_padrao)
        self.ui_cientifica.vezes.clicked.connect(self.operacoes_padrao)
        self.ui_cientifica.menos.clicked.connect(self.operacoes_padrao)
        self.ui_cientifica.mais.clicked.connect(self.operacoes_padrao)
        self.ui_cientifica.igual.clicked.connect(self.igual)
        self.ui_cientifica.sen.clicked.connect(self.operacoes_avancada)
        self.ui_cientifica.cos.clicked.connect(self.operacoes_avancada)
        self.ui_cientifica.tg.clicked.connect(self.operacoes_avancada)
        self.ui_cientifica.pow.clicked.connect(self.pow)

    def apaga_um(self):
        if(self.display_txt == ""):
            pass
        elif self.display_txt[-1].isnumeric():
            self.display_txt = self.display_txt[:-1]
        else:
            while(not self.display_txt[-1].isnumeric()):
                self.display_txt = self.display_txt[:-1]
        self.ui_comum.display.setText(self.display_txt)
        self.ui_cientifica.display.setText(self.display_txt)

    def apaga_C(self):
        self.display_txt = ''
        self.ui_comum.display.setText(self.display_txt)
        self.ui_cientifica.display.setText(self.display_txt)

    def escreve_display(self):
        sender = self.Widgets_Cientifica.sender()
        sender = self.Widgets_Comum.sender()
        if self.display_txt == "":
            self.display_txt = self.display_txt + sender.text()
            self.ui_cientifica.display.setText(self.display_txt)
            self.ui_comum.display.setText(self.display_txt)
        elif self.display_txt[-1] == ")":
            pass
        else:
            self.display_txt = self.display_txt + sender.text()
            self.ui_cientifica.display.setText(self.display_txt)
            self.ui_comum.display.setText(self.display_txt)

    def muda_menu_comum(self):
        self.Widgets_Menu.close()
        self.Widgets_Comum.show()
        self.display_txt = ''
        self.ui_comum.display.setText(self.display_txt)
        self.ui_cientifica.display.setText(self.display_txt)

    def muda_menu_cientifica(self):
        self.Widgets_Menu.close()
        self.Widgets_Cientifica.show()
        self.display_txt = ''
        self.ui_cientifica.display.setText(self.display_txt)
        self.ui_comum.display.setText(self.display_txt)

    def muda_cientifica_menu(self):
        self.Widgets_Menu.show()
        self.Widgets_Cientifica.close()

    def muda_comum_menu(self):
        self.Widgets_Menu.show()
        self.Widgets_Comum.close()

    def virgula(self):

        sender = self.Widgets_Comum.sender().text()
        if sender in self.display_txt:
            pass
        elif(self.display_txt == ''):
            self.display_txt = '0.'

        else:
            self.display_txt =self.display_txt + sender
        self.ui_cientifica.display.setText(self.display_txt)
        self.ui_comum.display.setText(self.display_txt)

    def operacoes_padrao(self):
        sender = self.Widgets_Cientifica.sender()
        sender = self.Widgets_Comum.sender()
        if(self.display_txt[-1].isnumeric()) or self.display_txt[-1] == ")":
            self.display_txt = self.display_txt + sender.text()
            self.ui_cientifica.display.setText(self.display_txt)
            self.ui_comum.display.setText(self.display_txt)
        else:
            pass

    def operacoes_avancada(self):
        sender = self.Widgets_Cientifica.sender()
        sender = self.Widgets_Comum.sender()
        characteres = ("/","*","-","+",")")
        if(self.display_txt == ""):
            pass
        elif(self.display_txt[-1].isnumeric()):
            x = ""
            while (self.display_txt[-1].isnumeric() or self.display_txt[-1] == "."):
                x = x + self.display_txt[-1]
                self.display_txt = self.display_txt[:-1]
                if self.display_txt == "" or self.display_txt in characteres:
                    break
            sender = sender.text()[:-2]
            self.display_txt = self.display_txt + sender + x[::-1] + ")"
            self.ui_cientifica.display.setText(self.display_txt)
            self.ui_comum.display.setText(self.display_txt)
        else:
            pass

    def pow(self):
        sender = self.Widgets_Cientifica.sender()
        sender = self.Widgets_Comum.sender()
        if(self.display_txt == ""):
            pass
        elif(self.display_txt[-1].isnumeric() or self.display_txt[-1] == ")"):
            self.display_txt = self.display_txt + sender.text()
            self.ui_cientifica.display.setText(self.display_txt)
            self.ui_comum.display.setText(self.display_txt)

    def igual(self):
        operacoes = ("sin", "cos", "tan", "sqrt")
        for i in operacoes:
            if i in self.display_txt:
                self.display_txt = self.display_txt.replace(i, "math." + i)
        if self.display_txt[-1].isnumeric() or self.display_txt[-1] == ")":
            self.display_txt = str(eval(self.display_txt))
            self.ui_cientifica.display.setText(self.display_txt)
            self.ui_comum.display.setText(self.display_txt)
        else:
            pass     

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controler = Controler()

    controler.Widgets_Menu.show()
    sys.exit(app.exec_())