# Cine Norte

Aplicacion web de cartelera construida con Django.

## Requisitos

- Python 3.10 o superior
- PowerShell en Windows

## Instalacion y ejecucion

Abre una terminal en la carpeta raiz del proyecto:

```powershell
cd C:\ruta\a\cine_norte
```

### 1. Crear el entorno virtual

```powershell
python -m venv .venv
```

### 2. Activar el entorno virtual

```powershell
.\.venv\Scripts\Activate.ps1 o .venv\Scripts\Activate
```

Si PowerShell bloquea la activacion de scripts, ejecuta PowerShell como usuario y usa:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar las dependencias

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Ejecutar las migraciones

```powershell
python manage.py migrate
```

### 5. Iniciar el servidor

```powershell
python manage.py runserver
```

Abre en el navegador:

- Cartelera: http://127.0.0.1:8000/peliculas/
- Administracion: http://127.0.0.1:8000/admin/

Para detener el servidor, presiona `Ctrl+C`. Para salir del entorno virtual:

```powershell
deactivate
```

## Estructura principal

- `config/`: configuracion y URLs principales de Django.
- `cartelera/`: vistas, rutas y plantillas de la cartelera.
- `templates/`: plantilla base del sitio.
- `static/`: archivos CSS y otros recursos estaticos.
- `requirements.txt`: dependencias del proyecto.
