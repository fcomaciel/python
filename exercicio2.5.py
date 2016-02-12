# -*- coding: utf-8 -*-

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

# tempCelsius = input('Digite a temperatura em Celcius: ')
tempFahrenheit = input('Digite a temperatura em Fahrenheit: ')
"""
Fórmula para conversão de °C para °F
°F = (°C × 9) / 5 + 32
Fórmula para conversão de °F para °C
°C = (°F - 32) × 5 / 9
Fórmula para conversão de °C para °K
°K = °C + 273.15
Fórmula para conversão de °K para °C
°C = °K - 273.15
Fórmula para conversão de °K para °F
°F = (°K * 9 / 5) - 459.67
Fórmula para conversão de °F para °K
°K = (ºF + 459.67) * 5 / 9
Fonte:
http://www.rapidtables.com/convert/temperature/fahrenheit-to-kelvin.htm
"""
"""
tempFahrenheit = (tempCelsius * 9.0) / 5.0 + 32.0

print '%3.1f C° equivale a: %3.1f F°' % (tempCelsius, tempFahrenheit)
"""
tempCelsius = (tempFahrenheit - 32.0) * 5.0 / 9.0

print '%3.1f °F equivale a: %3.1f °C' % (tempFahrenheit, tempCelsius)
