# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 05:31:11 2022

@author: Asus
"""

#funciones de orden superior
def dato():
    while True:
        n=int("Ingresar un número mayor a 1:")
        if n>1:
            return n

#Creamos una función que genere la lista fibonacci

def fibo(n):
    lista=[]
    for i in range(0,n):
        if i==0 or i==1:
            lista.append(1)
        else: 
            lista.append(lista[-2]+lista[-1])
return lista

# Función para mostrar nuestra serie fibo

def muestrafibo(lista):
    for i in lista:
        if(i!=lista[-1])
            print(f{i},end="+")
        else:
            print(f{i})

x=dato()
fibo(n)
muestrafibo(lista)
            
