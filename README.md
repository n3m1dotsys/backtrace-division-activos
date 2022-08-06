# backtrace-division-activos

Este repositorio contiene la implementación del algoritmo que resuelve el 
problema de la división de activos mediante el esquema algoritmico backtrace.

## Problema

El problema consiste en una lista o vector de valores enteros de una serie de 
activos que tienen que ser repartidos entre 2 socios de forma equitativa. 
El problema puede no tener solución para ciertas listas, por ejemplo si la
suma de los valores no da un número par.

## El esquema algoritmico *Backtrace* o *Vuelta atrás*

Este esquema consiste en resolver el problema dividiendolo en pasos en los
que se ha de tomar una decisión. En esa toma de decisión se tomará una de 
forma arbitraria y se avanzará hasta el siguiente nodo de toma de decisión 
donde se tomará la siguiente decisión de forma arbitraria. Así hasta que o
solucione el problema o se de cuenta que no pueda resolver el problema. 
Para el segundo caso, el algoritmo probará con la siguiente decisión posible
en ese nodo de toma de decisión, y realizará el mismo proceso de antes. Si 
en el nodo en el que se encuentra se queda sin decisiones que tomar para 
resolver el problema entonces hará lo que se denomina *"vuelta atrás"*, y
retrocederá al anterior nodo donde analizará el resto de decisiones posibles
y elaborandolas como ha hecho anteriormente, hasta que encuentra la solución.

## *Backtrace* en el problema de división de activos

Para este problema, dividiremos cada activo en una toma de decisión que 
consistirá en darle el activo al socio 1 o al socio 2. De forma arbitraria, 
empezaremos dandole los activos al socio 1, hasta que no podamos darle más, 
porque la suma de los valores rebasaría la mitad y luego le daremos los 
activos al socio 2. Si en algun momento vemos que rebasamos el valor de 
la suma de los activos del socio 2 en ese caso volveremos a la anterior 
decisión en la que dimos el activo al socio 1, y en vez de darsela a él 
se la daremos al socio 2, y volveremos a darle activos al socio 1 hasta 
que no podamos y despues al socio 2, como hemos hecho antes.

Para hacer esto haremos una función que llamaremos de forma recursiva de
forma condicional tal y como hemos descrito en el anterior parrafo.

## Funcionamiento del programa

Si se ejecuta desde un IDE o desde la consola de comandos sin argumentos este
se ejecutará para el caso predeterminado definido en las primeras lineas del 
programa. 

Se puede cambiar este vector en el mismo script o ejecutando el programa en 
la consola de comandos añadiendo el vector despues de la llamada al programa.

``` sh
python3 division_activos.py 10 9 5 3 3 2 2 2 2 2
```

`
