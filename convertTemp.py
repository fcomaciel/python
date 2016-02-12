# -*- coding: utf-8 -*-

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

print """
Opções para conversão:
----------------------
1. Celcius para Fahrenheit
2. Fahrenheit para Celcius
3. Celcius para Kelvin
4. Kelvin para Celcius
5. Kelvin para Fahrenheit
6. Fahrenheit para Kelvin
7. Encerra o programa 
"""

temp = raw_input('Digite a opção desejada: ')

if temp == '1':
	tempCelsius = input('Digite a temperatura em Celcius: ')
	tempFahrenheit = (tempCelsius * 9.0) / 5.0 + 32.0
	print '%3.1f°C equivale a: %3.1f°F' % (tempCelsius, tempFahrenheit)
	
elif temp == '2':
	tempFahrenheit = input('Digite a temperatura em Fahrenheit: ')
	tempCelsius = (tempFahrenheit - 32.0) * 5.0 / 9.0
	print '%3.1f°F equivale a: %3.1f°C' % (tempFahrenheit, tempCelsius)

elif temp == '3':
	tempCelsius = input('Digite a temperatura em Celcius: ')
	tempKelvin = tempCelsius + 273.15
	print '%3.1f°C equivale a: %3.1f°K' % (tempCelsius, tempKelvin)

elif temp == '4':
	tempKelvin = input('Digite a temperatura em Kelvin: ')
	tempCelsius = tempKelvin - 273.15
	print '%3.1f°K equivale a: %3.1f°C' % (tempCelsius, tempKelvin)	

else:
	print 'Error!'
	print 'Digite: C ou c para converter de Celcius para Fahrenheit;'
	print 'Digite: F ou f para converter de Fahrenheit para Celcius.'
