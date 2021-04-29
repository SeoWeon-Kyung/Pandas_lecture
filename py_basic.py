import sys
import decimal
a = 10
b = 3.14

a = sys.maxsize
b = sys.maxsize + 100
print(f'{a}, {b}')

string = 'Hello Python!'

print(string[4::-1])

a, b, c = 3, 25, 2
print(a + b)
print(a / b)

d = 0.1 + 0.1 + 0.3 - 0.2
e = decimal.Decimal('0.1')
print(f'{d}, {e}')

#list
a = [1, 2, 3]
b = [4, 5, 6]

print(a*3)
print(a+b)

c = list(n*2 for n in range(1, 11)) #리스트 컴프리헨션
print(c)

#Tuple
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[4::-1])
print(a[0::2])

tu_a = (1, 2, 3)

#Dictionary
a = {'name': 'TV', 'price': 100000}
a['price']=1200000
print(a['price'])

#Set -  중복 삭제 
a = {1, 2, 3, 4, 4, 5}
print(a)
b = list(a)
print(b[0])

class Calc():
    def __init__(self, a, b):
        self._a = a
        self._b = b
    
    def add(self):
        return self._a + self._b
    
    def multi(self):
        return self._a * self._b

calc = Calc(3, 4)
add_num = calc.add()
multi_num = calc.multi()
print(f'add: {add_num}, mul: {multi_num}')


