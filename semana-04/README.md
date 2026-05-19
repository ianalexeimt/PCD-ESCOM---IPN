# Reto Semana 4: Sistema de Inventario Modular

**Materia:** Programación para Ciencia de Datos (IPN)

## Descripción
Sistema modular en Python que evalúa un inventario a partir de un archivo CSV para identificar qué productos necesitan ser reabastecidos dependiendo de sus niveles de stock.

## Estructura del Proyecto
- `main.py`: Orquestador principal del sistema.
- `models/producto.py`: Clase de dominio del producto y su lógica de inventario.
- `utils/validators.py`: Filtros de limpieza para ignorar datos corruptos o valores negativos.
- `utils/io.py`: Lógica de lectura y creación de directorios para reportes.

## Cómo Ejecutar
Ejecuta el programa desde la raíz del proyecto. El sistema creará los directorios de salida automáticamente si no existen:
```bash
python main.py
```

## Entrada
El sistema lee de forma automática el archivo en `data/inventario.csv`.
- Se requiere que el archivo tenga 6 columnas: `sku`, `nombre`, `categoria`, `precio`, `stock`, `stock_minimo`.
- Los SKUs duplicados o líneas con datos corruptos se ignoran de manera silenciosa.

## Salida
El programa genera el archivo `outputs/reporte_inventario.csv`.
- Contiene 7 columnas, añadiendo `unidades_faltantes` y `valor_inventario`.
- Solo incluye productos cuyo stock actual sea menor al mínimo.
- Está ordenado de mayor a menor según las unidades faltantes.

## Autor
**Ian Alexei Muñoz Tanasescu**
