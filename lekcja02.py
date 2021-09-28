import re

items = [[0, 'a', 2], [5, 'b', 0], [2, 'c', 1]]
print(sorted(items))


def second(item):
    '''zwraca item[1]'''
    return item[1]


# !!!!!!!!!!!!!!!!!!!!sortowanie według 2 elementu, czyli abc
print(sorted(items, key=second))

###!!!!!!!!!!!!!!!!!osiągnięcie tego samego za pomocą metody lambda - metoda stosowana tylko w przypadku prostych zwróceń:
print("sortowanie za pomocą lambdy")
print(sorted(items, key=lambda item: item[1]))
print(sorted(items, key=lambda item: item[2]))
#############!!!!!!!!!!!!!lambdy są mniej czytelne, stosujemy je bardzo rzadko

cc_list = '''Bartek Oberc<boberc@gmail.com>,
Roman Polanski<rpolanski@gmail.com>,
Henryk Sienkiewicz<hsienkiewicz@gmail.com>,
Bob Marley<bmarley@gmail.com>
'''
print("sprawdzam czy na liście cc_list jest gość o imieniu roman:")
print('Roman' in cc_list)

#!!!!!!!!!!!!!!!A TERAZ ROBIMY TO SAMO TYLKO ZA POMOCĄ BIBLIOTEKI RE(REGEX)
print("wynik szukania przez re.search: ")
print(re.search(r'Bartek', cc_list))

#!!!!!!!!to samo tylko z instrukcją if
if(re.search(r'Bartek',cc_list)):
    print('znaleziono imię Bartek')

#!!!!!!!!!grupy nazwane
print("GRUPY NAZWANE\n")
matched = re.search(r'(?P<nazwa>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)',cc_list)
print(matched.group('nazwa'))
matched.group(0)
matched.group(1)
matched.group(2)
matched.group(3)

print(f'''nazwa: {matched.group("nazwa")}
Domena pomocnicza: {matched.group("SLD")}
Domena główna:{matched.group("TLD")}''')

#!!!!!metoda findall zwraca wszystkie znalezione wartości!!!
matched = re.findall(r'\w+\@\w+\.\w+',cc_list)
print(matched)
print("a teraz dzieli wszystko na grupy")
matched_dz = re.findall(r'(\w+)\@(\w+)\.(\w+)',cc_list)
podzielone_na_grupy=matched_dz
print(matched_dz)

ends = [x[2] for x in matched_dz]
print("wszystkie końcówki adresów: "+str(ends))

#!!!!!!!!!!!!!!!METODA FINDITER!!!!!!!!!!!!!!!!!!! metoda szuka, a jak już znajdzie to się zatrzymuje
matched_finditer = re.finditer(r'\w+\@\w+\.\w+', cc_list)
print("A TERAZ FINDITER")
print(matched_finditer)
print(next(matched_finditer))
print(next(matched_finditer))
print(next(matched_finditer))
print(next(matched_finditer))

#a teraz finditer tylko w pętli FOR
matched_for = re.finditer("(?P<nazwa>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)",cc_list)
for m in matched_for:
    print(m.groupdict())

#!!!!!!!!!!!!!!!!!!!!!re.sub - podstawianie!!!!!!!!!!!!!!!!!
print("!!!!!!!!!!!!!PODSTAWIANIE RE.SUB")
print(re.sub("\d", "#", "wprowadziłeś kod 09876"))
users = re.sub("(?P<nazwa>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)", "\g<TLD>.\g<SLD>.\g<nazwa>", cc_list)      #podstawiło poszczególne grupy w innych miejscach
print(users)
'''
wynik:
Bartek Oberc<com.gmail.boberc>,
Roman Polanski<com.gmail.rpolanski>,
Henryk Sienkiewicz<com.gmail.hsienkiewicz>,
Bob Marley<com.gmail.bmarley>
'''

#!!!!!!!!!!!!!!!!KOMPILOWANIE DO OBIEKTU ZAPEWNIA WZROST WYDAJNOŚCI
regex = re.compile(r'\w+\@\w+\.\w+')
print(regex.search(cc_list))

