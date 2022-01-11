"""
    Posicionando-se em um arquivo de texto com o uso de seek() e tell()
"""
import os

arquivo = 'teste_seek.txt'

handler = open(arquivo, 'w')
handler.write("Testando o uso do metodo seek().\nEsta e a segunda linha do arquivo.\nE esta, a terceira.")
handler.close()

handler = open(arquivo, 'r')
print(f'Após abrir o arquivo para leitura, a posição inicial do manipulador é {handler.tell()}.')
linha = handler.readline()
print(f'Linha 1: {linha}')
print(f'Após ler a primeira linha, a posição do manipulador é {handler.tell()}.')
print('Voltando o manipulador 24 bytes antes da posição atual e lendo uma linha a partir daí:')
handler.seek(handler.tell()-24, os.SEEK_SET)
linha = handler.readline()
print(f'Linha lida: {linha}')
print('Posicionando o manipulador 33 bytes a partir do início do arquivo e lendo uma linha:')
handler.seek(34, os.SEEK_SET)
linha = handler.readline()
print(f'Linha lida: {linha}')
handler.close()
