def vali_alfabeticas(y):
    bandera=True
    while bandera:
        try:
            if y.replace(" ","").isalpha():
                return y
        except ValueError:
            print("Dato inválido")
        
        y=input("Ingresalo de nuevo: ").strip() 
    

p=vali_alfabeticas(input("Digite: "))
print(p)