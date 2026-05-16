import sys

def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def temp_classifier(celcius):
    if celcius < 0:
        return "Congelante"
    elif 0 <= celcius <= 15:
        return "Frío"
    elif 15 < celcius <= 25:
        return "Templado"
    elif 25 < celcius <= 35:
        return "Cálido"
    elif 35 < celcius:
        return "Extremo"
    else:
        return "Ingrese una temperatura correcta"
