#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pilas


pilas.iniciar(titulo='Space Adventures', gravedad=(0, 0))

import escena_menu
escena_menu.EscenaMenu()

pilas.ejecutar()
