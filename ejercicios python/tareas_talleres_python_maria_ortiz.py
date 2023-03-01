# -*- coding: utf-8 -*-
"""Tareas talleres Python_Maria Ortiz.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D8WLgkVXzxpZucsO2bTkvZceYkBMQQOV

**Clase 1: Descargar programas y hacer hola mundo.**
"""

print("Hola mundo")

"""**Clase 2: tarea variables**"""

num_id = 1020304050
nombre = "Pepito"
apellido = "Perez"
direccion = "calle 80 # 80 - 20"
telefono = 3103103103
edad = 34
estado_civil = "soltero"
num_hijos = 4
estatura_cm = "176"
fecha_cont = "17/02/2022"
sueldo_bas = 3400000
dias_labr = 260
print(num_id)
print(nombre)
print(apellido)
print(direccion)
print(telefono)
print(edad)
print(estado_civil)
print(num_hijos)
print(estatura_cm)
print(fecha_cont)
print(sueldo_bas)
print(dias_labr)

"""**Taller clase 3 (refuerzo)**
1. Un vendedor recibe un sueldo base más un 10% extra por
comisión de sus ventas, el vendedor desea saber cuánto
dinero obtendrá por concepto de comisiones por las tres
ventas que realiza en el mes y el total que recibirá en
el mes tomando en cuenta su sueldo base y comisiones.
3. No toca hacerlo
2. Una tienda ofrece un descuento del 15% sobre el total
de la compra y un cliente desea saber cuánto deberá
pagar finalmente por su compra.
4. Un maestro desea saber qué porcentaje de hombres y que
porcentaje de mujeres hay en un grupo de estudiantes.
"""

sueldo_base = float(input("Digite su sueldo base: "))
venta1 = float(input("Digite el valor de la venta 1: "))
venta2 = float(input("Digite el valor de la venta 2: "))
venta3 = float(input("Digite el valor de la venta 3: "))
comision_ventas = ((venta1 + venta2 + venta3)*0.10)
total = comision_ventas + sueldo_base
print("La comision por las 3 ventas es= {:,.0f}".format(comision_ventas))
print("El total a recibir en el mes es= {:,.0f}".format(total))

compra = float(input("Digite el valor de su compra: "))
descuento = compra * 0.15
total = compra - descuento
print(f"Valor a pagar= {total}")

num_estudiantes = int(input("Digite el numero total de estudiantes: "))
num_mujeres = int(input("Digite el numero de estudiantes mujeres: " ))
num_hombres = int(input("Digite el numero de estudiantes hombres: " ))
porc_mujeres = (num_mujeres * 100)/num_estudiantes
porc_hombres = (num_hombres * 100)/num_estudiantes
print("El porcentaje de estudiantes mujeres es: {:,.1f}%".format(porc_mujeres))
print("El porcentaje de estudiantes hombres es: {:,.1f}%".format(porc_hombres))

"""**Taller clase 4**

Dando continuidad con la primera entrega del proyecto, en esta oportunidad el estudiante debe realizar las siguientes validaciones utilizando la sentencia condicional IF.

Si el empleado es mayor de 55 años disfrutará de un bono de prepensión correspondiente al 5% de su sueldo básico.

Si el empleado es casado y tiene hijos se le otorgará un paseo cada diciembre

Si el sueldo básico está entre 1000000 y 1500000 tendrá una comisión del 2% sobre el valor del sueldo; Si el sueldo básico está entre 1500001 y 2000000 tendrá una comisión del 5% sobre el valor del sueldo; para todos los demás casos no habrá comisión.

Si el empleado trabajó más de 20 días al mes y su sueldo es menor a 1000000 tendrá derecho a un bono de alimentación.
"""

edad = int(input("Digite su edad: "))
estado_civil = input("Digite su estado civil: ")
hijos = int(input("Digite su numero de hijos: "))
dias_labor_mes = int(input("Digite el numero de dias laborados en el mes: "))
sueldo_base = int(input("Digite su sueldo base: "))

if edad > 55:
  print("Disfrutará de un bono de prepensión correspondiente al 5% de su sueldo básico por ser mayor de 55 años.")
if estado_civil in "casado" and hijos > 0:
  print("Se le otorgará un paseo cada diciembre por estar casado y tener hijos.")
if sueldo_base >= 1000000 and sueldo_base <= 1500000:
  print("Tendrá una comision del 2% sobre el valor del sueldo.")
elif sueldo_base >= 15000001 and sueldo_base <= 2000000:
  print("Tendrá una comision del 5% sobre el valor del sueldo.")
else:
  print("No recibe ninguna comisión sobre el valor del sueldo.")
if dias_labor_mes > 20 and sueldo_base < 1000000:
  print("Tiene derecho a un bono de alimentación por los dias laborados y el valor de su sueldo.")

"""**Clase 5: Taller ciclo for**

1. Crear un bucle que cuente todos los números pares hasta
el 100 ciclo for
2. Haz una tabla de multiplicar utilizando el ciclo for
ciclo for
3. Escribir un programa que pregunte al usuario su edad y
muestre por pantalla todos los años que ha cumplido
(desde 1 hasta su edad). ciclo for
4. Escribir un programa que pida al usuario un número entero
positivo y muestre por pantalla todos los números
impares desde 1 hasta ese número separados por comas.
5. Encuentra la suma de todos los números pares del 1 al
100 ciclo for
"""

for i in range(0,102,2):
  print(i)

print("Tabla del 3")
for i in range(0,33,3):
  print(i)

edad = int(input("Digite su edad: "))
for i in range(1,edad+1):
  print(i)

num = int(input("Digite un número entero positivo: "))
for i in range(1,num,2):
  print(i, end=", ")

suma = 0
m = int(input("numero inicial: "))
n = int(input("numero final: "))
 
for i in range(m,n+1):
  if i % 2 == 0:
    suma += i
 
print("La suma es ",suma)

"""**Ejemplos aplicacion for y while a taller 1 y taller 2**"""

name = print(input("Digite su nombre: "))
for i in "pepito perez":
 print(i)

def validarsueldo(sue):
  if sueldo >= 1000000 and sueldo <= 1500000:
    print("Tendrá una comision del 2% sobre el valor del sueldo.")
  elif sueldo >= 1500001 and sueldo <= 2000000:
    print("Tendrá una comision del 5% sobre el valor del sueldo.")
  else:
    print("No recibe ninguna comisión sobre el valor del sueldo.")

resp = "Si"
while resp == "Si" or resp == "SI" or resp == "si":
      sueldo = int(input("Digite su sueldo base: "))
      validarsueldo(sueldo)
      resp = input("¿Desea realizar otra comparación?")