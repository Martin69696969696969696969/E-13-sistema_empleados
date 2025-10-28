class Empleado:
    def __init__(self, id_empleado=None, nombre=None, sexo=None, correo=None):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.sexo = sexo
        self.correo = correo
    
    def to_dict(self):
        return {
            'id_empleado': self.id_empleado,
            'nombre': self.nombre,
            'sexo': self.sexo,
            'correo': self.correo
        }
    
    def __str__(self):
        return f"ID: {self.id_empleado}, Nombre: {self.nombre}, Sexo: {self.sexo}, Correo: {self.correo}"