# Simple-Evolution
This very basic program simulates the evolution of a population over time. It is divided in four main parts:
+ the Blob class
+ food functions
+ animation function
+ data visualization

To run the simulation, just run `main.py` and insert the desired values for `FOOD` (starting food on the map), `BLOBS` (starting population) and `REFRESH` (how much food is reinserted each iteration).

All the data about the simulation is saved on a file called `data.csv` and running `data_visualization.py` it is plotted.

The only libraries needed are `matplolib` and `numpy`.

## Blob class
It's the file `blob.py` and it should be already enough commentated there, but we will give a general overview also here:
### `__init__(self, x, y, radius, heir, vis, spe, old_life)`
+ `x, y, radius` : initialization of the position and the size of the blob
+ `heir` : set to `False` by default, signal if the blob is descending from some other blob
+ `vis, spe` : starting value for vision and speed. The value of vision is the radius inside of which the blob can see food, the value of speed is how far it moved with one step
+ `old_life` : can be implemented to work in a _life calculator_ for the blob, but at the moment is not used
### `move(self)`
Simple method for randomly moving the blob according to some probabilities.
### `food_check(self, food_map)`
Check if there is food in a circle with as radius the value of vision of the blob.
### `color_change(self)`
Sets the color of the blob based on the attributes.


## Food functions
These are used to generate food in the map, and they are described in the code. Also the name should be self explanatory.

## Animation
In the `animate()` function (inside `main.py`) we have the core of the simulation. The code is commented, but roughly the idea is the following:
+ loop over all Blobs
    + if the blob has still energy
        + check for food in reach
        + if there is food move over it and eat it
        + if no food is found move somewhere else
    + else check if it has food to survive, if not kill him
    + check if the blob can make a baby, if so do it
+ add food at a given rate
+ graphical stuff

## Data Visualization
Once the simulation si done, the data about the life and features of all the blobs is saved, in order to be shown and possibly analized. To show it just run `data_visualization.py`.

# Notebook
There is also a Jupyter notebook version of the program, it is not very convenient though, since the animation is quite heavy and makes the whole notebook slow and not efficient. It is there anyway.

# TO-DO
+ optimize everything and clean it up
+ add more options to be chosen from input
+ add possibility to save the animation as gif
+ organize better main and check for libraries
+ ...
