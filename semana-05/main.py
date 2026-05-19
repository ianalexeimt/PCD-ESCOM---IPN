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
