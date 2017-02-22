#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton, QHBoxLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt


class Kalkulator(QWidget):
    def __init__(self, parent=None):
        super(Kalkulator, self).__init__(parent)

        self.interfejs()

    def interfejs(self):

        etykieta1 = QLabel("Współczynnik a:")
        etykieta2 = QLabel("Współczynnik b:")
        etykieta3 = QLabel("Współczynnik c:")
        etykieta4 = QLabel("Miejsce zerowe 1:")
        etykieta5 = QLabel("Miejsce zerowe 2:")


        self.a = QLineEdit()
        self.b = QLineEdit()
        self.c = QLineEdit()
        self.x1 = QLineEdit()
        self.x2 = QLineEdit()

        ukladT = QGridLayout()
        ukladT.addWidget(etykieta1, 0, 0)
        ukladT.addWidget(etykieta2, 0, 1)
        ukladT.addWidget(etykieta3, 0, 2)
        ukladT.addWidget(etykieta4, 3, 0)
        ukladT.addWidget(etykieta5, 3, 1)
        ukladT.addWidget(self.a, 1, 0)
        ukladT.addWidget(self.b, 1, 1)
        ukladT.addWidget(self.c, 1, 2)
        ukladT.addWidget(self.x1, 4, 0)
        ukladT.addWidget(self.x2, 4, 1)

        obliczBtn = QPushButton("&Oblicz", self)


        ukladH = QHBoxLayout()
        ukladH.addWidget(obliczBtn)


        ukladT.addLayout(ukladH, 2, 0, 1, 3)

        koniecBtn = QPushButton("&Koniec", self)
        ukladT.addWidget(koniecBtn, 5, 0, 1, 3)

        self.setLayout(ukladT)

        koniecBtn.clicked.connect(self.koniec)
        obliczBtn.clicked.connect(self.dzialanie)

        self.resize(500, 250)
        self.setWindowTitle("Obliczanie miejsc zerowych.")
        self.show()

    def closeEvent(self, event):

        odp = QMessageBox.question(
            self, 'Komunikat',
            "Czy na pewno koniec?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if odp == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def koniec(self):
        self.close()

    def dzialanie(self):
        nadawca = self.sender()
        try:

            a = float(self.a.text())
            b = float(self.b.text())
            c = float(self.c.text())
            delta = (b*b)-4*(a*c)
            print("Delta wynosi: %d" % (delta))


            if nadawca.text() == "&Oblicz":

                if delta>0:
                    pdelta = pow(delta,1/2.0)
                    print("Pierwiastek z delty wynosi: %d" % (pdelta))
                    x1 = (-b-pdelta)/2*a
                    x2 = (-b+pdelta)/2*a
                    print("Delta dodatnia, posiada dwa miejsca zerowe x1 i x2, ktorych wartosci wynosza: %d  i  %d" % (x1,x2))
                elif delta==0:
                    x1=-b/2*a
                    print("Delta wynosi 0, posiada więc ona jedno miejsce zerowe, ktorej wartosc to %d" % (x1))


            self.x1.setText(str(x1))
            self.x2.setText(str(x2))



        except (ValueError, ZeroDivisionError):
            QMessageBox.warning(self, "Błąd", "Błędne dane!", QMessageBox.Ok)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Kalkulator()
    sys.exit(app.exec_())
