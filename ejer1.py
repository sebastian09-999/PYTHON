#Ejercicio 1 
Salario=float(input("Ingrese su salario mensual: "))
if Salario < 12000000:
    tasa=0.0
elif Salario <=15000000:
    tasa=0.03
elif Salario<=20000000:
    tasa=0.05
elif Salario<=30000000:
    tasa=0.08
else:
    tasa=0.10
    
impuesto=Salario*tasa

print("Resultado")
print(f"Monto total a pagar de impuesto:${impuesto:,}")