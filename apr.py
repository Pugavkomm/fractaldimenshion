import scipy as sp
import matplotlib.pyplot as plt
def mnkGP(x,y):
    d=1 # степень полинома
    fp, residuals, rank, sv, rcond = sp.polyfit(x, y, d, full=True) # Модель
    f = sp.poly1d(fp) # аппроксимирующая функция


    return fp[1]
