# -*- coding:utf-8 -*-

"""
Description:
------------
    Destion de l'utilisateurs (enregistrement, authentification)

Cahier des charges: 
------------------
    Enregistrement (sing_in):
        Description:
            Création du compte de l'utilisateur nom, mot de passe.
        Etapes:
            - Le nom, et le mot de passe de l'utilisateur sont demandé.
            - Le nom de l'utilisateur est enregistré dans un fichier txt (user.txt).
              Le nom est enregistré tout en majuscule prefixé de Nom = .
            - Le mot de passe doit être hasher pui enregistre dans un fichier txt (user.txt).
              Le mot de passe est enrgistré sous ça forme hasher préfixé de Password =  .

    Connection (login):
        Description:
            Connection de l'utilisateur nom, mot de passe.
        Etapes:
            - Le nom, et le mot de passe de l'utilisateur sont demandé.
            - Le nom cet comparer au nom les deux non doivent être tout en majuscule
            - le hasher du mot de passe est comparé au mot de passe sauvegarder.
    Modifier (modifier):
        En attente
        ###Revoire si possible###
"""
import hashlib
from codage_mawa import CodageMawa
import gestion_data
import sqlite3

def sing_in(nom:str, master_password:str, database='database.db') -> str:
    """
        *** sing_in
    """
    assert type(nom) == str
    assert type(master_password) == str
    assert type(database) == str and (database.split('.'))[-1] == 'db'
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        requete = "select * from user WHERE nom = '{}'".format(nom)
        cursor.execute(requete)
        user = cursor.fetchone()
    if user == None:
        master_key = CodageMawa('None').master_key_genrator()
        hash_master_password = hashlib.sha1(master_password.encode()).hexdigest()
        if len(master_key) > len(master_password):
            for i in range(len(master_key)-len(master_password)):
                master_password += master_password[:(len(master_key)-len(master_password))]
        my_pass = CodageMawa(master_password)
        chiffre_master_key = my_pass.encode(master_key)
        with sqlite3.connect(database) as connection:
            cursor = connection.cursor()
            requete = "insert into user (nom, master_password, master_key) values ('{}', '{}', '{}')".format(nom,hash_master_password, chiffre_master_key)
            cursor.execute(requete)
            connection.commit()
        with sqlite3.connect(database) as connection:
            cursor = connection.cursor()
            requete = "select * from user WHERE nom = '{}' AND master_password = '{}'".format(nom,hash_master_password)
            cursor.execute(requete)
            user = cursor.fetchone()
        dict_user = {'id':user[0], 'nom':user[1], 'master key':my_pass.decode(user[3])}
        return dict_user
    else:
        return False
    
def login(nom:str, master_password:str, database='database.db'):
    """
    """
    assert type(nom) == str
    assert type(master_password) == str
    assert type(database) == str and (database.split('.'))[-1] == 'db'
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        requete = "select * from user WHERE nom = '{}' AND master_password = '{}'".format(nom, hashlib.sha1(master_password.encode()).hexdigest())
        cursor.execute(requete)
        user = cursor.fetchone()
    if user != None:
        if len(user[3]) > len(master_password):
            for i in range(len(user[3])-len(master_password)):
                master_password += master_password[:(len(user[3])-len(master_password))]
        my_pass = CodageMawa(master_password)
        dict_user = {'id':user[0], 'nom':user[1], 'master key':my_pass.decode(user[3])}
        return dict_user
    else:
        return False
        

def modifier(nom:str, master_password:str, new_nom:str, new_password:str, database='database.db') -> bool:
    """
    """

    assert type(nom) == str 
    assert type(master_password) == str
    assert type(new_nom) == str 
    assert type(new_password) == str
    assert type(database) == str and (database.split('.'))[-1] == 'db'
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        requete = "select * from user WHERE nom = '{}' AND master_password = '{}'".format(nom, hashlib.sha1(master_password.encode()).hexdigest())
        cursor.execute(requete)
        user = cursor.fetchone()
    if user != None:
        if len(user[3]) > len(master_password):
            for i in range(len(user[3])-len(master_password)):
                master_password += master_password[:(len(user[3])-len(master_password))]
        my_pass = CodageMawa(master_password)
        dict_user = {'id':user[0], 'nom':user[1], 'master key':my_pass.decode(user[3])}
        hash_new_password = hashlib.sha1(new_password.encode()).hexdigest()
        if len(user[3]) > len(new_password):
            for i in range(len(user[3])-len(new_password)):
                new_password += master_password[:(len(user[3])-len(new_password))]
        with sqlite3.connect(database) as connection:
            cursor = connection.cursor()
            requete = f"UPDATE user SET nom = '{new_nom}', master_key = '{CodageMawa(new_password).encode(dict_user['master key'])}',  master_password = '{hash_new_password}' WHERE id = {str(dict_user['id'])}"
            cursor.execute(requete)
            connection.commit()
        return True
    else:
        return False

if __name__ == '__main__':
    pass