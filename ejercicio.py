usuarios={}

def vali_codigo(x):
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

def vali_notas(x):
    bandera=True
    while  bandera:
        try:
            int_x = float(x)
            if int_x >= 0 and int_x<=50:
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

bandera=True
while bandera:
    codigo=vali_codigo(input("Ingresa tu codigo: "))
    if codigo==999:
        bandera=False
    else:
        nombre=vali_alfabeticas(input("Digita tu nombre: "))
        nota1=vali_notas(input("Digita tu nota #1: "))
        nota2=vali_notas(input("Digita tu nota #2: "))
        nota3=vali_notas(input("Digita tu nota #3: "))

        nota1_1=nota1*0.30
        nota2_2=nota2*0.30
        nota3_3=nota3*0.40
        nota_def=nota1_1+nota2_2+nota3_3
        if nota_def>3.0:
            resultado="APROBO"
        else:
            resultado="REPROBO"

        usuarios[codigo]={
                "codigo": id,
                "name": nombre,
                "nota_definitiva": nota_def,
                "resul": resultado
            }

print("RESUMEN DE LA CALIFICACION TRIPULANTE")
print("-"*30)

print(usuarios)
#corregir detalle


