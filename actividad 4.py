#importamos la librería que vamos a usar
import numpy as np


#lista de edades
edades = [23, 45, 12, 67, 34, 89, 22, 10]
print("Lista de edades:", edades) #mostramos la lista de edades


#calcular la media
media_edades = np.mean(edades)
print("Media de edades:", media_edades) #mostramos la media de edades


#calculamos la desviación estándar
desviacion_estandar_edades = np.std(edades)
print("Desviación estándar de edades:", desviacion_estandar_edades) #mostramos la desviación estándar de edades



