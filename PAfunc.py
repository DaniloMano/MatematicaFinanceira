# Atividade nº 1 do Professor Márcio:
# fazer função simples de PA em python usando linspace como no exemplo do professor:
# Implementação de exemplo:
# np.linspace(a,b,n)
# vetor
# a1=1
# a100=10
# n=100
# r=?
# an = a1+ (n-1)*r
# r=(an-a1)/(n-1)

import numpy as np


def pa(a,b,n):
    r = np.linspace(a,b,n)
    return r

def np_result(a1, a100, n):
    pa_result = pa(a1, a100, n)
    return pa_result

def hard_result(a1, a100, n):
    r = (a100 - a1) / (n - 1)
    pa_array = []
    for i in range(n):
        an = a1 + i * r
        pa_array.append(an)
    return pa_array
    

def compare_results(a1, a100, n):
    np_r = np_result(a1, a100, n)
    hard_r = hard_result(a1, a100, n)
    print("Resultado usando np.linspace:", np_r)
    print("Resultado usando fórmula direta:", hard_r)
    if (np.array_equal(np_r, hard_r)) == True:
        print("Os resultados são iguais. Glória, essa budega ta funcionando")
    if (np.array_equal(np_r, hard_r)) == False:
        print("Os resultados são diferentes. Ô cagada grande visse")

a1 = 1
a100 = 10
n = 100

compare_results(a1, a100, n)