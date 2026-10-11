import calendar

def dias_mes(anio, mes):
    return calendar.monthrange(anio, mes)[1]

anio = int(input("Ingrese año: "))
mes = int(input("Ingrese mes: "))
print(dias_mes(anio, mes))