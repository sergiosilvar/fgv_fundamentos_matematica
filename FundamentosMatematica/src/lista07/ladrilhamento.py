# -*- coding: iso-8859-15 -*-
'''
Created on 25/01/2013

@author: sergio
'''

import Image

def ladrilharL(n, coord_ocupada):
    """Retorna um array de coordenadas para o ladrilhamento em L de um piso de tamanho
    2^n x 2^n quadrados, onde um quadrado é ocupado por algo."""
    if n <2: 
        print "O valor de \'n\' deve ser maior do que 1."
    else: 
        tamanhoLado = pow(2,n)
        tamanhoArea = tamanhoLado*tamanhoLado
        
        return tamanhoLado, tamanhoArea

if __name__ == '__main__':
    print ladrilharL(3,(0,0))