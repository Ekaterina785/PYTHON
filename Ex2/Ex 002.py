n = int(input('Введите трехзначное число'))
a1 = n % 10
n = n // 10
a2 = n % 10
n = n // 10
a3 = n
print (a1 + a2 + a3)