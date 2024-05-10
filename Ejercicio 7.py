import math

def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area

radio1 = 5
radio2 = 10
radio3 = 2.5

# Muestra los resultados
print("El área de un círculo con radio", radio1, "es:", calcular_area_circulo(radio1))
print("El área de un círculo con radio", radio2, "es:", calcular_area_circulo(radio2))
print("El área de un círculo con radio", radio3, "es:", calcular_area_circulo(radio3))
