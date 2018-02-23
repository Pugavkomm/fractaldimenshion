import numpy as np
import matplotlib.pyplot as plt
from collective_function import collective_width
import multiprocessing


# #  программа которая рассчитывает фрактальную размерность аттрактора. Необходимо восползоваться программой,
# которая считает ширину отрезка collective_function
# известна минимальное значение и максимальное значение. Необходимо покрыть гиперкуб гиперкубиками


def shift(el, it, start_it, d, a, alpha, beta, nonlinear):
    ##  данная функция производит смещение, чтобы центр находился в нуле. Необходимо для упрощения обработки.
    matrix = collective_width(el, it, start_it, d, a, alpha, beta, nonlinear)
    minim = matrix.min()
    maxim = matrix.max()

    mean = abs((maxim - minim) / 2)
    matrix = matrix + abs(minim) - mean
    return matrix


def fractal_dimenshion(el, it, start_it, d, a, alpha, beta, nonlinear, delta):
    elements = collective_width(el, it, start_it, d, a, alpha, beta, nonlinear)
    minim = elements.min()
    maxim = elements.max()
    it = it - start_it
    #  зададим начальные значения итераций
    QuantStep = 2  # начальное количство отрезков по каждой переменной, в последствии умножается на 2
    epsilon = abs(maxim) + abs(minim)
    step = epsilon / 2
    # создаем переменные для работы с гиперкубиками:
    accurancy = 10  # задаем исходную точность для начала цикла
    s = 0
    n = 1
    itstep = it - start_it
    l = 0
    D2 = 10
    while accurancy > delta:
        l += 1
        Quant = 0
        for i in range(itstep):

            save1 = np.zeros(el)
            for j in range(el):
                EqLeft = minim
                for k in range(QuantStep):
                    if EqLeft <= elements[j][i] <= EqLeft + step:
                        save1[j] = k + 1
                        break
                    elif elements[j][i] == maxim or elements[j][i] == minim:
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
                        if save1[k] == 0.:
                            print("EHAAA")
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
        n *= 2
        D = -np.log(Quant) / np.log(step)
        accurancy = abs(D2 - D) / D
        D2 = D
        print(accurancy)
        QuantStep *= 2
        step /= 2
    return D


var_d = np.arange(.4, .46, .0001)
x = np.zeros(len(var_d))
y = np.zeros(len(var_d))
for i in range(1):
    def func(d):
        el, it = 20, 20000
        start_it = 1000
        alpha = .2
        beta = 0
        nonlinear = 'piece'
        a = 0
        delta = .01
        return fractal_dimenshion(el, it, start_it, d, a, alpha, beta, nonlinear, delta)


    d = var_d
    pool = multiprocessing.Pool(processes=4)
    y = pool.map(func, d)
plt.plot(var_d, y, '.', linestyle='--')
plt.savefig('img')
plt.show()
