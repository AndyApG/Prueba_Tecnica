from django.core.exceptions import ValidationError

import pandas as pd
from openpyxl import load_workbook

from ..models.auto import Auto
from ..models.cliente import  Cliente
from ..models.contrato import Contrato

def read_file(file):

    if file.name.endswith('.csv'):
        df = pd.read_csv(file,  encoding='utf8', sep=',')
        

    elif file.name.endswith('.xlsx'):
        df = pd.read_excel(file)
       
    else:
        raise ValidationError('Por favor selecciona un archivo CSV o XLSX.')
    
    expected_columns = ['Nombres', 
                        'Apellidos', 
                        'Número de documento', 
                        'Inicio de contrato', 
                        'Cuota semanal', 
                        'Marca del auto', 
                        'Modelo del auto', 
                        'Placa del auto']  
    
    column_names = df.columns
    if list(column_names) != expected_columns:
        raise ValidationError('f Número inválido de comumnas. se esperaba: {expected_columns}, \
                              tu archivo tiene {column_names}')
    
    for _, row in df.iterrows():
        auto, _= Auto.objects.update_or_create(marca=row['Marca del auto'], 
                                            modelo=row['Modelo del auto'], 
                                            placa=row['Placa del auto'])
        
        cliente, _ = Cliente.objects.get_or_create(nombre=row['Nombres'],
                                                   apellidos=row['Apellidos'],
                                                   num_doc=row['Número de documento'])
        
        Contrato.objects.get_or_create(ini_cont=row['Inicio de contrato'], 
                                       cuota=row['Cuota semanal'], 
                                       cliente=cliente, 
                                       auto=auto)