from tkinter import W
from faker import Faker
import csv
fake = Faker()

for i in range(156):
    with open('faker.csv', 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['instagrame', fake.name(), fake.password(), fake.name()+'@gmail.com'])
