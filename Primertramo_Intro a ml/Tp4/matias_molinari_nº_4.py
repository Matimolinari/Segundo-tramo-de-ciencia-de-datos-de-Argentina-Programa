# -*- coding: utf-8 -*-
"""Matias_Molinari Nº 4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E-swyEQu-k6CLUt3VrGKlQ-ykk2JhJyq

**Trabajo Practico Nº 4**
Analisis sobre data set

1= Buscar los siguiente data set en la web
* Titanic
* Iris
* Wine
* Indian Diabetes

2- Explicar de cada data set , sus diferente Variables

3- Deside justificando tu respuesta que tipo de categoria de variable son

4- Detectar y arreglar los siguientes coceptos

* Valores Ausente
* Valores Atipicos

5- De los difentes data set , se puede eliminar alguna columna

6- Realizar analisis univariados

* Grafico de frecuencia
* Grafico de torta
* Histograma
* etc

7- En base a los graficos del punto 6 realizar distintas concluciones

8- Realizar analisis de corelacion y explicar que variable estan correlacionadas

9-Realizar un analisis de grafico de cherrnoff y detectar outlires

PD Pueden Buscar data set de kaggle

Voy a dejar separado los data sets elegidos que son:

Titanic y Wine
"""

#librerias que usaremos en ambos data set sets.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import seaborn as sns



"""# Titanic

https://www.kaggle.com/c/titanic/overview

usaremos el archivo train.csv
"""

Titanic = pd.read_csv('/content/train.csv')

Titanic

"""2. Variables y explicacion
3. Deside justificando tu respuesta que tipo de categoria de variable son

"""

print(Titanic.dtypes)

print(Titanic.describe())

"""Si tenemos que describir cada una de las variables seria:


1. **PassengerId**: Identificador único para cada pasajero en el Titanic. Es de tipo entero (int64).

2. **Survived**: Indica si el pasajero  sobrevivió (1) o no (0) al hundimiento del Titanic. Es de tipo entero (int64).

3. **Pclass**: Clase en la que viajó el pasajero en el Titanic (1ra, 2da o 3ra). Es de tipo entero (int64).

4. **Name**: Nombre del pasajero. Es de tipo objeto (object), lo que generalmente indica una cadena de texto.

5. **Sex**: Género del pasajero (masculino o femenino). Es de tipo objeto (object).

6. **Age**: Edad del pasajero. Es de tipo flotante (float64).

7. **SibSp**: Número de hermanos/cónyuges a bordo del Titanic. Es de tipo entero (int64).

8. **Parch**: Número de padres/hijos a bordo del Titanic. Es de tipo entero (int64).

9. **Ticket**: Número del ticket de embarque. Es de tipo objeto (object).

10. **Fare**: Tarifa que el pasajero pagó por el viaje. Es de tipo flotante (float64).

11. **Cabin**: Número de cabina en la que el pasajero se alojó. Es de tipo objeto (object).

12. **Embarked**: Puerto de embarque del pasajero (C = Cherbourg, Q = Queenstown, S = Southampton). Es de tipo objeto (object).

En resumen tenemos entonces un total de 12 variables donde las podemos dividir en:



1.   Variables numericas:PassengerId, Survived, Pclass, Age, SibSp, Parch, Fare
2.   Variables categoricas:Name, Sex, Ticket, Cabin, Embarked

4. Detectar y arreglar los siguientes coceptos

* Valores Ausente
* Valores Atipicos
"""

valores_ausentes = Titanic.isna().sum()
print(valores_ausentes)

#Vamos a corroborar si tiene datos nulos
Titanic_limpio = Titanic.dropna(inplace=True)
print(Titanic_limpio)

"""5. No vamos a eliminar ninguna columna

6. Realizar analisis univariados

* Grafico de frecuencia
* Grafico de torta
* Histograma
* etc

Vamos a usar la variable "Pclass" para los graficos
"""

#Grafico de histograma
plt.figure(figsize=(6, 4))
plt.hist(Titanic['Pclass'], bins=3, edgecolor='black', alpha=0.7)
plt.title('Histograma de Clase de Pasajero')
plt.xlabel('Clase de Pasajero')
plt.ylabel('Frecuencia')
plt.show()

#Gráfico de Frecuencia
plt.figure(figsize=(6, 4))
Titanic['Pclass'].value_counts().sort_index().plot(kind='bar')
plt.title('Gráfico de Frecuencia de Clase de Pasajero')
plt.xlabel('Clase de Pasajero')
plt.ylabel('Frecuencia')
plt.show()

#Gráfico de Torta
plt.figure(figsize=(6, 6))
Titanic['Pclass'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'lightgreen', 'lightcoral'])
plt.title('Gráfico de Torta de Clase de Pasajero')
plt.legend(labels=['1ra Clase', '2da Clase', '3ra Clase'])
plt.show()

"""7. En base a los graficos del punto 6 realizar distintas concluciones

Bueno como hicimos el analisis de la misma variable en los 3 graficos podemos observar que lo que hicimos fue plasmar las 3 clases de pasajeros en el barco.
Podemos ver que los primeros dos graficos plasman con un grafico de barras donde en el histograma tenemos mas detallado las clases de pasajero en el de frecuencia es mas directo la muestro de cuantos pasajeros estan en cada clase en base a su frecuencia.

En el de pizza al ser 3 clases es mucho mas facil comprender gracias al % la cantidad de personas distribuidas en ellas.
No podemos decir cual clase era mejor dado que la variable no lo indica.

8- Realizar analisis de corelacion y explicar que variable estan correlacionadas

Vamos a analizar otras variables para esto
"""

analisis_de_correlacion= ['Age','Fare','SibSp']

#Vamos a hacer una matriz de correlacion
matriz = Titanic[analisis_de_correlacion].corr()

#Visulizacion

plt.figure(figsize=(8, 6))
sns.heatmap(matriz, annot=True, cmap='coolwarm')
plt.title('Mapa de Calor de Correlación')
plt.show()

"""La explicacion de un mapa de calor es lo siguiente: los valores van desde -1 hasta 1.
Un valor positivo cerca de 1 indica una correlación positiva fuerte, mientras que un valor negativo cerca de -1 indica una correlación negativa fuerte. Un valor cercano a 0 indica una correlación débil o nula.

Si la casilla correspondiente a la intersección de dos variables está más oscura, eso sugiere una correlación más fuerte (positiva o negativa) entre esas variables. Si está más clara, la correlación es más débil.

# Wine

https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009

usaremos el archivo winequality-red.csv
"""

vinito = pd.read_csv('/content/winequality-red.csv')

vinito

"""2- Explicar de cada data set , sus diferente Variables

3- Deside justificando tu respuesta que tipo de categoria de variable son


"""

print(vinito.dtypes)

print(vinito.describe())

"""1. fixed acidity: Esta variable representa la cantidad de ácido fijo en el vino.

2. volatile acidity: Esta variable se refiere a la cantidad de ácido volátil en el vino.

3. citric acid: Representa la cantidad de ácido cítrico en el vino.

4. residual sugar: Esta variable indica la cantidad de azúcar residual en el vino.

5. chlorides: Representa la cantidad de cloruros en el vino.

6. free sulfur dioxide: Indica la cantidad de dióxido de azufre libre en el vino.

7. total sulfur dioxide: Representa la cantidad total de dióxido de azufre en el vino.

8. density: Indica la densidad del vino.

9. pH: Representa el pH del vino.

10. sulphates: Indica la cantidad de sulfatos en el vino.

11. alcohol: Representa el contenido de alcohol en el vino.

12. quality: Esta variable representa la calidad del vino, siendo un valor entero que varía de 0 a 10. Aunque se almacena como un entero, podría considerarse una variable ordinal, ya que tiene un orden específico pero las diferencias entre las categorías pueden no ser iguales.

Por lo tanto tenemos 11 variables numericas y 1 donde representa la calidad del vino entre unos unicos valores en un rango especifico de 0 a 10

4- Detectar y arreglar los siguientes coceptos

* Valores Ausente
* Valores Atipicos

5- De los difentes data set , se puede eliminar alguna columna
"""

datos_ausentes = vinito.isnull().sum()

print(datos_ausentes)

"""No contiene datos nulos/ ausentes

6- Realizar analisis univariados

* Grafico de frecuencia
* Grafico de torta
* Histograma
* etc

7- En base a los graficos del punto 6 realizar distintas concluciones
"""

plt.figure(figsize=(6, 6))
Titanic['Pclass'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'lightgreen', 'lightcoral'])
plt.title('Gráfico de Torta de Clase de Pasajero')
plt.legend(labels=['1ra Clase', '2da Clase', '3ra Clase'])
plt.show()

#Grafico  de torta.

plt.figure(figsize=(6, 6))
vinito['quality'].value_counts().plot(kind='pie', autopct='%1.1f%%')
labels = vinito['quality'].value_counts().index
plt.title('Gráfico de Torta de Calidad del Vino')
plt.legend(labels, loc='best')
plt.show()

# Histograma para la variable 'volatile acidity'
plt.figure(figsize=(8, 6))
plt.hist(vinito['volatile acidity'], bins=20, edgecolor='black', alpha=0.7)
plt.title('Histograma de Acidez Volátil')
plt.xlabel('Acidez Volátil')
plt.ylabel('Frecuencia')
plt.show()

# Gráfico de Frecuencia para la variable 'fixed acidity'
plt.figure(figsize=(8, 6))
sns.countplot(x='fixed acidity', data=vinito)
plt.title('Gráfico de Frecuencia de Acidez Fija')
plt.xlabel('Acidez Fija')
plt.ylabel('Frecuencia')
plt.xticks(ticks=range(0, int(vinito['fixed acidity'].max()) + 80 ,2), rotation=90)
plt.show()

"""1.   Grafico de pizza: si bien no queda del todo lindo podemos ver la clasificacion de los mejores vinos estan entre el rango de 5 y 6
2.   Grafico de histograma: Muestra la distrubucion de acido volatil en el vino donde llega a un pico en un valor de 0.7

3. Grafico de frecuencia: Muestra la acidez fija, por ejemplo en el 7.1 tenemos una frecuencia de casi 70 esto quiere decir que tenemos esa cantidad de obversaciones en base al valor del eje X

8- Realizar analisis de corelacion y explicar que variable estan correlacionadas
"""

#vamos a meter todas las variables
matriz2 = vinito.corr()


# Generar un mapa de calor de la matriz de correlación
plt.figure(figsize=(10, 8))
sns.heatmap(data=matriz2, annot=True, cmap='coolwarm')
plt.title('Mapa de Calor de Correlación')
plt.show()

"""si observamos, hay una  correlación alta y positiva entre dos variables (por ejemplo, 'alcohol' y 'quality'), esto podría significar que a medida que el contenido de alcohol aumenta, la calidad del vino tiende a aumentar también.

9-Realizar un analisis de grafico de cherrnoff y detectar outlires
"""



"""# Punto 9


Para ambos casos sucede lo mismo.
El analisis grafico de cherrnoff es una técnica de visualización que se utiliza para representar múltiples variables en forma de caras humanas. Cada variable se mapea en diferentes atributos faciales, como tamaño de los ojos, forma de la boca, longitud de la nariz, etc.

En el siguiente link pude encontrar un ejemplo.

http://reyesestadistica.blogspot.com/2018/04/analisis-grafico-de-datos-multivariados.html

Es  un metodo donde se usan demasiadas variables y en los dataframe elegidos para este trabajo no las tiene aparte es una forma compleja de llevarlo  a cabo y por ultimo es dificil de interpretar

Una alternativa para identifcar outliers podria usarse el diagrama de caja (boxplot) .
"""