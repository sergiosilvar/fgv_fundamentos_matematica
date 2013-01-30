'''
Created on 26/01/2013

@author: sergio


'''

import Image
import ImageDraw
import collections
import matplotlib.pyplot as plt
import numpy
import sys

# CONSTANTES
BILL = -1
PATH = ".\\saida"
COR_BORDA = "black"
TAM_BORDA=1
PIXEL = 50
LADO_QUAD = PIXEL

# FUNCOES
def validar_entradas(n, coordenada_Bill):
    if not valor_n_eh_correto(n):
        print "ALERTA: O valor de \'n\' deve ser maior do que 1."
        return 0
    elif not coord_ocupada_eh_correta(pow(2, n), coordenada_Bill):
        print "ALERTA: A coordenada ocupada por BILL " + str(coordenada_Bill) + " estah alem do tamanho da matriz: entre 0 e " + str(pow(2, n) - 1)
        return 0
    return 1

def valor_n_eh_correto(n):
    return n >= 1
        
def coord_ocupada_eh_correta(tamanho, coord_ocupada):
    x, y = coord_ocupada
    return x < tamanho and x >= 0 and y < tamanho and y >= 0

def criar_matriz(tam_lado, coord_Bill):
    # x = arange(16).reshape(4,4) #cria array multidim 4x4 de 0 a 15 
    matriz = numpy.zeros((tam_lado, tam_lado), int)
    matriz[coord_Bill] = BILL
    return matriz



def matriz_tem_coord_ocupada(matriz):
    return  (len(numpy.argwhere(matriz <> 0))) #argwhere retorna 0 quando nao encontra. where retorna 2.
    

def ocupa_coordenada(matriz, coord, id_L):
    matriz[coord] = id_L


def ladrilhar(matriz, ids_L ):
    tam_matriz = len(matriz)
    metade_tam_matriz = tam_matriz / 2
    id_L_ocupar = ids_L.popleft()
    if tam_matriz == 2:
        for i in range(tam_matriz):
            for j in range(tam_matriz):
                if matriz[i, j] == 0:
                    matriz[i, j] = id_L_ocupar
    elif tam_matriz > 2:
    # Ocupar os cantos centrais dos quadrantes que nao tem o Bill.
        quadrante_1 = matriz[0:metade_tam_matriz, 0:metade_tam_matriz]
        if not matriz_tem_coord_ocupada(quadrante_1):
            ocupa_coordenada(matriz,canto_quadrante_1(tam_matriz), id_L_ocupar)
        
        quadrante_2 = matriz[0:metade_tam_matriz, metade_tam_matriz:tam_matriz]
        if not matriz_tem_coord_ocupada(quadrante_2):
            ocupa_coordenada(matriz,canto_quadrante_2(tam_matriz), id_L_ocupar)
        
        quadrante_3 = matriz[metade_tam_matriz:tam_matriz, 0:metade_tam_matriz]
        if not matriz_tem_coord_ocupada(quadrante_3):
            ocupa_coordenada(matriz,canto_quadrante_3(tam_matriz), id_L_ocupar)
        
        quadrante_4 = matriz[metade_tam_matriz:tam_matriz, metade_tam_matriz:tam_matriz]
        if not matriz_tem_coord_ocupada(quadrante_4):
            ocupa_coordenada(matriz,canto_quadrante_4(tam_matriz), id_L_ocupar)
        
    # Ladrilhar os quadrantes.
        ladrilhar(quadrante_1, ids_L)
        ladrilhar(quadrante_2, ids_L)
        ladrilhar(quadrante_3, ids_L)
        ladrilhar(quadrante_4, ids_L)

def canto_quadrante_1(tamanho_matriz):
    metade_tam_matriz = tamanho_matriz/2
    return (metade_tam_matriz-1,metade_tam_matriz-1)

def canto_quadrante_2(tamanho_matriz):
    metade_tam_matriz = tamanho_matriz/2
    return (metade_tam_matriz-1,metade_tam_matriz)

def canto_quadrante_3(tamanho_matriz):
    metade_tam_matriz = tamanho_matriz/2
    return (metade_tam_matriz,metade_tam_matriz-1)

def canto_quadrante_4(tamanho_matriz):
    metade_tam_matriz = tamanho_matriz/2
    return (metade_tam_matriz,metade_tam_matriz)

        
def norte_eh_igual(matriz, row, col):
    if row == 0: return 0
    return matriz[row,col] == matriz[row-1,col]

def leste_eh_igual(matriz, row, col):
    if col == len(matriz)-1: return 0
    return matriz[row,col] == matriz[row,col+1]

def sul_eh_igual(matriz, row, col):
    if row == len(matriz)-1: return 0
    return matriz[row,col] == matriz[row+1,col]

def oeste_eh_igual(matriz, row, col):
    if col == 0: return 0
    return matriz[row,col] == matriz[row,col-1]



def pinta_borda(draw, x0, y0, x1, y1):
    return draw.line([x0, y0, x1, y1],fill="black")

def pinta_borda_norte(draw, row, col):
    x0 = col*LADO_QUAD
    y0 = row*LADO_QUAD
    x1 = x0+LADO_QUAD
    y1 = y0
    draw.line([(x0, y0),(x1,y1)],fill="black")


def pinta_borda_leste(draw, row, col):
    x0 = (col+1)*LADO_QUAD
    y0 = row*LADO_QUAD
    x1 = (col+1)*LADO_QUAD
    y1 = (row+1)*LADO_QUAD
    pinta_borda(draw, x0, y0, x1, y1)




def pinta_bill(draw, row, col):
    x0 = col*LADO_QUAD
    y0 = row*LADO_QUAD
    x1 = x0+LADO_QUAD
    y1 = y0+LADO_QUAD
    draw.rectangle([x0,y0,x1,y1],fill=COR_BORDA)


def criar_imagem(matriz,arquivo):
# Prepara dimensoes e objeto draw    
    DIM_MATRIZ = len(matriz)
    LADO_IMG = (DIM_MATRIZ*LADO_QUAD)+1
    img = Image.new("RGB", (LADO_IMG,LADO_IMG), "white")
    draw = ImageDraw.Draw(img)
    #draw.rectangle([0,0,LADO_IMG-1,LADO_IMG-1], outline=COR_BORDA)
# Desenha a grid
    draw.line([0,0,0,LADO_IMG-1],fill=COR_BORDA,width=TAM_BORDA)
    draw.line([LADO_IMG-1,0,LADO_IMG-1,LADO_IMG-1],fill=COR_BORDA,width=TAM_BORDA)
    draw.line([LADO_IMG-1,LADO_IMG-1,0,LADO_IMG-1],fill=COR_BORDA,width=TAM_BORDA)
    draw.line([0,LADO_IMG-1,0,0],fill=COR_BORDA,width=TAM_BORDA)
    for row in range(DIM_MATRIZ):
        for col in range(DIM_MATRIZ):
            if matriz[row,col] == BILL:
                pinta_bill(draw,row,col)
            if not norte_eh_igual(matriz,row,col):
                pinta_borda_norte(draw,row,col)
            if not leste_eh_igual(matriz,row,col):
                pinta_borda_leste(draw,row,col)
#            if not sul_eh_igual(matriz,row,col):
#                pinta_borda_sul(draw,row,col)
#            if not oeste_eh_igual(matriz,row,col):
#                pinta_borda_oeste(draw,row,col)
    
# Salva arquivo    
    img.save(arquivo+".png")

def executar(n, coordenada_Bill):
# VERIFICAR SE ENTRADAS SAO CORRETAS
    if (not validar_entradas(n, coordenada_Bill)):
        sys.exit()
# INICIALIZACAO DE VARIAVEIS
    # O tamanho do lado eh uma potencia de 2 do valor dado.
    tamanho_lado = pow(2, n)
    # A quantidade de ids para identificar os L eh a formula (lado^2-1)/3
    num_maximo = (pow(tamanho_lado,2)-1)/3 
    ids_L = collections.deque([i+1 for i in range( num_maximo)])
    x,y = coordenada_Bill
    nome_arquivo = PATH+"\\n_%s_lados_%s_coordbill_%s_%s_" % (n,tamanho_lado, x, y)

# INICIO DO ALGORITMO DE LADRILHAMENTO.
    matriz = criar_matriz(tamanho_lado, coordenada_Bill)
    ladrilhar(matriz, ids_L)
    # Calcula leading space necesario para boa formatacao do arquivo.
    leading_space = str(len(str(num_maximo)))
    # Salva arquivo texto com a matriz.
    numpy.savetxt(nome_arquivo+".txt", matriz,"%"+leading_space+"d")
    # Salva arquivo csv para abrir no Excel.
    numpy.savetxt(nome_arquivo+".csv", matriz,"%d",delimiter=";")
    
    criar_imagem(matriz,nome_arquivo)   
    
    return matriz
# FIM DO ALGORITMO DE LADRILHAMENTO.


if __name__ == '__main__':
    executar(5,(16,16))
#    executar(1, (1, 0))
#    executar(2, (3, 2))
#    executar(3, (1, 5))
#    executar(4, (2, 2))
#    executar(5, (23, 17))
    print("FIM DO PROGRAMA.")    






