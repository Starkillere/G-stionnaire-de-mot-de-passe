#-* coding:utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QTextEdit
import gestion_data
import gestion_master_key
import gestion_user
import sys

#menu principal (login or singin)
class Menu_1(QWidget):
    def __init__(self):
        super().__init__()
        self.is_login = False
        self.is_singin = False
        self.setGeometry(200,200, 400, 300)
        self.setWindowTitle("Bienvenue")
        self.__creat_button()

    def __creat_button(self):
        button_login = QPushButton("Login", self)
        button_login.setGeometry(190, 50, 111, 41)
        button_login.move(260, 100)
        button_login.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"Segoe MDL2 Assets\";")
        button_login.clicked.connect(self.login)

        button_singin = QPushButton("Singin", self)
        button_singin.setGeometry(190, 50, 111, 41)
        button_singin.move(10, 100)
        button_singin.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"Segoe MDL2 Assets\";")
        button_singin.clicked.connect(self.singin)
    
    def login(self):
        self.is_login = True
        self.close()

    def singin(self):
        self.is_singin = True
        self.close()

#Menu singin
class Menu_2(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(400, 300)
        self.setMaximumSize(400, 300)
        self.setWindowTitle("Crée un compte")
        self.setStyleSheet("background-color: rgb(4, 3, 3);")
        self.create_button()
        self.create_label()
        self.create_linedit()

    def create_button(self):
        self.bouton_confirmer = QPushButton("confirmer", self)
        self.bouton_confirmer.move(200, 200)
        self.bouton_confirmer.clicked.connect(self.confirmer)
        self.bouton_confirmer.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 14pt \"Segoe Script\";")
    
    def create_label(self):
        self.label_nom = QLabel("Nom : ", self)
        self.label_nom.setGeometry(350, 10, 61, 31)
        self.label_nom.move(0, 0)
        self.label_nom.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Sitka Text\";")

        self.label_password = QLabel("Mot de passe : ", self)
        self.label_password.move(0, 59)
        self.label_password.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Sitka Text\";")

    def create_linedit(self):
        self.lineEdit_nom = QLineEdit(self)
        self.lineEdit_nom.setGeometry(440, 9, 151, 31)
        self.lineEdit_nom.move(59, 0)
        self.lineEdit_nom.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n")

        self.lineEdit_password = QLineEdit(self)
        self.lineEdit_password.setGeometry(440, 9, 151, 31)
        self.lineEdit_password.move(150, 59)
        self.lineEdit_password.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n")
    
    def confirmer(self):
        nom = self.lineEdit_nom.text()
        password = self.lineEdit_password.text()
        self.master_key = gestion_user.sing_in(nom, password)
        self.close()

class Menu_3(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(400, 300)
        self.setMaximumSize(400, 300)
        self.setWindowTitle("Crée un compte")
        self.setStyleSheet("background-color: rgb(4, 3, 3);")
        self.create_button()
        self.create_label()
        self.create_linedit()

    def create_button(self):
        self.bouton_confirmer = QPushButton("confirmer", self)
        self.bouton_confirmer.move(200, 200)
        self.bouton_confirmer.clicked.connect(self.confirmer)
        self.bouton_confirmer.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 14pt \"Segoe Script\";")
    
    def create_label(self):
        self.label_nom = QLabel("Nom : ", self)
        self.label_nom.setGeometry(350, 10, 61, 31)
        self.label_nom.move(0, 0)
        self.label_nom.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Sitka Text\";")

        self.label_password = QLabel("Mot de passe : ", self)
        self.label_password.move(0, 59)
        self.label_password.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Sitka Text\";")

    def create_linedit(self):
        self.lineEdit_nom = QLineEdit(self)
        self.lineEdit_nom.setGeometry(440, 9, 151, 31)
        self.lineEdit_nom.move(59, 0)
        self.lineEdit_nom.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n")

        self.lineEdit_password = QLineEdit(self)
        self.lineEdit_password.setGeometry(440, 9, 151, 31)
        self.lineEdit_password.move(150, 59)
        self.lineEdit_password.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n")
    
    def confirmer(self):
        nom = self.lineEdit_nom.text()
        password = self.lineEdit_password.text()
        self.master_key = gestion_user.login(nom, password)
        self.close()

class Menu_4(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1200, 700)
        self.setMaximumSize(1200, 700)
        self.setWindowTitle("Menu Principal")
        self.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.create_button()
        self.create_label()
        self.create_linedit()
        self.create_textedit()

    def create_button(self):
        self.button_nouveau = QPushButton("Nouveau mot de passe", self)
        self.button_nouveau.move(50, 50)
        #self.button_nouveau.clicked.connect()
        self.button_nouveau.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 14pt ;")

        self.afficher_all = QPushButton("Afficher tout les mots de passe", self)
        self.afficher_all.move(50, 100)
        #selfafficher_all.clicked.connect()
        self.afficher_all.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 14pt ;")

        self.trouver = QPushButton("Trouver un mot de passe", self)
        self.trouver.move(50, 150)
        #selftrouver.clicked.connect()
        self.trouver.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 14pt ;")

        self.importa = QPushButton("Importer des mots de passe", self)
        self.importa.move(50, 200)
        #selfimporta.clicked.connect()
        self.importa.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 14pt ;")

        self.tout_supprimer = QPushButton("Tout supprimer", self)
        self.tout_supprimer.move(50, 250)
        #selftout_supprimer.clicked.connect()
        self.tout_supprimer.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 14pt ;")

        self.modifier = QPushButton("modifier", self)
        self.modifier.move(50, 300)
        #selfmodifier.clicked.connect()
        self.modifier.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 14pt ;")

        self.confirmer = QPushButton("Confirmer", self)
        self.confirmer.move(777, 300)
        #selfconfirmer.clicked.connect()
        self.confirmer.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 14pt ;")

        self.modifier_profile = QPushButton("modifier profile", self)
        self.modifier_profile.move(1000, 0)
        #selfmodifier_profile.clicked.connect()
        self.modifier_profile.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 14pt ;")

    def create_label(self):
        self.label_platforme = QLabel("Platforme : ", self)
        self.label_platforme.move(600, 50)
        self.label_platforme.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: 14pt \"Sitka Text\";")

        self.label_nom = QLabel("nom : ", self)
        self.label_nom.move(600, 100)
        self.label_nom.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Sitka Text\";")

        self.label_password = QLabel("Le mot de passe : ", self)
        self.label_password.move(600, 150)
        self.label_password.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Sitka Text\";")

        self.label_mail = QLabel("mail : ", self)
        self.label_mail.move(600, 200)
        self.label_mail.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Sitka Text\";")

        self.label_fichier = QLabel("fichier : ", self)
        self.label_fichier.move(600, 250)
        self.label_fichier.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Sitka Text\";")

    def create_linedit(self):
        self.lineEdit_platforme = QLineEdit(self)
        self.lineEdit_platforme.setGeometry(770, 50, 151, 31)
        self.lineEdit_platforme.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n")

        self.lineEdit_nom = QLineEdit(self)
        self.lineEdit_nom.setGeometry(670, 100, 151, 31)
        self.lineEdit_nom.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n")

        self.lineEdit_password = QLineEdit(self)
        self.lineEdit_password.setGeometry(770, 150, 151, 31)
        self.lineEdit_password.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n")

        self.lineEdit_mail = QLineEdit(self)
        self.lineEdit_mail.setGeometry(670, 200, 151, 31)
        self.lineEdit_mail.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n")

        self.lineEdit_fichier = QLineEdit(self)
        self.lineEdit_fichier.setGeometry(670, 250, 151, 31)
        self.lineEdit_fichier.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n")

    def create_textedit(self):
        self.affichage = QTextEdit(self)
        self.affichage.setGeometry(200, 340, 850, 350)
        self.affichage.setStyleSheet("font: 16pt \"Segoe UI Emoji\";\n"
"color: rgb(0, 85, 0);\n"
"background-color: rgb(0, 0, 0);")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    menu1 = Menu_1()
    menu1.show()
    app.exec_()
    if menu1.is_login:
        menu3 = Menu_3()
        while not menu3.master_key:
           menu3.show()
           app.exec_()
        master_key = menu3.master_key
    elif menu1.is_singin: 
        menu2 = Menu_2()
        menu2.show()
        app.exec_()
        master_key = menu2.master_key 
          
    app = QApplication(sys.argv)
    menu = Menu_4()
    menu.show()
    app.exec_()