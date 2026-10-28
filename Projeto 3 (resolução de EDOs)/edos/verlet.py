import numpy as np

def Verlet(fun, xv0, t_eval):
    '''
    Método de Verlet para resolver dy/dt = f(t, y) com condição inicial y0.
    As soluções são calculadas nos instantes de tempo t_eval. Aqui y e o
    retorno da função f(t, y) devem ser compatíveis: ambos devem ser 
    escalares, ou ambos devem ser arrays do mesmo formato.
    INPUT
    fun (callable): Função f(t, y) que define a EDO.
    xv0 (float ou array): Condição inicial (posição e velocidade).
    t_eval (iterable): Instantes de tempo nos quais a solução será calculada.
    OUTPUT
    x (array): Valores aproximados da solução nos instantes de t_eval.
    '''

    n = len(xv0)//2
    x0 = xv0[:n]
    v0 = xv0[n:]
    
    dt = t_eval[1] - t_eval[0]

    x = [x0]

    x.append(x0 + v0*dt + 0.5*fun(t_eval[0], x0)*dt**2)

    for t in t_eval[1:-1]:
        x.append(2*x[-1] - x[-2] + fun(t, x[-1])*dt**2)

        return x