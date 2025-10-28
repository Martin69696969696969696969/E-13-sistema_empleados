import tkinter as tk
from tkinter import ttk, messagebox
from database import DatabaseManager
from empleado import Empleado

class SistemaEmpleadosGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Registro de Empleados")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        # Conexión a la base de datos
        self.db = DatabaseManager()
        
        # Variables de control
        self.nombre_var = tk.StringVar()
        self.sexo_var = tk.StringVar()
        self.correo_var = tk.StringVar()
        self.buscar_var = tk.StringVar()
        
        self.crear_widgets()
        self.actualizar_lista_empleados()
    
    def crear_widgets(self):
        """Crea todos los elementos de la interfaz"""
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Título
        titulo = ttk.Label(main_frame, text="Sistema de Registro de Empleados", 
                          font=('Arial', 16, 'bold'))
        titulo.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Sección de búsqueda
        self.crear_seccion_busqueda(main_frame, 1)
        
        # Sección de formulario
        self.crear_seccion_formulario(main_frame, 2)
        
        # Sección de lista de empleados
        self.crear_seccion_lista(main_frame, 3)
    
    def crear_seccion_busqueda(self, parent, row):
        """Crea la sección de búsqueda"""
        search_frame = ttk.LabelFrame(parent, text="Buscar Empleado", padding="10")
        search_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        search_frame.columnconfigure(1, weight=1)
        
        ttk.Label(search_frame, text="ID del Empleado:").grid(row=0, column=0, padx=(0, 10))
        
        buscar_entry = ttk.Entry(search_frame, textvariable=self.buscar_var, width=20)
        buscar_entry.grid(row=0, column=1, padx=(0, 10), sticky=(tk.W, tk.E))
        
        buscar_btn = ttk.Button(search_frame, text="Buscar", command=self.buscar_empleado)
        buscar_btn.grid(row=0, column=2, padx=(0, 10))
        
        limpiar_btn = ttk.Button(search_frame, text="Limpiar", command=self.limpiar_busqueda)
        limpiar_btn.grid(row=0, column=3)
    
    def crear_seccion_formulario(self, parent, row):
        """Crea la sección del formulario para agregar empleados"""
        form_frame = ttk.LabelFrame(parent, text="Agregar Nuevo Empleado", padding="10")
        form_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        form_frame.columnconfigure(1, weight=1)
        
        # Nombre
        ttk.Label(form_frame, text="Nombre:").grid(row=0, column=0, padx=(0, 10), pady=5, sticky=tk.W)
        nombre_entry = ttk.Entry(form_frame, textvariable=self.nombre_var, width=30)
        nombre_entry.grid(row=0, column=1, columnspan=2, pady=5, sticky=(tk.W, tk.E))
        
        # Sexo
        ttk.Label(form_frame, text="Sexo:").grid(row=1, column=0, padx=(0, 10), pady=5, sticky=tk.W)
        sexo_combo = ttk.Combobox(form_frame, textvariable=self.sexo_var, 
                                 values=["M", "F", "Otro"], state="readonly", width=27)
        sexo_combo.grid(row=1, column=1, columnspan=2, pady=5, sticky=(tk.W, tk.E))
        
        # Correo
        ttk.Label(form_frame, text="Correo:").grid(row=2, column=0, padx=(0, 10), pady=5, sticky=tk.W)
        correo_entry = ttk.Entry(form_frame, textvariable=self.correo_var, width=30)
        correo_entry.grid(row=2, column=1, columnspan=2, pady=5, sticky=(tk.W, tk.E))
        
        # Botones del formulario
        btn_frame = ttk.Frame(form_frame)
        btn_frame.grid(row=3, column=0, columnspan=3, pady=(10, 0))
        
        agregar_btn = ttk.Button(btn_frame, text="Agregar Empleado", 
                               command=self.agregar_empleado)
        agregar_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        limpiar_btn = ttk.Button(btn_frame, text="Limpiar Campos", 
                               command=self.limpiar_campos)
        limpiar_btn.pack(side=tk.LEFT)
    
    def crear_seccion_lista(self, parent, row):
        """Crea la sección de la lista de empleados"""
        list_frame = ttk.LabelFrame(parent, text="Lista de Empleados", padding="10")
        list_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)
        parent.rowconfigure(row, weight=1)
        
        # Treeview para mostrar empleados
        columns = ('ID', 'Nombre', 'Sexo', 'Correo')
        self.tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=12)
        
        # Configurar columnas
        self.tree.heading('ID', text='ID')
        self.tree.heading('Nombre', text='Nombre')
        self.tree.heading('Sexo', text='Sexo')
        self.tree.heading('Correo', text='Correo')
        
        self.tree.column('ID', width=50)
        self.tree.column('Nombre', width=200)
        self.tree.column('Sexo', width=80)
        self.tree.column('Correo', width=200)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Botón eliminar
        eliminar_btn = ttk.Button(list_frame, text="Eliminar Empleado Seleccionado", 
                                command=self.eliminar_empleado)
        eliminar_btn.grid(row=1, column=0, pady=(10, 0), sticky=tk.W)
        
        # Bind double click para editar
        self.tree.bind('<Double-1>', self.editar_empleado_seleccionado)
    
    def actualizar_lista_empleados(self):
        """Actualiza la lista de empleados en el Treeview"""
        # Limpiar treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Obtener empleados de la base de datos
        empleados = self.db.obtener_empleados()
        
        # Insertar empleados en el treeview
        for empleado in empleados:
            self.tree.insert('', tk.END, values=(
                empleado.id_empleado,
                empleado.nombre,
                empleado.sexo,
                empleado.correo
            ))
    
    def agregar_empleado(self):
        """Agrega un nuevo empleado a la base de datos"""
        nombre = self.nombre_var.get().strip()
        sexo = self.sexo_var.get()
        correo = self.correo_var.get().strip()
        
        # Validaciones
        if not nombre:
            messagebox.showerror("Error", "El nombre es obligatorio")
            return
        
        if not sexo:
            messagebox.showerror("Error", "El sexo es obligatorio")
            return
        
        if not correo:
            messagebox.showerror("Error", "El correo es obligatorio")
            return
        
        if '@' not in correo:
            messagebox.showerror("Error", "El correo electrónico no es válido")
            return
        
        # Crear objeto Empleado
        nuevo_empleado = Empleado(nombre=nombre, sexo=sexo, correo=correo)
        
        # Agregar a la base de datos
        empleado_id = self.db.agregar_empleado(nuevo_empleado)
        
        if empleado_id:
            messagebox.showinfo("Éxito", f"Empleado agregado correctamente\nID generado: {empleado_id}")
            self.limpiar_campos()
            self.actualizar_lista_empleados()
        else:
            messagebox.showerror("Error", "No se pudo agregar el empleado. Verifique que el correo no exista.")
    
    def eliminar_empleado(self):
        """Elimina el empleado seleccionado"""
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un empleado para eliminar")
            return
        
        # Obtener ID del empleado seleccionado
        item = seleccion[0]
        empleado_id = self.tree.item(item, 'values')[0]
        
        # Confirmar eliminación
        confirmar = messagebox.askyesno(
            "Confirmar Eliminación", 
            f"¿Está seguro de que desea eliminar al empleado con ID {empleado_id}?"
        )
        
        if confirmar:
            if self.db.eliminar_empleado(empleado_id):
                messagebox.showinfo("Éxito", "Empleado eliminado correctamente")
                self.actualizar_lista_empleados()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el empleado")
    
    def buscar_empleado(self):
        """Busca un empleado por ID"""
        id_buscar = self.buscar_var.get().strip()
        if not id_buscar:
            messagebox.showwarning("Advertencia", "Ingrese un ID para buscar")
            return
        
        try:
            empleado_id = int(id_buscar)
        except ValueError:
            messagebox.showerror("Error", "El ID debe ser un número válido")
            return
        
        empleado = self.db.buscar_empleado_por_id(empleado_id)
        
        if empleado:
            # Limpiar y seleccionar el empleado en el treeview
            for item in self.tree.get_children():
                if self.tree.item(item, 'values')[0] == empleado_id:
                    self.tree.selection_set(item)
                    self.tree.focus(item)
                    self.tree.see(item)
                    break
            messagebox.showinfo("Empleado Encontrado", str(empleado))
        else:
            messagebox.showinfo("No Encontrado", f"No se encontró ningún empleado con ID {empleado_id}")
    
    def editar_empleado_seleccionado(self, event):
        """Permite editar el empleado seleccionado al hacer doble click"""
        seleccion = self.tree.selection()
        if not seleccion:
            return
        
        item = seleccion[0]
        empleado_id = self.tree.item(item, 'values')[0]
        
        empleado = self.db.buscar_empleado_por_id(empleado_id)
        if empleado:
            self.mostrar_ventana_edicion(empleado)
    
    def mostrar_ventana_edicion(self, empleado):
        """Muestra una ventana para editar el empleado"""
        edicion_window = tk.Toplevel(self.root)
        edicion_window.title(f"Editar Empleado ID: {empleado.id_empleado}")
        edicion_window.geometry("400x300")
        edicion_window.resizable(False, False)
        edicion_window.transient(self.root)
        edicion_window.grab_set()
        
        # Variables de control
        nombre_var = tk.StringVar(value=empleado.nombre)
        sexo_var = tk.StringVar(value=empleado.sexo)
        correo_var = tk.StringVar(value=empleado.correo)
        
        # Widgets de edición
        ttk.Label(edicion_window, text="Nombre:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        nombre_entry = ttk.Entry(edicion_window, textvariable=nombre_var, width=30)
        nombre_entry.grid(row=0, column=1, padx=10, pady=10)
        
        ttk.Label(edicion_window, text="Sexo:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        sexo_combo = ttk.Combobox(edicion_window, textvariable=sexo_var, 
                                 values=["M", "F", "Otro"], state="readonly", width=27)
        sexo_combo.grid(row=1, column=1, padx=10, pady=10)
        
        ttk.Label(edicion_window, text="Correo:").grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        correo_entry = ttk.Entry(edicion_window, textvariable=correo_var, width=30)
        correo_entry.grid(row=2, column=1, padx=10, pady=10)
        
        def guardar_cambios():
            nombre = nombre_var.get().strip()
            sexo = sexo_var.get()
            correo = correo_var.get().strip()
            
            if not nombre or not sexo or not correo:
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return
            
            if '@' not in correo:
                messagebox.showerror("Error", "El correo electrónico no es válido")
                return
            
            # Actualizar empleado (en una implementación real, agregarías un método update_empleado en DatabaseManager)
            messagebox.showinfo("Info", "Funcionalidad de edición en desarrollo")
            edicion_window.destroy()
        
        ttk.Button(edicion_window, text="Guardar Cambios", 
                  command=guardar_cambios).grid(row=3, column=0, columnspan=2, pady=20)
    
    def limpiar_campos(self):
        """Limpia los campos del formulario"""
        self.nombre_var.set("")
        self.sexo_var.set("")
        self.correo_var.set("")
    
    def limpiar_busqueda(self):
        """Limpia el campo de búsqueda"""
        self.buscar_var.set("")
        self.actualizar_lista_empleados()
    
    def __del__(self):
        """Cierra la conexión a la base de datos al destruir la instancia"""
        if hasattr(self, 'db'):
            self.db.cerrar_conexion()