#-* coding:utf-8 -*-
"""
    Projet: Gestionaire de mot de passe (GDM-001)
    Nom: GDM-001
    Initié: le 07/03/2022 18h35
    Terminé: le 16/03/2022 23h56
    Crée par: Starkiller
    langage: python3 (version 3.9)
"""
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QTextEdit
import gestion_data 
import gestion_user
import sys

'''Interface graphique
'''

class Menu_1(QWidget):
    def __init__(self):
        super().__init__()
        self.is_login = False
        self.is_singin = False
        self.setGeometry(200,200, 400, 300)
        self.setWindowTitle("Bienvenue")
        self.__creat_button()

    def __creat_button(self):
        button_login = QPushButton("Log in", self)
        button_login.setGeometry(190, 50, 111, 41)
        button_login.move(260, 100)
        button_login.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"Segoe MDL2 Assets\";")
        button_login.clicked.connect(self.login)

        button_singin = QPushButton("Sign in", self)
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

        self.retour_ = QPushButton("Retour", self)
        self.retour_.move(1,260)
        self.retour_.clicked.connect(self.retour)
        self.retour_.setStyleSheet("color: rgb(255, 255, 255);\n"
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

        self.ERREUR = QLabel("Nom déjà utilisé !", self)
        self.ERREUR.move(0, 109)
        self.ERREUR.setStyleSheet("color: rgb(0, 0, 0);\n"
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
        global user
        nom = self.lineEdit_nom.text()
        password = self.lineEdit_password.text()
        self.user = gestion_user.sing_in(nom, password)
        if self.user == False:
            self.lineEdit_nom.clear()
            self.lineEdit_password.clear()
            self.ERREUR.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 14pt \"Sitka Text\";")
        else:
            self.lineEdit_nom.clear()
            self.lineEdit_password.clear()
            user =  self.user
            self.close()
            menu4.show()

    def retour(self):
        self.ERREUR.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 14pt \"Sitka Text\";")
        self.lineEdit_nom.clear()
        self.lineEdit_password.clear()
        self.close()
        menu1.show()
    

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

        self.retour_ = QPushButton("Retour", self)
        self.retour_.move(1,260)
        self.retour_.clicked.connect(self.retour)
        self.retour_.setStyleSheet("color: rgb(255, 255, 255);\n"
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

        self.ERREUR = QLabel("Incorrect !", self)
        self.ERREUR.move(0, 109)
        self.ERREUR.setStyleSheet("color: rgb(0, 0, 0);\n"
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
        global user
        nom = self.lineEdit_nom.text()
        password = self.lineEdit_password.text()
        self.user = gestion_user.login(nom, password)
        if self.user == False:
            self.lineEdit_nom.clear()
            self.lineEdit_password.clear()
            self.ERREUR.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 14pt \"Sitka Text\";")
        else:
            self.lineEdit_nom.clear()
            self.lineEdit_password.clear()
            user =  self.user
            self.close()
            menu4.show()
    
    def retour(self):
        self.ERREUR.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 14pt \"Sitka Text\";")
        self.lineEdit_nom.clear()
        self.lineEdit_password.clear()
        self.close()
        menu1.show()

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
        self.modifier_profile.move(910, 0)
        self.modifier_profile.clicked.connect(self.modifier_profile_)
        self.modifier_profile.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 11pt ;")

        self.deconnexion = QPushButton("déconnexion", self)
        self.deconnexion.move(1070, 0)
        self.deconnexion.clicked.connect(self.deconnect)
        self.deconnexion.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 11pt ;")

        self.oky_caractere = QPushButton("caractère autoriser mdp ", self)
        self.oky_caractere.move(580,0)
        self.oky_caractere.clicked.connect(self.show_char)
        self.oky_caractere.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 11pt ;")

        self.delt_com = QPushButton("supprimer profile", self)
        self.delt_com.move(780, 0)
        self.delt_com.clicked.connect(self.delt_profile)
        self.delt_com.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 11pt ;")


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
        self.affichage.clear()
        all_ = gestion_data.lecture(True, user['master key'], user['id'])
        self.affichage.append("Platforme, Nom, Password, mail")
        for com in all_:
             self.affichage.append(f"{com['platforme']}, {com['nom']}, {com['password']}, {com['mail']}")

    def rechercher(self):
        self.close()
        mode2.show()

    def importation(self):
        self.close()
        mode3.show()

    def delt_all(self):
        self.affichage.clear()
        gestion_data.supprimer(True, user['id'])
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
    
    def deconnect(self):
        self.affichage.clear()
        self.close()
        menu1.show()
    
    def show_char(self):
        self.affichage.clear()
        self.affichage.append("'a', 'b', 'c', 'd', 'e', 'f', 'g',\n 'o', 'p', 'q', 'r', 's', 't', 'u', \n'h', 'i', 'j', 'k', 'l', 'm', 'n', \n'v', 'w', 'x', 'y', 'z', 'A', 'B', \n'C', 'D', 'E', 'F', 'G', 'H', 'I', \n'J', 'K', 'L', 'M', 'N', 'O', 'P', \n'Q', 'R', 'S', 'T', 'U', 'V', 'W', \n'X', 'Y', 'Z', '1', '2', '3', '4', \n'5', '6', '7', '8', '9', '0', ' ', \n'!', '@', '#', '$', '%', '^', '&', \n'*', '(', ')', '/', '-', '_', '\\',\n '{', '}', '|', '`', '°','[', ']', \n'+', '.', '?', ';', ':', '!', '§',\n '¤', '€', '£', '¨', '<',  '>','~',\n '\'', '\"', ',', '=',")
    
    def delt_profile(self):
        self.affichage.clear()
        gestion_user.delt_user(user["nom"], user['id'])
        self.close()
        menu1.show()

class Menu_5(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(700, 500)
        self.setMaximumSize(700, 500)
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

        self.menuprincipal = QPushButton("Menu Principal", self)
        self.menuprincipal.move(475, 0)
        self.menuprincipal.clicked.connect(self.retour)
        self.menuprincipal.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 95, 143);\n"
"font: 14pt ;")

    
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

        self.ERREUR = QLabel("Incorrect !", self)
        self.ERREUR.move(0, 0)
        self.ERREUR.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 14pt \"Sitka Text\";")

        self.consigne = QLabel("Tout les champs doivent\nobligatoirement être remplie.\n(si vous ne souhaiter\npas modifier remplicez avec l'anciene valeur )", self)
        self.consigne.move(100, 300)
        self.consigne.setStyleSheet("color: rgb(163, 47,37);\n"
"font: 14pt \"Sitka Text\";")

    def create_linedit(self):
        self.lineEdit_mot_pass = QLineEdit(self)
        self.lineEdit_mot_pass.move(170, 50)
        self.lineEdit_mot_pass.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n")
        self.lineEdit_nom = QLineEdit(self)
        self.lineEdit_nom.move(170, 100)
        self.lineEdit_nom.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n")

        self.lineEdit_password = QLineEdit(self)
        self.lineEdit_password.move(178, 150)
        self.lineEdit_password.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n")
    
    def confirmer(self):
        global user
        password = self.lineEdit_mot_pass.text()
        new_nom = self.lineEdit_nom.text()
        new_password = self.lineEdit_password.text()
        self.lineEdit_mot_pass.clear()
        self.lineEdit_nom.clear()
        self.lineEdit_password.clear()
        if gestion_user.modifier(user['nom'], password, new_nom=new_nom, new_password=new_password) and len(new_nom) > 0 and len(new_password) > 0:
            user['nom'] = new_nom
            self.close()
            menu4.show()     
        else:
            self.ERREUR.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 14pt \"Sitka Text\";")

    def retour(self):
        self.lineEdit_mot_pass.clear()
        self.lineEdit_nom.clear()
        self.lineEdit_password.clear()   
        self.close()
        menu4.show()

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
"color: rgb(0, 0, 0);\n")

        self.lineEdit_password = QLineEdit(self)
        self.lineEdit_password.setGeometry(770, 150, 151, 31)
        self.lineEdit_password.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n")

        self.lineEdit_mail = QLineEdit(self)
        self.lineEdit_mail.setGeometry(670, 200, 151, 31)
        self.lineEdit_mail.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n")

    def create_textedit(self):
       self.affichage = QTextEdit(self)
       self.affichage.setGeometry(200, 340, 850, 350)
       self.affichage.setStyleSheet("font: 16pt \"Segoe UI Emoji\";\n"
"color: rgb(0, 85, 0);\n"
"background-color: rgb(255, 255, 255);")

    def confirmer(self):
        self.affichage.clear()
        platforme = self.lineEdit_platforme.text()    
        nom = self.lineEdit_nom.text()
        password = self.lineEdit_password.text()
        mail = self.lineEdit_mail.text()
        if len(mail) == 0:
            if gestion_data.save_password(user['id'], platforme, nom, password, user['master key']):
                self.affichage.append("Successfull")
            else:
                self.affichage.append("Erreur:Caractère inconue dans le mot de passe.")
        else:
            if gestion_data.save_password(user['id'], platforme, nom, password, user['master key'], mail):
                self.affichage.append("Successfull")
            else:
                self.affichage.append("Erreur:Caractère inconue dans le mot de passe.")

        self.lineEdit_platforme.clear()
        self.lineEdit_nom.clear()
        self.lineEdit_mail.clear()
        self.lineEdit_password.clear()

    def retour(self):
        self.lineEdit_platforme.clear()
        self.lineEdit_nom.clear()
        self.lineEdit_mail.clear()
        self.lineEdit_password.clear()
        self.affichage.clear()   
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
"color: rgb(0, 0, 0);\n")

    def create_textedit(self):
       self.affichage = QTextEdit(self)
       self.affichage.setGeometry(200, 340, 850, 350)
       self.affichage.setStyleSheet("font: 16pt \"Segoe UI Emoji\";\n"
"color: rgb(0, 85, 0);\n"
"background-color: rgb(255, 255, 255);")

    def confirmer(self):
        self.affichage.clear()
        platforme = self.lineEdit_platforme.text()    
        nom = self.lineEdit_nom.text()
        com = gestion_data.lecture(False, user['master key'], user['id'], nom=nom, platforme=platforme)
        if com == False:
           self.affichage.append("Aucun contenue correspondant .")
        else:
            self.affichage.append("Platforme, Nom, Password, mail")    
            self.affichage.append(f"{com['platforme']}, {com['nom']}, {com['password']}, {com['mail']}")
        self.lineEdit_platforme.clear()
        self.lineEdit_nom.clear()

    def retour(self):
        self.affichage.clear()
        self.lineEdit_platforme.clear()
        self.lineEdit_nom.clear()  
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
"color: rgb(0, 0, 0);\n")

    def create_textedit(self):
       self.affichage = QTextEdit(self)
       self.affichage.setGeometry(200, 340, 850, 350)
       self.affichage.setStyleSheet("font: 16pt \"Segoe UI Emoji\";\n"
"color: rgb(0, 85, 0);\n"
"background-color: rgb(255, 255, 255);")

    def confirmer(self):
        self.affichage.clear()
        fichier = self.lineEdit_fichier.text()
        if (fichier.split('.'))[-1] != 'csv' or not '.' in list(fichier):
            self.affichage.append("le fichier doit obligatoirement être de type csv  et non vide !" )    
        elif gestion_data.importation(fichier, user['master key'], user['id']):
            self.affichage.append("Successfull") 
        else:
            self.affichage.append("Votre fichier ne contient pas les en-têtes 'platforme', 'nom', 'password', 'mail\nOu bien certains des mots de passe contient des caractère inconnues")

        self.lineEdit_fichier.clear()

    def retour(self):
        self.lineEdit_fichier.clear()
        self.affichage.clear()   
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
"color: rgb(0, 0, 0);\n")

    def create_textedit(self):
       self.affichage = QTextEdit(self)
       self.affichage.setGeometry(200, 340, 850, 350)
       self.affichage.setStyleSheet("font: 16pt \"Segoe UI Emoji\";\n"
"color: rgb(0, 85, 0);\n"
"background-color: rgb(255, 255, 255);")

    def confirmer(self):
        self.affichage.clear()
        platforme = self.lineEdit_platforme.text()    
        nom = self.lineEdit_nom.text()
        gestion_data.supprimer(False, user["id"], platforme, nom)
        self.affichage.append("Successfull")
        self.lineEdit_platforme.clear()
        self.lineEdit_nom.clear()

    def retour(self):
        self.affichage.clear()
        self.lineEdit_platforme.clear()
        self.lineEdit_nom.clear()   
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

        self.consigne = QLabel("Tout les champs doivent\nobligatoirement être remplie.\n(si vous ne souhaiter\npas modifier remplicez avec l'anciene valeur )", self)
        self.consigne.move(100, 200)
        self.consigne.setStyleSheet("color: rgb(163, 47,37);\n"
"font: 14pt \"Sitka Text\";")


    def create_lineEdit(self):
        self.lineEdit_platforme = QLineEdit(self)
        self.lineEdit_platforme.setGeometry(770, 50, 151, 31)
        self.lineEdit_platforme.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n")

        self.lineEdit_nom = QLineEdit(self)
        self.lineEdit_nom.setGeometry(670, 100, 151, 31)
        self.lineEdit_nom.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n")

        self.lineEdit_new_nom = QLineEdit(self)
        self.lineEdit_new_nom.setGeometry(670, 200, 151, 31)
        self.lineEdit_new_nom.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n")

        self.lineEdit_new_password = QLineEdit(self)
        self.lineEdit_new_password.setGeometry(670, 250, 151, 31)
        self.lineEdit_new_password.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n")

    def create_textedit(self):
       self.affichage = QTextEdit(self)
       self.affichage.setGeometry(200, 340, 850, 350)
       self.affichage.setStyleSheet("font: 16pt \"Segoe UI Emoji\";\n"
"color: rgb(0, 85, 0);\n"
"background-color: rgb(255, 255, 255);")

    def confirmer(self):
        self.affichage.clear()
        platforme = self.lineEdit_platforme.text()    
        nom = self.lineEdit_nom.text()        
        new_nom = self.lineEdit_new_nom.text()
        new_password = self.lineEdit_new_password.text()
        if len(new_nom) > 0 and len(new_password) > 0:
            if gestion_data.modifier(platforme, nom, user['id'], user['master key'], new_nom, new_password): 
                self.affichage.append("Successfull")
            else:
                self.affichage.append("Erreur:Caractère inconue dans le mot de passe.")
        else:
            self.affichage.append("Incorect")

        self.lineEdit_new_nom.clear()
        self.lineEdit_new_password.clear()
        self.lineEdit_platforme.clear()
        self.lineEdit_nom.clear()

    
    def retour(self):
        self.lineEdit_new_nom.clear()
        self.lineEdit_new_password.clear()
        self.lineEdit_platforme.clear()
        self.lineEdit_nom.clear()
        self.affichage.clear()  
        self.close()
        menu4.show()


if __name__ == '__main__':
    user:dict = {}
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
