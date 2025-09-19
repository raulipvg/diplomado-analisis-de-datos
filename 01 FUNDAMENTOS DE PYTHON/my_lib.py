# Esta es librería de prueba

def factorial(n: int) -> int:
    """
    ### Función: `factorial`

    Calcula el factorial de un número entero no negativo `n` usando recursividad.  
    El factorial de un número entero `n` (denotado como `n!`) es el producto de todos los enteros positivos menores o iguales a `n`.

    #### Parámetros:
    - `n` (int): Número entero no negativo para el cual se desea calcular el factorial.

    #### Retorno:
    - (int): El factorial de `n`. Si `n` es 0, el resultado es 1, ya que `0!` es 1 por definición.

    #### Errores:
    - Si `n` es negativo, lanza un `ValueError` porque el factorial no está definido para números negativos.

    #### Ejemplo:
    ```python
    resultado = factorial(5)
    print(resultado)  # Salida: 120
    ```

    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)



def isBisiesto(n: int) -> bool:
    """
    ### Función: `isBisiesto`

    Determina si el año ingresado es del tipo Bisiesto (366 días) o no. 

    #### Parámetros:
    - `n` (int): Número entero no negativo para el cual se desea determinar si corresponde a año Bisiesto.

    #### Retorno:
    - (bool): Entrega una valor Boolean, que es True si es Bisiesto, y False si no lo es.

    #### Errores:
    - No hay manejo de errores.

    #### Ejemplo:
    ```python
    resultado = isBisiesto(2004)
    print(resultado)  # Salida: True
    ```
    """
    if n%400==0:
        return True
    elif n%100==0:
        return False
    elif n%4==0:
        return True
    else: 
        return False

