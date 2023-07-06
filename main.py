"""
Existen muchos tipos de felinos, los cuales se caracterizan por tener un comportamiento muy similar, más allá de las diferencias que puedan tener en cuanto a tamaño o hábitat. Con esto en mente se propone modelar la clase Felino, la cual tiene como característica su energía y si requiere dormir o no. Además debe entender los mensajes: comer, que aumenta su energía en 0.1 puntos por cada gramo que ingiere, jugar(minutos) que disminuye su energía 10 puntos por cada media hora de juego y saber_hora(horario), el cual, si la hora está entre las 11 y las 19, el felino duerme.

Los chitas, si bien tienen un comportamiento similar, también hacen cosas particulares. Por ejemplo, pueden correr muy rápido, lo que gasta muy rápido su energía (30 puntos cada 100 metros), sin embargo al comer recuperan el doble de energía que los felinos normales.

Definí las clases Felino y Chita, hacé que esta última herede de la primera, agregando y/o redefiniendo los métodos necesarios.
"""

class Felino:
    def __init__(self, energia):
        self.energia = energia
        self.domir = None
        
    def get_energia(self):
        return self.energia
    
    def comer(self, gramos):
        self.energia += (0.1*gramos)
    
    def jugar(self, minutos):
        self.energia -= ((1/3) * minutos)

    def saber_hora(self, horario):
        if horario in range(11,20):
            self.domir = True
            print("El felino esta dormido")    
        elif horario in range(0,11):
            self.domir = False
            print("El felino esta despierto")
        elif horario in range(21,23):
            self.domir = False
            print("El felino esta despierto")
        else: 
            print("inserte un valor valido de horas en formato HH")


class Chita(Felino):
# Asumo que le van a pasar solo números a mi método.
    def correr(self, metros):
        self.energia -= ((3/10)* metros)
    
    def comer(self, gramos):
        self.energia += (2*(0.1*gramos))

baghera = Chita(0)
baghera.comer(1000)
print(baghera.get_energia())
baghera.correr(100)
print(baghera.get_energia())
baghera.jugar(3)
print(baghera.get_energia())
baghera.saber_hora(0)
baghera.saber_hora(13)
baghera.saber_hora(22)