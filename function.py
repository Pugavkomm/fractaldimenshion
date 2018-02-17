'''поместим необходимые функции нашей задачи. А точнее кубическую функцию для нелинейности,
все отображение...'''


# зададим кусочно линейную функцию
def piecewise_line(u, beta=0.5, alpha=0.2):
    if u < .5:
        return -alpha * 2 * u + beta
    elif u > .5:
        return -alpha * 2 * (u - 1) + beta
    else:
        print("Попали на разрыв")


# кубичческая функция:
# параметр a отвечает за положение корня, позволяет управлять нашей функцией

def nonlin_func(a, u, alpha=1):
    return alpha * u * (u - a) * (1 - u)


# создадим функцию задающю отображение
# необходимые действия связанные с номером элемента проведем уже в основной части программы

def next_iter(a, d, early, present, next, alpha=1, beta=0, nonlin='cube'):
    if nonlin == 'cube':
        return present + d * (next - 2 * present + early) + nonlin_func(a, present, alpha)
    if nonlin == 'piece':
        return present + d * (next - 2 * present + early) + piecewise_line(present, beta, alpha)


# функция для системы записанной в новых переменных, дл решения в виде стационарных волн

def stat_iter(a, d, x, y, alpha=1):
    return (d * x + (1 - 2 * d) * y + nonlin_func(a, y, alpha)) / (1 - d)


# статическое решение

def static_iter(a, d, x, y, alpha=1):
    # print(2*y - alpha/d*nonlin_func(a, y, alpha) - x)
    return 2 * y - alpha * nonlin_func(a, y, alpha) / d - x


def two_c_stat_solve_piecewise(d, alpha, beta, x_four, x_three, x_one, c=2):
    return (x_four - (1 - 2 * d) * x_three - x_one - alpha * piecewise_line(x_three, beta, alpha)) / d
