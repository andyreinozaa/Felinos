#Felino y Chita 🐆
Este código define clases para modelar el comportamiento de los felinos e incluye funcionalidades para un felino genérico (Felino) y un tipo específico de felino llamado Chita (Guepardo). Aquí tienes una breve descripción del código:

##Felino
La clase Felino representa diferentes tipos de felinos. Tiene atributos para la energía y la necesidad de dormir (dormir). La clase incluye los siguientes métodos:

get_energia: Devuelve el nivel de energía actual.
comer: Aumenta el nivel de energía en 0.1 puntos por cada gramo de comida consumida.
jugar: Disminuye el nivel de energía en 10 puntos por cada media hora de juego.
saber_hora: Determina si el felino está durmiendo según la hora proporcionada.

## Chita
La clase Chita es una subclase de Felino, que representa el comportamiento del guepardo. Hereda los atributos y métodos de Felino y agrega el siguiente método:

correr: Disminuye el nivel de energía en 30 puntos por cada 100 metros recorridos.
comer: Aumenta el nivel de energía el doble en comparación con los felinos normales por cada cantidad de comida consumida.

El código también incluye un ejemplo de creación de una instancia de Chita llamada baghera y demuestra el uso de los métodos definidos.
