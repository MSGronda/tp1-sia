# Trabajo Practico 1 - SIA

## Requisitos:
1) Python 3
2) Pip 3

## Ejecucion:
1) Ejecutar en una linea de comnados (con pip instalado):
```
pip install -r requirements.txt
```


2) Preparar el archivo configuration.json para la ejecucion:
```json
{
  "singleAlgorithmData" : {
    "run": false,
    "showBoardMoves" : true,
    "algorithm": "bfs",
    "heuristic": "manhattan_distance",
    "board": "board2.txt"
  },

  "heuristicsComparison" : {
    "run": false,
    "board": "board2.txt",
    "iterations": 100
  },

  "timesComparison" : {
    "run": false,
    "board": "board2.txt",
    "iterations": 5,
    "heuristic": "manhattan_distance"
  },
  "stepsComparison" : {
    "run": false,
    "board": "board_benchmark.txt",
    "heuristic": "manhattan_distance"
  },
  "frontierComparison" : {
    "run": false,
    "board": "board2.txt",
    "heuristic": "manhattan_distance"
  },
  "nodesExpandedComparison" : {
    "run": false,
    "board": "board2.txt",
    "heuristic":"lost_game"
  }
}
```
El archivo .json tiene la confugracion necesaria para correr los algoritmos que generan datos.

i)Para obtener los datos de un algoritmo propio por la terminal, se debe modificar la siguiente seccion:
```json
"singleAlgorithmData" : {
    "run": false,
    "showBoardMoves" : true,
    "algorithm": "bfs",
    "heuristic": "manhattan_distance",
    "board": "board2.txt"
  },
```
Donde la propiedad **run** se debe colocar en **true**
La propiedad showBoardMoves puede estar en **true** o en **false** segun se quiera o no ver el paso a paso en el tablero.
la propiedad **algorithm** puede ser cualquiera
de las siguientes: 

- dfs
- bfs
- greedy
- a_star


La propiedad **Heuristic** solo se aplicara si selecciono en la propiedad **algorithm** las opciones **greedy** o **a_star**.

Los valores que puede tomar son:

- average_distance
- combined_heuristic
- euclidian_distance
- lost_game
- manhattan_distance
- manhattan_wall_detection

La propiedad **board** puede ser cualquiera de los tableros provistos en 
el directorio **Boards**. Puede agregar tableros propios a dicho directorio y ejecutar tambien.
Las opciones validas son:

- board.txt
- board2.txt
- board3.txt
- board4.txt
- board5.txt
- board6.txt
- board7.txt
- board8.txt
- board9.txt
- board_benchmark.txt

Un ejemplo de ejecucion podria ser el siguiente:

```json
{
  "singleAlgorithmData" : {
    "run": true,
    "showBoardMoves" : true,
    "algorithm": "a_star",
    "heuristic": "manhattan_distance",
    "board": "board_benchmark.txt"
  },

  "heuristicsComparison" : {
    "run": false,
    "board": "board2.txt",
    "iterations": 100
  },

  "timesComparison" : {
    "run": false,
    "board": "board2.txt",
    "iterations": 5,
    "heuristic": "manhattan_distance"
  },
  "stepsComparison" : {
    "run": false,
    "board": "board_benchmark.txt",
    "heuristic": "manhattan_distance"
  },
  "frontierComparison" : {
    "run": false,
    "board": "board2.txt",
    "heuristic": "manhattan_distance"
  },
  "nodesExpandedComparison" : {
    "run": false,
    "board": "board2.txt",
    "heuristic":"lost_game"
  }
}
```
Solo se ejecutara singleAlgorithm data,a con el algoritmo A*, con la heuristica manhattan_distance contra el tablero board_benchmark.

Para ver la comparacion de heuristicas, solo se debe aclarar el numero de iteraciones y elegir un tablero, y poner la propiedad 
**run** en **true**
un ejemplo de ejecucion es el siguiente:

```json
{
  "singleAlgorithmData" : {
    "run": false,
    "showBoardMoves" : true,
    "algorithm": "a_star",
    "heuristic": "manhattan_distance",
    "board": "board_benchmark.txt"
  },

  "heuristicsComparison" : {
    "run": true,
    "board": "board2.txt",
    "iterations": 400
  },

  "timesComparison" : {
    "run": false,
    "board": "board2.txt",
    "iterations": 5,
    "heuristic": "manhattan_distance"
  },
  "stepsComparison" : {
    "run": false,
    "board": "board_benchmark.txt",
    "heuristic": "manhattan_distance"
  },
  "frontierComparison" : {
    "run": false,
    "board": "board2.txt",
    "heuristic": "manhattan_distance"
  },
  "nodesExpandedComparison" : {
    "run": false,
    "board": "board2.txt",
    "heuristic":"lost_game"
  }
}
```

Para compara el tiempo de ejecucion entre los 4 algoritmos, debe seleccionar
el tablero y la heuristica a utilizar por los algoritmos A* y greedy.

un ejemplo de ejecucion podria ser el siguiente

```json
{
  "singleAlgorithmData" : {
    "run": false,
    "showBoardMoves" : true,
    "algorithm": "a_star",
    "heuristic": "manhattan_distance",
    "board": "board_benchmark.txt"
  },

  "heuristicsComparison" : {
    "run": false,
    "board": "board2.txt",
    "iterations": 400
  },

  "timesComparison" : {
    "run": true,
    "board": "board_benchmark.txt",
    "iterations": 5,
    "heuristic": "lost_game"
  },
  "stepsComparison" : {
    "run": false,
    "board": "board_benchmark.txt",
    "heuristic": "manhattan_distance"
  },
  "frontierComparison" : {
    "run": false,
    "board": "board2.txt",
    "heuristic": "manhattan_distance"
  },
  "nodesExpandedComparison" : {
    "run": false,
    "board": "board2.txt",
    "heuristic":"lost_game"
  }
}
```

Para ejecutar la comparacion por pasos, debe seleccionar el tablero y la heuristica a utilizar por A* y greeedy.
Un ejemplo de un json valido para esta ejecucion podria ser

```json
{
  "singleAlgorithmData" : {
    "run": false,
    "showBoardMoves" : true,
    "algorithm": "a_star",
    "heuristic": "manhattan_distance",
    "board": "board_benchmark.txt"
  },

  "heuristicsComparison" : {
    "run": false,
    "board": "board2.txt",
    "iterations": 400
  },

  "timesComparison" : {
    "run": false,
    "board": "board_benchmark.txt",
    "iterations": 5,
    "heuristic": "lost_game"
  },
  "stepsComparison" : {
    "run": true,
    "board": "board_benchmark.txt",
    "heuristic": "manhattan_distance"
  },
  "frontierComparison" : {
    "run": false,
    "board": "board2.txt",
    "heuristic": "manhattan_distance"
  },
  "nodesExpandedComparison" : {
    "run": false,
    "board": "board2.txt",
    "heuristic":"lost_game"
  }
}
```

para correr la comparacion por nodos expandidos y nodos en frontera restantes al finalizar el algoritmo es analogo.


3) Tras configurar **configuartion.json**, simplemente,
parado en el directorio raiz del proyecto correr
```
python __main__.py
```


## RECOMENDAMOS FUERTEMENTE CORRER SOLO UN ALGORITMO A LA VEZ, OSEA QUE EL JSON SOLO TENGA UN ATRIBUTO RUN EN TRUE. SINO EL PROGRAMA EJECUTARIA TODO LO QUE ESTE EN TRUE Y PUEDE LLEVAR A DEMORAS LARGAS

Recomendacion para heuristicComparison y timesComparison:
Dado que se puede definir la cantidad de iteraciones a correr, aconsejamos que si se selecciona el board1 o board9, poner una cantidad baja de iteraciones dado que puede llegar a tardar mucho tiempo. 

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
