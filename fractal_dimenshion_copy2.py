import numpy as np
import numpy.linalg as linalg
import matplotlib.pyplot as plt
from collective_function import collective_width
import sklearn.linear_model as lm
import apr

# #  программа которая рассчитывает фрактальную размерность аттрактора. Необходимо восползоваться программой,
# которая считает ширину отрезка collective_function
# известна минимальное значение и максимальное значение. Необходимо покрыть гиперкуб гиперкубиками

# vars
el, it = 7, 9000

start_it = 2000
d = .25
alpha = .2
beta = 0
nonlinear = 'piece'
a = 0
delta = .1


def shift(el, it, start_it, d, a, alpha, beta, nonlinear):
    ##  данная функция производит смещение, чтобы центр находился в нуле. Необходимо для упрощения обработки.
    matrix = collective_width(el, it, start_it, d, a, alpha, beta, nonlinear)
    minim = matrix.min()
    maxim = matrix.max()

    mean = abs((maxim - minim) / 2)
    matrix = matrix + abs(minim) - mean
    return matrix


def fractal_dimenshion(el, it, start_it, d, a, alpha, beta, nonlinear, delta):
    elements = shift(el, it, start_it, d, a, alpha, beta, nonlinear)
    minim = elements.min()
    maxim = elements.max()
    it = it - start_it
    #  зададим начальные значения итераций
    QuantCube = 2 ** el  # начальное количество кубиков
    QuantStep = 2  # начальное количство отрезков по каждой переменной, в последствии умножается на 2
    epsilon = abs(maxim) + abs(minim)
    step = epsilon / 2
    # создаем переменные для работы с гиперкубиками:
    accurancy = 10  # задаем исходную точность для начала цикла
    D1 = -10000
    s = 0
    x = []
    y = []
    Quant1 = 1000

    res = 10
    n = 1
    o = 8
    itstep = it - start_it
    x = []
    y = []
    for l in range(o):
        Quant = 0
        for i in range(itstep):
            save1 = np.zeros(el)
            for j in range(el):
                EqLeft = -(abs(maxim) + abs(minim)) / 2
                for k in range(QuantStep):
                    if EqLeft < elements[j][i] < EqLeft + step:
                        save1[j] = k + 1
                        break
                    elif elements[j][i] == EqLeft + step:
                        save1[j] = k + 1
                        break
                    else:
                        EqLeft += step

            if i == 0:
                save = save1
                Quant += 1
                s = 1
            else:
                for j in range(Quant):
                    symbol1 = ''
                    symbol2 = ''
                    for k in range(el):
                        symbol1 += str(int(save1[k]))
                        if Quant > 1:
                            symbol2 += str(int(save[j][k]))
                        else:
                            symbol2 += str(int(save[k]))
                    if symbol2 == symbol1:
                        s = 1
                        break
                    else:
                        s = 0
            if s == 0:
                Quant += 1
                save = np.vstack((save, save1))
        #print(Quant)
        if l > 0:
            x.append(np.log(step))
            y.append(np.log(Quant))
        n *= 2
        #QuantCube = (2 ** el) ** n
        QuantStep = QuantStep * 2
        step /= 2
        #res = Quant1 - Quant
    #D = -np.log(Quant)/np.log(step)
    #print(D)
    D1 = -apr.mnkGP(x,y)
    #plt.plot(x, y, '.')
    #plt.show()
    return D1


var_d = np.arange(.44 , .4801, .0001)

x = np.zeros(len(var_d))
y = np.zeros(len(var_d))
for i in range(len(var_d)):
    d = var_d[i]

    y[i] = fractal_dimenshion(el, it, start_it, d, a, alpha, beta, nonlinear, delta)
    print(y[i])
plt.plot(var_d,y,'.', linestyle = '--')
plt.show()