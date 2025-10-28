-- Script de creación de base de datos para Sistema de Empleados
-- Ejecutar este script en MySQL Workbench o desde la línea de comandos

-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS sistema_empleados;
USE sistema_empleados;

-- Crear usuario para la aplicación (opcional pero recomendado)
-- CREATE USER 'app_empleados'@'localhost' IDENTIFIED BY 'Password123!';
-- GRANT ALL PRIVILEGES ON sistema_empleados.* TO 'app_empleados'@'localhost';
-- FLUSH PRIVILEGES;

-- Crear tabla de empleados
CREATE TABLE IF NOT EXISTS empleados (
    id_empleado INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    sexo ENUM('M', 'F', 'Otro') NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    activo BOOLEAN DEFAULT TRUE,
    INDEX idx_nombre (nombre),
    INDEX idx_correo (correo),
    INDEX idx_fecha_registro (fecha_registro)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Crear tabla para auditoría (opcional para tracking de cambios)
CREATE TABLE IF NOT EXISTS auditoria_empleados (
    id_auditoria INT AUTO_INCREMENT PRIMARY KEY,
    id_empleado INT NOT NULL,
    accion ENUM('INSERT', 'UPDATE', 'DELETE') NOT NULL,
    datos_anteriores JSON,
    datos_nuevos JSON,
    fecha_auditoria TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR(50) DEFAULT USER(),
    INDEX idx_empleado (id_empleado),
    INDEX idx_fecha (fecha_auditoria),
    FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Insertar datos de ejemplo
INSERT INTO empleados (nombre, sexo, correo) VALUES
('Juan Pérez García', 'M', 'juan.perez@empresa.com'),
('María López Martínez', 'F', 'maria.lopez@empresa.com'),
('Carlos Rodríguez Silva', 'M', 'carlos.rodriguez@empresa.com'),
('Ana Fernández Castro', 'F', 'ana.fernandez@empresa.com'),
('Pedro Sánchez Ruiz', 'M', 'pedro.sanchez@empresa.com'),
('Laura González Méndez', 'F', 'laura.gonzalez@empresa.com'),
('Miguel Torres Díaz', 'M', 'miguel.torres@empresa.com'),
('Isabel Ramírez Ortiz', 'F', 'isabel.ramirez@empresa.com'),
('Jorge Navarro Jiménez', 'M', 'jorge.navarro@empresa.com'),
('Sofía Herrera Vega', 'F', 'sofia.herrera@empresa.com'),
('Alejandro Molina Santos', 'M', 'alejandro.molina@empresa.com'),
('Carmen Reyes Flores', 'F', 'carmen.reyes@empresa.com'),
('David Castillo Rojas', 'M', 'david.castillo@empresa.com'),
('Elena Vargas Campos', 'F', 'elena.vargas@empresa.com'),
('Roberto Medina Peña', 'M', 'roberto.medina@empresa.com');

-- Crear vistas útiles
CREATE OR REPLACE VIEW vista_empleados_activos AS
SELECT 
    id_empleado,
    nombre,
    sexo,
    correo,
    DATE_FORMAT(fecha_registro, '%d/%m/%Y %H:%i') AS fecha_registro_formateada,
    CASE 
        WHEN sexo = 'M' THEN 'Masculino'
        WHEN sexo = 'F' THEN 'Femenino'
        ELSE 'Otro'
    END AS sexo_completo
FROM empleados 
WHERE activo = TRUE
ORDER BY nombre;

-- Crear procedimientos almacenados útiles

-- Procedimiento para buscar empleados por nombre
DELIMITER //
CREATE PROCEDURE sp_buscar_empleados_por_nombre(IN patron_nombre VARCHAR(100))
BEGIN
    SELECT 
        id_empleado,
        nombre,
        sexo,
        correo,
        fecha_registro
    FROM empleados 
    WHERE nombre LIKE CONCAT('%', patron_nombre, '%')
    AND activo = TRUE
    ORDER BY nombre;
END //
DELIMITER ;

-- Procedimiento para obtener estadísticas
DELIMITER //
CREATE PROCEDURE sp_obtener_estadisticas_empleados()
BEGIN
    SELECT 
        COUNT(*) AS total_empleados,
        SUM(CASE WHEN sexo = 'M' THEN 1 ELSE 0 END) AS hombres,
        SUM(CASE WHEN sexo = 'F' THEN 1 ELSE 0 END) AS mujeres,
        SUM(CASE WHEN sexo = 'Otro' THEN 1 ELSE 0 END) AS otros,
        MIN(fecha_registro) AS fecha_primer_registro,
        MAX(fecha_registro) AS fecha_ultimo_registro
    FROM empleados 
    WHERE activo = TRUE;
END //
DELIMITER ;

-- Triggers para auditoría automática

-- Trigger para INSERT
DELIMITER //
CREATE TRIGGER tr_empleados_after_insert
    AFTER INSERT ON empleados
    FOR EACH ROW
BEGIN
    INSERT INTO auditoria_empleados (id_empleado, accion, datos_nuevos)
    VALUES (
        NEW.id_empleado,
        'INSERT',
        JSON_OBJECT(
            'nombre', NEW.nombre,
            'sexo', NEW.sexo,
            'correo', NEW.correo,
            'fecha_registro', NEW.fecha_registro
        )
    );
END //
DELIMITER ;

-- Trigger para UPDATE
DELIMITER //
CREATE TRIGGER tr_empleados_after_update
    AFTER UPDATE ON empleados
    FOR EACH ROW
BEGIN
    INSERT INTO auditoria_empleados (id_empleado, accion, datos_anteriores, datos_nuevos)
    VALUES (
        NEW.id_empleado,
        'UPDATE',
        JSON_OBJECT(
            'nombre', OLD.nombre,
            'sexo', OLD.sexo,
            'correo', OLD.correo
        ),
        JSON_OBJECT(
            'nombre', NEW.nombre,
            'sexo', NEW.sexo,
            'correo', NEW.correo
        )
    );
END //
DELIMITER ;

-- Trigger para DELETE
DELIMITER //
CREATE TRIGGER tr_empleados_after_delete
    AFTER DELETE ON empleados
    FOR EACH ROW
BEGIN
    INSERT INTO auditoria_empleados (id_empleado, accion, datos_anteriores)
    VALUES (
        OLD.id_empleado,
        'DELETE',
        JSON_OBJECT(
            'nombre', OLD.nombre,
            'sexo', OLD.sexo,
            'correo', OLD.correo,
            'fecha_registro', OLD.fecha_registro
        )
    );
END //
DELIMITER ;

-- Consultas de verificación
SELECT '=== ESTADÍSTICAS DE EMPLEADOS ===' AS '';
CALL sp_obtener_estadisticas_empleados();

SELECT '=== EMPLEADOS ACTIVOS ===' AS '';
SELECT * FROM vista_empleados_activos;

SELECT '=== AUDITORÍA RECIENTE ===' AS '';
SELECT 
    id_auditoria,
    id_empleado,
    accion,
    DATE_FORMAT(fecha_auditoria, '%d/%m/%Y %H:%i') AS fecha_auditoria,
    usuario
FROM auditoria_empleados 
ORDER BY fecha_auditoria DESC 
LIMIT 5;