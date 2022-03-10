#-*- coding:utf-8 -*-
from codage_maoua import CodageMoua

def generate_master_key() -> str:
    my_pass = CodageMoua()
    return my_pass.master_key_genrator()

def save_master_key(master_key:str, master_password:str, fichier='master_key.txt') -> bool:
    """
    """
    assert type(master_password) == str
    assert type(master_key) == str
    assert type(fichier) == str and (fichier.split('.'))[-1] == 'txt'
    if len(master_key) > len(master_password):
        master_password += master_password[:(len(master_key)-len(master_password))]
    my_pass = CodageMoua(master_password)
    chiffre_master_key = my_pass.encode(master_key)
    with open(fichier, 'w', encoding='utf-8', newline='') as file:
        file.write(f'master key={chiffre_master_key}')
    return True

def return_master_key(master_password:str, fichier='master_key.txt') -> str:
    """
    """
    assert type(master_password) == str
    assert type(fichier) == str and (fichier.split('.'))[-1] == 'txt'
    with open(fichier, 'r', encoding='utf-8') as file:
        donnees = [tuple(((data.replace(' ', '')).replace('\n', '')).split('=')) for data in file]
        donnees = dict(donnees)
    chiffre_master_key = donnees['master key']
    if len(chiffre_master_key) > len(master_password):
        master_password += master_password[:(len(chiffre_master_key)-len(master_password))]
    my_pass = CodageMoua(master_password)
    master_key = my_pass.decode(chiffre_master_key)

    return master_key