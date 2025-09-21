class Alumno:
    def __init__(self, matricula, nombre, carrera):
        self.matricula = matricula
        self.nombre = nombre
        self.carrera = carrera
        self.calificaciones = []

    def agregar_calificaciones(self):
        print("Ingresa 3 calificaciones del alumno:")
        for i in range(1, 4):
            cal = float(input(f"Calificación {i}: "))
            self.calificaciones.append(cal)

    def promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones) if self.calificaciones else 0

    def mostrar(self):
        print("\n--- Alumno ---")
        print(f"Matrícula: {self.matricula}")
        print(f"Nombre: {self.nombre}")
        print(f"Carrera: {self.carrera}")
        print(f"Calificaciones: {self.calificaciones}")
        print(f"Promedio: {self.promedio():.2f}")


# Lista de alumnos
alumnos = []

def buscar_alumno(matricula):
    for alumno in alumnos:
        if alumno.matricula == matricula:
            return alumno
    return None


# Menú principal de alumnos
while True:
    print("\n*** MENÚ DE ALUMNOS ***")
    print("1) Registrar alumno")
    print("2) Consultar alumno")
    print("3) Modificar alumno")
    print("4) Eliminar alumno")
    print("5) Mostrar todos")
    print("0) Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        m = input("Matrícula: ")
        n = input("Nombre: ")
        c = input("Carrera: ")
        nuevo = Alumno(m, n, c)
        nuevo.agregar_calificaciones()
        alumnos.append(nuevo)
        print("Alumno registrado.")

    elif opcion == "2":
        m = input("Matrícula a buscar: ")
        alumno = buscar_alumno(m)
        if alumno:
            alumno.mostrar()
        else:
            print("No encontrado.")

    elif opcion == "3":
        m = input("Matrícula a modificar: ")
        alumno = buscar_alumno(m)
        if alumno:
            alumno.nombre = input("Nuevo nombre: ")
            alumno.carrera = input("Nueva carrera: ")
            alumno.calificaciones = []
            alumno.agregar_calificaciones()
            print("Alumno actualizado.")
        else:
            print("No encontrado.")

    elif opcion == "4":
        m = input("Matrícula a eliminar: ")
        alumno = buscar_alumno(m)
        if alumno:
            alumnos.remove(alumno)
            print("Alumno eliminado.")
        else:
            print("No encontrado.")

    elif opcion == "5":
        if alumnos:
            for a in alumnos:
                a.mostrar()
        else:
            print("No hay alumnos registrados.")

    elif opcion == "0":
        print("Saliendo del sistema de alumnos...")
        break
    else:
        print("Opción inválida.")
