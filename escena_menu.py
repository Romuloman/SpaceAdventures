#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pilas
from pilas.escenas import Escena


class EscenaMenu(Escena):

    def __init__(self):
        Escena.__init__(self)
        self.fondo = pilas.fondos.Fondo('data/fondo_menu.jpeg')
        self.generar_titulo()
        pilas.avisar('Seleccione lo que desea hacer')
        self.generar_menu()
       
    def generar_titulo(self):
        texto = pilas.actores.Texto('Space Adventures', magnitud=45, y=200)
        texto.color = pilas.colores.naranja
    
        

    def generar_menu(self):
        opciones = [
		            ('Jugar', self.comenzar),
		            ('Ayuda', self.ayuda),
                    ('Agradecimientos', self.agradecimientos),
		            ('Salir', self.salir),
		           ]
        self.menu = pilas.actores.Menu(opciones)
        self.menu.color = pilas.colores.blanco

    def comenzar(self):
        import JuegoRomulo
        JuegoRomulo.Juego()

    def ayuda(self):
        import escena_ayuda
        escena_ayuda.EscenaAyuda()

    def agradecimientos(self):
        import escena_agradecimientos
        escena_agradecimientos.EscenaAgradecimientos()

    def salir(self):
        pilas.terminar()
