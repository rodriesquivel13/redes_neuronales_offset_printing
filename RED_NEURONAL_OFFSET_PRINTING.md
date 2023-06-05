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

Obervese el siguiente diagrama:

![Diagrama de una red neuronal](diagrama.pdf)

## El problema de escoger el metodo de impresión correcto para cada sustrato.

En mi experiencia en la industria de la impresión, la elección del tipo de papel adecuado es crucial para obtener resultados de alta calidad. Sin embargo, los clientes a menudo se enfrentan al desafío de seleccionar el sustrato correcto para sus proyectos, especialmente cuando no están familiarizados con los diferentes tipos de papel disponibles en el mercado. En este contexto, el uso de redes neuronales puede brindar una solución efectiva al problema de selección de tipos de papel. Estas redes pueden aprender a partir de datos históricos y características del proyecto para realizar recomendaciones precisas y personalizadas a los clientes.

La elección incorrecta del tipo de papel puede tener un impacto significativo en el resultado final de un proyecto de impresión. Un sustrato inadecuado puede afectar la calidad de la impresión, la legibilidad de los textos, la durabilidad del producto y la experiencia del cliente. Además, la variedad de tipos de papel disponibles en el mercado puede resultar abrumadora para los clientes que no tienen conocimientos especializados en la materia. Por lo tanto, es esencial contar con un sistema inteligente que pueda ayudar a los clientes a seleccionar el tipo de papel más apropiado para sus necesidades específicas.

El problema de selección de tipos de papel se presenta cuando un cliente necesita imprimir un proyecto, pero desconoce qué tipo de sustrato sería el más adecuado. El cliente puede tener información sobre las propiedades deseadas del papel, como el gramaje, la opacidad, la textura y la resistencia al desgarro. Sin embargo, debido a la falta de conocimiento sobre los diferentes tipos de papel disponibles en el mercado y cómo se relacionan estas propiedades con cada uno, tomar una decisión informada puede resultar complicado.

En este escenario, se propone utilizar redes neuronales para ayudar al cliente en la selección del tipo de papel. La idea es entrenar una red neuronal utilizando datos históricos de proyectos similares, junto con las propiedades del papel utilizado en cada caso. La red neuronal aprenderá los patrones y relaciones entre las características del proyecto y los tipos de papel, lo que permitirá realizar recomendaciones precisas en función de las necesidades y preferencias del cliente.

La solución propuesta proporcionará al cliente una herramienta inteligente que, al ingresar las características del proyecto, generará una recomendación de tipo de papel. Esto ahorrará tiempo y esfuerzo al cliente al eliminar la necesidad de investigar manualmente las numerosas opciones disponibles en el mercado. Además, al tener en cuenta las propiedades deseadas del papel, la red neuronal podrá brindar recomendaciones personalizadas que se ajusten a las necesidades específicas de cada proyecto.

En resumen, la utilización de redes neuronales en el problema de selección de tipos de papel ofrece la posibilidad de mejorar la toma de decisiones de los clientes, proporcionando recomendaciones precisas y personalizadas. Este enfoque inteligente no solo simplificará el proceso de selección, sino que también garantizará la calidad y satisfacción en los proyectos de impresión.

