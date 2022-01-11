#! /usr/bin/env python

"""
    This suite tests the properties of the class Produto
    written by Gabriel Heberle on December 20th, 2021    
"""

import unittest
from produto import Produto

class ProdutoUnitTest(unittest.TestCase):
    def setUp(self):
        self.codigo = 1234
        self.descricao = 'My Amazing Product'
        self.preco = 15.97
        self.prod = Produto(self.codigo, self.descricao, self.preco)
    
    def tearDown(self):
        del self.prod
    
    def test_basic_properties(self):
        self.assertEqual(self.prod.codigo, self.codigo)
        self.assertEqual(self.prod.descricao, self.descricao)
        self.assertEqual(self.prod.preco, self.preco)

    def test_entrada_estoque(self):
        # testing if newly created object has null stock
        self.assertEqual(self.prod.quant_estoque, 0)

        # testing integer entry
        entrada = 50
        self.prod.entrada_estoque(entrada)
        self.assertEqual(self.prod.quant_estoque, entrada)
        
        # testing float entry
        entrada = 24.5
        estoque_atual = self.prod.quant_estoque + entrada
        self.prod.entrada_estoque(entrada)
        self.assertEqual(self.prod.quant_estoque, estoque_atual)
    
    def test_saida_estoque(self):
        # testing if newly created object has null stock
        self.assertEqual(self.prod.quant_estoque, 0)
        self.prod.entrada_estoque(100)
        estoque_inicial = self.prod.quant_estoque

        # testing integer entry
        saida = 12
        self.prod.saida_estoque(saida)
        self.assertEqual(self.prod.quant_estoque, estoque_inicial - saida)
        
        # testing float entry
        saida = 37.1
        estoque_atual = self.prod.quant_estoque - saida
        self.prod.saida_estoque(saida)
        self.assertEqual(self.prod.quant_estoque, estoque_atual)

if __name__ == '__main__':
    unittest.main(verbosity=2)
