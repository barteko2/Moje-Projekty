# NAPISZ FUNKCJĘ PYTHONA, KTÓRA PRZYJMUJE JAKO ARGUMENT NAZWĘ I WYŚWIETLA JĄ

def show_title(title):
    print(title)


show_title("odbyt")


# NAPISZ FUNKCJĘ PYTHONA KTÓRA PRZYJMUJE CIĄG JAKO ARGUMENT I INFORMUJE CZY TEN CIĄG JEST NAPISANY WIELKIMI CZY MAŁYMI LITERAMI

def check_title(title):
    if title.islower(): print("to są małe litery")
    elif title.isupper(): print("to są wielkie litery")
    else: print("mieszane")

check_title("NAP")

def lista_skladana(wyraz):
    skladana = [list(wyraz) for i in range(1)]
    return skladana

print(lista_skladana("i ja ciebie też"))


def parzysta_nieparzysta():
    n = 0
    for i in range(10):
        n += 1
        yield n % 2

czyparzysta = parzysta_nieparzysta()

for i in czyparzysta:
    if(i % 2 == 0):
        print("parzysta")
    else:
        print("nieparzysta")



