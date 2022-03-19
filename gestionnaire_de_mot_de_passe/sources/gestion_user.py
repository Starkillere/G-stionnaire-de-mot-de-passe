# -*- coding:utf-8 -*-
"""
    *** gestion_user.py ***

    Description:
    ------------
        Gestion de l'utilisateurs (enregistrement, authentification, modification du compte)
    
    Fonction:
    ---------
        - sing_in : Création du compte de l'utilisateur nom, mot de passe.
        - login : Connection de l'utilisateur nom, mot de passe.
        - modifier : Modification du compte de l'utilisateur.
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

        Explication:
        ------------
            Etape 1: On vérifie si il n'y a pas déjà dans la base de données user un utilisateur qui a 
                     le nom saise par l'utilisateur.
            Etape 2: Si Etape 1 == non : on crée une master clé pour l'utilisateur.
            Etape 3: On récuper le hasher du mot de passe de l'utilisateur dans une variable.
            Etape 4: On verifie que le mot de passe a la même taille que la master key.
            Etape 5: Si Etape 4 == non : on incrémente le mot de passe avec les (longueur master key - longueur mot de passe)
                     première lettre de mot de passe (longueur master key - longueur mot de passe) fois pour avoir 
                     longueur master key - longueur mot de passe = 0
                     soit :
                        longueur master key = longueur mot de passe
            Etape 6: On enregistre le nom , le mot de passe hasher  et la master key chiffré avec le mot de passe 
                     Dans la base de données user.
            Etape 7: On recuper les in formation de l'utilisateur dans la base de données .
                    On déchiffre la master key avec le mot de passe
            Etape 8 : On retourne un dictionnaire avec l'id le nom et la master key de l'utilisateur.

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
        
        Explication:
        ------------
            Etape 1: On veridie si le mot de passe de l'utilisateur et son nom sont correctent.
            Etape 2: Si Etape 1 == oui: On verifie que le mot de passe a la même taille que la master key chiffré.
            Etape 3: Si Etape 2 == non : on incrémente le mot de passe avec les (longueur master key chiffré - longueur mot de passe)
                     première lettre de mot de passe (longueur master key chiffré - longueur mot de passe) fois pour avoir 
                     longueur master key chiffré - longueur mot de passe = 0
                     soit :
                        longueur master key chiffré = longueur mot de passe
            Etape 4: On déchiffre la master key chiffré
            Etape 4:.
            Etape 5: On retourne un dictionnaire avec l'id le nom et la master key de l'utilisateur.

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
        
        Explication:
        ------------
            Etape 1: On verifie si le mot de passe de l'utilisateur est correct.
            Etape 2: On verifie que le mot de passe a la même taille que la master key chiffré
            Etape 3: Si Etape 2 == non : on incrémente le mot de passe avec les (longueur master key chiffré - longueur mot de passe)
                     première lettre de mot de passe (longueur master key chiffré - longueur mot de passe) fois pour avoir 
                     longueur master key chiffré - longueur mot de passe = 0
                     soit :
                        longueur master key chiffré = longueur mot de passe
            Etape 3: On déchiffre la master key chiffré.
            Etape 4: On verifie que le nouveau mot de passe a la même taille que la master key.
            Etape 5: Si Etape 4 == non: on incrémente le nouveau mot de passe avec les (longueur master key  -  longueur nouveau mot de passe)
                     première lettre de mot de passe (longueur master key  - longueur nouveau mot de passe) fois pour avoir 
                     longueur master key -   longueur  nouveau mot de passe = 0
                     soit :
                        longueur master key  = longueur nouveau mot de passe
            Etape 6: On chiffre le master key avec le nouveau mot de passe.
            Etape 7: On modifie le nom par new_nom et master_key par la nouvelle valeur chiffré avec new_password
                     et  master_password par le hasher de new_password.

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
                retourne True
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
        if user_exist == None:
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