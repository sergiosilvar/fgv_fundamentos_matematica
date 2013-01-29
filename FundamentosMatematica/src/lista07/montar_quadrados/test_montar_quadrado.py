'''
Created on 27/01/2013

@author: sergio
'''
from lista07.meu_log import MeuLog
from numpy.ma.testutils import assert_equal
from src.lista07.montar_quadrados import montar_quadrado as mq
import logging
import unittest

XY_PARA_TAM_3_4 = (abs(3.0 - 4)) / 2, (3.0 + 4) / 2

class Test(unittest.TestCase):

    def setUp(self):
        log = MeuLog().get_logger()
        log.setLevel(logging.CRITICAL)
        unittest.TestCase.setUp(self)

    def test_calculaxy(self):
        assert_equal(mq.calcula_xy(-1, 1), mq.ERRO)
        assert_equal(mq.calcula_xy(1, -0.001), mq.ERRO)
        assert_equal(mq.calcula_xy(0, 1), mq.ERRO)
        assert_equal(mq.calcula_xy(1, 0), mq.ERRO)
        assert_equal(mq.calcula_xy(1, 1) , mq.ERRO)
        assert_equal(mq.calcula_xy(3, 4), XY_PARA_TAM_3_4)
        assert_equal(mq.calcula_xy(4, 3), XY_PARA_TAM_3_4)
        
    
    def test_criar_quadrado(self):
        assert_equal(mq.montar_quadrados([3,4]), XY_PARA_TAM_3_4)
        #mq.montar_quadrados([3,4,6])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_criar_quadrado']
    unittest.main()