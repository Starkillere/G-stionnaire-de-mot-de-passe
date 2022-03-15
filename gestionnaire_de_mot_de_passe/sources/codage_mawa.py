#-*- coding:utf-8 -*-

import os
import sys
import random
from operator import xor

class CodageMawa:
    """
        ** Class CodageMawa **

        Description:
        ------------
            Permet de chiffré et de déchiffré du text de façon symétrique.
        
        Méthodes:
        ---------
            __init__: Constructeur, prend un paramètre , la clé de chiffrement de type str.
                      méthode appelée lors de l'instanciation d'un objet de type CodageMaou.
                      ne retourne rien.

            __algorithme: Méthode privé de la class CadageMaoua algorithme qui prend en paramètre 
                          un nombre (type int) et qui retourne son image par la fonction definie par
                          f(x) = -x + longeur du tableau de carractère (self.elements) , sur 
                          [0; longeur du tableau de carractère]

            __inv_algorithme: Méthode privé de la class CadageMaoua algorithme qui prend en paramètre 
                              un nombre (type int) et qui retourne son image par la fonction definie par
                              f(x) = | x - longeur du tableau de carractère (self.elements) | , sur 
                              [0; longeur du tableau de carractère]  . (inverse de __algorithme)

            master_key_genrator: Génerateur de master clé, permet de génerer une mster clé de 32 carractère.
            
            encode: Permet de chiffré un mot de passe passé en paramètre de la méthode par la clé définie comme
            attribue de l'objet.

            decode: Permet de déchiffré un mot de passe passé en paramètre de la méthode par la clé définie comme
            attribue de l'objet.

        Attribues:
        ---------
            self.elements: liste de carractères , utiliser pour chiffré et déchiffré .
            self.master_key: la master key utilisé pour chiffré et déchiffré .

        
        Tests:
        ------
            >>> my_pass = CodageMawa('Anrezki')
            >>> chiffre = my_pass.encode("ikzerna")
            >>> print(my_pass.decode(chiffre))
            ikzerna         
    """
    def __init__(self, master_key:str):

        '''Constructeur'''

        assert type(master_key) == str
        self.elements:list = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
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
                              '{', '}', '|', '`', '°','[', ']',
                              '+', '.', '?', ";", ':', '!', '§',
                              '¤', '€', '£', '¨', '<',  '>','~',
                              '=', 'Σ']

        self.master_key = master_key    
    
    def __algorithme(self, valeur:int) -> int :
        """
            ** __algorithme **

            Description:
            -------------
                Méthode privé de la class CadageMaoua algorithme qui prend en paramètre 
                un nombre (type int) et qui retourne son image par la fonction definie par
                f(x) = -x + longeur du tableau de carractère (self.elements) , sur 
                [0; longeur du tableau de carractère]

            IN:
            ---
                valeur: Variable de type int

            OUT:
             ----
                res: Image de valeur par la fonction definie par f(x) = -x + longeur du tableau de carractère (self.elements) , sur 
                [0; longeur du tableau de carractère] (Variable de type int)

            Tests:
            ------
                >>> print(__algorithme(len(self.elements)))
                0  
        """
        assert type(valeur) == int
        res = -valeur + len(self.elements)
        return res
    
    def __inv_algorithme(self, valeur:int) -> int :
        """
            ** __inv_algorithme **

            Description:
            -------------
                Méthode privé de la class CadageMaoua algorithme qui prend en paramètre 
                un nombre (type int) et qui retourne son image par la fonction definie par
                f(x) = | x - longeur du tableau de carractère (self.elements) | , sur 
                [0; longeur du tableau de carractère]  . (inverse de __algorithme)

            IN:
            ---
                valeur: Variable de type int
            
            OUT:
            ----
                res: Image de valeur par la fonction definie par f(x) = | x - longeur du tableau de carractère (self.elements) |
                sur [0; longeur du tableau de carractère] . (inverse de __algorithme)   
            Tests:
             ------
                >>> print(__algorithme(0)) == len(self.elements)
                True 
        """
        assert type(valeur) == int
        res = abs(valeur - len(self.elements))
        return res

    def master_key_genrator(self) -> str :
        """
            ** master_key_genrator **

            Description:
            -------------
                Génerateur de master clé, permet de génerer une mster clé de 32 carractère.

            Explication:
            ------------
                Etape 1: On génerer des nombre pseudo aléatoires (mode longeur du tableau de carractère) 
                     crypthographiquement sécuriser avec random.SystemRandom().randint(). On enregistre les nombres
                     dans un tableau.
                Etape 2: On remplace chaque nombre par la lettre correspondant dans le tableau.
                Etape 3: On transforme le tableau de lettre en chaine de carractères.
            IN:
            ---
                Ne prend pas de paramètre .
            
            OUT:
            ----
                retourne une master key sous la forme d'une chaine de carractère.
            Tests:
            ------
                >>> my_master_key = CodageMawa.master_key_genrator()
                >>> type(my_master_key) == str
                True 
        """
        bytes = os.urandom(32)
        csprng = random.SystemRandom()
        master_key = [self.elements[csprng.randint(0, sys.maxsize)%(len(self.elements)-1)] for i in range(32)]
        master_key = ''.join(master_key)
        return master_key
                        
    def encode(self, password:str) -> str :
        """
            ** encode **

            Description:
            ------------
                Permet de chiffré un mot de passe passé en paramètre de la méthode par la clé définie comme
                attribue de l'objet.

            Explication:
            ------------
                Pour faire le chiffrement il faut que la longuer du password soit égale à la longuer de la master key.

                Etape 1 : Si la longueur du password  est inférieur à la  longueur de la master key on incrémente le password
                  avec des lettres pseudo aléatoirs préfixé de 'Σ' pour pouvoir le repérer lors du déchiffrement.
                  'Σ' marque la fin du mot de passe et le début de la chaine aléatoir.

                Etape 2: On change les carractères de la master key et du password par leurs index dans le tableau de 
                 carratère (self.elements).

                Etape 3: On change chaque valeur du passeword par son image par __algorithme (mode longeur du tableau de carractère).

                Etape 4: On adition  le résulta de l'etape 3 par la master key (mode longeur du tableau de carractère).  

                Etape 5: On change chaque valeur par le carractères correspondant dans le tableau (self.elements)

            IN:
            ---
                prend un paramètre, le mot de passe à chiffré .
                password: variable de type str .
            OUT:
            ----
                retourn le mot de passe chiffré.
            Tests:
            ------
                >>> my_pass = CodageMawa('Anrezki')
                >>> chiffre = my_pass.encode("ikzerna")
                >>> print(chiffre)
                sd+ai>i
        """
        assert type(password) == str
        if len(self.master_key) > len(password):
            password += 'Σ'+''.join([self.elements[random.SystemRandom().randint(0, sys.maxsize)%len(self.elements)] for i in range((len(self.master_key) - len(password))-1)])
        valeurs_master_key = [self.elements.index(value) for value in self.master_key]
        valeurs_password = [self.elements.index(value) for value in password]
        res_algo_password = [self.__algorithme(value)%len(self.elements) for value in valeurs_password]
        chiffre = [(valeurs_master_key[i] +  res_algo_password[i])%len(self.elements) for i in range(len(valeurs_master_key))]
        return ''.join([self.elements[value] for value in chiffre])

    def decode(self, chiffre:str) -> str :
        """
            ** decode **

            Description:
            ------------
                Permet de déchiffré un mot de passe passé en paramètre de la méthode par la clé définie comme
                attribue de l'objet.
        
            Explication:
            ------------
                Etape 1: On change les carractères de la master key et du dhiffré par leurs index dans le tableau de 
                carratère (self.elements).

                Etape 2: On change chaque valeur du chiffré par son image par __inv_algorithme (mode longeur du tableau de carractère).

                Etape 3: On adition  le résulta de l'etape 2 par la master key (mode longeur du tableau de carractère).  

                Etape 4: On change chaque valeur par le carractères correspondant dans le tableau (self.elements)
            IN:
            ---
                Prend en parametre le chiffré qu'on souhaite déchiffré.
                chiffre: variable de type str .
            OUT:
            ----
                retourne le mot de passe déchiffré.

            Tests:
            -----
                >>> my_pass = CodageMawa('Anrezki')
                >>> clair = my_pass.decode('sd+ai>i')
                ikzerna
        """
        assert type(chiffre) == str
        valeurs_master_key = [self.elements.index(value) for value in self.master_key]
        valeurs_chiffre = [self.elements.index(value) for value in chiffre]
        res_inv_algo_password = [(valeurs_chiffre[i] - valeurs_master_key[i])%len(self.elements) for i in range(len(valeurs_master_key))]
        clair =  [self.__inv_algorithme(value)%len(self.elements) for value in res_inv_algo_password]
        return (''.join([self.elements[value] for value in clair]).split('Σ'))[0]

if __name__ == '__main__':
    pass