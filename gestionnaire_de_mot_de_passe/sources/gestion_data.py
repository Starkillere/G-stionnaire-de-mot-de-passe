#-*- coding:utf-8 -*-

import csv
import sqlite3
from codage_maoua import CodageMoua

def save_password(platforme:str, nom:str, password:str,  master_key:str, mail=None, database='databaose.db') -> bool:
    assert type(platforme) == str
    assert type(password) == str
    assert type(nom) == str
    assert type(master_key) == str
    assert type(mail) == str or mail == None
    assert type(database) == str and (database.split('.'))[-1] == 'db'
    my_pass = CodageMoua(master_key)
    chiffre_password =  my_pass.encode(password)
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        requete = "insert into gestionnaire (platforme, nom, password, mail) values ('{platforme}', '{nom}', '{chiffre_password}, '{mail}')".format(platforme=platforme, nom=nom, chiffre_password=chiffre_password, mail=mail)
        cursor.execute(requete)     
        connection.commit()
    return True

def lecture(return_all:bool, master_key:str, database='databaose.db', nom=None, platforme=None):
    assert type(master_key) == str
    assert type(return_all) == bool
    def get_nom(contact):
        return contact[1]
    requete = 'select * from gestionnaire'
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        if return_all:
            password = cursor.execute(requete)
            password = list(password)
            password.sort(key=get_nom)
            my_pass = CodageMoua(master_key)
            lise_password = []
            for i in password:
                dictc = {}
                dictc['platforme'] = i[1]
                dictc['nom'] = i[2]
                dictc['password'] = my_pass.decode(i[3])
                dictc['mail'] = i[4]
                lise_password.append(dictc)
            return lise_password
        else:
            assert type(nom) == str
            assert type(platforme) == str
            passwords = cursor.execute(requete)
            my_pass = CodageMoua(master_key)
            for password in passwords:
                if password[1] == platforme and password[2] == nom:
                    dictc = {'platforme': password[1], 'nom': password[2], 'password': my_pass.decode(password[3]), 'mail': password[4]}
                    return dictc
            else:
                return False

def importation(fichier_user:str, master_key:str, database='databaose.db') -> bool:
    assert type(fichier_user) == str and (fichier_user.split('.'))[-1] == 'csv'
    assert type(database) == str and (database.split('.'))[-1] == 'db'
    assert type( master_key) == str
    with open(fichier_user, 'r', encoding='utf-8') as fichier:
        passwords = [dict(contact) for contact in csv.DictReader(fichier)]
    if list(passwords[0].keys()) == ['platforme', 'nom', 'password', 'mail']:
        with sqlite3.connect(database) as connection:
            cursor = connection.cursor()
            my_pass = CodageMoua(master_key)
            for password in passwords:
                requete = "insert into gestionnaire (platforme, nom, password, mail) values ('{platforme}', '{nom}', '{chiffre_password}, '{mail}')".format(platforme=password['platforme'], nom=password['nom'], chiffre_password=my_pass.decode(password['chiffre_password']), mail=password['mail'])
                cursor.execute(requete)
                connection.commit()
    else:
       return False
    return True

def supprimer(delt_all:bool, platforme=None, nom=None, database='databaose.db') -> bool:
    assert type(delt_all) == bool
    assert type(database) == str and (database.split('.'))[-1] == 'db'
    if delt_all:
        with sqlite3.connect(database) as connection:
            cursor = connection.cursor()
            requete = 'TRUNCATE TABLE gestionnaire'
            cursor.execute(requete)
            connection.commit()
    else:
        assert type(platforme) == str
        assert type(nom) == str
        with sqlite3.connect(database) as connection:
            cursor = connection.cursor()
            requete = f'DELETE FROM gestionnaire WHERE nom = "{nom}" AND platforme = "{platforme}"'
            cursor.execute(requete)
            connection.commit()
    return True

def modifier(platforme:str, nom:str, database='databaose.db', master_key=None, new_nom=None, new_password=None) -> bool :
    assert type(platforme) == str
    assert type(nom) == str
    assert type(new_nom) == str or new_nom == None
    assert type(new_password) == str or new_password == None
    assert type(master_key) == str or master_key == None
    assert type(database) == str and (database.split('.'))[-1] == 'db'
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        if new_nom != None:
            requete = f"UPDATE gestionnaire SET nom = '{new_nom}' WHERE nom = '{nom}' AND platforme = '{platforme}'"
        if new_password != None:
            my_pass = CodageMoua(master_key)
            requete = f"UPDATE gestionnaire SET password = '{my_pass.encode(new_password)}' WHERE nom = '{nom}' AND platforme = '{platforme}'"
        cursor.execute(requete)
        connection.commit()
    return True

if __name__ == '__main__':
    pass