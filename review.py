access_global= []
estudiante={}

def vali_numericas(x):
    bandera=True
    while bandera:
        try:
            int_x = float(x)
            if int_x >= 0:
                bandera=False
        except ValueError:
            print("Dato inválido")
        if bandera:
            x=input("Ingresalo de nuevo: ").strip() 
    return int_x
    
def vali_alfabeticas(y):
    bandera=True
    while bandera:
        try:
            if y.replace(" ",""):
                bandera=False
        except ValueError:
            print("Dato inválido")
        if bandera:
            y=input("Ingresalo de nuevo: ").strip() 
    return y

def agregar_estudiante():
    codigo=vali_alfabeticas(input("Ingrese el código del estudiante: "))
    nombre=vali_alfabeticas(input("Ingrese el nombre completo del estudiante: "))
    notas_parciales = []
    for i in range(1,4):
        nota=vali_numericas((input(f"Ingrese la nota parcial {i + 1}: ")))
        notas_parciales.append(nota)
    nota_definitiva=sum(notas_parciales) / len(notas_parciales)
    
    estudiante = {
        "codigo": codigo,
        "nombre": nombre,
        "notas_parciales": notas_parciales,
        "nota_definitiva": nota_definitiva
    }
    
    access_global.append(estudiante)
    print("Estudiante registrado.")

def buscar_estudiante():
    codigo_buscar= input("Ingrese el código del estudiante a buscar: ")
    for estudiante in access_global:
        if estudiante["codigo"]==codigo_buscar:
            print("Código:", estudiante["codigo"])
            print("Nombre:", estudiante["nombre"])
            print("Notas Parciales:", estudiante["notas_parciales"])
            break
    else:
        print("Estudiante no encontrado.")

def actualizar_datos():
    codigo=vali_alfabeticas(("Ingrese el código del estudiante a actualizar: "))
    for estudiante in access_global:
        if estudiante["codigo"]==codigo:
            estudiante["nombre"] = input("Ingrese el nuevo nombre completo: ")
            for i in range(3):
                estudiante["notas_parciales"][i] = float(input(f"Ingrese la nueva nota parcial {i + 1}: "))
            estudiante["nota_definitiva"] = sum(estudiante["notas_parciales"]) / len(estudiante["notas_parciales"])
            print("Datos actualizados correctamente.")
            break
    else:
        print("Estudiante no encontrado.")

def borrar_estudiante():
    codigo_borrar = input("Ingrese el código del estudiante a borrar: ")
    for estudiante in access_global:
        if estudiante["codigo"] == codigo_borrar:
            access_global.remove(estudiante)
            print("Estudiante borrado correctamente.")
            break
    else:
        print("Estudiante no encontrado.")

def calcular_notas_definitivas():
    for estudiante in access_global:
        estudiante["nota_definitiva"] = sum(estudiante["notas_parciales"]) / len(estudiante["notas_parciales"])

def listar_estudiantes():
    for estudiante in access_global:
        print("Código:", estudiante["codigo"])
        print("Nombre:", estudiante["nombre"])
        print("Nota Definitiva:", estudiante["nota_definitiva"])
        print()

def promedio_general():
    if len(access_global) == 0:
        return 0
    total_notas_definitivas = sum(estudiante["nota_definitiva"] for estudiante in access_global)
    return total_notas_definitivas / len(access_global)

while True:
    print("MENÚ PRINCIPAL")
    print("1. Agregar un nuevo registro")
    print("2. Buscar un Estudiante")
    print("3. Actualizar datos del Estudiante")
    print("4. Borrar un estudiante")
    print("5. Calcular notas definitivas")
    print("6. Listar estudiantes con notas definitivas y ver promedio general")
    opcion = input("Seleccione una opción (1/2/3/4/5/6): ")

    if opcion == "1":
        agregar_estudiante()
    elif opcion == "2":
        buscar_estudiante()
    elif opcion == "3":
        actualizar_datos()
    elif opcion == "4":
        borrar_estudiante()
    elif opcion == "5":
        calcular_notas_definitivas()
    elif opcion == "6":
        listar_estudiantes()
        print("Promedio General del Curso:", promedio_general())
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
