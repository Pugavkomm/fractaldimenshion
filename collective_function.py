import numpy as np
from segment_function import segment


# # принимает на вход параметры и возвращает массив с данными, в которых содержится максимальная и минимальная ширина
#  отрезка, # и реализация. Возвращаемый массив состоит из: # реализцийй, т.е. el строчек и it столбцов,
# но содержится дополнительная строка, которая содержит в начале # минимальное и максимальное значение в реализции,
# сделано для удобства, чтобы работать лишь с одной функцией и одним массивом

def collective_width(el, it, start_it, d, a, alpha, beta, nonlinear):
    elements = segment(el, it, d, a, alpha, beta, nonlinear)  # реализация
    for i in range(el):  # заполняем массив элементами реализции с опр. момента времени
        if i == 0:  # отбарсываем начало, можно было сделать удобнее, но везде используется segment, нет смыслла
            # переписывать его заного
            matrix = elements[i][start_it:]
        else:
            matrix = np.vstack((matrix, elements[i][start_it:]))
    del elements
    return matrix

