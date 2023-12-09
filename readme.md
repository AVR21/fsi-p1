# Resolución Práctica 1 de Fundamentos de los Sistemas Inteligentes.

## Grupo de trabajo (Pr. Laboratorio 02.01):

+ Hernández Sánchez, Daniel
+ Medina Santana, Antonio
+ Viera Ruiz, Alejandro

## Objetivos
Se propone completar el código aportado para la práctica alojado en la [página web](http://cayetanoguerra.github.io/ia/) de la asignatura.

Para ello, implementar los siguientes algoritmos de búsqueda:

+ Ramificación y Acotación (*Branch & Bound*)
+ Ramificación y Acotación con subestimación

Añadir al programa principal, test suficientes para probar el correcto funcionamiento de los algoritmos descritos anteriormente.

## Recursos
El código a completar cuenta con tres scrips de **Python**:
+ [run.py](run.py) : Programa principal con batería de tests que hace uso de los algoritmos de búsqueda implementados.

+ [search.py](search.py) : Script de generación de problemas y desarrollo de los algoritmos de búsqueda.

+ [utils.py](utils.py) : Utilidades varias, implementación de las estructuras de datos necesarias para el funcionamiento de los algoritmos de búsqueda.

## Desarrollo de la práctica
Para comenzar, se analizan los ficheros aportados, podemos observar que [search.py](search.py) ya contiene la implementación de los algoritmos de búsqueda por niveles(*Breadth First Search*) y en profundidad(*Depth First Search*).

Para ello, generaliza el procedimiento de búsqueda dentro de la función *graph_search()* que es llamada con dos parámetros, el problema a resolver y la estructura de datos con la cual se resuelve.

Una vez comprendido esto, podemos ampliar esta implementación, desarrollando una estructura de datos que satisfaga las condiciones de cada búsqueda.

### Ramificación y Acotación
En este caso, se ha añadido una nueva estructura de datos basada en la interfaz *Queue* (Cola), con el mismo funcionamiento pero con un paso extra en la expansión de los nodos. Una vez se ha extendido el nodo, se ordena la cola de menor a mayor peso acumulado, de esa forma priorizamos que se visiten los nodos potencialmente más cercanos al objetivo.

### Ramificación y Acotación con subestimación
Al igual que en el caso anterior, se implementa una estructura de datos que funciona como una cola y se añade un paso extra. Esta vez, además de tener en cuenta el peso acumulado, el orden se ve influenciado por una heurística (de aquí parte el concepto de subestimación).

Dicha heurística debe acercarse al resultado sin superarlo, en caso contrario, podría no encontrarse la solución al problema. Como se explica en la práctica, la heurística que se usará en este algoritmo es la distancia en linea recta entre el nodo visitado y el objetivo. Sumando esta heurística al peso acumulado, obtenemos el nuevo criterio por el cual se ordena esta estructura de datos.

## Conclusión
A lo largo del desarrollo de la práctica se ha logrado implementar correctamente el algoritmo de búsqueda no informada de Ramificación y Acotación y el algoritmo de búsqueda informado homónimo con subestimación. Los resultados de los test implementados han sido satisfactorios y hemos podido comprender las utilidades de las funciones usadas.
