#-*- coding:utf-8 -*-

#-*- coding:utf-8 -*-

import os
import sys
import random
from operator import xor

class CodageMoua:

    """

        
    """

    def __init__(self):
        self.elements = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                        'o', 'p', 'q', 'r', 's', 't', 'u',
                        'h', 'i', 'j', 'k', 'l', 'm', 'n',
                        'v', 'w', 'x', 'y', 'z', 'A', 'B',
                        'C', 'D', 'E', 'F', 'G', 'H', 'I',
                        'J', 'K', 'L', 'M', 'N', 'O', 'P',
                        'Q', 'R', 'S', 'T', 'U', 'V', 'W',
                        'X', 'Y', 'Z', '1', '2', '3', '4',
                        '5', '6', '7', '8', '9', '0', ' ',
                        '!', '@', '#', '$', '%', '^', '&',
                        '*', '(', ')', '/', '-', '_', '\\',
                        '"', '\'', '{', '}', '|', '`', '°',
                        '[', ']',  '+', '.', '=', '?', ";", 
                        ':', '!', '§', '¤', '€', '£', '¨', 
                        '<',  '>', 'Σ', '~']
    
    def __algorithme(self, valeur:int) -> int :
        assert type(valeur) == int
        res = -valeur + len(self.elements)
        return res
    
    def __inv_algorithme(self, valeur:int) -> int :
        assert type(valeur) == int
        res = abs(valeur - len(self.elements))
        return res

    def master_key_genrator(self) -> str :
        bytes = os.urandom(32)
        csprng = random.SystemRandom()
        random_int = [self.elements[csprng.randint(0, sys.maxsize)%len(self.elements)] for i in range(32)]
        master_key = ''.join(random_int)
        return master_key
                        
    def encode(self, password:str, master_key:str) -> str :
        assert type(master_key) == str
        assert type(password) == str
        if len(master_key) > len(password):
            password += 'Σ'+''.join([self.elements[random.SystemRandom().randint(0, sys.maxsize)%len(self.elements)] for i in range((len(master_key) - len(password))-1)])
        valeurs_master_key = [self.elements.index(value) for value in master_key]
        valeurs_password = [self.elements.index(value) for value in password]
        res_algo_password = [self.__algorithme(value)%len(self.elements) for value in valeurs_password]
        chiffre = [(valeurs_master_key[i] +  res_algo_password[i])%len(self.elements) for i in range(len(valeurs_master_key))]
        return ''.join([self.elements[value] for value in chiffre])

    def decode(self, chiffre:str, master_key:str) -> str :
        assert type(master_key) == str
        assert type(chiffre) == str
        valeurs_master_key = [self.elements.index(value) for value in master_key]
        valeurs_chiffre = [self.elements.index(value) for value in chiffre]
        res_inv_algo_password = [(valeurs_chiffre[i] - valeurs_master_key[i])%len(self.elements) for i in range(len(valeurs_master_key))]
        clair =  [self.__inv_algorithme(value)%len(self.elements) for value in res_inv_algo_password]
        return (''.join([self.elements[value] for value in clair]).split('Σ'))[0]

if __name__ == '__main__':
    pass
