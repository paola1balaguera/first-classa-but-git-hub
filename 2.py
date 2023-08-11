n=int(input("Ingrese le # de docentes: "))
usuarios={}
for i in range(1,n+1):
    id=int(input("Ingresa tu id: "))
    nombre=input("Digita tu nombre: ")
    categoria=int(input("Diga su categoria: "))
    horas_trabajadas=int(input("Digite el # de horas trabajadas: "))
    valor_hora=int(input("Diga el valor de la hora: "))
    honorarios_valor={1:25000,2:30000,3:40000,4:45000,5:60000}

    valor_honorario=honorarios_valor[categoria]*horas_trabajadas

    usuarios[id]={
        #"id": id,
        "name": nombre,
        "category": categoria,
        "hours": horas_trabajadas,
        "cost hour": valor_hora,
        "fee": valor_honorario
    }
    valor_total=0
    valor_total+=valor_honorario

print("INFORME")
print("-"*30)

for id in usuarios:

    print(usuarios[id]['name'], f"${usuarios[id]['fee']:,.0f}")



