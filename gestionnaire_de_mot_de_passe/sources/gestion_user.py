# -*- coding:utf-8 -*-
"""
    *** gestion_user.py ***

    Description:
    ------------
        Gestion de l'utilisateurs (enregistrement, authentification, modification du compte, suppression du compte)
    
    Fonction:
    ---------
        - sing_in : Création du compte de l'utilisateur nom, mot de passe.
        - login : Connection de l'utilisateur nom, mot de passe.
        - modifier : Modification du compte de l'utilisateur.
        - delt_user : Permet de supprimer le compte de l'utilisateur. 
"""
import hashlib
import gestion_data
from codage_mawa import CodageMawa
import sqlite3

def sing_in(nom:str, master_password:str, database='database.db') -> str:
    """
        *** sing_in ***

        Description:
        ------------
            Création du compte de l'utilisateur nom, mot de passe.
        IN:
        ---
            nom: paramètre de la fonction sing_in (type: str) correspond au nom de l'utilisateur

            master_password:  paramètre de la fonction sing_in (type: str) correspond au mot de passe de l'utilisateur

            database: paramètre de la fontion sing_in (valeur par défaut: database.db, type str) 
                      correspond à la base de données pour la quelle on souhaite enregistré des données
                      doit obligatoirement être une base de données sqlite et doit contenir les table user et gestionnaire.

        OUT:
        ----
            si nom déjà utilisé:
                rtourne False
            si non:
                retourne un dictionnaire avec l'id le nom et la master key de l'utilisateur
    """
    assert type(nom) == str
    assert type(master_password) == str
    assert type(database) == str and (database.split('.'))[-1] == 'db'
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        requete = "select * from user WHERE nom = ? "
        cursor.execute(requete, [(nom)])
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
            requete = "insert into user (nom, master_password, master_key) values (?, ?, ?)"
            cursor.execute(requete, [(nom),(hash_master_password), (chiffre_master_key)])
            connection.commit()
        with sqlite3.connect(database) as connection:
            cursor = connection.cursor()
            requete = "select * from user WHERE nom = ? AND master_password = ? "
            cursor.execute(requete, [(nom),(hash_master_password)])
            user = cursor.fetchone()
        dict_user = {'id':user[0], 'nom':user[1], 'master key':my_pass.decode(user[3])}
        return dict_user
    else:
        return False
    
def login(nom:str, master_password:str, database='database.db'):
    """
        *** login ***

        Description:
        ------------
            Connection de l'utilisateur nom, mot de passe.

        IN:
        ---
            nom: paramètre de la fonction login(type: str) correspond au nom de l'utilisateur

            master_password:  paramètre de la fonction login (type: str) correspond au mot de passe de l'utilisateur

            database: paramètre de la fontion login (valeur par défaut: database.db, type str) 
                      correspond à la base de données pour la quelle on souhaite enregistré des données
                      doit obligatoirement être une base de données sqlite et doit contenir les table user et gestionnaire.
        OUT:
        ----
           si nom ou mot de passe incorrecte:
                rtourne False
            si non:
                retourne un dictionnaire avec l'id le nom et la master key de l'utilisateur   
    """
    assert type(nom) == str
    assert type(master_password) == str
    assert type(database) == str and (database.split('.'))[-1] == 'db'
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        requete = "select * from user WHERE nom = ? AND master_password = ?"
        cursor.execute(requete, [(nom), (hashlib.sha1(master_password.encode()).hexdigest())])
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
        *** modifier ***

        Description:
        ------------
            Modification du compte de l'utilisateur.
        IN:
        ---
            nom: paramètre de la fonction modifier (type: str) correspond au nom de l'utilisateur

            master_password:  paramètre de la fonction modifier (type: str) correspond au mot de passe de l'utilisateur

            new_nom :paramètre de la fonction modifier (valeur par défaut: None, type str) correspond au nouveau nom de l'utilisateur.

            new_password: :paramètre de la fonction modifier (valeur par défaut: None, type str) correspond au nouveau mot de passe de l'utilisateur.

            database: paramètre de la fontion modifier (valeur par défaut: database.db, type str) 
                      correspond à la base de données pour la quelle on souhaite enregistré des données
                      doit obligatoirement être une base de données sqlite et doit contenir les table user et gestionnaire.
        
        OUT:
        ---
            si mot de passe correct:
                si new_nom pas déjà utilisé ou égale au nom de l'utilisateur:
                    retourne True
                si nom:
                    retourne 9
            si non:
                retourne False    
    """
    assert type(nom) == str 
    assert type(master_password) == str
    assert type(new_nom) == str 
    assert type(new_password) == str
    assert type(database) == str and (database.split('.'))[-1] == 'db'
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        requete = "select * from user WHERE nom = ? AND master_password = ?"
        cursor.execute(requete, [(nom), (hashlib.sha1(master_password.encode()).hexdigest())])
        user = cursor.fetchone()
    if user != None:
        with sqlite3.connect(database) as connection:
            cursor = connection.cursor()
            requete = "select * from user WHERE nom = ?"
            cursor.execute(requete, (new_nom,))
            user_exist = cursor.fetchone()
        if user_exist == None or new_nom ==  nom:
            if len(user[3]) > len(master_password):
                for i in range(len(user[3])-len(master_password)):
                    master_password += master_password[:(len(user[3])-len(master_password))]
            my_pass = CodageMawa(master_password)
            dict_user = {'id':user[0], 'nom':user[1], 'master key':my_pass.decode(user[3])}
            hash_new_password = hashlib.sha1(new_password.encode()).hexdigest()
            if len(user[3]) > len(new_password):
                for i in range(len(user[3])-len(new_password)):
                    new_password += new_password[:(len(user[3])-len(new_password))]
            with sqlite3.connect(database) as connection:
                cursor = connection.cursor()
                requete = f"UPDATE user SET nom = ?, master_key = ?,  master_password = ? WHERE id = ?"
                cursor.execute(requete, [(new_nom), (CodageMawa(new_password).encode(dict_user['master key'])), (hash_new_password), (dict_user['id'])])
                connection.commit()
            return True
        else:
            return 5
    else:
        return False

def delt_user(nom:str, var_id:int, database='database.db'):
    """
        *** delt_user ***

        Description:
        ------------
            Permet de supprimer le compte de l'utilisateur.
        IN:
        ---
            nom: paramètre de la fonction delt_user(type: str) correspond au nom de l'utilisateur.

            var_id: paramètre de la fonction delt_user (type: int) correspond à l'id de l'utilisateur.

            database: paramètre de la fontion modifier (valeur par défaut: database.db, type str) 
                      correspond à la base de données pour la quelle on souhaite enregistré des données
                      doit obligatoirement être une base de données sqlite et doit contenir les table user et gestionnaire.
        OUT:
        ----
            retourne True   
    """
    assert type(nom) == str
    assert type(var_id) == int
    assert type(database) == str and (database.split('.'))[-1] == 'db'
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        requete = "DELETE FROM user WHERE nom = ?"
        cursor.execute(requete, [nom])
        connection.commit()
    gestion_data.supprimer(True, var_id)
    return True