n = int(input('Введите шестизначное число'))
a1 = n % 10
n = n // 10
a2 = n % 10
n = n // 10
a3 = n % 10
n = n // 10
a4 = n % 10
n = n // 10
a5 = n % 10
n = n // 10
a6 = n % 10
if ((a1 + a2 + a3) == (a4 + a5 + a6)): 
    print ("Yes")
else: 
    print ("No")