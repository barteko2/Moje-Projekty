import re
line = '127.0.0.1 - rj [08/Nov/2019:14:43:30] "GET HTTP/1.0" 200'

print(re.search(r'(?P<IP>\d+\.\d+\.\d+\.\d+)', line))

m = re.search(r'(?P<IP>\d+\.\d+\.\d+\.\d+)', line)
print("wypisz wartości z grupy IP")
print(m.group('IP'))

r = r'\[(?P<Time>\d\d/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})\]'
m = re.search(r, line)
print(m.group('Time'))

#!!!!!!!!!!!!!!!!!!jednoczesne pobieranie wielu elementów
r = r'(?P<IP>\d+\.\d+\.\d+\.\d+)'
r += r' - (?P<User>\w+) '
r += r'\[(?P<Time>\d\d/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})\]'
r += r' (?P<Request>".+")'
m = re.search(r, line)
print("\n#!!!!!!!!!!!!!!!!Wszystkie grupy w jednej linii:")
print(m.group('IP','User','Time','Request'))

print("problem")
reg = r'(?P<IP>\d+\.\d+\.\d+\.\d+)'
reg += r' - (?P<User>\w+) '
reg += r'\[(?P<Time>08/Nov/\d{4}:\d{2}:\d{2}:\d{2} [-+]\d{4})\]'
reg += r' (?P<Request>"GET .+")'
n = re.search(reg,line)
#print(n.group('IP','User','Time','Request'))
matched = re.finditer(reg, access_log)
for m in matched:
    print(n.group('IP'))