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