# Lector de csv y xlms

Aplicación en Django, que permite registrarte iniciar sesión, cargar archivos .csv y .xlsx para su visualización y selección de columnas previamente conocidas. 

## Requisitos previos

- Python 3.10.12
- Django 4.2.14
- pip 22.0.2 
- Git 2.34.1

## Instalación

### 1. Clonar el repositorio

```bash
    git clone https://github.com/AndyApG/Prueba_Tecnica.git
    cd Prueba_Tecnica
```
### 2. Crear y activar un entorno virtual
```bash

    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`

```
### 3. Instalar las dependencias
```bash
pip install -r requirements.txt
cd project
```
### 4. Crea las migraciones
```bash
python manage.py make migrate
```
### 5. Crea un superusuario
```bash
python manage.py createsuperuser

```
## 6. Correr localmente
```bash
python manage.py runserver
```
