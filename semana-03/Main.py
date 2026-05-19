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

def main():
    productos={}
    is_first_line=True

    for line in sys.stdin:
        clean_line=line.strip()
        if is_first_line:
            is_first_line=False
            continue

        if not clean_line:
            continue

        parsed_result=line_parser(clean_line)
        if parsed_result:
            producto=parsed_result[0]
            cantidad=parsed_result[1]
            precio=parsed_result[2]

            if producto not in productos:
                productos[producto]={'unidades': 0, 'ingreso': 0.0}