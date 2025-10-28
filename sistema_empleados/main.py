#!/usr/bin/env python3
import tkinter as tk
from gui import SistemaEmpleadosGUI

def main():
    try:
        root = tk.Tk()
        app = SistemaEmpleadosGUI(root)
        root.mainloop()
    except Exception as e:
        print(f"Error al ejecutar la aplicación: {e}")

if __name__ == '__main__':
    main()