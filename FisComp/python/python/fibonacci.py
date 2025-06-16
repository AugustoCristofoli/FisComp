# -*- coding: utf-8 -*-

def fib(n): 
    """Imprime os números da sequência de Fibonacci até o número n.

    """
    i, j = 0, 1
    while i < n:
        print(i, end=' ') #O argumento end pode ser usado para evitar uma nova linha após a saída
        i,j=j,i+j


def fib_lista(n): 
    """Função que retorna uma lista contendo os números da sequência de Fibonacci até o número n."""
    lista=[]
    i, j = 0, 1
    while i < n:
        lista.append(i)
        i,j=j,i+j
    return lista
