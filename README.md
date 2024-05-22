# Título del Proyecto:
Ciencia de datos aplicada al análisis de señales electrorretinográficas derivadas del estudio de un modelo de degeneración retinal.

## Descripción:

Como mi Proyecto Integrador de la carrera de grado Ingeniería Biomédica se propuso llevar a cabo el procesamiento, análisis, clasificación y agrupamiento de señales electrorretinográficas derivadas del estudio de un modelo de degeneración retinal por exposición a luz LED de baja intensidad. Cabe destacar que hasta el momento el análisis de dichas señales suele ser acotado, limitándose a definir la morfología de la señal en el dominio del tiempo. Por lo tanto, el fin es aprovechar las herramientas que brinda el procesamiento de señales y aprendizaje automático para lograr un análisis exhaustivo del modelo de degeneración retinal. 
Programando en Lenguaje Python y aplicando aprendizaje no supervisado a la base de datos de señales de ERG se pretende investigar si es posible hallar algún punto de inflexión a partir del cual el mecanismo de degeneración retinal desencadenado es irreversible.

## Pasos del análisis proyecto

![DIAGRAMA DE FLUJO RESULTADOS](https://github.com/mlzulatto/PI-ERG/assets/138075122/3c22ad0e-27f9-4be7-b738-a03cbf790d41)


### Orden de los archivos

-Archivo de funciones (Python): En este archivo py. se encontraran las funciones basicas utilizadas durante el proyecto. 
**Utils.py**

-Escaneo: En este archivo se realiza el Escaneo de carpetas donde encontramos las señales en formato txt., extracción de características, filtrado, visualización de señales crudas y procesadas.

**Escaneo,Extracción de Características y filtrado .ipynb**

-Análisis de datos estadísticos.


-Etiquetado, correlación y escalado.

**CorrelacionEscalado_SeisEtiqeutas.ipynb**

**CorrelacionEscalado_TresEtiquetas_23-04.ipynb**

-Modelos de aprendizaje con 6 etiquetas: Archivo con analisis de aprendizaje no supervisado con los grupo iniciales que posterior a la limpieza de datos fueron 6.

**DataFrame_ForClassifier_SeisEtiquetas.ipynb**

**modelos vs. datasets- SEIS ETIQUETAS.ipynb**

-Modelos de aprendizaje con 3 etiquetas: Archivo con analisis de aprendizaje no supervisado con los grupo recomendados para optimización del modelo.

**DataFrame_ForClassifier_TresEtiquetas_23-04.ipynb**

**modelos vs. datasets- TRES ETIQUETAS.ipynb**

-Visualización de gráficos de barra.

**graficos de barra No Supervisados.ipynb**

## Resultados

![Copia de DIAGRAMA DE FLUJO RESULTADOS 2](https://github.com/mlzulatto/PI-ERG/assets/138075122/2f03be53-628e-4196-84e8-8fa0e35f4869)


Se realiza un resumen acompañado de un diagrama de flujo ilustrado en la figura 53, definido como una representación gráfica de un algoritmo o
proceso, que permite visualizar los resultados obtenidos al final de cada etapa del proyecto, los
cuales fueron enumerados en la figura para poder definirlos detalladamente a continuación.

➔ RESULTADO (1): El primer resultado obtenido está asociado al acondicionamiento y
procesamiento de las señales. El filtro aplicado permitió eliminar el ruido que suele
acompañar a las señales de origen biológico, logrando un suavizado a lo largo de toda la
señal. A su vez, el filtrado contribuyó a suprimir la componente continua de las señales,
y es por esto que se observa un corrimiento considerable de la señal respecto al eje de
ordenadas.

➔ RESULTADO (2): La extracción de características pre y post filtrado permitió obtener
resultados que aportaron a distintos objetivos. En primer lugar, la extracción de
características de la onda “a” y onda “b” (amplitud, latencia, ancho) , que se obtuvieron
previo al filtrado permitieron determinar las frecuencias de corte del filtro a partir del
análisis de los anchos en cada onda. En segundo lugar, la extracción de características
post filtrado generó dos tipos de parámetros bien diferenciados. Por un lado, las
características de cada onda mencionadas anteriormente, sumado a una nueva
característica denominada pendiente entre la onda “a” y onda “b”. Y, por otro lado, se
obtuvieron parámetros estadísticos obtenidos de las señales (mínimo, máximo, media,
desvío estándar y energía). Estos dos grupos de características, se sometieron a
procesos de Etiquetado, escalado y correlación y permitieron adaptar y generar dos
DataFrame muy útiles para el posterior entrenamiento de los modelos de Aprendizaje
Automático.

➔ RESULTADO (3): una vez etiquetadas las señales según la cantidad de días de exposición
a luz, se entrenó el modelo con métodos de Aprendizaje Supervisado. Los distintos
métodos implementados fueron evaluados a través de una comparación de la métrica
F1-Score obtenida para cada uno, acompañado de un análisis de sus matrices de
confusión. En el mismo se identificó que el método Random Forest tiene el mejor
desempeño frente al entrenamiento. Sin embargo, los resultados no fueron los
esperados, esto se debía a la poca cantidad de señales con las que se trabajó, y al
desbalance en la cantidad de señales en las distintas etiquetas.

➔ RESULTADO (4) y (6): debido a los resultados del punto anterior y la posibilidad de
mejorarlos, se decidió someter las señales a un modelo de Aprendizaje No Supervisado.
Para esto, se trabajaron las señales sin etiquetas, a diferencia del entrenamiento
Supervisado mencionado anteriormente. Posterior a la elección del método, se
compararon los resultados a través del índice Random Score, el cual evidenció que se
obtuvo una mejor agrupación cuando se utilizan 3 Clusters (K-Means con 3 Clusters). A
partir de estos resultados acompañados de las matrices Etiquetas vs. Cluster, se decide
agrupar las señales en 3 grupos bien diferenciados: retina no degenerada, en proceso
de degeneración y retina degenerada. Estos resultados se retroalimentaron en el
Aprendizaje Supervisado nuevamente para la obtención del “RESULTADO (6)”.

➔ RESULTADO (5): La visualización de los gráficos de barra obtenidos de las matrices
Etiquetas vs. Cluster, permitió analizar el comportamiento de las señales ante los niveles
de exposición a luz. En éstos gráficos se observó como las barras pertenecientes a un
determinado cluster (en donde se agrupan las señales de los animales con las retinas
más sanas) decrecen hacia el día 3 y 4 de las etiquetas, y a su vez, las barras
correspondientes a otro cluster (que pertenece a las señales de los animales con las
retinas más dañadas) crecen desde el día 3 y 4. Esto permitió evidenciar la hipótesis
planteada en X respecto a la existencia de un punto de inflexión entre los días 3 y 4 de
exposición a luz a partir del cual la degeneración retinal podría ser irreversible.

➔ RESULTADO (6): acompañado de los “RESULTADOS (5)”, se llevó a cabo una reducción
de etiquetas y nuevamente se sometió las señales a modelos de Aprendizaje
Supervisado. De esta etapa se obtuvieron grandes mejoras debido al balance en la
cantidad de señales en cada etiqueta que se logró al realizar una reducción de las
mismas.


## Conlusiones

Por un lado, se logró un análisis de las señales en el
dominio del tiempo con mayor precisión, disminuyendo considerablemente la posibilidad de
error en los valores de las características gracias a las herramientas de los lenguajes de
programación. Sumado a esto, el análisis en el dominio de la frecuencia permitió conocer en
mayor profundidad las señales ERG y llevar a cabo el proceso de filtrado, obteniendo mejoras
considerables en la morfología de las señales y por lo tanto, mejores resultados en la extracción
de características. Por último, los modelos de aprendizaje automático demostraron, a pesar de
la escasa cantidad de señales, ser herramientas de gran potencial en el diagnóstico precoz de la
DR debido a la exposición a luz.



