from datetime import datetime
eventos={}
def vali_numerica(x):
    bandera=True
    while   bandera:
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
        if bandera:
            y=input("Ingresalo de nuevo: ").strip() 
    return y

def vali_fecha(test_str):
    format = "%Y-%m-%d"
    d=True
    try:
        d=bool(datetime.strptime(test_str, format))
    except ValueError:
        d=False
    return d



def add_evento():
    name=vali_alfabeticas(input("Ingresa el nombre del evento: "))
    date=vali_fecha(input("\nIntroduzca la fecha de inicio (YYYY-M-D: \n"))
    place=vali_alfabeticas(input("Ingresa el nombre del lugar: "))
    cap_max=vali_numerica(input("Ingrese la capacidad maxima de asistentes al evento:  "))
    prize=vali_numerica(input("Ingrese el precio de netrada: "))
    
    eventos[name]={
        "fecha": date,
        "lugar": place,
        "capacidad_maxi": cap_max,
        "precio": prize 
    }


def modificar_evento():
    print("Que deseas modificar: ")
    print("1- Fecha")
    print("2- Lugar")
    print("3- Precio de entrada")
    op=vali_numerica(input("Ingrese una opcion de 1-3: "))
    if op==1:
        n=vali_alfabeticas("Ingresa el nombre dle evento: ")
        if n in eventos:
            nueva_fecha=vali_fecha(input("Ingresa la nueva fecha: "))
            eventos[n]["fecha"]= nueva_fecha
            print("DATOS ACTUALIZADOS: ")
            print(eventos[n]["name"], f"fecha: {eventos[n]['lugar']}",f"lugar: {eventos[n]['fecha']}", f"capacidad maxima: {eventos[n]['capacidad_maxi']}", f"precio entrada: {[n]['precio']}")

    if op==2:
        l=vali_alfabeticas("Ingresa el lugar del evento: ")
        if l in eventos:
            nuevo_lugar=vali_alfabeticas(input("Ingresa el nuevo lugar del evento: "))
            eventos[n]["lugar"]= nuevo_lugar

    if op==3:
        




