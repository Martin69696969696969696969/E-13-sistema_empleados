import mysql.connector
from mysql.connector import Error
from empleado import Empleado

class DatabaseManager:
    def __init__(self):
        self.connection = None
        self.connect()
        self.create_table()
    
    def connect(self):
        """Establece conexión con la base de datos MySQL"""
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                database='sistemaempleados',
                user='root',
                password='toor'
            )
            if self.connection.is_connected():
                print("Conexión exitosa a MySQL")
        except Error as e:
            print(f"Error al conectar con MySQL: {e}")
    
    def create_table(self):
        """Crea la tabla de empleados si no existe"""
        try:
            cursor = self.connection.cursor()
            create_table_query = """
            CREATE TABLE IF NOT EXISTS empleados (
                id_empleado INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                sexo ENUM('M', 'F', 'Otro') NOT NULL,
                correo VARCHAR(100) UNIQUE NOT NULL,
                fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
            cursor.execute(create_table_query)
            self.connection.commit()
            cursor.close()
        except Error as e:
            print(f"Error al crear tabla: {e}")
    
    def agregar_empleado(self, empleado):
        """Agrega un nuevo empleado usando consultas preparadas"""
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO empleados (nombre, sexo, correo) VALUES (%s, %s, %s)"
            values = (empleado.nombre, empleado.sexo, empleado.correo)
            
            cursor.execute(query, values)
            self.connection.commit()
            empleado_id = cursor.lastrowid
            cursor.close()
            
            return empleado_id
        except Error as e:
            print(f"Error al agregar empleado: {e}")
            return None
    
    def obtener_empleados(self):
        """Obtiene todos los empleados"""
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM empleados ORDER BY id_empleado"
            cursor.execute(query)
            
            empleados = []
            for row in cursor.fetchall():
                empleado = Empleado(
                    id_empleado=row['id_empleado'],
                    nombre=row['nombre'],
                    sexo=row['sexo'],
                    correo=row['correo']
                )
                empleados.append(empleado)
            
            cursor.close()
            return empleados
        except Error as e:
            print(f"Error al obtener empleados: {e}")
            return []
    
    def eliminar_empleado(self, id_empleado):
        """Elimina un empleado por ID"""
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM empleados WHERE id_empleado = %s"
            cursor.execute(query, (id_empleado,))
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error al eliminar empleado: {e}")
            return False
    
    def buscar_empleado_por_id(self, id_empleado):
        """Busca un empleado por ID"""
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM empleados WHERE id_empleado = %s"
            cursor.execute(query, (id_empleado,))
            
            row = cursor.fetchone()
            cursor.close()
            
            if row:
                return Empleado(
                    id_empleado=row['id_empleado'],
                    nombre=row['nombre'],
                    sexo=row['sexo'],
                    correo=row['correo']
                )
            return None
        except Error as e:
            print(f"Error al buscar empleado: {e}")
            return None
    
    def cerrar_conexion(self):
        """Cierra la conexión a la base de datos"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada")