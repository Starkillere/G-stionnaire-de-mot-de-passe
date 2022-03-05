#-*- coding:utf-8 -*-

import os
import sys
import math
import random
from operator import xor

class CodageMoua:

    """

        
    """

    def __init__(self):
        self.element = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
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
                        '<', '>']
    
    def __algorithme_fermat(self, valeur:int) -> int :
        assert type(valeur) == int
        res = 2**2**valeur+1
        return res
    
    def __inv__algorithme_fermat(self, valeur:int) -> int :
        assert type(valeur) == int
        res = round(math.log((math.log(2**2**valeur+1)-1)/math.log(2))/math.log(2), 0)
        return res

    def master_key_genrator(self,  master_pasword:str) -> str :
        assert type(master_pasword) == str
        bytes = os.urandom(32)
        csprng = random.SystemRandom()
        random_int = csprng.randint(0, sys.maxsize)   
                        
    def encode(self, master_key:str, password:str) -> str :
        assert type(master_key) == str
        assert type(password) == str 
        if len(password) % 19 != 0:
            pass

    def decode(self, master_key:str,  password:str) -> str :
        assert type(master_key) == str
        assert type(password) == str

if __name__ == '__main__':
    my_pass = CodageMoua()