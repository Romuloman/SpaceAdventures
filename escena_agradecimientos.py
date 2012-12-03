#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pilas


class EscenaAgradecimientos(pilas.escenas.Escena):
    '''Representa a la escena que se desarrolla en la ayuda del juego'''

    def __init__(self):
        pilas.escenas.Escena.__init__(self)
        self.fondo = pilas.fondos.Fondo("data/fondo_juego.jpg")
        self.crear_texto_ayuda()
        pilas.eventos.pulsa_tecla_escape.conectar(self.cuando_pulsa_tecla)
        
    def crear_texto_ayuda(self):
        lucho = pilas.actores.Texto('Luciano Castillo')
        lucho.escala = 2
        lucho.color = pilas.colores.amarillo
        texto = pilas.actores.Texto('\nMuchas Gracias a:  \n \n Por la ayuda que nos brindo ')
        texto.color = pilas.colores.blanco
        texto.y= 100
        pilas.avisar('Para volver al menu precione ESC')

    def cuando_pulsa_tecla(self, *k, **kv):
        import escena_menu
        escena_menu.EscenaMenu()
