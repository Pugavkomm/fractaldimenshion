import numpy as np
import function


# зададим систему, но граничные условия будут давать отрезок

def segment(quant_el=100, quant_it=110, d=0.4, a=0.5, alpha=1, beta=0, nonlinear='cube'):
    elements = np.zeros((quant_el, quant_it))
    # for i in range(40, 60):
    # elements[i][0] = .01
    elements[1][0] = .1
    for i in range(quant_it - 1):
        for j in range(quant_el):
            if j == 0:
                elements[j][i + 1] = function.next_iter(a, d, 0, elements[j][i], elements[j + 1][i], alpha, beta,
                                                        nonlinear)
            elif j == quant_el - 1:
                elements[j][i + 1] = function.next_iter(a, d, elements[j - 1][i], elements[j][i], 0, alpha, beta,
                                                        nonlinear)
            else:
                elements[j][i + 1] = function.next_iter(a, d, elements[j - 1][i], elements[j][i], elements[j + 1][i],
                                                        alpha, beta, nonlinear)
    return elements
