'''numbers =[1,2,3,4,5,7,8,9]
numbers1 = [x ** 2 for x in numbers if x % 2 != 0]

print(numbers1)
def fun1(x):
    return x * x
numbers2 = list(map(lambda x : x * 2, numbers))
numbers3 = list(map(fun1,numbers))
print(numbers2)
print(numbers3)

def fun2(x):
    return x % 2 == 0

numbers4 = list(filter(fun2,numbers))
numbers5 = list(filter(lambda x: x% 2==0,numbers))
print(numbers4)
print(numbers5)

from functools import reduce
numbers6 = reduce(lambda x, y: x if x>y else y, numbers)
print(numbers6)
b=10
example = "2+2-1+b"
result = eval(example)
print(result)
code = """
for i in range(3):
    print("witaj ", i)
"""
exec(code)
'''
import re
from collections import Counter

text = "The argparse module makes it easy to write user-friendly command-line interfaces. The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv. The argparse module also automatically generates help and usage messages. The module will also issue errors when users give the program invalid arguments"
listo3 = text.split()
def filto(x):
    if (x == "a" or x =="the" or x=="I" or x=="to" or x=="The"):
        x="0"
    else:
        return x
listo = list(filter(filto,listo3))
print(listo)
ilosSlow = len(listo)
listozda = re.split(r'[.!?]+', text)
listoakapit = text.split("\n")
ilozdan = len(listozda)
iloakapit = len(listoakapit)
listo2 = listo
print(ilosSlow,ilozdan,iloakapit)
counterlist = Counter(listo)
mostBrords = counterlist.most_common(3)
print(mostBrords)

def reo(listi,last):
    for x in listi:
        if x[0]=='a' or x[0]=='A':
            x = x[slice(None, None, -1)]
        last.append(x)

listoronto = []
reo(listo,listoronto)
print(listoronto)