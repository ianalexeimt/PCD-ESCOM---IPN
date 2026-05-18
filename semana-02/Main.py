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

def main():
    encabezados = sys.stdin.readline()
    if not encabezados:
        return

    print("ciudad,temperatura_celsius,clasificacion")

    for data in sys.stdin:
        if not data.strip():
            continue

        parts = [part.strip() for part in data.split(",")]

        if len(parts) == 3:
            ciudad = parts[0]
            temperatura = parts[1]
            unidad = parts[2].upper()

            if unidad not in ['C', 'F']:
                continue

            try:
                temp_val = float(temperatura)
            except ValueError:
                continue

            if unidad == 'F':
                temp_celcius = fahrenheit_to_celcius(temp_val)
            else:
                temp_celcius = temp_val

            clasificacion = temp_classifier(temp_celcius)
            print(f"{ciudad},{temp_celcius:.1f},{clasificacion}")

if __name__ == "__main__":
    main()