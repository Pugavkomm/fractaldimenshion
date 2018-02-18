import numpy as np
import matplotlib.pyplot as plt
from collective_function import collective_width

# #  программа которая рассчитывает фрактальную размерность аттрактора. Необходимо восползоваться программой,
# которая считает ширину отрезка collective_function
# известна минимальное значение и максимальное значение. Необходимо покрыть гиперкуб гиперкубиками

# vars
el, it = 10, 1500
start_it = 500
d = .25
alpha = .6
beta = 0
nonlinear = 'piece'
a = 0
delta = 1


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
    while accurancy > delta:
        mem = ['']  # переменная для хранения символов кубов
        Quant = 0
        for i in range(it):
            save = np.zeros(el)  # переменная для сохранения индексов кубика
            ##  На каждой итерации создаем эту переменную, чтобы не занимать слишком много памяти, она будет
            ##  хранить данные только для одной итерации
            symbol = ""
            for j in range(el):
                EqLeft = -(epsilon) / 2  # минимальное значение на переменной
                for k in range(QuantStep):
                    if EqLeft < elements[j][i] < EqLeft + step:
                        symbol += str(k + 1)  # индекс на одной из осей
                        break
                    elif elements[j][i] == EqLeft:
                        symbol += str(k + 1)
                        save[j] = k + 1
                        #print('попадание на границу гиперкубов')  # необходимо в последствие учесть это и считать,
                        # что в этом случае принадлежит обоим кубикам данная точка
                        break
                    EqLeft += step
            if i == 0:
                mem.append(symbol)
                s = 1
            elif i!= 0:
                for k in range(len(mem)):
                    if mem[k] == symbol:
                        print(mem)
                        s = 0
                        break
                    elif mem[k] != "" and mem[k] != symbol:
                        s = 1
            if s == 1:
                #print('yes')
                Quant += 1







fractal_dimenshion(el, it, start_it, d, a, alpha, beta, nonlinear, delta)
