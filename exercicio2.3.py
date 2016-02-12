# -*- coding: utf-8 -*-

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

horas = input('Informe a quantidade de horas trabalhas: ')
vlhora = input('Informe o valor pago a Hora/Trabalhada: ')

salario = float(horas) * float(vlhora)

print 'Salário bruto: R$ %6.2f' % salario
