#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pilas
from pilas.simbolos import *
from pilas import eventos

class MoverseConWASD(pilas.habilidades.Habilidad):
    '''Hace que un actor se pueda mover con las teclas:
        
        W --> arriba
        S --> abajo
        A --> izquierda
        D --> derecha
        G --> boton
        
        Facilita el uso de un segundo mando, muy usado en juegos multiplayer'''

    def __init__(self, receptor):
        pilas.habilidades.Habilidad.__init__(self, receptor)
        self.w = False
        self.s = False
        self.a = False
        self.d = False
        self.g = False
        
        pilas.eventos.pulsa_tecla.conectar(self.cuando_pulsa_la_tecla)
        pilas.eventos.suelta_tecla.conectar(self.cuando_suelta_la_tecla)
            
    def __call__(self, ngfs):
        return self
                
    def cuando_pulsa_la_tecla(self, evento):
        self.procesar_cambio_de_estado_en_la_tecla(evento.codigo, True)

    def cuando_suelta_la_tecla(self, evento):
        self.procesar_cambio_de_estado_en_la_tecla(evento.codigo, False)

    def procesar_cambio_de_estado_en_la_tecla(self, codigo, estado):
        mapa = {
            w: 'w',
            s: 's',
            a: 'a',
            d: 'd',
            g: 'g',
        }

        if mapa.has_key(codigo):
            setattr(self, mapa[codigo], estado)

    def w(self):
        return self.w

    def a(self):
        return self.a

    def s(self):
        return self.s

    def d(self):
        return self.d

    def g(self):
        return self.g
