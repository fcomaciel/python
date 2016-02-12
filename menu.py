# -*- coding: utf-8 -*-

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
	print """
As opções de convesão são:
--------------------------
1. Celcius para Fahrenheit
2. Fahrenheit para Celcius
3. Celcius para Kelvin
4. Kelvin para Celcius
5. Kelvin para Fahrenheit
6. Fahrenheit para Kelvin
7. Encerra o programa """

cls()

ans = True
while ans:
	menu()
	ans = raw_input('Digite uma das Opções: ')
	if ans == '1':
		cls()
		tempCelsius = input('Digite a temperatura em Celcius: ')
		tempFahrenheit = ((tempCelsius * 9.0) / 5.0 + 32.0)
		print '%3.1f°C equivale a: %3.1f°F' % (tempCelsius, tempFahrenheit)
		sim = raw_input('Deseja fazer outra convesão? - (s/N): ')
		if sim == 's' or sim == 'S':
			continue
		else:
			break		
	elif ans == '2':
		cls()
		tempFahrenheit = input('Digite a temperatura em Fahrenheit: ')
		tempCelsius = ((tempFahrenheit - 32.0) * 5.0 / 9.0)
		print '%3.1f°F equivale a: %3.1f°C' % (tempFahrenheit, tempCelsius)
		sim = raw_input('Deseja fazer outra convesão? - (s/N): ')
		if sim == 's' or sim == 'S':
			continue
		else:
			break
	elif ans == '3':
		cls()
		tempCelsius = input('Digite a temperatura em Celcius: ')
		tempKelvin = (tempCelsius + 273.15)
		print '%3.1f°C equivale a: %3.1f°K' % (tempCelsius, tempKelvin)
		sim = raw_input('Deseja fazer outra convesão? - (s/N): ')
		if sim == 's' or sim == 'S':
			continue
		else:
			break
	elif ans == '4':
		cls()
		tempKelvin = input('Digite a temperatura em Kelvin: ')
		tempCelsius = (tempKelvin - 273.15)
		print '%3.1f°K equivale a: %3.1f°C' % (tempCelsius, tempKelvin)
		sim = raw_input('Deseja fazer outra convesão? - (s/N): ')
		if sim == 's' or sim == 'S':
			continue
		else:
			break
	elif ans == '5':
		cls()
		tempKelvin = input('Digite a temperatura em Kelvin: ')
		tempFahrenheit = ((tempKelvin * 9 / 5) - 459.67)
		print '%3.1f°K equivale a: %3.1f°F' % (tempKelvin, tempFahrenheit)
		sim = raw_input('Deseja fazer outra convesão? - (s/N): ')
		if sim == 's' or sim == 'S':
			continue
		else:
			break		
	elif ans == '6':
		cls()
		tempFahrenheit = input('Digite a temperatura em Fahrenheit: ')
		tempKelvin = ((tempFahrenheit + 459.67) * 5 / 9)
		print '%3.1f°K equivale a: %3.1f°F' % (tempFahrenheit, tempKelvin)
		sim = raw_input('Deseja fazer outra convesão? - (s/N): ')
		if sim == 's' or sim == 'S':
			continue
		else:
			break		
	elif ans == '7':
		cls()
		break
	else:
		print 'Opção desconhecida!'