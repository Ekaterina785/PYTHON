n = int(input('n'))
m = int(input('m'))
k = int(input ('долек отломить: '))
if n * m - k == m or n * m - k == n or m * n - k == m * n // 2:
    print("yes")
else:
    print('no')