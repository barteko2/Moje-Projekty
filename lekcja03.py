#!!!!!!!!!!!!!!!!!!GENERATORY -YIELD!!!!!!!!!!!!!!!!!!!!!!!!!!
import sys

print("!!!!!!!!!!!!!!!!!!!GENERATORY")
def count():
    n=0
    while True:
        n += 1
        yield n

counter = count()
print(counter)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

#!!!!!!!!!!!!!!!!ciąg fibonacciego
print("CIĄG FIBONACCIEGO")
def fib():
    first = 0
    last = 1
    while True:
        first, last = last, first+last
        yield first

f = fib()
for x in f:
    print(x)
    if x>100:
        break
'''print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))'''
#!!!!!!!!!!!!!!!!!GENERATORY SKŁADANE!!!!!!!!!!!!!!!!!!!!!!!!!
list_o_nums = [x for x in range(100)]
gen_o_nums = (x for x in range(100))
print(next(gen_o_nums))
print(next(gen_o_nums))
print(list_o_nums)
print(gen_o_nums)

#!!!!!!!!!sprawdzenie która metoda jest bardziej wydajna:
print(sys.getsizeof(list_o_nums))
print(sys.getsizeof(gen_o_nums))


