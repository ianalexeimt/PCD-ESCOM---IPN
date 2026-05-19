import sys

def line_parser (original_line):
    parts=original_line.strip().split(',')
    if len(parts) != 4:
        return None

    producto=parts[1].strip()
    cantidad_raw=parts[2].strip()
    precio_raw=parts[3].strip()

    try:
        cantidad_clean=int(cantidad_raw)
        precio_clean=float(precio_raw)
        if cantidad_clean <= 0 or precio_clean < 0:
            return None
        return producto, cantidad_clean, precio_clean
    except ValueError:
        pass

