# Reto Semana 5: Perfilador de Datasets

**Materia:** Programación para Ciencia de Datos (IPN)

## Descripción
Herramienta de línea de comandos en Python que analiza cualquier archivo CSV para generar un reporte automático de calidad de datos, detectando tipos de variables, valores nulos y unicidad por columna (con protección contra columnas incompletas).

## Requisitos
- Python 3.8 o superior

## Instalación

### 1. Clonar el repositorio
```bash
git clone [https://github.com/usuario/reto-semana-05.git](https://github.com/usuario/reto-semana-05.git)
cd reto-semana-05
```

### 2. Crear ambiente virtual
```bash
python -m venv .venv
```

### 3. Activar ambiente virtual
```bash
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```

## Uso
El sistema recibe parámetros obligatorios para especificar los archivos de entrada y salida:
```bash
python main.py --input <archivo_entrada.csv> --output <archivo_salida.csv>
```

### Ejemplo
```bash
python main.py --input data/ventas.csv --output outputs/perfil_ventas.csv
```

## Formato de Salida
El perfil generado contiene las siguientes columnas:

| Columna | Descripción |
|---------|-------------|
| nombre_columna | Nombre de la columna analizada |
| tipo_inferido | Tipo detectado (numerico/texto/fecha/booleano) tras predominancia >80% |
| total_registros | Total de filas contabilizadas |
| valores_nulos | Cantidad de celdas vacías |
| porcentaje_nulos | Porcentaje de valores nulos (2 decimales) |
| valores_unicos | Cantidad de valores distintos detectados |
| porcentaje_unicos | Porcentaje de unicidad (2 decimales) |
| ejemplo_valor | Primer valor válido detectado en la columna |

## Autor
**Ian Alexei Muñoz Tanasescu**
