# CacheAlgoritmo

Se implementaron las políticas de reemplazo:

LRU, ÓTIMO, CLOCK, LFU

Como workload se utilizaron traces de Wikipedia y se le estableció un cierto formato por parte de la profesora.

Para ejecutar el script  del proyecto por línea de comando, establecemos como formato el siguiente:
<workload_file> <policy> <cache size (number of entries)> 
Ejemplo (evaluando una cache con 50000 entradas): 
$python simulador-cache.py workload.txt LRU 50000




Descripciones de Políticas de reemplazo implementadas.

LRU
Se utilizaron listas para la implementación de este algoritmo en python, en el cual se verificaba si un url del workload está en caché, si no estaba y la cache aún no llegaba al límite (tamaño), se insertaba en caché (miss), cuándo la caché está llena, y el url a insertar, no se encuentra en la cache se procede a reemplazar por el menos reciente usado, el cual se llevaba el orden a travéz de otra lista para obtener el índice del “mas_antiguo” y poder realizar el reemplazo por el nuevo url.

Algoritmo Óptimo

Este algoritmo tiene como finalidad retirar la página que vaya a ser referenciada más tarde. Como se puede deducir, para esto el sistema operativo debería ver en cuánto tiempo será usada cada página en memoria y elegir la que está más distante. El problema de este algoritmo es que necesita conocimiento del futuro, por lo que es imposible su implementación de manera optima. Como solo es un algoritmo teórico, en nuestra implementación (no óptima) utilizamos listas para poder recorrer las páginas que están disponibles en caché y asi poder remplazar la que se utilizara en el plazo más largo.

CLOCK
En el algoritmo clock , se usó  un arreglo de dos dimensiones el cual  se dividió de la siguiente manera: el arreglo estaba compuesto de arreglos que tiene un tamaño de 3, en el primer índice se almacena el puntero, en el segundo la palabra que se va a usar y en el tercero el bit se segunda oportunidad como por ejemplo: 
[[Puntero, palabra, bit], [Puntero, palabra, bit] ………..]. 
El arreglo principal tendrá el tamaño de la caché, para la elaboración del algoritmo se dividió en 2 parte, la primera será para ingresar y comparando los datos hasta que se llene el arreglo, la segunda parte es cuando el arreglo está lleno se procederá a comparar que si esa palabra se encuentra  ingresada, si lo está se pone el bit de segunda oportunidad igual a 1 y si no está se procede a reemplazar según el puntero.

LFU
Se utilizó un método de conteo para lo cual se implementó un diccionario de datos asociado a la frecuencia que las páginas han sido referenciadas, esto facilita la selección del elemento de menor Contador para ser reemplazado por la nueva página que será insertada en caché.




