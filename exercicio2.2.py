# -*- coding: utf-8 -*-

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

nome = raw_input('Digite seu nome: ')
print 'Olá %s' % nome
