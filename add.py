import csv
import pandas as pd

df= pd.read_csv('DB_CSV.csv')

print (df)

with open('DB_CSV.csv', newline='',mode= 'r+') as eggs:
    lector = csv.reader(eggs , delimiter=',')
    for row in lector:
        print(row , list(enumerate (row)))

