import os
import tabulate
empresa={}
persona=[]

def vali_numericas(x):
    bandera=True
    while bandera:
        try:
            int_x = int(x)
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
            if y.replace(" ","").isalpha():
                bandera=False
        except ValueError:
            print("Dato inválido")
        if not bandera:
            y=input("Ingresalo de nuevo: ").strip() 
    return y


def buscar_usuario(nd):
    for empleado in persona:
        if empleado[0] == nd:
            return empleado
    return None

def new_usu():
    nd=vali_numericas(input("Ingrese su numero de documento: "))
    if buscar_usuario(nd):
            print("El empleado ya existe.")
            #return menu
    n=vali_alfabeticas(input("Ingrese us nombre: "))
    e=vali_numericas(input("Ingrese su edad: "))
    eps=vali_alfabeticas(input("Ingrese le nombre de su eps: "))
    user={
        "numdoc": nd,
        "nombre": n,
        "edad": e,
        "eps": eps
    }
    persona.append(user)
    empresa.append(persona)

def delate_regi(nd):
    
    usu=buscar_usuario(nd)
    if usu:
        persona.remove(usu)
        print(f"El usuario {usu[0]} ha sido eliminado exitosamente.")
    else:
        print("El empleado no ha sido encontrado.")

def listado_total():
    for usuario in persona:
        print("\n---")
        print(f"ID: {usuario[0]}, Nombre: {usuario[1]}, Edad: {usuario[2]}, Eps: {usuario[3]}")

def atuali_usuario():
    print("Modificar usuario:")
    doc=vali_numericas(input("Ingresa el # de su documento: "))
    if doc in persona:
            print("Datos actuales del usuario:")
            print(persona[doc], f"NOMBRE: {persona[doc]['nombre']}, EDAD: {persona[doc]['edad']}, EPS:{persona[doc]['eps']}")
            print("¿Qué desea modificar?")  
            print("1- Nombre")
            print("2- Edad")
            print("3- Eps")
            opcion=vali_numericas(input("Seleccione una opción (1-3): "))
    
            if opcion==1:
                nuevo_nombre=vali_alfabeticas(input("Ingresa el nuevo nombre: "))
                persona[doc]['nombre']=nuevo_nombre
                print("DATOS ACTUALIZADOS: ")
                print(persona[doc], f"NOMBRE: {persona[doc]['nombre']}, EDAD: {persona[doc]['edad']}, EPS:{persona[doc]['eps']}")

            if opcion==2:
                nueva_edad=vali_numericas(input("Ingresa la nueva edad: "))
                persona[doc]['edad']=nueva_edad
                print("DATOS ACTUALIZADOS: ")
                print(persona[doc], f"NOMBRE: {persona[doc]['nombre']}, EDAD: {persona[doc]['edad']}, EPS:{persona[doc]['eps']}")
            else:
                print("Selecciona una opción válida")
    else:
            print("USUARIO NO ENCONTRADO")
            return



#print("|{:<20}|".format(nombre))
#" "*6+


def main():
    a=True
    while a:
        print("{:>30}".format("Selecciona una opcion: "))
        print("{:>40}".format("1- Ingresa un nuevo registro"))
        print("{:>34}".format("2- Elimina un registro"))
        print("{:>36}".format("3- Mostrar listado total"))
        print("{:>42}".format("4- Busca y muestra un registro"))
        print("{:>36}".format("5- Actualiza un registro"))
        print("{:>33}".format("6- Salir del registro"))
        
        op=vali_numericas(input("{:>40}".format("Ingresa una opcion de 1-6: ")))
        if op<1 or op>6:
            print("Opción inválida.")
        else:
            if op==1:
                new_usu()
            if op==2:
                delate_regi()
            if op==3:
                listado_total()
            if op==4:
                buscar_usuario()
            if op==5:
                atuali_usuario()
            if op==6:
                print("SALIENDO DEL PROGRAMA.....")
                break

main()




