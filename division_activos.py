#!/usr/bin/env python3
import sys

# Modificar este vector para otros casos
VECTOR_PREDETERMINADO = [10, 9, 5, 3, 3, 2, 2, 2, 2, 2]


def dividir(x, suma1, suma2, sumat, k, v):
    """ALGORITMO DEL PROGRAMA
    Divide los activos de una sociedad de forma equitativa utilizando el
    esquema algoritmico "Vuelta Atras" o "Backtrace"

    :param x: lista de activos a distribuir (Ejemplo: [10,9,5,3,3,2,2,2,2,2])
    :type  x: list
    :param suma1: suma de los valores de los activos para el socio 1
    :type  suma1: int
    :param suma2: suma de los valores de los activos para el socio 2
    :type  suma2: int
    :param sumat: suma total de los valores de los activos en x
    :type  sumat: int
    :param k: posición en :param x: del activo que se está avaluando
    :type  k: int
    :param v: lista de distribución de activos (Ejemplo: [1,2,2,2,2,1,1,1,1,1])
    :type  v: list

    """
    # Estas dos lineas son para crear nuevos objetos, de forma que no altera
    # los vectores 'v' y 'x' de las llamadas recursivas precedentes. No son
    # ordenes que tengan que ver con el algoritmo, es más bien que Python
    # es un poco tonto y a veces hay que hacer tonterías para que no se ponga
    # tonto
    x = list(x)
    v = list(v)
    # Mensaje por pantalla de la llamada a la función recursiva que se ha
    # realizado
    print(f"dividir({str(x)},{str(suma1)},{str(suma2)},{str(sumat)}," +
          f"{str(k)},{str(v)})")
    # Comprobación de si ha terminado el algoritmo
    if k == len(x):
        # Si ha terminado (k apunta al ultimo elemento de x) comprueba si es
        # una solución correcta
        if suma1 == suma2:
            # Si la suma de ambos socios es igual es factible
            procesar(x, v)
            sys.exit(0)  # Esto finaliza la ejecución del programa.
    else:
        # Si no ha terminado tenemos que elegir a quien le damos el activo en
        # la posición k. Empezamos dandoselo al socio 1, si no puede darselo al
        # socio 1 en el momento en el que se da cuenta el algoritmo volverá
        # atrás hasta este punto donde intentará hacer lo mismo con el socio 2.
        # Si no puede darselo a ningún socio, en ese caso esta llamada
        # recursiva finalizará, y la llamada anterior tendrá que reintentar
        # darle el activo a otro socio o retroceder
        v[k] = 1
        # Primero comprobamos que pueda darle el activo al socio 1 de forma
        # general, es decir que si le damos el activo al socio 1 el valor
        # de los activos que este tiene no sobrepase la mitad de la suma
        # total de los valores
        if suma1 + x[k] <= sumat // 2:
            print(f"Dando el activo en {str(k)} con valor {str(x[k])} a 1")
            suma1 = suma1 + x[k]
            # Aquí realiza la llamada recursiva, es realizar el mismo proceso
            # definido por esta función con otra parametrización.
            dividir(list(x), suma1, suma2, sumat, k+1, list(v))
            # Si por algún motivo no puede resolver el problema dandole el
            # activo al socio 1, deshace la suma y comprueba si puede darselo
            # al socio 2
            suma1 = suma1 - x[k]
        # Aquí salimos del if o si no hemos podido entrar en el primer caso
        # intentamos darle el activo al socio 2
        v[k] = 2
        # Hacemos el mismo proceso que hemos hecho para el socio 1 pero con
        # el socio 2
        if suma2 + x[k] <= sumat // 2:
            print(f"Dando el activo en {str(k)} con valor {str(x[k])} a 2")
            suma2 = suma2 + x[k]
            dividir(list(x), suma1, suma2, sumat, k+1, list(v))
            suma2 = suma2 / x[k]
        # Tras comprobar si es posible darle el activo a cada socio, y probar
        # si podemos resolver el problema dandoselo, si no se cumplieran alguna
        # de las dos condiciones, en ese caso por esta rama no puede
        # solucionarse el problema, y habria que dar vuelta atrás, probando a
        # dar al otro socio el activo o haciendo una vuelta atrás más hasta
        # que encuentre una rama por la que pueda intentar resolver el problema.
        print("Por aquí no ha solución, vuelta atrás")


def procesar(x, v):
    """Procesa el resultado de la operación y lo muestra por pantalla

    :param x: Lista de activos
    :param v: Lista de distribución

    """
    activos1 = []
    activos2 = []
    for activo, donde in zip(x, v):
        if donde == 1:
            activos1.append(activo)
        else:
            activos2.append(activo)
    print(f"1: {str(activos1)}")
    print(f"2: {str(activos2)}")


def print_help():
    """Escribe un texto de ayuda de como utilizar el programa

    """
    print("Uso del programa: ")
    print("python division_activos.py [vector]")
    print("Ejemplos: ")
    print("python division_activos.py 9 4 2 2 2 1")
    print("python division_activos.py")
    print("Para el segundo caso se utilizará el vector de pruebas:")
    print(VECTOR_PREDETERMINADO)


def main():
    """Función principal, sirve para inicializar vairables y el proceso del
    algoritmo

    """
    if len(sys.argv) > 2:
        x = []
        for element in sys.argv[1:]:
            x.append(int(element))
    else:
        x = VECTOR_PREDETERMINADO
    v = [0] * len(x)
    sumat = 0
    for element in x:
        try:
            sumat += int(element)
        except ValueError:
            print_help()
            sys.exit(1)
    print(f"Dividiendo los activos {str(x)}...")
    dividir(list(x), 0, 0, sumat, 0, list(v))


main()
