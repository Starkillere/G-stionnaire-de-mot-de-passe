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
import gestion_master_key 
import gestion_data

def sing_in(nom:str, password:str, fichier='user.txt') -> str:
    """
    """
    assert type(nom) == str
    assert type(password) == str
    assert type(fichier) == str and (fichier.split('.'))[-1] == 'txt'

    with open(fichier, 'w', encoding='utf-8', newline='') as file:
        file.write(f'Nom = {nom.upper()}\nPassword = {hashlib.sha1(password.encode()).hexdigest()}')
    master_key = gestion_master_key.generate_master_key()
    gestion_master_key.save_master_key(master_key, password)
    gestion_data.supprimer(True)
    return gestion_master_key.return_master_key(password)


def login(nom:str, password:str, fichier='user.txt'):
    """
    """

    assert type(nom) == str
    assert type(password) == str
    assert type(fichier) == str and (fichier.split('.'))[-1] == 'txt'

    with open(fichier, 'r', encoding='utf-8') as file:
        donnees = [tuple(((data.replace(' ', '')).replace('\n', '')).split('=')) for data in file]
        donnees = dict(donnees)
    if nom.upper() == donnees['Nom'] and hashlib.sha1(password.encode()).hexdigest() == donnees['Password']:
        master_key = gestion_master_key.return_master_key(password)
        return master_key
    return False
        

def modifier(master_password:str, new_nom:None, new_password:None, fichier='user.txt') -> bool:
    """
    """
    assert type(master_password) == str
    assert type(new_nom) == str or type(new_nom) == None
    assert type(new_password) == str or type(new_password) == None
    assert type(fichier) == str and (fichier.split('.'))[-1] == 'txt'

    with open(fichier, 'r', encoding='utf-8') as file:
        donnees = [tuple(((data.replace(' ', '')).replace('\n', '')).split('=')) for data in file]
        donnees = dict(donnees)
        
    if donnees['Password'] !=  hashlib.sha1(master_password.encode()).hexdigest():
        return False

    if new_nom != None:
        donnees['Nom'] = new_nom
    if new_password != None:
        master_key =  gestion_master_key.return_master_key(master_password)
        gestion_master_key.save_master_key(master_key, new_password)
        donnees['Password'] = hashlib.sha1(new_password.encode()).hexdigest()
        
    with open(fichier, 'w', encoding='utf-8', newline='') as file:
        file.write(f"Nom = {donnees['Nom'].upper()}\nPassword = {donnees['Password']}")
    return True

if __name__ == '__main__':
    pass