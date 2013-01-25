# -*- coding: iso-8859-15 -*-
'''
Created on 25/01/2013

@author: sergio

exercicio 12, permutacoes com até 18 números
'''

def permutacao(n):
    resultado = []
    if n == 1:
        resultado.append([n])
    else:
        permutacao_anterior = permutacao(n-1)
        resultado.append(permutacao_anterior + [n])
        resultado.append([n] + permutacao_anterior)
        
    return resultado
if __name__ == '__main__':
    print permutacao(3)
    #print [1,2,3]+[4,5,6]