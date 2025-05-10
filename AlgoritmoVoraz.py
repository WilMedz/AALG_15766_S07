denominaciones = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05]

monto = float(input("ingrese el monto a pagar : "))

cantidades = []

for de in denominaciones:
    cant = int(monto // de)
    cantidades.append(cant)
    monto = round(monto - cant * de, 2)  
        
print("cantidad por denominación :")
for i in range(len(denominaciones)):
    print(f"{cantidades[i]} de ${denominaciones[i]}")