n = int(input('Введите трехзначное число'))
n_sum = 0
while n:
    n_sum +=n % 10
    n //= 10
print(n_sum)

