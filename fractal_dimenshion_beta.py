import numpy as np
import matplotlib.pyplot as plt
from collective_function import collective_width
import multiprocessing
import pylab

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
    elements = shift(el, it, start_it, d, a, alpha, beta, nonlinear)  # реализация, причем сдвинута
    minim = elements.min()
    maxim = elements.max()
    #  зададим начальные значения итераций
    quantstep = 2  # начальное количство отрезков по каждой переменной, в последствии умножается на 2
    epsilon = abs(maxim) + abs(minim)
    step = epsilon / 2  # шаг, c которым идем по отрезкам (он же равен стороне отрезка)
    # создаем переменные для работы с гиперкубиками:
    accurancy = 10  # задаем исходную точность для начала цикла
    s = 0  # переменная характеризующая включение для того, чтобы определять попала ли точка в новый кубик или нет
    itstep = it - start_it  # так как выкидываем начало, то смещаем количество итераций
    points = 6 # количество итераций (делений стороны на 2)
    x = np.zeros(points)
    y = np.zeros(points)
    for l in range(points):  # основной цикл, в нем происходит деление пополам
        quant = 0
        # пербираем все элементы и проверяем попали ли они в гиперкубик
        for i in range(itstep):
            save1 = np.zeros(el)
            for j in range(el):
                EqLeft = minim
                for k in range(quantstep):
                    if EqLeft <= elements[j][i] <= EqLeft + step:
                        save1[j] = k + 1
                        break
                    elif elements[j][i] == maxim or elements[j][i] == minim:
                        save1[j] = k + 1
                        break

                    else:
                        EqLeft += step
## Для проверки не будем использовать стандартные алгоритмы, а упростим задачу на случай обобщений на любую размерность
## пространства, будем обозначать гиперкубики индивидуальными нумерами и сравнивать их с определенной точкой. Так
## как проверяется принадлежность каждой точки опр. кубику. Если точка принадлежит гиперкубику, которого не было раньше
## значит мы добавляем в счетчик количества кубиков +1, а так же запоминаем его, для дальнейшего сравнения
            if i == 0:
                save = save1
                quant += 1
                s = 1
            else:
                for j in range(quant):
                    symbol1 = ''
                    symbol2 = ''
                    for k in range(el):
                        if save1[k] == 0.:
                            print("EHAAA")
                        symbol1 += str(int(save1[k]))
                        if quant > 1:
                            symbol2 += str(int(save[j][k]))
                        else:
                            symbol2 += str(int(save[k]))
                    if symbol2 == symbol1:
                        s = 1
                        break
                    else:
                        s = 0
            if s == 0:
                quant += 1
                save = np.vstack((save, save1))
        x[l] = np.log(step)
        y[l] = np.log(quant)
        D = -np.log(quant) / np.log(step)
        D2 = D
        quantstep *= 2
        step /= 2
    m, b = pylab.polyfit(x, y, 1)
    #pylab.plot(x, y, 'yo', x, m*x+b, '--k')
    #pylab.show()
    print('d = ', d, ', m = ', -m)
    return -m
var_d = np.arange(.46, .47, .0001)
x = np.zeros(len(var_d))
y = np.zeros(len(var_d))
for i in range(1):
    def func(d):
        el, it = 7, 4000
        start_it = 1000
        alpha = .2
        beta = 0
        nonlinear = 'piece'
        a = 0
        delta = .1
        return fractal_dimenshion(el, it, start_it, d, a, alpha, beta, nonlinear, delta)
    d = var_d
    pool = multiprocessing.Pool(processes=3)
    y = pool.map(func, d)
plt.plot(var_d, y, '.', linestyle='--')
plt.savefig('img')
plt.show()
