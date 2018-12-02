# Вычисление сложного процента
# Входные данные:
# t - колличество лет;
# P - основная сумма вклада;
# r - ежегодная процентная ставка

# Флормула: Pe^(rt)

import sys
import math

t = int(sys.argv[1])
P = int(sys.argv[2])
r = float(sys.argv[3])

Sum = P * math.exp(t*r)
print('Сумма вклада со сложным процентом: ' + str(Sum) )