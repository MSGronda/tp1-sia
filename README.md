# Trabajo Practico 1 - SIA

## Requisitos:
1) Python 3
2) Pip 3

## Ejecucion:
1) Ejecutar en una linea de comnados (con pip instalado):
```
pip install -r requirements.txt
```
2) Ejecutar los distintos algoritmos con:
```
python <nombre_archivo>
```

## Uso de clase Sokoban
Para usar la clase Sokoban se puede usar su contructor. A este se le debe pasar el _path_ de un board.
```
game = Sokoban("./Boards/board.txt")
```

La tambien clase implementa los siguientes metodos:
- \_\_hash__ : devuelve el hash para el estado acutal
- \_\_deepcopy__ : devuelve una copia profunda del estado actual
- \_\_eq__ : devuelve positivo si 2 clases son iguales, es decir, dos estados son iguales

## Armado de Boards:
- Los boards consisten de una matrix de n x n, en donde se modela el area de juego.
- Los characteres puestos en dicha matrix simbolizan los distintos elementos del juego. Estos son:

| Character | Descripcion |
|---|-------------|
| Espacio | Espacio vacio |
| # | Pared |
| % | Caja |
| * | Objetivo |
| $ | Jugador |
| @ | Objetivo con caja encima |
| & |  Objetivo con jugador encima |

