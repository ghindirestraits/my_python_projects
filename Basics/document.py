#! /usr/bin/env python

"""
    This class represents a document
"""

import datetime

class Document():
    def __init__(self, num:str, date_creation:datetime, summary:str) -> None:
        self.__num = num
        self.__date_creation = date_creation
        self.__summary = summary

    def __str__(self) -> str:
        result = '\nDocumento n.: ' + self.__num + '\n'
        result += 'Data de criaçao: ' + datetime.datetime.strftime(self.__date_creation, '%d/%m/%Y') + '\n'
        result += 'Resumo: ' + self.__summary + '\n'
        return result

    @property
    def number(self) -> str:
        return self.__number

    
    @property
    def date_creation(self) -> datetime:
        return self.__date_creation

    @property
    def summary(self) -> str:
        return self.__summary

    @summary.setter
    def summary(self, summary:str) -> None:
        if (summary=='') or (summary == None):
            raise Exception("Um resumo deve ser fornecido!")
        else:
            self.__summary = summary
