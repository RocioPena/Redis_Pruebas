# Crear una calculadora que solo sume

## To-Do List

| Tarea                                  | En Proceso | Terminado |
|----------------------------------------|------------|-----------|
| |  | Investigar de como insertar numeros en /*Redis*/  |
| | Obtener numeros para la interfaz desde /*Redis*/ | Solo obtuve lo siguiente, desde <u>app1.py</u>: <img src="/workspace/Redis_Pruebas/img/dosindices.png"> |
|  | |  Insertar numeros desde python (no interfaz), y se utilizo expire para que se borren: <u>expire.py</u> |
|  |  | Como insertar numeros desde la interfaz y guardarlos en /*Redis*/ si se visualizan desde la terminal y se expiran: <u>interfaz.py</u> |
| Insertar los numeros y mostrarlos en la interfaz |  |  |
|  |  |  |
| En python obtener los dos numeros y realizar la suma, y que muestre en la terminal |  |  |
| Despues de la suma en python que lo muestre en la interfaz |  |  |



### Investigar de como insertar numeros en /*Redis*/

Para seleccionar una base de datos es con 

```
SELECT [index]
```
En este caso se esta utilizando el 1

<br>


Y para insertar datos en un tipo lista
```
RPUSH clave 0 0

RPUSH numeros 2 9
```

y para que se regresen es 
```
LRANGE numeros 0 -1
```

