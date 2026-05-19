def leer_inventario(ruta_archivo):
    """Lee el archivo de inventario y retorna una lista de diccionarios."""
    productos_raw = []
    
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            
            if not lineas:
                return productos_raw
            
            encabezados = lineas[0].strip().split(',')
            
            for linea in lineas[1:]:
                linea = linea.strip()
                if not linea:
                    continue
                
                valores = linea.split(',')
                if len(valores) == len(encabezados):
                    producto_dict = dict(zip(encabezados, valores))
                    productos_raw.append(producto_dict)
                    
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_archivo}")
        
    return productos_raw

def escribir_reporte(productos, ruta_archivo):
    """Escribe el reporte de productos que necesitan reorden."""
    encabezados = [
        "sku", "nombre", "categoria", "stock_actual", 
        "stock_minimo", "unidades_faltantes", "valor_inventario"
    ]
    
    with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(','.join(encabezados) + '\n')
        
        for p in productos:
            linea = f"{p.sku},{p.nombre},{p.categoria},{p.stock},"
            linea += f"{p.stock_minimo},{p.unidades_faltantes()},{p.valor_inventario():.2f}"
            archivo.write(linea + '\n')