class Empleado:
    def __init__(self, codigo, nombre, area, salario):
        self.codigo = codigo
        self.nombre = nombre
        self.area = area
        self.salario = salario

    def calcular_iva(self):
        return self.salario * 0.16 if self.salario >= 3000 else 0

    def salario_neto(self):
        return self.salario - self.calcular_iva()

    def mostrar(self):
        print("\n--- Empleado ---")
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Área: {self.area}")
        print(f"Salario bruto: ${self.salario:.2f}")
        print(f"IVA: ${self.calcular_iva():.2f}")
        print(f"Salario neto: ${self.salario_neto():.2f}")


# Lista de empleados
empleados = []

def buscar_empleado(codigo):
    for emp in empleados:
        if emp.codigo == codigo:
            return emp
    return None


# Menú principal de empleados
while True:
    print("\n*** MENÚ DE EMPLEADOS ***")
    print("1) Registrar empleado")
    print("2) Consultar empleado")
    print("3) Modificar empleado")
    print("4) Eliminar empleado")
    print("5) Mostrar todos")
    print("0) Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        c = input("Código: ")
        n = input("Nombre: ")
        a = input("Área: ")
        s = float(input("Salario: $"))
        nuevo = Empleado(c, n, a, s)
        empleados.append(nuevo)
        print("Empleado agregado.")

    elif opcion == "2":
        c = input("Código a buscar: ")
        emp = buscar_empleado(c)
        if emp:
            emp.mostrar()
        else:
            print("No encontrado.")

    elif opcion == "3":
        c = input("Código a modificar: ")
        emp = buscar_empleado(c)
        if emp:
            emp.nombre = input("Nuevo nombre: ")
            emp.area = input("Nueva área: ")
            emp.salario = float(input("Nuevo salario: $"))
            print("Empleado actualizado.")
        else:
            print("No encontrado.")

    elif opcion == "4":
        c = input("Código a eliminar: ")
        emp = buscar_empleado(c)
        if emp:
            empleados.remove(emp)
            print("Empleado eliminado.")
        else:
            print("No encontrado.")

    elif opcion == "5":
        if empleados:
            for e in empleados:
                e.mostrar()
        else:
            print("No hay empleados registrados.")

    elif opcion == "0":
        print("Saliendo del sistema de empleados...")
        break
    else:
        print("Opción inválida.")
