import numpy as np
import matplotlib.pyplot as plt
from collective_function import collective_width

# #  программа которая рассчитывает фрактальную размерность аттрактора. Необходимо восползоваться программой,
# которая считает ширину отрезка collective_function
# известна минимальное значение и максимальное значение. Необходимо покрыть гиперкуб гиперкубиками

# parametr
el, it = 3, 1500
start_it = 500
d = .25
alpha = .6
beta = 0
nonlinear = 'piece'
a = 0
delta = 1


def shift(el, it, start_it, d, a, alpha, beta, nonlinear):
    matrix = collective_width(el, it, start_it, d, a, alpha, beta, nonlinear)
    minim = matrix.min()
    maxim = matrix.max()

    mean = abs((maxim - minim) / 2)
    matrix = matrix + abs(minim) - mean
    return matrix


def fractal_dimenshion(el, it, start_it, d, a, alpha, beta, nonlinear, delta):
    s = 0
    elements = shift(el, it, start_it, d, a, alpha, beta, nonlinear)
    minim = elements.min()
    maxim = elements.max()
    # mean = abs(maxim - minim)/2
    quant = 2 ** el  # количество элементов, начинаем с двух
    epsilon = abs(maxim) + abs(minim)
    accurancy = 100
    step = 2

    while accurancy > delta:
        quant_el = 0
        mem = np.zeros((quant, el))
        epsilon = epsilon / 2
        for i in range(it - start_it):

            save = np.zeros(el)
            for j in range(el):
                eq = -(abs(maxim) + abs(minim)) / 2
                for k in range(step):
                    if eq + epsilon > elements[j][i] > eq:
                        save[j] = k + 1
                        break
                    elif elements[j][i] == eq and k != 0 and k != step - 1:
                        save[j] = k + 1
                        break
                    elif elements[j][i] == eq and k != 0 and k == step - 1:
                        save[j] = k
                        break
                    elif elements[j][i] == eq and k == 0:
                        save[j] = k + 1
                        break
                    else:
                        eq += epsilon

            test = []
            test1 = np.zeros(el)
            for i in range(el):
                test.append(save[i])
            for i in range(quant):
                for j in range(el):
                    if test[j] == mem[i][j]:
                        s = 1

                    else:   
                        s = 0
                        break
                print(test, mem[i])
                if s == 1:
                    quant_el += 1
                    break


        print(quant_el)
        accurancy /= 2
        quant = quant * (2 ** el)
        step *= 2

fractal_dimenshion(el, it, start_it, d, a, alpha, beta, nonlinear, delta)
