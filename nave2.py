# -*- encoding: utf-8 -*-


import pilas
from pilas.actores import Animacion
import math
from pilas.simbolos import *
from pilas import eventos
from mando2 import MoverseConWASD

class Nave2(Animacion):
    "Representa una nave que puede disparar."

    def __init__(self, x=0, y=0, velocidad=2):
        self.contador_frecuencia_disparo = 0
        self.disparos = []
        self.velocidad = velocidad
        grilla = pilas.imagenes.cargar_grilla("data/nave2.png", 2)
        Animacion.__init__(self, grilla, ciclica=True, x=x, y=y)
        self.radio_de_colision = 20
        self.aprender(pilas.habilidades.PuedeExplotar)
        self.habilidad1 = MoverseConWASD(self)
        self.aprender(self.habilidad1)
    


    
    def actualizar(self):
        
        if self.habilidad1.a :
            self.rotacion -= self.velocidad
        elif self.habilidad1.d :
            self.rotacion += self.velocidad

        if self.habilidad1.w :
            self.avanzar()

        self.contador_frecuencia_disparo += 1

        if self.habilidad1.g :
            if self.contador_frecuencia_disparo > 10:
                self.contador_frecuencia_disparo = 0
                self.disparar()
        
        self.eliminar_disparos_innecesarios()


    def eliminar_disparos_innecesarios(self):
        for d in list(self.disparos):
            if d.x < -320 or d.x > 320 or d.y < -240 or d.y > 240:
                d.eliminar()
                self.disparos.remove(d)


    def disparar(self):
        "Hace que la nave dispare."
        disparo_nuevo = pilas.actores.Disparo(self.x, self.y, self.rotacion, 4)
        self.disparos.append(disparo_nuevo)

    def avanzar(self):
        "Hace avanzar la nave en direccion a su angulo."
        rotacion_en_radianes = math.radians(-self.rotacion + 90)
        dx = math.cos(rotacion_en_radianes) * self.velocidad
        dy = math.sin(rotacion_en_radianes) * self.velocidad
        self.x += dx
        self.y += dy

    def definir_enemigos(self, grupo, cuando_elimina_enemigo=None):
        """hace que una nave tenga como enemigos a todos los actores del grupo.

        El argumento cuando_elimina_enemigo tiene que ser una funcion que
        se ejecutara cuando se produzca la colision."""
        self.cuando_elimina_enemigo = cuando_elimina_enemigo
        pilas.mundo.colisiones.agregar(self.disparos, grupo, self.hacer_explotar_al_enemigo)

    def hacer_explotar_al_enemigo(self, mi_disparo, el_enemigo):
        "Es el método que se invoca cuando se produce una colisión 'tiro <-> enemigo'"
        mi_disparo.eliminar()
        el_enemigo.eliminar()

        if self.cuando_elimina_enemigo:
            self.cuando_elimina_enemigo()
