# modelosuno_lavadera_100102

* Entrega 2
- Impresión del problema.
  * Cambios con respecto la entrega anterior es que se aumentaron la cantidad de restricciones, el problema es el mismo
- Ideas de como lo van a intentar resolver
  * mantuve la resolucion anterior, pero ahora voy a llevar al limite de fuerza bruta.
- Comentarios sobre los cambios que hagan en el código a medida que intentan mejorar el resultado.
  * agregue randomizaciones y multithreading, tomando la mejor opcion.
  * estoy usando 100 threads y 1000 ciclos en cada thread.
- Comentarios finales de la entrega
  * el resultado es bastante malo de 692, proxima entrega buscaria cambiar el modelo
  * pros:
    * el codigo sigue siendo eficiente.
  * cons:
    * fuerza bruta no es optimo.
* Entrega 1
- Impresión del problema:
  * me entere a ultimo momento del tp, y de la primera entrega lo realice en una hora durante la noche, y lo pense como un ejercicio de logica, y el resultado no fue optimo claramente
- Ideas de como lo van a intentar resolver:
  * la resolucion pensada fue como un problema de grafos, leer el archivo armar un grafo, y por cada prenda poner vecinos a las prendas que no pueden lavarse con la misma.  
  * luego recorrer este grafo, e ir seprando en tandas.
- Comentarios sobre los cambios que hagan en el código a medida que intentan mejorar el resultado.
  * realice el codigo como lo plantie, primero no tuve en cuenta los conflictos de las prendas vecinas, entonces agregue otro loop para verificar.
  * pros: 
    * es un codigo simple y eficiente.
  * cons:
    * no es nada optimo.
- Comentarios finales de la entrega
  * hice lo que pude con la hora de tiempo que tenia (realice la entrega antes de la prorroga), siguiente entrega sera modelar algo real.


* Entrega 3 

Modelizar el problema mediante Programación Lineal Entera, no implementar el modelo en un solver, solo presentarlo y explicar las restricciones
  Subirlo al GitHub y marcar la entrega subiendo una solución de la tercera instancia

* Objetivo: minimizar la cantidad de tandas de lavado de prendas, teniendo en cuenta que hay prendas que no pueden lavarse juntas
* Restricciones:

Es un ejercicio de coloreo, lo podemos pensar como un grafo G(V (vertices),E (aristas)), donde los vertices son las prendras, y las aristas
representa que estas aristas no pueden lavarse juntas.
Entonces planteo el modelo clasico de Coloreo

 ```math
 $ x_ij, w_j \in {0, 1} $ Si dos prendas son adyacentes(destiñen) no pueden estar en la misma tanda  $x_ij$ = vertice i esta en tanda j 
 $ x_ij + x_kj \le w_j si [i, k] \in E para todo j = 1,...,N $  Si algun prenda esta en la tanda j se fuerza wj a valer 1
 $ \sum_{j=1}^N x_ij = 1 para todo i \in V $  Cada prenda puede estar en una sola tanda
 $ Min z = \sum_{j=1}^N w_j $ Minimiza la cantida de colores
```


