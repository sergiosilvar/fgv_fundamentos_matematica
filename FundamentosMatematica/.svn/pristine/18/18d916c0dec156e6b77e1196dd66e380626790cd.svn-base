'''
Created on 27/01/2013

@author: sergio
'''
PX_P_CM = 46 # pixel por cm

class Quadrado():
    '''
    classdocs
    '''
    
    def __init__(self,lado_cm,cor,x0=0,y0=0):
        '''
        Constructor
        x0 - coordenada x de origem.
        x0 - coordenada y de origem.
        lado - tamanho adimensional do lado.
        '''
        self.x0 = x0
        self.y0 = y0
        self.lado_cm = lado_cm
        self.lado_px = lado_cm*PX_P_CM
        self.x0y0_x1y1 = [(x0,y0),(x0+self.lado_px,y0+self.lado_px)]
        self.cor = cor