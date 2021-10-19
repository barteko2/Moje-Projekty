import csv
import pandas as pd

file_path = 'Zeszyt1.csv'

with open(file_path, newline = '') as csv_file:
    off_reader = csv.reader(csv_file,delimiter = ';')
    for _ in range(5):
        print(next(off_reader))

df = pd.read_csv('Zeszyt1.csv')

print(type(df))


print("pierwsze trzy")
print(df.head(3))

print("DESCRIBE")
print(df.describe())

print('\nWYŚWIETLENIE KOLUMNY O PODANEJ NAZWIE')
print(df['PreviousUserCount'])

#s = pd.Series([1,2,3])
#print(s.describe())