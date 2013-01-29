'''
Created on 26/01/2013

@author: sergio
'''
import unittest
import ladrilhamento_matriz
from numpy.ma.testutils import assert_equal

class Test(unittest.TestCase):

    def test_valor_n_eh_correto(self):
        assert( ladrilhamento_matriz.valor_n_eh_correto(3))
        assert(not ladrilhamento_matriz.valor_n_eh_correto(0))
        assert(not ladrilhamento_matriz.valor_n_eh_correto(-1))
        
    def test_coord_ocupada_eh_correta(self):
        assert(not ladrilhamento_matriz.coord_ocupada_eh_correta(2, (-1,0)))
        assert(not ladrilhamento_matriz.coord_ocupada_eh_correta(2, (0,-1))) 
        assert(ladrilhamento_matriz.coord_ocupada_eh_correta(2, (1,0)))    
        assert(not ladrilhamento_matriz.coord_ocupada_eh_correta(2, (2,0)))  
        assert(not ladrilhamento_matriz.coord_ocupada_eh_correta(2, (0,2))) 

    def test_criar_matriz(self):
        n = 2
        coord_bill = (0,0)
        matriz = ladrilhamento_matriz.criar_matriz(n, coord_bill)
        assert_equal(matriz[coord_bill],ladrilhamento_matriz.BILL)
        
        n = 3
        coord_bill = (2,1)
        matriz = ladrilhamento_matriz.criar_matriz(n, coord_bill)
        assert_equal(matriz[coord_bill],ladrilhamento_matriz.BILL)
        
        n = 8
        coord_bill = (6,7)
        matriz = ladrilhamento_matriz.criar_matriz(n, coord_bill)
        assert_equal(matriz[coord_bill],ladrilhamento_matriz.BILL)
    
    def test_canto_quadrante_1(self):
        tamanho = 2
        canto_quadrante_1 = ladrilhamento_matriz.canto_quadrante_1(tamanho)
        assert_equal(canto_quadrante_1, (0,0))
    
        tamanho = 4
        canto_quadrante_1 = ladrilhamento_matriz.canto_quadrante_1(tamanho)
        assert_equal(canto_quadrante_1, (1,1))

        tamanho = 8
        canto_quadrante_1 = ladrilhamento_matriz.canto_quadrante_1(tamanho)
        assert_equal(canto_quadrante_1, (3,3))

        tamanho = 16
        canto_quadrante_1 = ladrilhamento_matriz.canto_quadrante_1(tamanho)
        assert_equal(canto_quadrante_1, (7,7))
        
    def test_canto_quadrante_2(self):
        tamanho = 2
        canto_quadrante_2 = ladrilhamento_matriz.canto_quadrante_2(tamanho)
        assert_equal(canto_quadrante_2, (0,1))
    
        tamanho = 4
        canto_quadrante_2 = ladrilhamento_matriz.canto_quadrante_2(tamanho)
        assert_equal(canto_quadrante_2, (1,2))

        tamanho = 8
        canto_quadrante_2 = ladrilhamento_matriz.canto_quadrante_2(tamanho)
        assert_equal(canto_quadrante_2, (3,4))

        tamanho = 16
        canto_quadrante_2 = ladrilhamento_matriz.canto_quadrante_2(tamanho)
        assert_equal(canto_quadrante_2, (7,8))        

    def test_canto_quadrante_3(self):
        tamanho = 2
        canto_quadrante_3 = ladrilhamento_matriz.canto_quadrante_3(tamanho)
        assert_equal(canto_quadrante_3, (1,0))
    
        tamanho = 4
        canto_quadrante_3 = ladrilhamento_matriz.canto_quadrante_3(tamanho)
        assert_equal(canto_quadrante_3, (2,1))

        tamanho = 8
        canto_quadrante_3 = ladrilhamento_matriz.canto_quadrante_3(tamanho)
        assert_equal(canto_quadrante_3, (4,3))

        tamanho = 16
        canto_quadrante_3 = ladrilhamento_matriz.canto_quadrante_3(tamanho)
        assert_equal(canto_quadrante_3, (8,7)) 
        
    def test_canto_quadrante_4(self):
        tamanho = 2
        canto_quadrante_4 = ladrilhamento_matriz.canto_quadrante_4(tamanho)
        assert_equal(canto_quadrante_4, (1,1))
    
        tamanho = 4
        canto_quadrante_4 = ladrilhamento_matriz.canto_quadrante_4(tamanho)
        assert_equal(canto_quadrante_4, (2,2))

        tamanho = 8
        canto_quadrante_4 = ladrilhamento_matriz.canto_quadrante_4(tamanho)
        assert_equal(canto_quadrante_4, (4,4))

        tamanho = 16
        canto_quadrante_4 = ladrilhamento_matriz.canto_quadrante_4(tamanho)
        assert_equal(canto_quadrante_4, (8,8)) 

        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_criar_matriz']
    unittest.main()