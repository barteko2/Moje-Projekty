
'''#CZYTANIE Z JEDNEGO PLIKU I ZAPISYWANIE DO DRUGIEGO
with open('big-data.txt', 'r') as source_file:
    with open('big-data-corrected.txt','w') as target_file:
        for line in source_file:
            target_file.write(line)
'''

def line_reader(file_path):
    with open(file_path,'r') as source_file:
        for line in source_file:
            yield line
reader = line_reader('big-data.txt')
with open('big-data-corrected.txt','w') as target_file:
    for line in reader:
        target_file.write(line)
'''
Jeśli nie chcesz lub nie możesz skorzystać ze znaków zakończenia wiersza do rozdzielenia danych
— tak może być w przypadku dużego pliku binarnego — możesz odczytywać dane w kawałkach. Liczbę
bajtów do odczytania w każdym fragmencie należy przekazać do metody read obiektu file
'''

#!!!!!!!!!!!!HASZOWANIE HASŁA ZA POMOCĄ BIBLIOTEKI HASHLIB
import hashlib

secret = "To jest hasło lub dokument tekstowy"
bsecret = secret.encode()
m = hashlib.md5()
m.update(bsecret)
print(m.digest())


#!!!!!!!!!!!SZYFROWANIE ZA POMOCĄ BIBLIOTEKI CRYPTOGRAPHY
from cryptography.fernet import Fernet
key = Fernet.generate_key()

print(key)

f = Fernet(key)
message = b"Tutaj tajne dane"
encrypted = f.encrypt(message)
print(encrypted)

f = Fernet(key)
print(f.decrypt(encrypted))

