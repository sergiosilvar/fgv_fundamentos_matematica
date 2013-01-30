# -*- coding: iso-8859-15 -*-
'''
Created on 25/01/2013

@author: sergio

Sequencia de Gray
'''



def gray(quantidade=2):
    if quantidade >= 2:
        lista = gray(quantidade-1) 
        listaComZero = []
        listaComUm = []
        for elemento in lista: #passo 2
            listaComZero.append("0"+elemento) #passo 2A 
            listaComUm.append("1"+elemento) # passo2B
        listaComUm.reverse() #passo 2C
        return listaComZero+listaComUm #passo 2D
    else:
        return ["0","1"]
    
    

if __name__ == '__main__':
# rENTRADA
    n = 6

# INICIO DO PROGRAMA    
    arquivo = ".\\saida\\gray_n_%s.txt" %(n)
    f = open(arquivo,"w")
    codigo= gray(n)
    for i in codigo:
        f.write(i+'\n')
    f.close()
    print "Arquivo criado em " + arquivo
    print "FIM DO PROGRAMA"