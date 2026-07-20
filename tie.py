import math
from datetime import date

# 1. Pedir datos al usuario
width_tire = float(input("enter the width of the tire: "))
aspect_ratio = int(input("Enter the aspect of the tire: "))
inches_diameter = float(input("Enter the diameter in inches: "))

# 2. Calcular
inner = aspect_ratio * width_tire / 100 + 2540 * inches_diameter
v = math.pi * width_tire ** 2 * aspect_ratio * inner / 10000000000

# 3. Mostrar resultado
print(f"The volume of the tire is: {v:.2f} ")

# 4. Obtener fecha
from datetime import date
today = date.today()

# 5. Guardar en el log
with open("volumes.txt", "a") as file:
    file.write(f"{today}, {width_tire}, {aspect_ratio}, {inches_diameter}, {v:.2f}\n")