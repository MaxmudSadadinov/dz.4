n= int(input('Введите кол-во монет'))
O = 0
R = 0
for i in range(n):
    r = int(input('положение монет 0 или 1'))
    if r == 0 :
        O = O +1
    elif r==1:
        R = R + 1
min = min(O, R)
print (f'Кол-во монет, чтобы перевернуть: {min}')
        