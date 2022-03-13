#-*- coding:utf-8 -*-

"""
-------------------------------------
Projet: Gestionnaire de mot de passe #
-------------------------------------
crée par: Starkiller
initié le : 14/03/2022
"""

from PyQt5.QtWidgets import QApplication, QWidget

import sys

app = QApplication.instance() 
if not app:
    app = QApplication(sys.argv)

fen1 = QWidget()
fen1.setWindowTitle("Fenetre 1")
fen1.resize(500,250)
fen1.move(300,50)
fen1.show()

fen2 = QWidget()
fen2.setWindowTitle("Fenetre 2")
fen2.resize(400,300)
fen2.move(200,150)
fen2.show()

app.exec_()