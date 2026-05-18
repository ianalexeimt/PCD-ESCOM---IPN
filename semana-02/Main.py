import sys

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def temp_classifier(celsius):
    if celsius < 0:
        return "Congelante"
    elif celsius <= 15:
        return "Frio"
    elif celsius <= 25:
        return "Templado"
    elif celsius <= 35:
        return "Calido"
    else:
        return "Extremo"

def main():
    encabezados = sys.stdin.readline()
    if not encabezados:
        return

    print("ciudad,temperatura_celsius,clasificacion")

    for data in sys.stdin:
        if not data.strip():
            continue

        parts = [part.strip() for part in data.split(",")]

        if len(parts) != 3:
            continue

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
            temp_celsius = fahrenheit_a_celsius(temp_val)
        else:
            temp_celsius = temp_val

        clasificacion = temp_classifier(temp_celsius)
        print(f"{ciudad},{temp_celsius:.1f},{clasificacion}")

if __name__ == "__main__":
    main()