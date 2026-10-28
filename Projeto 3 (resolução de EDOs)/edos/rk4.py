import numpy as np

def RK4(fun, y0, t_eval):
        '''
 Método de Runge-Kutta de quarta ordem para resolver dy/dt = f(t, y) com condição inicial y0.
 As soluções são calculadas nos instantes de tempo t_eval. Aqui y e o
 retorno da função f(t, y) devem ser compatíveis: ambos devem ser 
 escalares, ou ambos devem ser arrays do mesmo formato.
 INPUT
 fun (callable): Função f(t, y) que define a EDO.
 y0 (float ou array): Condição inicial.
 t_eval (iterable): Instantes de tempo nos quais a solução será calculada.
 OUTPUT
 y (array): Valores aproximados da solução nos instantes de t_eval.
 ''' 
        dt = t_eval[1] - t_eval[0]

        y = [y0]

        for t in t_eval[:-1]:

                y_last = np.array(y[-1])
                
                k1 = fun(t , y_last)
                k2 = fun(t + dt/2, y_last + k1*dt/2)
                k3 = fun(t + dt/2, y_last + k2*dt/2)
                k4 = fun(t + dt, y_last + dt * k3)

                y.append(y_last + dt/6 *(k1 + 2*k2 + 2*k3 + k4))

        y = np.array(y)

        return y



                