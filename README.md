# Redes Neuronales
*Por: Rodrigo Esquivel Castillo*

**MAESTRÍA EN CIENCIA DE DATOS**

## Historia y contexto de las redes neuronales.

Las redes neuronales artificiales son sistemas computacionales inspirados en la estructura y funcionamiento de las redes neuronales biológicas. Estas redes están compuestas por unidades de procesamiento llamadas "neuronas artificiales" que se conectan entre sí formando capas y realizando operaciones matemáticas para procesar información.

La etimología de las redes neuronales artificiales se deriva del término "neurona", que proviene del griego "neuron", que significa "cuerda" o "nervio". En el contexto de las redes neuronales artificiales, el término "artificial" se refiere a que estas redes son creadas por el ser humano y no se encuentran de forma natural en organismos vivos.

En las redes neuronales reales, las neuronas son células especializadas que forman parte del sistema nervioso de los seres vivos. Estas células están interconectadas y transmiten señales eléctricas y químicas para procesar y transmitir información en el cuerpo.

Las redes neuronales artificiales buscan emular, de manera simplificada, el funcionamiento de las redes neuronales reales en los seres vivos. A través de la utilización de algoritmos y estructuras matemáticas, se intenta modelar la capacidad de aprendizaje y reconocimiento de patrones de las redes neuronales biológicas en un entorno computacional.

En resumen, las redes neuronales artificiales son sistemas computacionales que imitan, en cierta medida, el funcionamiento de las redes neuronales reales presentes en los seres vivos. Su nombre hace referencia a la inspiración tomada de las neuronas biológicas para crear sistemas de procesamiento de información basados en unidades de procesamiento interconectadas.

## Ejemplos de aplicaciones de redes neuronales.

1. Conducción autónoma en Tesla:
Tesla, la compañía de vehículos eléctricos, ha utilizado redes neuronales artificiales en el desarrollo de su tecnología de conducción autónoma. Estas redes se entrenan con grandes volúmenes de datos de sensores y cámaras de los vehículos para reconocer patrones y tomar decisiones en tiempo real. La red neuronal permite al sistema de conducción autónoma de Tesla interpretar el entorno, reconocer objetos y tomar decisiones de dirección, aceleración y frenado, lo que contribuye a la conducción autónoma segura y eficiente.

2. Calibración de colores en impresión offset:
En la industria de la impresión offset, las redes neuronales artificiales se han utilizado para mejorar la calibración de colores en el proceso de impresión. Estas redes pueden analizar los datos de entrada, como perfiles de color, tipos de papel y ajustes de la máquina de impresión, y aprender a generar ajustes óptimos para lograr una reproducción precisa de los colores deseados en el producto final. Esto ayuda a reducir el desperdicio de material y a obtener resultados de impresión de alta calidad de manera más eficiente.

## Esquema general de las redes neuronales.

1. Propagación hacia adelante (Forward Propagation): Se calculan las salidas de la red neuronal para un conjunto de datos de entrada, utilizando los pesos y sesgos asignados.
2. Cálculo de la función de pérdida (Loss Function): Se evalúa la diferencia entre las salidas obtenidas y las salidas esperadas, utilizando una función de pérdida apropiada para el tipo de problema.
3. Retropropagación del error (Backpropagation): Se propaga el error hacia atrás a través de la red neuronal, ajustando los pesos y sesgos mediante el cálculo de gradientes.
4. Actualización de pesos y sesgos: Se actualizan los pesos y sesgos utilizando un algoritmo de optimización, como el descenso del gradiente, con el objetivo de minimizar la función de pérdida.
5. Repetición de los pasos 1 a 4: Se repiten los pasos 1 a 4 para diferentes conjuntos de datos de entrenamiento, hasta que la red neuronal alcance una precisión aceptable o se cumpla un criterio de detención.
6. Validación y prueba: Se utilizan conjuntos de datos separados para validar y probar la red neuronal entrenada, evaluando su rendimiento y precisión.
7. Ajuste de hiperparámetros: Se pueden realizar ajustes en los hiperparámetros de la red neuronal, como la tasa de aprendizaje, el número de capas ocultas o el número de neuronas, para mejorar el rendimiento.
8. Implementación y despliegue: Una vez entrenada y probada la red neuronal, se puede implementar en una aplicación o sistema para su uso en la resolución de problemas o toma de decisiones.

Obervese el siguiente diagrama:

![Diagrama de una red neuronal](diagrama.pdf)

## El problema de escoger el metodo de impresión correcto para cada sustrato.

En mi experiencia en la industria de la impresión, la elección del tipo de papel adecuado es crucial para obtener resultados de alta calidad. Sin embargo, los clientes a menudo se enfrentan al desafío de seleccionar el sustrato correcto para sus proyectos, especialmente cuando no están familiarizados con los diferentes tipos de papel disponibles en el mercado. En este contexto, el uso de redes neuronales puede brindar una solución efectiva al problema de selección de tipos de papel. Estas redes pueden aprender a partir de datos históricos y características del proyecto para realizar recomendaciones precisas y personalizadas a los clientes.

La elección incorrecta del tipo de papel puede tener un impacto significativo en el resultado final de un proyecto de impresión. Un sustrato inadecuado puede afectar la calidad de la impresión, la legibilidad de los textos, la durabilidad del producto y la experiencia del cliente. Además, la variedad de tipos de papel disponibles en el mercado puede resultar abrumadora para los clientes que no tienen conocimientos especializados en la materia. Por lo tanto, es esencial contar con un sistema inteligente que pueda ayudar a los clientes a seleccionar el tipo de papel más apropiado para sus necesidades específicas.

El problema de selección de tipos de papel se presenta cuando un cliente necesita imprimir un proyecto, pero desconoce qué tipo de sustrato sería el más adecuado. El cliente puede tener información sobre las propiedades deseadas del papel, como el gramaje, la opacidad, la textura y la resistencia al desgarro. Sin embargo, debido a la falta de conocimiento sobre los diferentes tipos de papel disponibles en el mercado y cómo se relacionan estas propiedades con cada uno, tomar una decisión informada puede resultar complicado.

En este escenario, se propone utilizar redes neuronales para ayudar al cliente en la selección del tipo de papel. La idea es entrenar una red neuronal utilizando datos históricos de proyectos similares, junto con las propiedades del papel utilizado en cada caso. La red neuronal aprenderá los patrones y relaciones entre las características del proyecto y los tipos de papel, lo que permitirá realizar recomendaciones precisas en función de las necesidades y preferencias del cliente.



La solución propuesta proporcionará al cliente una herramienta inteligente que, al ingresar las características del proyecto, generará una recomendación de tipo de papel. Esto ahorrará tiempo y esfuerzo al cliente al eliminar la necesidad de investigar manualmente las numerosas opciones disponibles en el mercado. Además, al tener en cuenta las propiedades deseadas del papel, la red neuronal podrá brindar recomendaciones personalizadas que se ajusten a las necesidades específicas de cada proyecto.




## Desarrollo matemático del problema. 

Tenemos un conjunto de 37 sustratos almacenados en el archivo ```datos_sustratos.csv``` cada uno de ellos con la información de 7 variables como lo son 
gramaje, opacidad (bajo=1, medio=2, alto=3), desgarre, obsorcion de tinta (bajo=1, medio=2, alto=3), pH, composicion del papel, metodo que se imprime el papel (1 = Offset, 0 = flexografia). La descripción matemática que podemos dar del algorito, esto sin entrar en mucho técnisimo matemático, es la siguiente: 


1.Lectura de datos y manipulación de matrices:

* Lee los datos de un archivo CSV y los almacena en una lista llamada datos_sustratos.
* Convierte la lista de datos en un array NumPy llamado datos_sustratos, lo que implica representar los datos como una matriz multidimensional.
* Utiliza la función ```np.delete()``` para eliminar columnas específicas de la matriz, en este caso, se eliminan las columnas 0 y 6 que corresponden al nombre del papel y a la composición del papel.
* La matriz resultante se guarda en la variable sustratos_numero.

2.Separación de características y etiquetas:

* Se utiliza la indexación de matrices de ```NumPy``` para separar las columnas correspondientes a las características y las etiquetas de los sustratos.
* La matriz de características se guarda en la variable caracteristicas, mientras que las etiquetas se almacenan en la variable etiquetas.

3.Creación del modelo de red neuronal:

* Se crea una instancia del modelo secuencial ```Sequential()``` de Keras.
* Se agregan capas densamente conectadas ```Dense()``` al modelo utilizando la función de activación ReLU (activation='relu') en la capa de entrada y la función de activación sigmoide ```activation='sigmoid'``` en la capa de salida.
* Las capas densas se pueden representar como matrices de pesos y vectores de sesgos, y la función de activación realiza operaciones matemáticas en estas matrices y vectores.

4.Compilación del modelo:

* Se utiliza el método ```compile()``` para configurar el modelo con una función de pérdida de entropía cruzada binaria ```loss='binary_crossentropy'```, un optimizador de descenso de gradiente estocástico ```optimizer='adam'```, y una métrica de exactitud ```metrics=['accuracy']```.
* La función de pérdida y el optimizador están basados en cálculos matemáticos y derivadas parciales para minimizar la pérdida y ajustar los pesos del modelo.

5.Ajuste del modelo:

* Se utiliza el método ```fit()``` para entrenar el modelo con las características ```caracteristicas``` y las etiquetas ```etiquetas``` de los sustratos.
* Durante el entrenamiento, se realizan operaciones matemáticas, como multiplicación de matrices, cálculo de funciones de activación y actualización de pesos, para minimizar la pérdida y mejorar la precisión del modelo.

6.Predicción de un nuevo sustrato:

* Se solicita al usuario que ingrese los datos de un nuevo sustrato, como el gramaje, la opacidad, la resistencia al desgarre, la absorción de tinta y el pH.
* Se realiza una serie de transformaciones matemáticas para convertir las categorías de opacidad, resistencia y absorción en valores numéricos adecuados para la predicción.
* Los datos del nuevo sustrato se organizan en una matriz NumPy llamada ```nuevo_sustrato```.
* Se utiliza el método ```mpredict()``` del modelo para realizar una predicción basada en los datos del nuevo sustrato, lo que implica realizar cálculos matemáticos en las matrices de pesos y sesgos del modelo.

7.Resultado de la predicción:

* Se compara el valor de la predicción con un umbral $(0.5)$ para determinar si el sustrato es un "CANDIDATO A IMPRIMIRSE EN OFFSET" o no.
* La decisión se basa en una operación de comparación matemática ```prediccion[0][0] >= 0.5``` para determinar si el valor predicho es mayor o igual al umbral.
* Se imprime el resultado final en función de la comparación realizada.


## Resolviendo el problema en python. 

```import csv
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

#Definir los datos de entrada
#Primera componente es el nombre del papel
#Segunda componente es el gramaje
#Tercera componente es la opacidad (bajo=1, medio=2, alto=3)
#Cuarta componente es la resistencia al desgarre (bajo=1, medio=2, alto=3)
#Quinta componente es la obsorcion de tinta (bajo=1, medio=2, alto=3)
#Sexta componente es el pH
#Septima componente es la composicion del papel
#Octava es en el metodo que se imprime el papel (1 = Offset, 0 = flexografia)

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
    print("NO ES CANDIDATO A IMPRIMIRSE EN OFFSET")```
