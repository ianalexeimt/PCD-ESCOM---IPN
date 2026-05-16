# Reto: Procesador y Clasificador de Temperaturas

**Materia:** Programación para Ciencia de Datos (IPN)

## Descripción
Programa en Python que procesa un flujo de datos climáticos recibidos por entrada estándar. El sistema lee registros de ciudades con sus respectivas temperaturas, estandariza los valores convirtiendo las lecturas de Fahrenheit a Celsius cuando es necesario, clasifica el clima según su rango térmico y genera una nueva estructura de datos limpia en formato CSV.

## Reglas
- Omite la primera línea del flujo de entrada para ignorar los encabezados originales.
- Valida que los registros cuenten estrictamente con tres campos: ciudad, temperatura y unidad.
- Soporta las unidades **C** (Celsius) y **F** (Fahrenheit); cualquier otra unidad o dato mal formateado provoca que la línea sea descartada.
- Clasifica el nivel térmico en Celsius bajo los siguientes criterios:
  - **Congelante:** Menor a 0°C.
  - **Frío:** De 0°C a 15°C.
  - **Templado:** Más de 15°C hasta 25°C.
  - **Cálido:** Más de 25°C hasta 35°C.
  - **Extremo:** Mayor a 35°C.
- Muestra el resultado final de la temperatura redondeado a un solo decimal.

## Uso
Ejecuta el programa desde la terminal redirigiendo el archivo de datos hacia la entrada estándar del script. El sistema imprimirá en la consola los nuevos encabezados junto con las ciudades procesadas y su clasificación, permitiendo también redirigir la salida para guardarla en un nuevo archivo CSV.

## Autor
**Ian Alexei Muñoz Tanasescu**
