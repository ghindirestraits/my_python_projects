#! /usr/bin/env python

"""
    Classe que representa um produto
"""


class Produto:
    def __init__(self, codigo: int, descricao: str, preco: float) -> None:
        """
            Instancia um objeto da classe Produto

        Args:
            codigo (int): identificador do produto
            descricao (str): breve descrição do propósito do produto em questão
            preco (float): valor monetário do produto
            quant_estoque (float): quantidade disponível para uso
        """
        self.__codigo = codigo
        self.__descricao = descricao
        self.__preco = preco
        self.__quant_estoque = 0

    def entrada_estoque(self, quant: float) -> None:
        """
            Adiciona o valor de 'quant' ao estoque do produto

        Args:
            quant (float): quantidade a ser adicionada
        """
        self.__quant_estoque += quant

    def saida_estoque(self, quant: float) -> None:
        """
            Subtrai o valor de 'quant' do estoque do produto

        Args:
            quant (float): quantidade a ser subtraída
        """
        if self.__quant_estoque == 0:
            raise Exception("Estoque zerado, não é possível realizar a saída.")
        else:
            self.__quant_estoque -= quant

    def visualizar_quant_em_estoque(self) -> None:
        """
        Exibe a quantidade de produto disponível
        """
        print(f"A quantidade em estoque eh {self.__quant_estoque}")

    @property
    def codigo(self) -> int:
        """
            Retorna o codigo do respectivo produto

        Returns:
            int: codigo do produto
        """
        return self.__codigo

    @property
    def descricao(self) -> str:
        """
            Retorna a descricao do produto

        Returns:
            str: texto contendo informação sobre propósito do produto
        """
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str) -> None:
        """
            Altera o texto de descricao do produto

        Args:
            descricao (str): texto informando novo propósito do produto
        """
        self.__descricao = descricao

    @property
    def preco(self) -> float:
        """
            Retorna o valor do preço

        Returns:
            float: valor monetário do produto
        """
        return self.__preco

    @preco.setter
    def preco(self, preco: float) -> None:
        """
            Alterar o valor do preco do produto

        Args:
            preco (float): valor do novo preco do produto
        """
        if preco <= 0:
            raise Exception("Preco deve ser um valor positivo.")
        else:
            self.__preco = preco

    @property
    def quant_estoque(self) -> float:
        """
            Retorna a quantidade em estoque do produto

        Returns:
            float: quantidade em estoque
        """
        return self.__quant_estoque
