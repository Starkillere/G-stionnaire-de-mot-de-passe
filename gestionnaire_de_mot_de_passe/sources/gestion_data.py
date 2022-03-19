#-*- coding:utf-8 -*-
'''
    *** gestion_data.py ***

    Description:
    ------------
        Gestion des données de la table gestionnaire .
            - Enregistrement
            - Lecture
            - Recherche
            - Modification 
    Fonction:
    ---------
        save_password : Permet de sauveagarder un mot de passe.
        lecture : Permet de lire dans la table gestionnaire pour retrouver un mot de passe ou afficher tout les mot de passe.
        importation : Permet d'importer des données.
        supprimer: Permet de supprimer des données dans gestionaire.
        modifier: Permet de modifier des données.
'''
import csv
import sqlite3
from codage_mawa import CodageMawa

def save_password(var_id:int, platforme:str, nom:str, password:str,  master_key:str, mail=None, database='database.db') -> bool:
    '''
        *** save_password ***
        
        Description:
        ------------
            Permet de sauveagarder un mot de passe dans la base de données.

        Explication:
        ------------  
            Etape 1: On chiffre le mot de passe avec la master key
            Etape 2: On écrit l'var_id du nouveau mot de passe qui correspond à l'var_id de l'utilisateur
                     dans la table user , on écrit la platforme , le nom, le mot de passe et le mail.
            Etape 3 : On execute la requette
            Etape 4 : On commit pour sauvgarder
        
        IN:
        ---
            var_id: paramètre de la fonction save_password (type:int) correspond a l'var_id de l'utilisateur.
                Utilisé comme var_id du nouveau mot de passe, pour pour faire le lien avec l'utilisateur.
            
            platforme: paramètre de la fonction save_password (type:str) correspond à la platforme 
                       pour la quelle l'utilisateur souhaite crée un nouveau mot de passe.

            nom: paramètre de la fontion save_password (type:str) correspond au nom de l'utilisateur sur la platforme.

            password: paramètre de la fontion save_password (type:str) correspond au mot de passe de l'utilisateur sur la platforme.

            master_key: paramètre de la fontion save_password (type:str) correspond à la master key de l'utilisateur.
                         utilisé pour chiffré le mot de passe avant de l'enregistré.

            mail: paramètre de la fontion save_password (valeur par défaut:None sinon doit être de type str)
                  correspond au mail de l'utilisateur sur la platforme .

            database: paramètre de la fontion save_password (valeur par défaut: database.db, type str) 
                      correspond à la base de données pour la quelle on souhaite enregistré des données
                      doit obligatoirement être une base de données sqlite et doit contenir les table user et gestionnaire.
        OUT:
        ----
            retourne True

        Tests:
        ------
            >>> save_password(1, "instagrame", "Starkiller", "ikzerna",  "Anrezki", " Holden@gmail.com")
            True
    '''
    assert type(var_id) == int
    assert type(platforme) == str
    assert type(password) == str
    assert type(nom) == str
    assert type(master_key) == str
    assert type(mail) == str or mail == None
    assert type(database) == str and (database.split('.'))[-1] == 'db'
    if not 'Σ' in list(password):
        my_pass = CodageMawa(master_key)
        try:
            for i in password:
                my_pass.elements.index(i)
        except:
            return False
        chiffre_password =  my_pass.encode(password)
        with sqlite3.connect(database) as connection:
            cursor = connection.cursor()
            requete = "insert into gestionnaire (id, platforme, nom, password, mail) values (?, ?, ?, ?, ?)"
            cursor.execute(requete, [(var_id), (platforme), (nom), (chiffre_password), (mail)])     
            connection.commit()
        return True
    return False

def lecture(return_all:bool, master_key:str, var_id:int, database='database.db', nom=None, platforme=None):
    """
        *** lecture ***

        Description:
        ------------
            Permet de lire dans la table gestionnaire pour retrouver un mot de passe ou afficher tout les mot de passe.
        
        Explication:
        ------------
            mode 1: afficher tout (return_all == True)
                Etape 1 : On sélectionne tout les mot de passe ayant pou var_id l'var_id de l'utilisateur passé en paramètre
                Etape 2 : On trie la liste de tuple retourner avec la 3éme valeur (nom)
                Etape 3 : On transforme la liste de tuples retourner en une liste de dictionnaires avec les clé
                          ['platforme', 'nom', 'password', 'mail'] chaque dictionnaires de la liste correspond a un compte
                          avec la platforme  le nom , le mot de passe déchiffré et le mail.
            mode 2: rechercher (return_all == False)
                Etape 1 : On sélectionne tout les mot de passe ayant pou var_id l'var_id de l'utilisateur passé en paramètre
                Etape 2 : On recher dans cette liste le compte qui a pour nom le nom passé en en paramètre
                          et qui à pour platforme la platforme passé en paramètre.
        IN:
        ---
            return_all : paramètre de la fonction lecture (type:bool) permet de savoir si on veux afficher tout ou faire de la 
                         recherche.
            
            master_key : paramètre de la fontion lecture (type:str) correspond à la master key de l'utilisateur.
                         utilisé pour déchiffré le mot de passe avant de le retourner.
            
            var_id: paramètre de la fonction lecture (type:int) correspond a l'var_id de l'utilisateur.
                Utilisé pour repérer les compte de l'utilisateur.
            
            database: paramètre de la fontion lecture (valeur par défaut: database.db, type str) 
                      correspond à la base de données pour la quelle on souhaite retrouver des données
                      doit obligatoirement être une base de données sqlite et doit contenir les table user et gestionnaire.
            
            nom: paramètre de la fonction lecture (valeur par défaut:None sinon doit être de type str) correspond au
                 nom de l'utilisateur sur la platforme. Utilisé pour faire de la recherche.
            
            platforme: paramètre de la fonction lecture (valeur par défaut:None sinon doit être de type str) correspond à
                        la platforme . Utilisé pour faire de la recherche.
        OUT:
        ----
            si return_all == True:
                retourne la liste des compte de l'utilisateur.
            si non si return_all == False:
                si un compte correspond  a nom, platforme:
                    retourne le compte sous la forme d'un dictionnaire.
                si non :
                    retourne False            
    """
    assert type(var_id) == int
    assert type(master_key) == str
    assert type(return_all) == bool
    def get_nom(contact):
        return contact[2]
    requete = 'select * from gestionnaire WHERE id = ?'
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        if return_all:
            password = cursor.execute(requete, [(var_id)])
            password = list(password)
            password.sort(key=get_nom)
            my_pass = CodageMawa(master_key)
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
            passwords = cursor.execute(requete, [(var_id)])
            my_pass = CodageMawa(master_key)
            for password in passwords:
                if password[1].upper() == platforme.upper() and password[2].upper() == nom.upper():
                    dictc = {'platforme': password[1], 'nom': password[2], 'password': my_pass.decode(password[3]), 'mail': password[4]}
                    return dictc
            else:
                return False

def importation(fichier_user:str, master_key:str, var_id:int, database='database.db'):
    """
        *** importation ***

        Description:
        ------------
            Permet d'importer des données, des compte comptenue dans un fichier csv .
        
        Explcation:
        -----------
            Etape 1: On recupére tout le contenue du fichier csv de l'utilisateur sous la forme de liste de dictionnaire
            Etape 2: On verifier si les dictionnaire on bien les clés ['platforme', 'nom', 'password', 'mail']
            Etape 3: si oui pour l'etape 2  on écrit les données dans la table gestionnaire avec comme var_id l'var_id de l'utilisateur.
        IN:
        ---
            fichier_user : paramètre de la fonction importation (type str) fichier csv 

            var_id: paramètre de la fonction importation (type:int) correspond a l'var_id de l'utilisateur.
                Utilisé comme var_id du nouveau mot de passe, pour pour faire le lien avec l'utilisateur.

            database: paramètre de la fontion importation (valeur par défaut: database.db, type str) 
                      correspond à la base de données pour la quelle on souhaite enregistré des données
                      doit obligatoirement être une base de données sqlite et doit contenir les table user et gestionnaire.
            
            master_key:  paramètre de la fontion importation (type:str) correspond à la master key de l'utilisateur.
                         utilisé pour chiffré le mot de passe avant de l'enregistré.
        OUT:
        ----
        si fichier user contient les clé ['platforme', 'nom', 'password', 'mail'] :
            retourne True
        si non:
            retourne False
    """
    assert type(var_id) == int
    assert type(fichier_user) == str and (fichier_user.split('.'))[-1] == 'csv'
    assert type(database) == str and (database.split('.'))[-1] == 'db'
    assert type( master_key) == str
    try:
        with open(fichier_user, 'r', encoding='utf-8') as fichier:
            passwords = [dict(contact) for contact in csv.DictReader(fichier)]
    except FileNotFoundError:
        return 9
    try:
        if list(passwords[0].keys()) == ['platforme', 'nom', 'password', 'mail']:
            for passw in passwords:
                if not 'Σ' in list(passw['password']):
                    my_pass = CodageMawa(master_key)
                    try:
                        for i in passw['password']:
                            my_pass.elements.index(i)
                    except:
                        return False
                else:
                    return False
            with sqlite3.connect(database) as connection:
                cursor = connection.cursor()
                my_pass = CodageMawa(master_key)
                for password in passwords:
                    requete = "insert into gestionnaire (id, platforme, nom, password, mail) values (?, ?, ?, ?, ?)"
                    cursor.execute(requete, [(var_id), (password['platforme']), (password['nom']), (my_pass.encode(password['password'])), (password['mail'])])
                    connection.commit()
        else:
           return 2
        return True
    except IndexError:
        return 3

def supprimer(delt_all:bool, var_id:int, platforme=None, nom=None, database='database.db') -> bool:
    """
        *** supprimer ***

        Description:
        ------------
            Permet de supprimer des données dans gestionaire. si delt_all == True , supprime tout, 
            si delt_all == False supprimer le compte correspondant à nom, platforme.
        
        Explication:
        ------------
            mode 1: supprimer tout (delt_all == True)
                Etape 1 : On supprime tout les données ayant pour var_id l'var_id de l'utilisateur.
            mode 2: supprimer un compte (delt_all == False)
                Etape 1 : On supprime le compte ayant pour var_id l'var_id en paramètre , le nom en paramètre , la platforme en paramètre.
                
        IN:
        ---
            return_all : paramètre de la fonction supprimer (type:bool) permet de savoir si on souhaite tout supprimer ou supprimer un élément.
            
            var_id: paramètre de la fonction supprimer (type:int) correspond a l'var_id de l'utilisateur.
                Utilisé pour repérer les compte de l'utilisateur.
            
            database: paramètre de la fontion supprimer (valeur par défaut: database.db, type str) 
                      correspond à la base de données pour la quelle on souhaite retrouver des données
                      doit obligatoirement être une base de données sqlite et doit contenir les table user et gestionnaire.
            
            nom: paramètre de la fonction supprimer (valeur par défaut:None sinon doit être de type str) correspond au
                 nom de l'utilisateur sur la platforme. Utilisé pour faire de la recherche.
            
            platforme: paramètre de la fonction supprimer (valeur par défaut:None sinon doit être de type str) correspond à
                        la platforme . Utilisé pour faire de la recherche.
        OUT:
        ----
            si delt_all == True:
                supprime tout 
                retourne True
            si non si delt_all == False:
                supprime le compte
                retourne True
    """
    assert type(var_id) == int
    assert type(delt_all) == bool
    assert type(database) == str and (database.split('.'))[-1] == 'db'
    if delt_all:
        with sqlite3.connect(database) as connection:
            cursor = connection.cursor()
            requete = "DELETE FROM gestionnaire WHERE id = ? "
            cursor.execute(requete, [(var_id)])
            connection.commit()
    else:
        assert type(platforme) == str
        assert type(nom) == str
        with sqlite3.connect(database) as connection:
            cursor = connection.cursor()
            requete = 'DELETE FROM gestionnaire WHERE id = ? AND nom = ? AND platforme = ?'
            cursor.execute(requete, [(var_id), (nom), (platforme)])
            connection.commit()
    return True

def modifier(platforme:str, nom:str, var_id:int, master_key:str, new_nom:str, new_password:str,  database='database.db',) -> bool :
    """
        *** modifier ***

        Description:
        ------------
            Permet de modifier des données.
        
        Explication:
        ------------
            Etape 1: On chiffre le nouveau mot de passe avec la master key
            Etape 2: On modifie avec UPDATE si l'var_id ,le nom et la platforme correspondent.

        IN:
        ---
           var_id: paramètre de la fonction save_password (type:int) correspond a l'var_id de l'utilisateur.
                Utilisé comme var_id du nouveau mot de passe, pour pour faire le lien avec l'utilisateur.
            
            platforme: paramètre de la fonction save_password (type:str) correspond à la platforme 
                       pour la quelle l'utilisateur souhaite crée un nouveau mot de passe.

            nom: paramètre de la fontion save_password (type:str) correspond au nom de l'utilisateur sur la platforme.

            password: paramètre de la fontion save_password (type:str) correspond au mot de passe de l'utilisateur sur la platforme.

            database: paramètre de la fontion supprimer (valeur par défaut: database.db, type str) 
                      correspond à la base de données pour la quelle on souhaite retrouver des données
                      doit obligatoirement être une base de données sqlite et doit contenir les table user et gestionnaire. 
        OUT:
        ----
            retourne True
    """
    assert type(var_id) == int
    assert type(platforme) == str
    assert type(nom) == str
    assert type(new_nom) == str 
    assert type(new_password) == str 
    assert type(master_key) == str 
    assert type(database) == str and (database.split('.'))[-1] == 'db'
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        my_pass = CodageMawa(master_key)
        if not 'Σ' in list(new_password):
            try:
                for i in new_password:
                    my_pass.elements.index(i)
            except:
                return False
            requete = "UPDATE gestionnaire SET nom = ?, password = ?  WHERE id = ? AND nom = ? AND platforme = ?"
            cursor.execute(requete, [(new_nom), (my_pass.encode(new_password)), (var_id), (nom), (platforme)])
            connection.commit()
            return True
        return False