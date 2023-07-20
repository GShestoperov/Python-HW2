# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input("Введите N: "))
power = 1

print("Числа 2**k: ")
if N >= 1:
    print(1)
while power * 2 < N:
    power *= 2
    print(power)
