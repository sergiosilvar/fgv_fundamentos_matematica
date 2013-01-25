'''
Created on 25/01/2013

@author: sergio

Sequencia de Gray
'''

def gray(quantidade=2):
    if quantidade <> 2:
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
    print gray(5)