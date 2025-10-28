# 📋 README - Sistema de Registro de Empleados
📖 Descripción
Sistema de gestión de empleados desarrollado en Python con interfaz gráfica Tkinter y base de datos MySQL. Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre registros de empleados de manera segura y eficiente.

✨ Características
🖼️ Interfaz gráfica intuitiva con Tkinter

🗄️ Base de datos MySQL con consultas seguras

👥 Gestión completa de empleados (Agregar, Ver, Eliminar, Buscar)

🛡️ Validación de datos y prevención de inyecciones SQL

🎯 Generación automática de IDs

📊 Estructura modular y código escalable

🔍 Búsqueda por ID de empleados

## 🏗️ Estructura del Proyecto
```bash
text
sistema_empleados/
├── main.py                 # Punto de entrada de la aplicación
├── database.py            # Gestión de conexión y operaciones con MySQL
├── empleado.py            # Modelo de datos Empleado
├── gui.py                 # Interfaz gráfica con Tkinter
├── setup_database.py      # Script de configuración inicial de BD
└── README.md              # Este archivo
```
## 📋 Prerrequisitos
Software Requerido
Python 3.8+

MySQL Server 8.0+

Bibliotecas Python:

mysql-connector-python

tkinter (incluido en Python por defecto)

Instalación de Dependencias
bash
```bash
pip install mysql-connector-python
```
## ⚙️ Configuración
1. Configuración de la Base de Datos
Ejecutar el script de configuración inicial (solo una vez):
```
bash
```bash
python setup_database.py
Este script:

Crea la base de datos sistema_empleados

Crea la tabla empleados con la estructura necesaria

Inserta datos de ejemplo
```
2. Configurar Credenciales de MySQL
En los archivos database.py y setup_database.py, actualiza las credenciales:

python
```bash
# En database.py y setup_database.py
connection_config = {
    'host': 'localhost',
    'user': 'root',           # Tu usuario de MySQL
    'password': 'tu_password' # Tu contraseña de MySQL
}
```
## 🚀 Ejecución
Una vez configurada la base de datos, ejecuta la aplicación:

bash
python main.py
🎯 Funcionalidades
👀 Ver Empleados
Lista completa de todos los empleados registrados

Información mostrada: ID, Nombre, Sexo, Correo

Actualización automática al realizar cambios

## ➕ Agregar Empleado
Campos requeridos:

Nombre (texto)

Sexo (selección: M, F, Otro)

Correo electrónico (validado)

ID generado automáticamente por la base de datos

Validaciones:

Campos obligatorios

Formato de correo electrónico

Correo único en el sistema

## 🔍 Buscar Empleado
Búsqueda por ID de empleado

Resaltado en la lista

Información detallada en ventana emergente

## ❌ Eliminar Empleado
Eliminación por selección en la lista

Confirmación antes de eliminar

Actualización inmediata de la lista

## 🗃️ Estructura de la Base de Datos
```bash
Tabla: empleados
Campo	Tipo	Descripción
id_empleado	INT AUTO_INCREMENT	ID único del empleado (PK)
nombre	VARCHAR(100)	Nombre completo del empleado
sexo	ENUM('M','F','Otro')	Sexo del empleado
correo	VARCHAR(100)	Correo electrónico único
fecha_registro	TIMESTAMP	Fecha y hora de registro automática
```
## 🛠️ Desarrollo
```bash
Modelo de Datos (empleado.py)
python
class Empleado:
    def __init__(self, id_empleado=None, nombre=None, sexo=None, correo=None):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.sexo = sexo
        self.correo = correo
Gestión de Base de Datos (database.py)
Clase DatabaseManager con métodos para:

agregar_empleado() - Insertar nuevo empleado

obtener_empleados() - Obtener todos los registros

eliminar_empleado() - Eliminar por ID

buscar_empleado_por_id() - Buscar empleado específico

Interfaz Gráfica (gui.py)
Clase SistemaEmpleadosGUI que incluye:

Formulario de registro

Lista de empleados con Treeview

Funciones de búsqueda y eliminación

Validaciones y mensajes de usuario
```
## 🔒 Seguridad
Consultas preparadas para prevenir inyecciones SQL

Validación de entrada en el lado del cliente y servidor

Manejo de errores robusto

Conexiones seguras a la base de datos

🐛 Solución de Problemas
```bash
Error de Conexión a MySQL
python
# Verificar en database.py:
# - Host correcto
# - Usuario y contraseña válidos
# - Base de datos existe (ejecutar setup_database.py)
Error "ModuleNotFoundError"
bash
# Instalar dependencias faltantes
pip install mysql-connector-python
La aplicación no inicia
Verificar que setup_database.py se ejecutó correctamente
```
Revisar credenciales de MySQL en database.py

📝 Registro de Cambios
Versión 1.0.0

✅ Gestión básica de empleados (CRUD)

✅ Interfaz gráfica con Tkinter

✅ Conexión a MySQL segura

✅ Validación de datos

✅ Búsqueda por ID

## 🚀 Próximas Características
Edición de empleados existentes

Exportación de datos a Excel/PDF

Filtros avanzados de búsqueda

Backup automático de base de datos

Roles de usuario y autenticación

## Evidencia

<img width="2833" height="1830" alt="image" src="https://github.com/user-attachments/assets/a68b60dc-9981-4ef6-8472-2d746696879f" />

## 👥 Contribución
Fork del proyecto

Crear una rama para la feature (git checkout -b feature/nuevaFeature)

Commit de los cambios (git commit -am 'Agregar nueva feature')

Push a la rama (git push origin feature/nuevaFeature)

Crear Pull Request

## 📄 Licencia
Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para detalles.

## 📞 Soporte
Para soporte o consultas: 667733445533

Revisar la sección de Solución de Problemas

Crear un issue en el repositorio

¡Disfruta usando el Sistema de Registro de Empleados! 🎉
