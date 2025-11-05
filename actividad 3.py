import numpy as np


#lista de edades
edades = [23, 45, 12, 67, 34, 89, 22, 10]
print("Lista de edades:", edades)


#calcular la media
media_edades = np.mean(edades)
print("Media de edades:", media_edades)


#calcular la mediana
mediana_edades = np.median(edades)
print("Mediana de edades:", mediana_edades)


#calcular la varianza
varianza_edades = np.var(edades)
print("Varianza de edades:", varianza_edades)

#calcular la desviación estándar
desviacion_estandar_edades = np.std(edades)
print("Desviación estándar de edades:", desviacion_estandar_edades)
