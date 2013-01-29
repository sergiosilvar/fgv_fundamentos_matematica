'''
Created on 27/01/2013

@author: sergio

Meu monitor:    29,3 cm x 16,5 cm
                1366 px x 768 px
                11" x 6,5"
                13,2" diagonal
                ~ 46 px/cm
                ~ 118 px/"
'''

from numpy.lib.scimath import sqrt
import figuras
from test.test_multiprocessing import sqr
import Image
import ImageDraw
import os
import random
import subprocess
import sys





ERRO = -999

VISUALIZADOR = "C:\\Windows\\system32\\mspaint.exe"
PATH = ".\\saida"

# Tela LARGURA X ALTURA  cm em pixels. 
PX_P_CM = 46
TELA_LARGURA = 16*PX_P_CM
TELA_ALTURA = 9*PX_P_CM  
TELA_METADE_LARGURA = int(TELA_LARGURA /2)
TELA_METADDE_ALTURA= int(TELA_ALTURA /2)
TELA_MARGEM = 10

# CORES
VERDE = (102,255,102)
AMARELO = (255,255,102)
AZUL = (0,204,204)
MARROM = (204,102,0)
ROSA = (255,105,180)
BRANCO = (255,255,255)
CORES = [VERDE,AMARELO,AZUL,MARROM,ROSA,BRANCO]

CONTORNO = "black"
#CONTORNO = None


def color(i):
    return CORES[i]
#    r = random.randint(0,255)
#    random.seed(r)
#    g = random.randint(0,255)
#    random.seed(r)
#    b = random.randint(0,255)
#    return (r,g,b)
#    i_color = random()
#    r = i_color % 10
#    g = (i_color//10) % 10
#    b = (i_color//100) % 10
#    return(r*25, g*25, b*25)

def abendar(s):
    print(s)
    sys.exit(s)

def calcula_x_risco(q1,q2):
    lado_a = q1.lado_px*1.0
    lado_b = q2.lado_px*1.0
    if lado_a<= 0 or lado_b <= 0:
        print("ERRO: Um dos tamanhos nao eh positivo. Lado lado_a: %s, lado lado_b : %s." % (lado_a, lado_b))
        return ERRO

    if lado_a ==  lado_b:
        print ("ERRO: Os lados nao podem ser iguais. Lado lado_a: %s, lado lado_b : %s." % (lado_a, lado_b))
        return ERRO

    x = (abs(lado_a - lado_b)) / 2
    y = (lado_a+lado_b) / 2
    return int(x)


def limpar_pasta_imagens():
    for the_file in os.listdir(PATH):
        file_path = os.path.join(PATH, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception, e:
            print e

def ver_imagem(nome_arquivo):
    return subprocess.call([VISUALIZADOR, nome_arquivo])

#def desenhar_quadrado_tela(lado_cm):
#    nome_arquivo = "quadrado_tela.png"
#    img = Image.new("RGB", (TELA_LARGURA,TELA_ALTURA),(255,255,255))
#    draw = ImageDraw.Draw(img)
#    q = figuras.Quadrado(10,10,lado_cm,AMARELO)
#    draw.rectangle((q.x0y0_x1y1), q.cor)
#    img.save(nome_arquivo)
#    ver_imagem(nome_arquivo)



def salvar_arquivo(lado_cm, img,riscado=0):
    if riscado == 0:
        nome_arquivo = PATH + "\\quadrado_tam_%s.png" % (lado_cm)
    else:
        nome_arquivo = PATH + "\\quadrado_tam_%s_riscado.png" % (lado_cm)
    img.save(nome_arquivo)
    return nome_arquivo

def desenhar_quadrado(q):
    if CONTORNO == None:
        lado_imagem = q.lado_px
    else:
        lado_imagem = q.lado_px+1
    img = Image.new("RGBA", (lado_imagem,lado_imagem),q.cor)
    
    draw = ImageDraw.Draw(img)
    draw.rectangle(q.x0y0_x1y1, q.cor, CONTORNO)
    return img,draw
    #ver_imagem(nome_arquivo)
    


def salvar_poligono(tam, pol_coord,rumo):
    # tam+1 por causa do CONTORNO
    img_pol = Image.new("RGBA", [tam+1, tam+1], BRANCO)
    draw_pol = ImageDraw.Draw(img_pol)
    draw_pol.polygon(pol_coord, "blue", "black")
    img_pol.save(PATH + "\\pol_%s.png" %(rumo))

def riscar_quadrado(q, img,draw,x):
    # APENAS PARA entende quais coordanas usar    
    inicio_linha1 = (x,0)
    fim_linha1 = (q.lado_px-x,q.lado_px)
    draw.line([inicio_linha1,fim_linha1],fill="black")

    inicio_linha2 = (0,q.lado_px-x)
    fim_linha2 = (q.lado_px,x)
    draw.line([inicio_linha2,fim_linha2],fill="black")

    # Poligono resultante do risco.
    pol1_coord = [(0,0), (x,0), (q.lado_px/2,q.lado_px/2), (0,q.lado_px-x) ] 
    salvar_poligono(q.lado_px, pol1_coord,"oeste")
    
    pol2_coord = [(x,0), (q.lado_px,0), (q.lado_px,x), (q.lado_px/2,q.lado_px/2)] 
    salvar_poligono(q.lado_px, pol2_coord,"norte")
    
    pol3_coord = [(q.lado_px/2,q.lado_px/2), (q.lado_px,x), (q.lado_px,q.lado_px), (q.lado_px-x,q.lado_px)] 
    salvar_poligono(q.lado_px, pol3_coord,"leste")
    
    pol4_coord = [(0,q.lado_px-x), (q.lado_px/2,q.lado_px/2), (q.lado_px-x,q.lado_px), (0,q.lado_px)] 
    salvar_poligono(q.lado_px, pol4_coord,"sul")

    
def montar_quadrados(tam_quadrados=[]):
    qd = []
    for i in range(len(tam_quadrados)):
        qd.append(figuras.Quadrado(tam_quadrados[i],color(i)))
    
    if len(qd) < 2:
        print("ERRO: A lista de tamanho de quadrados tem que ser maior ou igual a 2.")
        return ERRO
    elif len(qd) >= 2:
        # Criar as imagens de todos os quadrados dados.
        for quad_i in qd:
            img,draw = desenhar_quadrado(quad_i)
            nome_arquivo = salvar_arquivo(quad_i.lado_cm, img)
            quad_i.nome_arquivo = nome_arquivo

        
        x_risco = calcula_x_risco(qd[1],qd[0])
        img1 = Image.open(qd[1].nome_arquivo)
        draw1 = ImageDraw.Draw(img1)
        riscar_quadrado(qd[1],img1,draw1,x_risco)
        salvar_arquivo(qd[1].lado_cm, img1,riscado=1)

        # Novo quadrado montado
        n_area = qd[0].lado_px * qd[1].lado_px
        n_lado = int(sqrt(n_area))

#        x_risco = calcula_x_risco(qd[1],qd[0])
#        riscar_quadrado(qd[1],img1,draw1,x_risco)
#        salvar_arquivo(qd[1].lado_cm, img1,riscado=1)
#        
        
        
    return qd



if __name__ == '__main__':
    limpar_pasta_imagens()
    montar_quadrados([4,5])
    print "FIM DO PROGRAMA."