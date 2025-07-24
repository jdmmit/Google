#!/usr/bin/env python
# coding: utf-8

# # Guía anotada paso a paso: ¡Hola, Python!
# 
# Este notebook contiene el código utilizado en los videos instructivos del [Módulo 1: ¡Hola, Python!](https://www.coursera.org/learn/get-started-with-python/home/module/1).
# 

# ## Introducción
# 
# Esta guía paso a paso es un Jupyter Notebook anotado y organizado para coincidir con el contenido de cada módulo. Contiene el mismo código mostrado en los videos del módulo. Además del contenido idéntico al cubierto en los videos, encontrarás información adicional a lo largo de la guía para explicar el propósito de cada concepto, por qué el código se escribe de cierta manera y consejos para ejecutarlo.
# 
# Mientras ves cada uno de los siguientes videos, aparecerá un mensaje en el video para avisarte que contiene instrucciones y ejemplos de código. El mensaje te dirigirá a la sección relevante en el notebook para el video específico que estás viendo. Sigue el notebook mientras el instructor explica el código.
# 
# Para ir directamente al código de un video en particular, usa los siguientes enlaces:
# 
# 1.   **[Descubre más sobre Python](#1)**
# 2.   **[Jupyter Notebook](#2)**
# 3.   **[Programación orientada a objetos](#3)**
# 4.   **[Variables y tipos de datos](#4)**
# 5.   **[Crea nombres de variables precisos](#5)**
# 6.   **[Tipos de datos y conversiones](#6)**

# <a name="1"></a>
# ## 1. [Descubre más sobre Python](https://www.coursera.org/learn/get-started-with-python/lecture/JC2zu/discover-more-about-python)
# 

# In[1]:


# Imprimir en la consola.
print("Hello, world!")


# In[2]:


# Imprimir en la consola.
print(22)


# In[3]:


# Aritmética simple
(5 + 4) / 3


# In[4]:


# Asignar variables.
country = 'Brazil'
age = 30

print(country)
print(age)


# In[5]:


# Evaluaciones
# Los dobles signos de igual se usan para comprobar equivalencia.
10**3 == 1000


# In[6]:


# Evaluaciones
# Un solo signo igual se reserva para asignaciones.
10 ** 3 = 1000


# In[7]:


# Evaluaciones
# Los dobles signos de igual se usan para comprobar equivalencia.
10 * 3 == 40


# In[8]:


# Evaluaciones
# Los dobles signos de igual se usan para comprobar equivalencia.
10 * 3 == age


# In[9]:


# Sentencias condicionales
if age >= 18:
    print('adult')
else:
    print('minor')


# In[10]:


# Bucles
for number in [1, 2, 3, 4, 5]:
    print(number)


# In[11]:


# Bucles
my_list = [3, 6, 9]

for x in my_list:
    print(x / 3)


# In[12]:


# Funciones
def is_adult(age):

    if age >= 18:
        print('adult')
    else:
        print('minor')


# In[13]:


# Usar la función que se acaba de crear.
is_adult(14)


# In[14]:


# Usar la función incorporada sorted().
new_list = [20, 25, 10, 5]

sorted(new_list)


# <a name="2"></a>
# ## 2. [Jupyter Notebooks](https://www.coursera.org/learn/get-started-with-python/lecture/2l42i/jupyter-notebooks)

# **NOTA:** La celda de importaciones debe ejecutarse antes de algunas de las siguientes celdas. Este paso de configuración no se mostró en el video, pero lo aprenderás más adelante en el curso.

# In[37]:


# Importaciones.
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns


# In[38]:


# Crear una lista.
my_list = [10, 'gold', 'dollars']


# In[39]:


# Usar la función auxiliar para calcular la puntuación F1 utilizada en los siguientes gráficos.
def f1_score(precision, recall):
    score = 2*precision*recall / (precision + recall)
    score = np.nan_to_num(score)

    return score


# In[40]:


# Generar un gráfico de la puntuación F1 para diferentes valores de precisión y recall.
x = np.linspace(0, 1, 101)
y = np.linspace(0, 1, 101)
X, Y = np.meshgrid(x, y)
Z = f1_score(X, Y)
fig = plt.figure()
fig.set_size_inches(10, 10)
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=2, cstride=3, cmap='plasma')

ax.set_title('$F_{1}$ de precisión, recall', size=18)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.view_init(35, -65)


# **NOTA:** Las siguientes celdas usan markdown (como esta celda) para crear texto formateado como encabezados, listas, tablas y ecuaciones matemáticas. Puedes seleccionar cualquier celda y entrar en modo edición para ver el texto markdown. Luego ejecuta la celda para ver el resultado.

# ### **Sección 2**
# 
# * Parte 1:
# * Parte 2:

# |Título|Autor|Fecha|
# |:--|:--|:-:|
# |El arte de la guerra|Sun Tzu|siglo V a.C.|
# |Don Quijote de la Mancha|Miguel de Cervantes Saavedra|1605|
# |Orgullo y prejuicio|Jane Austen|1813|
# 

# $$
#   \int_0^\infty \frac{x^3}{e^x-1}\,dx = \frac{\pi^4}{15}
# $$

# <a name="3"></a>
# ## 3. [Programación orientada a objetos](https://www.coursera.org/learn/get-started-with-python/lecture/1SJMN/object-oriented-programming) 

# In[41]:


# Asignar una cadena a una variable y comprobar su tipo.
magic = 'HOCUS POCUS'
print(type(magic))


# In[42]:


# Usar el método swapcase() para convertir mayúsculas a minúsculas.
magic = 'HOCUS POCUS'
magic = magic.swapcase()
magic


# In[43]:


# Usar el método replace() para reemplazar letras por otras.
magic = magic.replace('cus', 'key')
magic


# In[44]:


# Usar el método split() para dividir la cadena en dos cadenas.
magic = magic.split()
magic


# In[45]:


# Preparar la celda para crear el dataframe `planets`.
# (Esta celda no se mostró en el video.)
import pandas as pd
data = [['Mercury', 2440, 0], ['Venus', 6052, 0,], ['Earth', 6371, 1],
        ['Mars', 3390, 2], ['Jupiter', 69911, 80], ['Saturn', 58232, 83],
        ['Uranus', 25362, 27], ['Neptune', 24622, 14]
]

cols = ['Planet', 'radius_km', 'moons']

planets = pd.DataFrame(data, columns=cols)


# In[46]:


# Mostrar el dataframe `planets`.
planets


# In[47]:


# Usar el atributo shape para ver el número de filas y columnas.
planets.shape


# In[48]:


# Usar el atributo columns para ver los nombres de las columnas.
planets.columns


# <a name="4"></a>
# ## 4. [Variables y tipos de datos](https://www.coursera.org/learn/get-started-with-python/lecture/k3ex2/variables-and-data-types) 

# In[15]:


# Asignar una lista con las edades de los jugadores.
age_list = [34, 25, 23, 19, 29]


# In[16]:


# Encontrar la edad máxima y asignarla a la variable `max_age`.
max_age = max(age_list)
max_age


# In[17]:


# Convertir `max_age` a cadena.
max_age = str(max_age)
max_age


# In[18]:


# Reasignar el valor de `max_age`.
max_age = 'ninety-nine'
max_age


# In[19]:


# PRIMERO, VUELVE A EJECUTAR LA SEGUNDA CELDA DE ESTE VIDEO.
# Verificar el valor contenido en `max_age` (DEBERÍA MOSTRAR 34).
max_age


# In[20]:


# Encontrar la edad mínima y asignarla a la variable `min_age`.
min_age = min(age_list)

# Restar `min_age` de `max_age`
max_age - min_age


# <a name="5"></a>
# ## 5. [Crea nombres de variables precisos](https://www.coursera.org/learn/get-started-with-python/lecture/fB03O/create-precise-variable-names) 

# In[55]:


# Intentar asignar un valor a una palabra reservada genera un error de sintaxis.
else = 'a todos les gustan los espárragos'


# In[56]:


# La palabra "asparagus" está mal escrita. Eso está permitido.
esparagus = 'a todos les gustan los esparagus'


# In[57]:


# Orden de operaciones
2 * (3 + 4)


# In[58]:


# Orden de operaciones
(2 * 3) + 4


# In[59]:


# Orden de operaciones
3 + 4 * 10


# <a name="6"></a>
# ## 6. [Tipos de datos y conversiones](https://www.coursera.org/learn/get-started-with-python/lecture/z9zda/data-types-and-conversions)

# In[60]:


# Suma de 2 enteros
print(7+8)


# In[61]:


# Suma de 2 cadenas
print("hello " + "world")


# In[62]:


# No se puede sumar una cadena y un entero.
print(7+"8")


# In[63]:


# La función type() verifica el tipo de dato de un objeto.
type("A")


# In[64]:


# La función type() verifica el tipo de dato de un objeto.
type(2)


# In[65]:


# La función type() verifica el tipo de dato de un objeto.
type(2.5)


# In[66]:


# Conversión implícita
print(1 + 2.5)


# In[67]:


# Conversión explícita (La función str() convierte un número a cadena.)
print("2 + 2 = " + str(2 + 2))


# **¡Felicidades!** Has completado este laboratorio. Sin embargo, puede que no veas una marca de verificación verde en la plataforma de Coursera. Continúa tu progreso sin importar la marca. Solo haz clic en el icono de "guardar" en la parte superior de este notebook para asegurar que tu trabajo quede registrado.
