import random
#1 Напишіть функцію аddRightDigit (d, k), яка повинна додавати до цілого позитивного числа K справа цифру D (D - цілочисельне значення в діапазоні 0-9, К - цілочисельне значення).
def add_right_digit(d,k):
    return k * 10 + d

kx = 12
d1 = 3
d2 = 5
print('kx = ' , kx)
kx = add_right_digit(d1, kx)
print('kx after adding d1 : ',kx)
kx = add_right_digit(d2,kx)
print('kx after adding d2 : ' , kx)

print('-------------')

#2 Напишіть функцію, яка приймає два цілих числа n і k і повертає число, що містить k перших цифр числа n.
def number_return(n = random.randint(1000, 100000), k = random.randint(1, 4)):
    if isinstance(n, int) and isinstance(k, int):
        return str(n)[:k]
print(number_return())
