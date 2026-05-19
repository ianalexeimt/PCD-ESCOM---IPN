import argparse
import sys
import os

def es_valor_nulo (valor):
    if valor is None:
        return True
    if isinstance(valor, str) and valor.strip() == '':
        return True
    return False

def es_numerico (valor):
    try:
        float(str(valor).replace(',', '').strip())
        return True
    except ValueError:
        pass
    except TypeError:
        pass
    return False

def es_fecha (valor):
    v=str(valor).strip()
    if len(v) >= 10 and v[4] == '-' and v[7] == '-':
        try:
            partes=v[:10].split('-')
            anio=int(partes[0])
            mes=int(partes[1])
            dia=int(partes[2])
            if 1900 <= anio <= 2100 and 1 <= mes <= 12 and 1 <= dia <= 31:
                return True
        except ValueError:
            pass
        except IndexError:
            pass
    return False


def es_booleano (valor):
    v=str(valor).strip().lower()
    if v in ['true', 'false', 'yes', 'no', 'si', '1', '0', 't', 'f']:
        return True
    return False

def inferir_tipo (valores):
    valores_validos=[]
    for v in valores:
        if not es_valor_nulo(v):
            valores_validos.append(v)

    if not valores_validos:
        return 'texto'

    total=len(valores_validos)
    umbral=0.8
    num_fechas=0
    num_booleanos=0
    num_numericos=0

    for v in valores_validos:
        if es_fecha(v):
            num_fechas+=1
        if es_booleano(v):
            num_booleanos+=1
        if es_numerico(v):
            num_numericos+=1

    if num_fechas/total >= umbral:
        return 'fecha'
    if num_booleanos/total >= umbral:
        return 'booleano'
    if num_numericos/total >= umbral:
        return 'numerico'
    return 'texto'

def perfilar_columna (nombre, valores):
    total=len(valores)
    nulos=0
    valores_no_nulos=[]

    for v in valores:
        if es_valor_nulo(v):
            nulos+=1
        else:
            valores_no_nulos.append(v)

    unicos_set=set(valores_no_nulos)
    unicos=len(unicos_set)

    if valores_no_nulos:
        ejemplo=valores_no_nulos[0]
    else:
        ejemplo=''

    tipo=inferir_tipo(valores)

    if total > 0:
        pct_nulos=round(nulos/total * 100, 2)
        pct_unicos=round(unicos/total * 100, 2)
    else:
        pct_nulos=0.00
        pct_unicos=0.00

    return {'nombre_columna': nombre, 'tipo_inferido': tipo, 'total_registros': total, 'valores_nulos': nulos, 'porcentaje_nulos': pct_nulos, 'valores_unicos': unicos, 'porcentaje_unicos': pct_unicos, 'ejemplo_valor': ejemplo}

def leer_csv (ruta):
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            lineas=f.readlines()
            if not lineas:
                return [], []

            encabezados=lineas[0].strip().split(',')
            filas=[]
            for linea in lineas[1:]:
                linea_limpia=linea.strip()
                if linea_limpia:
                    filas.append(linea_limpia.split(','))
            return encabezados, filas
    except FileNotFoundError:
        sys.exit(1)

def escribir_csv (ruta, perfiles):
    directorio=os.path.dirname(ruta)
    if directorio and not os.path.exists(directorio):
        os.makedirs(directorio)

    columnas=['nombre_columna', 'tipo_inferido', 'total_registros', 'valores_nulos', 'porcentaje_nulos', 'valores_unicos', 'porcentaje_unicos', 'ejemplo_valor']

    with open(ruta, 'w', encoding='utf-8') as f:
        f.write(','.join(columnas) + '\n')

        for p in perfiles:
            pct_nulos_str=f"{p['porcentaje_nulos']:.2f}"
            pct_unicos_str=f"{p['porcentaje_unicos']:.2f}"
            valores=[str(p['nombre_columna']), str(p['tipo_inferido']), str(p['total_registros']), str(p['valores_nulos']), pct_nulos_str, str(p['valores_unicos']), pct_unicos_str, str(p['ejemplo_valor'])]
            f.write(','.join(valores) + '\n')

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--input', '-i', required=True)
    parser.add_argument('--output', '-o', required=True)
    args=parser.parse_args()

    resultado_lectura=leer_csv(args.input)
    encabezados=resultado_lectura[0]
    filas=resultado_lectura[1]

    if not encabezados:
        sys.exit(1)

    perfiles=[]
    for i, nombre_col in enumerate(encabezados):
        valores=[]
        for fila in filas:
            if i < len(fila):
                valores.append(fila[i])
            else:
                valores.append('')
        perfil=perfilar_columna(nombre_col, valores)
        perfiles.append(perfil)

    escribir_csv(args.output, perfiles)

if __name__ == '__main__':
    main()