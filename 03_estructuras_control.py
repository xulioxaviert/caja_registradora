#. estructuras de control
if True:
    print("Esto es verdadero")
else:
    print("Esto es falso")
    
num = 10
if num < 5:
    print("El número es menor que 5")
elif num == 10:
    print("El número es igual a 10")
else:
    print("El número es menor o igual que 5")

for i in range(5):
    print("Iteración:", i)

while False:
    print("Esto nunca se imprimirá")

# ejemplo de instances de control
x = 10
if x > 0:
    print("x es positivo")
elif x < 0:
    print("x es negativo")
if isinstance(x, int):
    print("x es un entero")
# ejemplo de operadores lógicos
if x > 0 and x < 20:
    print("x está entre 0 y 20")    
elif x < 0 or x > 20:
    print("x está fuera del rango de 0 a 20")
    
    
a = True    
b = False
if a and b:
    print("Ambos son verdaderos")
elif a or b:    
    print("Al menos uno es verdadero")
else:
    print("Ambos son falsos")
    
    
# ejemplos de bucles for y while
for i in range(1, 6):
    print("Número:", i)
for letter in "Python":
    print("Letra:", letter) 
    
x= {"nombre": "Xulio", "edad": 30, "ciudad": "Madrid"}
for key, value in x.items():
    print(f"{key}: {value}")    
        
#ejemplos de bucles for

