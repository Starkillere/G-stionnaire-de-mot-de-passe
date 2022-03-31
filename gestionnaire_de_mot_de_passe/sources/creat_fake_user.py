# -*- coding:utf-8 -*-
'''
    *** creat_fake_user.py ***
    
    Description:
    ------------
        Permet de crée de faux utilisateur  et de les enregistré dans le fichier faker.csv

    Module externe utiliser:
    ------------------------
        faker.py:
            "Faker est un package Python qui génère de fausses données pour vous.
             Que vous ayez besoin de démarrer votre base de données, de créer de beaux documents XML,
             de remplir votre persistance pour les tests ou d'anonymiser les données d'un service de production,
             Faker est fait pour vous. "
        
            documentation: https://faker.readthedocs.io/en/master/
'''
from faker import Faker
from random import choice
import csv

fake = Faker()
platforme = ['instagram', 'Discord', 'neo', 'Facebook', 'openclassroom', 'youtube']
for i in range(200):
    with open('faker.csv', 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow([choice(platforme), fake.name(), fake.password(), fake.name()+'@gmail.com'])