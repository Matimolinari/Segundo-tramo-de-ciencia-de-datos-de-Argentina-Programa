![image](https://github.com/Matimolinari/Segundo-tramo-de-ciencia-de-datos-de-Argentina-Programa/assets/102113644/777587d3-47d4-483e-a678-6918edcda2a3)



# Argentina Programa 4.0

# Julio de 2023 - Octubre de 2023.

# Segundo tramo de Ciencia de datos dictado por la Universidad Nacional de Salta(UNSA).

## En las carpetas encontraremos ambos tramos donde la primer parte sobre Machine Learning  utilizamos el lenguaje python para llevar a cabo dichas actividades, estas actividades consistian de lo siguiente:

## En el primer tp sobre bases de datos vistas en clases:
Trabajo Practico Nº 4**
Analisis sobre data set

-Explicar de cada data set , sus diferente Variables

- Deside justificando tu respuesta que tipo de categoria de variable son

- Detectar y arreglar los siguientes coceptos

* Valores Ausente
* Valores Atipicos

- De los difentes data set , se puede eliminar alguna columna

- Realizar analisis univariados

* Grafico de frecuencia
* Grafico de torta
* Histograma
* etc

* En base a los graficos del punto 6 realizar distintas concluciones

* Realizar analisis de corelacion y explicar que variable estan correlacionadas

* Realizar de ser  posible un analisis de grafico de cherrnoff y detectar outlires.


## Luego para finalizar el primer tramo tuvimos que elegir otro data set fuera de los vistos en clases y seguir las siguientes consignas:

* Realizar una introduccion al dataset de que se trata,definir sus variables (Diccionario de datos)

* Identificar el tipo de variable,decide justificando su respuesta.

* Detectar Valores Ausente y Valores Atipicos .Decidir si eliminarlos y el por que de la eleccion

* Realizar un analisis univariado y en base a esos graficos,sacar conclusiones

* Realizar analisis de matriz corelacion y explicar que variable estan correlacionadas\

* Sobre el Dataset Elegido  explique si se puede reducir las dimensiones  y que representa esas  nuevas variables

## Luego de tener aprobados los trabajos practicos pasamos  a la segunda etapa que fue usar las librerias de python "PANDAS Y NUMPY". Este trayecto tambien constaba de dos trabajos uno integrador y otro sobre redes neuronales.
El primero nos dieron opciones de data set para elegir y a partir de eso tuvimos que seguir los siguientes pasos:

* Ingresar el data set

* Aplicar el proceso de EDA

* Aplicar el proceso de limpieza

* Aplicar el proceso para definir las variables de esta manera poder aplicar regresion lineal y logistica.

* Aplicar metricas de evaluacion sobre los modelos.

* Sacar una conclusion en funcion de nuestros resultados.

## Y por ultimo el tp de redes Neuronales fue realizar un análisis y construcción de una nueva base de datos utilizando datos climáticos y de simulación aleatoria. A continuación se detallan los pasos:

Reconstrucción de la Base de Datos Climática:

Seleccionar una ciudad.
* Calcular la temperatura promedio entre la temperatura máxima y mínima de cada día.
* Graficar los datos de tiempo vs. temperatura.
* Seleccionar un período donde la gráfica sea creciente.
* Simulación Aleatoria para Generar Variables Adicionales:

* Agregar a la nueva base de datos una columna con variables generadas mediante simulación aleatoria.
* Incluir la variable "Precio del Kilo de Helado" utilizando regresión lineal en función de la temperatura.
* Introducir la variable categórica "Compra Helado" con probabilidad del 80% de decidir no comprar si el precio supera el 40% del precio inicial.

Diseño de Perceptrones:

* Generar tres perceptrones conectados entre sí.
* Establecer condiciones basadas en la temperatura y el precio del helado para decidir la compra.
* Asignar pesos de manera aleatoria.
* Utilizar funciones de activación como la función de salto finito o la función sigmoide.

Implementación y Evaluación de los Perceptrones:

* Implementar los perceptrones sobre la base de datos generada.
* Utilizar como entrada las variables de temperatura y precio del helado.
* Comparar las respuestas de la red neuronal con la variable categórica "Compra Helado".
* Medir la proporción de respuestas correctas para evaluar la exactitud de la red.
