# -*- coding: iso-8859-15 -*-
'''
Created on 25/01/2013

@author: sergio

exercicio 12, permutacoes com até 18 números
'''
import datetime
import logging
import sys

  
def permutacao(conjunto):
    # Condicao de parada do algoritmo.
    if len(conjunto) <= 1:
        return [conjunto]
    r = []
    
    # Percorre todos os elementos do conjunto
    for i in range(len(conjunto)):
       # Cria subconjunto dos primeiros i-1 elementos do com os últimos i+1 elementos.
        subconj =  conjunto[:i] + conjunto[i+1:]
        p = permutacao(subconj)
        for x in p:
            r.append(conjunto[i:i+1] + x)
    return r        

if __name__ == '__main__':
#ENTRADA
    n = 10

# INICIO DO PROGRAMA    
    if n >10: 
        print "ALERTA: Este computador NAO tem capacidae para n > 10!!"
        sys.exit()
    s = "INÍCIO para n="+str(n)+": " + str(datetime.datetime.now())
    f = open(".\\saida\\permutacao_n_%s.txt" %(n),"w")
    print s 
    f.write(s+'\n')
    for item in permutacao([i for i in range(n)]):
        f.write(str(item)+'\n')
    s = "FIM   para n="+str(n)+": " + str(datetime.datetime.now())
    f.write(s)
    f.close()
    print s