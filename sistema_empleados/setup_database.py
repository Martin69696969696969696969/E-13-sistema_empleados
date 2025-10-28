#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error

def setup_database():
    """Configura la base de datos y crea las tablas"""
    
    connection_config = {
        'host': 'localhost',
        'user': 'root',  # Cambia por tu usuario de MySQL
        'password': 'toor'   # Cambia por tu contraseña de MySQL
    }
    
    try:
        # Conectar a MySQL
        connection = mysql.connector.connect(**connection_config)
        cursor = connection.cursor()
        
        print("✅ Conectado a MySQL server")
        
        # Crear base de datos
        cursor.execute("CREATE DATABASE IF NOT EXISTS sistemaempleados")
        cursor.execute("USE sistemaempleados")
        print("✅ Base de datos 'sistemaempleados' creada/verificada")
        
        # Crear tabla de empleados
        create_table_query = """
        CREATE TABLE IF NOT EXISTS empleados (
            id_empleado INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            sexo ENUM('M', 'F', 'Otro') NOT NULL,
            correo VARCHAR(100) UNIQUE NOT NULL,
            fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
        """
        cursor.execute(create_table_query)
        print("✅ Tabla 'empleados' creada/verificada")
        
        # Insertar datos de ejemplo
        sample_data = [
            ('Juan Pérez García', 'M', 'juan.perez@empresa.com'),
            ('María López Martínez', 'F', 'maria.lopez@empresa.com'),
            ('Carlos Rodríguez Silva', 'M', 'carlos.rodriguez@empresa.com'),
            ('Ana Fernández Castro', 'F', 'ana.fernandez@empresa.com'),
            ('Pedro Sánchez Ruiz', 'M', 'pedro.sanchez@empresa.com'),
            ('Laura González Méndez', 'F', 'laura.gonzalez@empresa.com'),
            ('Miguel Torres Díaz', 'M', 'miguel.torres@empresa.com'),
            ('Isabel Ramírez Ortiz', 'F', 'isabel.ramirez@empresa.com')
        ]
        
        insert_query = "INSERT IGNORE INTO empleados (nombre, sexo, correo) VALUES (%s, %s, %s)"
        cursor.executemany(insert_query, sample_data)
        connection.commit()
        print(f"✅ {cursor.rowcount} registros de ejemplo insertados")
        
        # Verificar datos
        cursor.execute("SELECT COUNT(*) FROM empleados")
        count = cursor.fetchone()[0]
        print(f"✅ Total de empleados en la base de datos: {count}")
        
        cursor.close()
        connection.close()
        print("✅ Configuración de base de datos completada exitosamente")
        
    except Error as e:
        print(f"❌ Error durante la configuración: {e}")

if __name__ == "__main__":
    setup_database()