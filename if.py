#Necesito que dada una edad, decida el programa si soy mayor o menor de edad.
#Mayor de edad es 18 o +
#Si es mayor de 70 avisarle que es jubilado
edad = 105
if edad >= 18:
    print("usted es mayor de edad")
    if edad>100:
            print('Bienvenida Mirtha Legrand')
            edad = 2
    if edad>70:
        print("usted es jubilado")
        
else:
    print("usted es menor de edad")