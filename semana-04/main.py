from models.producto import Producto
from utils.validators import validar_producto
from utils.io import leer_inventario, escribir_reporte

def crear_productos (datos_raw):
    productos=[]
    skus_procesados=set()

    for datos in datos_raw:
        sku=datos.get('sku')
        if sku in skus_procesados:
            continue

        es_valido=validar_producto(sku, datos.get('nombre'), datos.get('categoria'), datos.get('precio'), datos.get('stock'), datos.get('stock_minimo'))

        if not es_valido:
            continue

        try:
            producto=Producto(sku=sku, nombre=datos['nombre'], categoria=datos['categoria'], precio=float(datos['precio']), stock=int(datos['stock']), stock_minimo=int(datos['stock_minimo']))
            productos.append(producto)
            skus_procesados.add(sku)
        except ValueError:
            pass

    return productos

def main():
    archivo_inventario='data/inventario.csv'
    archivo_reporte='outputs/reporte_inventario.csv'

    datos_raw=leer_inventario(archivo_inventario)
    productos=crear_productos(datos_raw)

    necesitan_reorden=[]
    for p in productos:
        if p.necesita_reorden():
            necesitan_reorden.append(p)

    necesitan_reorden=sorted(necesitan_reorden, key=lambda x: x.unidades_faltantes(), reverse=True)
    escribir_reporte(necesitan_reorden, archivo_reporte)

if __name__ == '__main__':
    main()