# -*- coding: utf-8 -*-
"""proyecto redes neuronales impresion terminado.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FUD2D7pw7AqJaV3AzcGfA_Cu3hLqkHei
"""

import csv
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Leer los datos del archivo CSV
datos_sustratos = []
with open('datos_sustratos.csv', 'r', encoding='latin-1') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for linea in lector_csv:
        datos_sustratos.append(linea)

# Convertir los datos en un array NumPy
datos_sustratos = np.array(datos_sustratos[1:], dtype=np.object)

# Convertir los datos a números de punto flotante
sustratos_numero = np.array(np.delete(datos_sustratos, [0, 6], axis=1), dtype=np.float32)

# Separar las características y las etiquetas
etiquetas = sustratos_numero[:, -1]  # Última columna
caracteristicas = sustratos_numero[:, :-1]  # Todas las columnas excepto la última

# Crear el modelo
model = Sequential()
model.add(Dense(10, input_dim=5, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compilar el modelo
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Ajustar el modelo
model.fit(caracteristicas, etiquetas, epochs=50, batch_size=1)

# Datos de un nuevo sustrato para predecir
gramaje = input("Ingrese el gramaje del sustrato: ")
opacidad = input("Ingrese grado de opacidad (baja, media o alta): ")
resistencia = input("Ingrese grado de resistencia al desgarre (baja, media o alta): ")
absorcion = input("Ingrese grado de absorción de tinta (baja, media o alta): ")
pH = input("Ingrese el pH del papel: ")
impresion = 0

if opacidad == "baja":
    opacidad = 1
elif opacidad == "media":
    opacidad = 2
elif opacidad == "alta":
    opacidad = 3
else:
    opacidad = 0

if resistencia == "baja":
    resistencia = 1
elif resistencia == "media":
    resistencia = 2
elif resistencia == "alta":
    resistencia = 3
else:
    resistencia = 0

if absorcion == "baja":
    absorcion = 1
elif absorcion == "media":
    absorcion = 2
elif absorcion == "alta":
    absorcion = 3
else:
    absorcion = 0

# Datos de un nuevo sustrato para predecir
nuevo_sustrato = np.array([[float(gramaje), float(opacidad), float(resistencia), float(absorcion), float(pH)]], dtype=np.float32)
prediccion = model.predict(nuevo_sustrato)

if prediccion[0][0] >= 0.5:
    print("CANDIDATO A IMPRIMIRSE EN OFFSET")
else:
    print("NO ES CANDIDATO A IMPRIMIRSE EN OFFSET")
