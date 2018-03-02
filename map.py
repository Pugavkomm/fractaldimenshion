import numpy as np
import matplotlib.pyplot as plt
from segment_function import segment
beta = 0
var_d = np.arange(0,1,.01)
var_alpha = np.arange(0,1,.01)
N  = 100
it = 1000
start_it = 500
for i in range(len(var_alpha)):
    for j in range((var_alpha)):
        matrix = segment(N, it, var_d[i], 0, var_alpha[j], beta, nonlinear='piece')
        for k in range(N):
            for m in range(it):
