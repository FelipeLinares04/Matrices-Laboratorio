import numpy as np
import random
import funciones

aleatorio = np.random.randint(18, 34, size=(5, 7))
mes = funciones.ultimos(aleatorio)
print(mes)


def dias(aleatorio):
    diccionario = {0:"lunes",1:"martes",2:"miercoles",3:"jueves",4:"viernes",5:"sabado",6:"domingo"}
    dia = diccionario[aleatorio]
    return dia

def mayor_semana(aleatorio):
    for i in range(5): 
        mayor_de_la_semana = max(aleatorio[i])
        for j in range(7):
            if mayor_de_la_semana == aleatorio[i][j]:
                dia=dias(j)
        

        print(f"la mayor temperatura en la semana {i+1}  es: {mayor_de_la_semana} el {dia}")


def menor_semana(aleatorio):
    for i in range(5): 
        menor_de_la_semana = min(aleatorio[i])
        for j in range(7,3):
            if menor_de_la_semana == aleatorio[i][j]:
                dia=dias(j)
        

        print(f"la menor temperatura en la semana {i+1}  es: {menor_de_la_semana} el {dia}")
        



def sumalista(listaNumeros):
   if len(listaNumeros) == 1:
        return listaNumeros[0]
   else:
        return listaNumeros[0] + sumalista(listaNumeros[1:])


print(mayor_semana(mes))
print(menor_semana(mes))


semana1 = mes[0,0:7]
suma1 = sumalista(semana1)
print(f"Promedio semana 1{suma1/7}")

semana2 = mes[1,0:7]
suma2 = sumalista(semana2)
print(f"Promedio semana 2{suma2/7}")

semana3 = mes[2,0:7]
suma3 = sumalista(semana3)
print(f"Promedio semana 3{suma3/7}")

semana4 = mes[3,0:7]
suma4 = sumalista(semana4)
print(f"Promedio semana 4{suma4/7}")

semana5 = mes[4,0:-4]
suma5 = sumalista(semana5)
print(f"Promedio semana 5{suma5/3}")