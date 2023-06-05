# Redes Neuronales
*Por: Rodrigo Esquivel Castillo*
**MAESTRÍA EN CIENCIA DE DATOS**

## Historia y contexto de las redes neuronales

Las redes neuronales artificiales son sistemas computacionales inspirados en la estructura y funcionamiento de las redes neuronales biológicas. Estas redes están compuestas por unidades de procesamiento llamadas "neuronas artificiales" que se conectan entre sí formando capas y realizando operaciones matemáticas para procesar información.

La etimología de las redes neuronales artificiales se deriva del término "neurona", que proviene del griego "neuron", que significa "cuerda" o "nervio". En el contexto de las redes neuronales artificiales, el término "artificial" se refiere a que estas redes son creadas por el ser humano y no se encuentran de forma natural en organismos vivos.

En las redes neuronales reales, las neuronas son células especializadas que forman parte del sistema nervioso de los seres vivos. Estas células están interconectadas y transmiten señales eléctricas y químicas para procesar y transmitir información en el cuerpo.

Las redes neuronales artificiales buscan emular, de manera simplificada, el funcionamiento de las redes neuronales reales en los seres vivos. A través de la utilización de algoritmos y estructuras matemáticas, se intenta modelar la capacidad de aprendizaje y reconocimiento de patrones de las redes neuronales biológicas en un entorno computacional.

En resumen, las redes neuronales artificiales son sistemas computacionales que imitan, en cierta medida, el funcionamiento de las redes neuronales reales presentes en los seres vivos. Su nombre hace referencia a la inspiración tomada de las neuronas biológicas para crear sistemas de procesamiento de información basados en unidades de procesamiento interconectadas.

## Ejemplos de aplicaciones de redes neuronales

1. Conducción autónoma en Tesla:
Tesla, la compañía de vehículos eléctricos, ha utilizado redes neuronales artificiales en el desarrollo de su tecnología de conducción autónoma. Estas redes se entrenan con grandes volúmenes de datos de sensores y cámaras de los vehículos para reconocer patrones y tomar decisiones en tiempo real. La red neuronal permite al sistema de conducción autónoma de Tesla interpretar el entorno, reconocer objetos y tomar decisiones de dirección, aceleración y frenado, lo que contribuye a la conducción autónoma segura y eficiente.

2. Calibración de colores en impresión offset:
En la industria de la impresión offset, las redes neuronales artificiales se han utilizado para mejorar la calibración de colores en el proceso de impresión. Estas redes pueden analizar los datos de entrada, como perfiles de color, tipos de papel y ajustes de la máquina de impresión, y aprender a generar ajustes óptimos para lograr una reproducción precisa de los colores deseados en el producto final. Esto ayuda a reducir el desperdicio de material y a obtener resultados de impresión de alta calidad de manera más eficiente.

## Esquema general de las redes neuronales

1. Propagación hacia adelante (Forward Propagation): Se calculan las salidas de la red neuronal para un conjunto de datos de entrada, utilizando los pesos y sesgos asignados.
2. Cálculo de la función de pérdida (Loss Function): Se evalúa la diferencia entre las salidas obtenidas y las salidas esperadas, utilizando una función de pérdida apropiada para el tipo de problema.
3. Retropropagación del error (Backpropagation): Se propaga el error hacia atrás a través de la red neuronal, ajustando los pesos y sesgos mediante el cálculo de gradientes.
4. Actualización de pesos y sesgos: Se actualizan los pesos y sesgos utilizando un algoritmo de optimización, como el descenso del gradiente, con el objetivo de minimizar la función de pérdida.
5. Repetición de los pasos 1 a 4: Se repiten los pasos 1 a 4 para diferentes conjuntos de datos de entrenamiento, hasta que la red neuronal alcance una precisión aceptable o se cumpla un criterio de detención.
6. Validación y prueba: Se utilizan conjuntos de datos separados para validar y probar la red neuronal entrenada, evaluando su rendimiento y precisión.
7. Ajuste de hiperparámetros: Se pueden realizar ajustes en los hiperparámetros de la red neuronal, como la tasa de aprendizaje, el número de capas ocultas o el número de neuronas, para mejorar el rendimiento.
8. Implementación y despliegue: Una vez entrenada y probada la red neuronal, se puede implementar en una aplicación o sistema para su uso en la resolución de problemas o toma de decisiones.

![Diagrama de una red neuronal](diagrama.pdf)
