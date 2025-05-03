#!/usr/bin/env python
# coding: utf-8

# In[11]:


import os
from pelicula import Pelicula

class ServicioPeliculas:
    NOMBRE_ARCHIVO = 'peliculas.txt'
    
    def __init__(self):
        pass
        
    def agregar_pelicula(self, pelicula):
        with open(self.__class__.NOMBRE_ARCHIVO, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    def listar_peliculas(self):
        with open(self.__class__.NOMBRE_ARCHIVO, 'r', encoding='utf8') as archivo:
            print('--- Listado de Películas ---')
            print(archivo.read())
            
    def eliminar_archivo_peliculas(self):
        os.remove(self.__class__.NOMBRE_ARCHIVO)
        print(f'Archivo eliminado: {self.__class__.NOMBRE_ARCHIVO}')     

