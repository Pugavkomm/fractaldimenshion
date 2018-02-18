import numpy as np
import matplotlib.pyplot as plt
from collective_function import collective_width
import sklearn.linear_model as lm
# #  программа которая рассчитывает фрактальную размерность аттрактора. Необходимо восползоваться программой,
# которая считает ширину отрезка collective_function
# известна минимальное значение и максимальное значение. Необходимо покрыть гиперкуб гиперкубиками

# vars
el, it = 3, 2000

start_it = 900
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
    #print(epsilon)
    step = epsilon / 2
    # создаем переменные для работы с гиперкубиками:
    accurancy = 10  # задаем исходную точность для начала цикла
    D1 = -10000
    s = 0
    x = []
    y = []
    Quant1 = 1000
    Quant = 10
    res = 10
    n = 1
    o = 0
    while abs(res) > .0001:
        o+=1
        #print('oy')


        VarCube = np.zeros((QuantCube, el))

        mem = ['']  # переменная для хранения символов кубов

        for i in range(it):
            save = np.zeros(el)  # переменная для сохранения индексов кубика
            ##  На каждой итерации создаем эту переменную, чтобы не занимать слишком много памяти, она будет
            ##  хранить данные только для одной итерации
            for j in range(el):
                EqLeft = -(epsilon) / 2  # минимальное значение на переменной
                for k in range(QuantStep):
                    if EqLeft < elements[j][i] < EqLeft + step:
                        #print('good')
                        #symbol += str(k + 1)  # индекс на одной из осей
                        save[j] = k + 1
                        break
                    elif elements[j][i] == EqLeft:
                        #symbol += str(k + 1)
                        save[j] = k + 1
                        #print('попадание на границу гиперкубов')  # необходимо в последствие учесть это и считать,
                        # что в этом случае принадлежит обоим кубикам данная точка
                        break
                    elif elements[j][i] == EqLeft + epsilon:
                        save[j] = k + 2
                    elif elements[j][i] == EqLeft:
                        save[j] = k + 1
                    elif elements[j][i] < EqLeft:
                        print("CHERNYA")
                        #print('попадание на границу гиперкубов')
                    EqLeft += step

            '''
            #print(symbol)
            if i == 0:
                mem.append(symbol)
                s = 1
            elif i!= 0:
                for k in range(len(mem)):
                    if mem[k] == symbol:
                        #print(mem)
                        s = 0
                        break
                    elif mem[k] != "" and mem[k] != symbol:
                        mem.append(symbol)
                        s = 1
            if s == 1:
                #print('yes')
                Quant += 1'''
            symbol1 = ''

            if i == 0:
                for j in range(el):
                    VarCube[0][j] = save[j]
            else:
                for j in range(QuantCube):
                    symbol2 = ''
                    for k in range(el):
                        if j == 0:
                            if save[k] == 0:
                                print('error')

                            symbol1 += str(save[k])
                            symbol2 += str(VarCube[j][k])
                        else:
                            symbol2 += str(VarCube[j][k])
                    if symbol2 == symbol1:
                        s = 1
                        break
                    else:
                        s = 0

            if s == 0:
                Quant += 1

        D = - np.log(Quant)/np.log(step)

        #print(D)
        if n == 1:
            n += 1
        else:
            n *= 2
        QuantCube = (2 ** el) ** n
        QuantStep = QuantStep * 2
        #print(step)
        step /= 2
        #accurancy = abs(D1 - D)/abs(D)
        x.append(np.log(Quant))
        y.append(np.log(step))
        res = Quant1 - Quant
        print(Quant1, Quant)
        Quant1 = Quant
        if o > 5:
            plt.plot(y,x, '.')
            plt.show()

    print(x,y)
    skm = lm.LinearRegression()
    skm.fit(y, x)
    print('coef', skm.coef_)
    return D




var_d = np.arange(.47 , .49, .0001)
x = np.zeros(len(var_d))
y = np.zeros(len(var_d))
for i in range(len(var_d)):
    d = var_d[i]

    y[i] = fractal_dimenshion(el, it, start_it, d, a, alpha, beta, nonlinear, delta)
    #print(y[i])
    #print(d)
plt.plot(var_d,y,'.')
plt.show()