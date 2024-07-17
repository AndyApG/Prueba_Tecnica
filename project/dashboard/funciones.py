import pandas as pd
from openpyxl import load_workbook
from django.core.exceptions import ValidationError
from .models import Auto, Cliente, Contrato

def read_file(file):
    if file.name.endswith('.csv'):
        df = pd.read_csv(file,  encoding='utf8', sep=',')
        column_names = df.columns

    elif file.name.endswith('.xlsx'):
        df = pd.read_excel(file)
        column_names = df.columns
    else:
        raise ValidationError("Por favor selecciona un archivo CSV o XLSX.")
    
    expected_columns = ['Nombres','Apellidos',
                        'Número de documento','Inicio de contrato',
                        'Cuota semanal','Marca del auto',
                        'Modelo del auto','Placa del auto']  
    if list(column_names) != expected_columns:
        raise ValidationError(f"Número inválido de comumnas. se esperaba: {expected_columns}, tu archivo tiene {df.columns}")
    
    for _, row in df.iterrows():
        auto, created_auto = Auto.objects.get_or_create(marca=row['Marca del auto'], modelo=row['Modelo del auto'], placa=row['Placa del auto'])
        cliente, created_cliente = Cliente.objects.get_or_create(nombre=row['Nombres'],apellidos=row['Apellidos'])
        contrato, created_contrato = Contrato.objects.get_or_create(num_doc=row['Número de documento'],ini_cont=row['Inicio de contrato'],
                                cuota=row['Cuota semanal'], cliente=cliente, auto=auto)