#-* coding:utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QTextEdit
import gestion_data 
import gestion_user
import sys

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
        menu3.show()

    def singin(self):
        self.is_singin = True
        self.close()
        menu2.show()

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
        global master_key
        nom = self.lineEdit_nom.text()
        password = self.lineEdit_password.text()
        self.master_key = gestion_user.sing_in(nom, password)
        master_key =  self.master_key
        self.close()
        menu4.show()

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
        global master_key
        nom = self.lineEdit_nom.text()
        password = self.lineEdit_password.text()
        self.master_key = gestion_user.login(nom, password)
        if self.master_key == False:
                self.lineEdit_nom.clear()
                self.lineEdit_password.clear()
        else:
                master_key =  self.master_key
                self.close()
                menu4.show()

class Menu_4(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1200, 700)
        self.setMaximumSize(1200, 700)
        self.setWindowTitle("Menu Principal")
        self.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.create_button()
        self.create_textedit()

    def create_button(self):
        self.button_nouveau = QPushButton("Nouveau mot de passe", self)
        self.button_nouveau.move(50, 50)
        self.button_nouveau.clicked.connect(self.senregistre)
        self.button_nouveau.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 14pt ;")

        self.afficher_all = QPushButton("Afficher tout les mots de passe", self)
        self.afficher_all.move(50, 100)
        self.afficher_all.clicked.connect(self.afficher_tout)
        self.afficher_all.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 14pt ;")

        self.trouver = QPushButton("Trouver un mot de passe", self)
        self.trouver.move(50, 150)
        self.trouver.clicked.connect(self.rechercher)
        self.trouver.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 14pt ;")

        self.importa = QPushButton("Importer des mots de passe", self)
        self.importa.move(50, 200)
        self.importa.clicked.connect(self.importation)
        self.importa.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 14pt ;")

        self.tout_supprimer = QPushButton("Tout supprimer", self)
        self.tout_supprimer.move(50, 250)
        self.tout_supprimer.clicked.connect(self.delt_all)
        self.tout_supprimer.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 14pt ;")

        self.supprimer = QPushButton("supprimer un mot de  passe", self)
        self.supprimer.move(50, 300)
        self.supprimer.clicked.connect(self.delt)
        self.supprimer.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 14pt ;")

        self.supprimer = QPushButton("modifier", self)
        self.supprimer.move(50, 350)
        self.supprimer.clicked.connect(self.modifier_)
        self.supprimer.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 14pt ;")

        self.modifier_profile = QPushButton("modifier profile", self)
        self.modifier_profile.move(1000, 0)
        self.modifier_profile.clicked.connect(self.modifier_profile_)
        self.modifier_profile.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 14pt ;")

    def create_textedit(self):
        self.affichage = QTextEdit(self)
        self.affichage.setGeometry(200, 340, 850, 350)
        self.affichage.setStyleSheet("font: 16pt \"Segoe UI Emoji\";\n"
"color: rgb(0, 85, 0);\n"
"background-color: rgb(0, 0, 0);")

    def senregistre(self):
        self.close()
        mode1.show()

    def afficher_tout(self):
        all_ = gestion_data.lecture(True, master_key)
        self.affichage.append("Platforme, Nom, Passmard, mail")
        for com in all_:
             self.affichage.append(f"{com['platforme']}, {com['nom']}, {com['password']}, {com['mail']}")

    def rechercher(self):
        self.close()
        mode2.show()

    def importation(self):
        self.close()
        mode3.show()

    def delt_all(self):
        gestion_data.supprimer(True)
        self.affichage.append("Successfull")  

    def delt(self):
        self.close()
        mode4.show()

    def modifier_(self):    
        self.close()
        mode5.show()

    def modifier_profile_(self):
        self.close()
        menu5.show()

class Menu_5(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(400, 300)
        self.setMaximumSize(400, 300)
        self.setWindowTitle("Modifir profile")
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
        self.label_mot_pass = QLabel("Mot de passe : ", self)
        self.label_mot_pass.move(0, 50)
        self.label_mot_pass.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Sitka Text\";")

        self.label_nom = QLabel("new Nom : ", self)
        self.label_nom.move(0, 100)
        self.label_nom.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Sitka Text\";")

        self.label_password = QLabel(" new Mot de passe : ", self)
        self.label_password.move(0, 150)
        self.label_password.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Sitka Text\";")

    def create_linedit(self):
        self.lineEdit_mot_pass = QLineEdit(self)
        self.lineEdit_mot_pass.move(170, 50)
        self.lineEdit_mot_pass.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n")
        self.lineEdit_nom = QLineEdit(self)
        self.lineEdit_nom.move(170, 100)
        self.lineEdit_nom.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n")

        self.lineEdit_password = QLineEdit(self)
        self.lineEdit_password.move(178, 150)
        self.lineEdit_password.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n")
    
    def confirmer(self):
        password = self.lineEdit_mot_pass.text()
        new_nom = self.lineEdit_nom.text()
        new_password = self.lineEdit_password.text()
        self.lineEdit_mot_pass.clear()
        self.lineEdit_nom.clear()
        self.lineEdit_password.clear()
        if gestion_user.modifier(password, new_nom=new_nom, new_password=new_password):
                self.close()
                menu4.show()     
        else:
                self.labele_error = QLabel("Erreur: verifier vos sasies", self)
                self.labele_error.setGeometry(200, 250, 61, 31)
                self.labele_error.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 14pt \"Sitka Text\";")

class  EnregistrementPassword(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1200, 700)
        self.setMaximumSize(1200, 700)
        self.setWindowTitle("Nouveau mot de passe")
        self.create_button()
        self.create_textedit()
        self.create_label()
        self.create_lineEdit()

    def  create_button(self):
        self.confirmer_ = QPushButton("Confirmer", self)
        self.confirmer_.move(777, 300)
        self.confirmer_.clicked.connect(self.confirmer)
        self.confirmer_.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 14pt ;")

        self.menuprincipal = QPushButton("Menu Principal", self)
        self.menuprincipal.move(1000, 0)
        self.menuprincipal.clicked.connect(self.retour)
        self.menuprincipal.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 14pt ;")

    def create_label(self):
        self.label_platforme = QLabel("Platforme : ", self)
        self.label_platforme.move(600, 50)
        self.label_platforme.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 14pt \"Sitka Text\";")

        self.label_nom = QLabel("nom : ", self)
        self.label_nom.move(600, 100)
        self.label_nom.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 14pt \"Sitka Text\";")

        self.label_password = QLabel("Le mot de passe : ", self)
        self.label_password.move(600, 150)
        self.label_password.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 14pt \"Sitka Text\";")

        self.label_mail = QLabel("mail : ", self)
        self.label_mail.move(600, 200)
        self.label_mail.setStyleSheet("color: rgb(0, 255, 0);\n"
"font: 14pt \"Sitka Text\";")

    def create_lineEdit(self):
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

    def create_textedit(self):
       self.affichage = QTextEdit(self)
       self.affichage.setGeometry(200, 340, 850, 350)
       self.affichage.setStyleSheet("font: 16pt \"Segoe UI Emoji\";\n"
"color: rgb(0, 85, 0);\n"
"background-color: rgb(0, 0, 0);")

    def confirmer(self):
        self.affichage.clear()
        platforme = self.lineEdit_platforme.text()    
        nom = self.lineEdit_nom.text()
        password = self.label_password.text()
        mail = self.lineEdit_mail.text()
        if len(mail) == 0:
            gestion_data.save_password(platforme, nom, password, master_key)
            self.affichage.append("Successfull")
        else:
            gestion_data.save_password(platforme, nom, password, master_key, mail)
            self.affichage.append("Successfull")

        self.lineEdit_platforme.clear()
        self.lineEdit_nom.clear()
        self.lineEdit_mail.clear()
        self.lineEdit_password.clear()

    def retour(self):   
        self.close()
        menu4.show()

class Rechercher(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1200, 700)
        self.setMaximumSize(1200, 700)
        self.setWindowTitle("Recherche")
        self.create_button()
        self.create_textedit()
        self.create_label()
        self.create_lineEdit()

    def  create_button(self):
        self.confirmer_ = QPushButton("Confirmer", self)
        self.confirmer_.move(777, 300)
        self.confirmer_.clicked.connect(self.confirmer)
        self.confirmer_.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 14pt ;")

        self.menuprincipal = QPushButton("Menu Principal", self)
        self.menuprincipal.move(1000, 0)
        self.menuprincipal.clicked.connect(self.retour)
        self.menuprincipal.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 14pt ;")

    def create_label(self):
        self.label_platforme = QLabel("Platforme : ", self)
        self.label_platforme.move(600, 50)
        self.label_platforme.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 14pt \"Sitka Text\";")

        self.label_nom = QLabel("nom : ", self)
        self.label_nom.move(600, 100)
        self.label_nom.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 14pt \"Sitka Text\";")

    def create_lineEdit(self):
        self.lineEdit_platforme = QLineEdit(self)
        self.lineEdit_platforme.setGeometry(770, 50, 151, 31)
        self.lineEdit_platforme.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n")

        self.lineEdit_nom = QLineEdit(self)
        self.lineEdit_nom.setGeometry(670, 100, 151, 31)
        self.lineEdit_nom.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n")

    def create_textedit(self):
       self.affichage = QTextEdit(self)
       self.affichage.setGeometry(200, 340, 850, 350)
       self.affichage.setStyleSheet("font: 16pt \"Segoe UI Emoji\";\n"
"color: rgb(0, 85, 0);\n"
"background-color: rgb(0, 0, 0);")

    def confirmer(self):
        self.affichage.clear()
        platforme = self.lineEdit_platforme.text()    
        nom = self.lineEdit_nom.text()
        com = gestion_data.lecture(False, master_key, nom=nom, platforme=platforme)
        if com == False:
           self.affichage.append("Aucun contenue correspondant .")
        else:
            self.affichage.append("Platforme, Nom, Passmard, mail")    
            self.affichage.append(f"{com['platforme']}, {com['nom']}, {com['password']}, {com['mail']}")
        self.lineEdit_platforme.clear()
        self.lineEdit_nom.clear()
    def retour(self):   
        self.close()
        menu4.show()

class Importation(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1200, 700)
        self.setMaximumSize(1200, 700)
        self.setWindowTitle("importer")
        self.create_button()
        self.create_textedit()
        self.create_label()
        self.create_lineEdit()

    def  create_button(self):
        self.confirmer_ = QPushButton("Confirmer", self)
        self.confirmer_.move(777, 300)
        self.confirmer_.clicked.connect(self.confirmer)
        self.confirmer_.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 14pt ;")

        self.menuprincipal = QPushButton("Menu Principal", self)
        self.menuprincipal.move(1000, 0)
        self.menuprincipal.clicked.connect(self.retour)
        self.menuprincipal.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 14pt ;")

    def create_label(self):
        self.label_fichier = QLabel("fichier : ", self)
        self.label_fichier.move(600, 250)
        self.label_fichier.setStyleSheet("color: rgb(255, 0, 255);\n"
"font: 14pt \"Sitka Text\";")

    def create_lineEdit(self):
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

    def confirmer(self):
        self.affichage.clear()
        fichier = self.lineEdit_fichier.text()
        if (fichier.split('.'))[-1] != 'csv':
            self.affichage.append("le fichier doit obligatoirement être de type csv !" )    
        if gestion_data.importation(fichier, master_key):
            self.affichage.append("Successfull") 
        else:
            self.affichage.append("Votre fichier ne contient pas les en-têtes 'platforme', 'nom', 'password', 'mail")

        self.lineEdit_fichier.clear()

    def retour(self):   
        self.close()
        menu4.show()

class Delte(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1200, 700)
        self.setMaximumSize(1200, 700)
        self.setWindowTitle("Delte")
        self.create_button()
        self.create_textedit()
        self.create_label()
        self.create_lineEdit()

    def  create_button(self):
        self.confirmer_ = QPushButton("Confirmer", self)
        self.confirmer_.move(777, 300)
        self.confirmer_.clicked.connect(self.confirmer)
        self.confirmer_.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 14pt ;")

        self.menuprincipal = QPushButton("Menu Principal", self)
        self.menuprincipal.move(1000, 0)
        self.menuprincipal.clicked.connect(self.retour)
        self.menuprincipal.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 14pt ;")

    def create_label(self):
        self.label_platforme = QLabel("Platforme : ", self)
        self.label_platforme.move(600, 50)
        self.label_platforme.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 14pt \"Sitka Text\";")

        self.label_nom = QLabel("nom : ", self)
        self.label_nom.move(600, 100)
        self.label_nom.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 14pt \"Sitka Text\";")

    def create_lineEdit(self):
        self.lineEdit_platforme = QLineEdit(self)
        self.lineEdit_platforme.setGeometry(770, 50, 151, 31)
        self.lineEdit_platforme.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n")

        self.lineEdit_nom = QLineEdit(self)
        self.lineEdit_nom.setGeometry(670, 100, 151, 31)
        self.lineEdit_nom.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n")

    def create_textedit(self):
       self.affichage = QTextEdit(self)
       self.affichage.setGeometry(200, 340, 850, 350)
       self.affichage.setStyleSheet("font: 16pt \"Segoe UI Emoji\";\n"
"color: rgb(0, 85, 0);\n"
"background-color: rgb(0, 0, 0);")

    def confirmer(self):
        self.affichage.clear()
        platforme = self.lineEdit_platforme.text()    
        nom = self.lineEdit_nom.text()
        gestion_data.supprimer(False, platforme, nom)
        self.affichage.append("Successfull")
        self.lineEdit_platforme.clear()
        self.lineEdit_nom.clear()

    def retour(self):   
        self.close()
        menu4.show()

class Modifier(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1200, 700)
        self.setMaximumSize(1200, 700)
        self.setWindowTitle("Modifier")
        self.create_button()
        self.create_textedit()
        self.create_label()
        self.create_lineEdit()

    def  create_button(self):
        self.confirmer_ = QPushButton("Confirmer", self)
        self.confirmer_.move(777, 300)
        self.confirmer_.clicked.connect(self.confirmer)
        self.confirmer_.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 14pt ;")

        self.menuprincipal = QPushButton("Menu Principal", self)
        self.menuprincipal.move(1000, 0)
        self.menuprincipal.clicked.connect(self.retour)
        self.menuprincipal.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 14pt ;")

    def create_label(self):
        self.label_platforme = QLabel("Platforme : ", self)
        self.label_platforme.move(600, 50)
        self.label_platforme.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 14pt \"Sitka Text\";")

        self.label_nom = QLabel("nom : ", self)
        self.label_nom.move(600, 100)
        self.label_nom.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 14pt \"Sitka Text\";")

        self.label_new_nom = QLabel("new nom : ", self)
        self.label_new_nom.move(510, 200)
        self.label_new_nom.setStyleSheet("color: rgb(0, 255, 255);\n"
"font: 14pt \"Sitka Text\";")

        self.label_new_password = QLabel("new mot de passe : ", self)
        self.label_new_password.move(510, 250)
        self.label_new_password.setStyleSheet("color: rgb(0, 255, 255);\n"
"font: 14pt \"Sitka Text\";")

    def create_lineEdit(self):
        self.lineEdit_platforme = QLineEdit(self)
        self.lineEdit_platforme.setGeometry(770, 50, 151, 31)
        self.lineEdit_platforme.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n")

        self.lineEdit_nom = QLineEdit(self)
        self.lineEdit_nom.setGeometry(670, 100, 151, 31)
        self.lineEdit_nom.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n")

        self.lineEdit_new_nom = QLineEdit(self)
        self.lineEdit_new_nom.setGeometry(670, 200, 151, 31)
        self.lineEdit_new_nom.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n")

        self.lineEdit_new_password = QLineEdit(self)
        self.lineEdit_new_password.setGeometry(670, 250, 151, 31)
        self.lineEdit_new_password.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n")

    def create_textedit(self):
       self.affichage = QTextEdit(self)
       self.affichage.setGeometry(200, 340, 850, 350)
       self.affichage.setStyleSheet("font: 16pt \"Segoe UI Emoji\";\n"
"color: rgb(0, 85, 0);\n"
"background-color: rgb(0, 0, 0);")

    def confirmer(self):
        self.affichage.clear()
        platforme = self.lineEdit_platforme.text()    
        nom = self.lineEdit_nom.text()        
        new_nom = self.lineEdit_new_nom.text()
        new_password = self.lineEdit_new_password.text()
        if len(new_password) != 0:
            gestion_data.modifier(platforme, nom, master_key=master_key, new_password=new_password) 
        if len(new_nom) != 0:
            gestion_data.modifier(platforme, nom, master_key=master_key, new_nom=new_nom)
        self.affichage.append("Successfull")

        self.lineEdit_new_nom.clear()
        self.lineEdit_new_password.clear()
        self.lineEdit_platforme.clear()
        self.lineEdit_nom.clear()

    
    def retour(self):   
        self.close()
        menu4.show()



if __name__ == '__main__':
    master_key = ''    
    app = QApplication(sys.argv)
    menu1 = Menu_1()
    menu3 = Menu_3() 
    menu2 = Menu_2()
    menu4 = Menu_4()
    menu5 = Menu_5()
    mode1 = EnregistrementPassword()
    mode2 = Rechercher()
    mode3 = Importation()
    mode4 = Delte()
    mode5 = Modifier()
    menu1.show()
    app.exec_()