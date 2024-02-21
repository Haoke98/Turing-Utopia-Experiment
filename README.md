# Turing Utopia Experiment
<center><a href="README.zh.md">中文</a> | English</center>

Built upon Conway's Game of Life, referencing the Utopia Experiment, and studying the butterfly effect, the project simulates and predicts non-living phenomena. It explores significant outcomes of minor changes and employs cellular automata, complex network models, and machine learning to provide new perspectives on future societal development.

## Core | Kernels
"Life Game" is a two-dimensional grid world, and each grid can be in two states: "alive" or "dead". The rules of the game are as follows:

* Each living cell is surrounded by eight adjacent grids.
* If a living cell is surrounded by 2 or 3 living cells, the cell will continue to survive in the next generation.
* If a living cell is surrounded by 0 or 1 living cells, the cell will die in the next generation.
* If a dead cell is surrounded by 3 living cells, the cell will be resurrected in the next generation.
* The initial state of the game is randomly generated. The game will continue to iterate according to the above rules until all cells die or reach a stable state.

The concept of life cycle:

* Birth: If there are exactly three live grids around a dead grid, the grid will become a live grid at the next moment.
* Survival: If a live grid is surrounded by 2 or 3 live grids, the grid will remain alive at the next moment.
* Death: If there are less than 2 or more than 3 living cells around a live cell, the cell will become a dead cell at the next moment.
* Permanence: If there are no live cells around a dead cell, the cell will remain dead at the next moment.

Features:

* Simple rules: The rules of the game of life are very simple, only four.
* Complex behavior: Despite its simple rules, the Game of Life can produce very complex behaviors, including stable structures, oscillators, gliders and even complex structures resembling living organisms.
* Universality: The Game of Life can be used to simulate various natural phenomena, such as cell division, biological growth, population migration, etc.

## Demo
![](assets/屏幕录制2024-02-21%2016.38.27.gif)

Input (random seed):
```shell
---------- Seed life matrix (initial seed) (20, 20)=400 ----------
[1 1 1 0 1 1 0 0 1 1 0 0 1 0 1 1 1 0 1 1]
[0 1 1 1 1 0 1 1 0 1 0 0 0 1 1 1 0 1 0 0]
[1 0 1 1 0 1 0 0 0 0 1 1 0 1 1 1 0 0 1 0]
[1 0 0 1 0 0 1 1 1 1 1 1 0 1 1 0 0 0 0 0]
[0 1 1 1 1 0 1 0 1 0 1 0 1 1 1 1 1 0 0 1]
[1 0 1 1 0 1 1 1 1 1 1 0 1 1 1 0 1 1 1 0]
[0 1 1 0 1 0 1 1 0 1 0 0 0 0 0 1 1 1 1 1]
[1 1 1 0 0 0 1 1 1 1 1 0 0 0 1 0 1 1 0 1]
[1 0 1 1 0 0 1 1 1 1 0 1 1 1 0 1 1 1 1 0]
[0 0 1 1 0 1 1 1 0 1 1 1 1 1 1 0 0 1 1 0]
[1 1 1 1 0 1 1 0 1 0 1 1 1 0 0 1 1 0 1 0]
[1 1 0 0 1 0 1 0 0 0 1 0 1 0 1 0 1 0 1 0]
[1 1 0 0 0 0 1 0 0 1 1 1 0 1 0 1 1 0 0 1]
[1 1 1 0 0 1 0 1 1 1 0 0 0 0 1 1 0 1 0 1]
[0 0 1 0 0 1 1 1 1 0 0 1 1 0 1 0 1 0 0 1]
[1 1 0 1 0 0 1 0 1 1 0 0 0 0 1 0 1 0 0 0]
[0 0 0 1 0 1 1 0 1 1 1 0 0 0 1 0 1 0 1 1]
[1 0 1 1 1 1 1 1 0 1 0 1 1 1 0 0 0 0 1 0]
[1 1 1 1 0 1 0 1 1 0 1 0 1 1 0 1 0 0 1 1]
[0 1 0 1 1 0 1 1 1 1 1 0 0 0 0 0 1 0 1 1]
-------------------------------------------------- ----
```
Review:
```shell
---------- Neighbor number matrix (20, 20)=400 ----------
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
[0 7 7 7 6 5 4 3 4 4 4 3 4 6 8 7 5 4 4 3]
[0 5 6 6 5 4 5 5 5 5 6 4 5 6 8 5 3 2 2 1]
[0 5 6 6 5 4 4 5 4 6 6 6 6 7 8 6 3 2 2 2]
[0 5 6 6 5 5 6 8 7 8 6 6 6 8 7 6 4 4 3 2]
[0 6 7 7 5 6 6 7 6 6 4 4 4 6 6 7 7 7 6 4]
[0 7 6 5 3 5 7 8 8 7 5 3 2 4 4 6 7 8 7 4]
[0 7 6 5 2 4 6 8 8 6 5 3 3 3 4 6 8 8 7 4]
[0 6 6 5 3 4 7 8 8 7 7 6 6 6 5 5 6 7 6 3]
[0 6 7 6 5 5 7 7 6 6 7 8 8 6 5 5 6 7 5 3]
[0 6 6 5 5 6 6 5 3 5 6 8 6 6 4 5 4 6 4 3]
[0 7 5 3 3 5 4 4 2 5 6 7 5 4 4 6 5 5 3 3]
[0 7 4 2 2 4 4 4 4 5 5 4 3 4 5 6 5 4 4 3]
[0 6 4 2 2 4 6 6 6 5 5 4 4 4 5 6 5 3 4 3]
[0 6 5 3 3 4 6 7 7 5 3 2 2 4 4 6 4 3 3 2]
[0 3 4 3 4 5 6 7 6 6 4 3 2 4 3 6 3 4 3 3]
[0 4 5 5 6 6 6 6 6 6 5 3 3 4 3 4 2 4 3 3]
[0 5 6 6 7 6 7 6 6 6 5 5 5 5 4 3 2 4 5 5]
[0 6 7 7 7 6 7 7 7 6 5 5 5 4 3 2 2 4 5 5]
[0 4 5 4 4 3 4 5 5 5 3 3 2 2 2 2 2 3 4 4]
----------------------------------------
```
After a trial:
```shell
The 1st Evolution:
Deaths: 205 Lives: 24 Births: 31 Final Life Units: 55
---------- New life matrix (20, 20)=400 ----------
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
[0 0 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0 1]
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0]
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0]
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1]
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
[0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0]
[0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0]
[0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1]
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1]
[0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 1]
[0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1]
[0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1]
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1]
[0 0 0 1 1 0 0 0 0 0 1 1 1 0 0 0 0 1 1 1]
[0 1 0 1 0 0 0 0 0 0 0 1 0 0 1 0 1 0 1 1]
[0 0 0 0 0 0 0 0 0 0 0 1 1 0 1 0 1 0 1 1]
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0]
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0]
[0 0 0 0 0 1 0 0 0 0 1 1 0 0 0 0 1 1 0 0]
----------------------------------------
```
Final output:
```shell
The 15th Evolution:
Death: 0 Survival: 12 Birth: 0 Final life units: 12
---------- New life matrix (20, 20)=400 ----------
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0]
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0]
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
[0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0]
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
[0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0]
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1]
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1]
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
[0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0]
----------------------------------------
After 15 evolutions, the reincarnation will no longer evolve (evolve).
```

## refer to
* [Game of Life](https://playgameoflife.com/)
* Utopian experiment
* The Butterfly Effect
*Three-body game

## Functions to be implemented soon

* [ ] Save the evolution process in real time. Just load the existing life evolution process every time you start it. If the seeds of life are gone, start a new reincarnation (Epoch).
* [ ] Real-time statistics of the number of births, number of survivors, number of deaths and number of lives to provide statistical curves📉.
* [ ] Calculate the ideal input?
   * Calculate what kind of input will last for a long time without dying?
   * Constantly conduct reincarnation experiments
   * Each round: Give a random initial life matrix.
   * Each round: Save the number of evolutions after several `evolution/evolution/trial` and entering the `steady state` (no more `evolution/evolution` or all `life units` die). (The evolution process does not need to be remembered)
   * Each round: Sort the saved content in reverse order by the number of evolutions. (It cannot be calculated by time, because time in the simulation world can be accelerated or expanded)
   * Each round: Once it enters the `steady state` (no further `evolution/evolution` or all `life units` die), the current cycle ends and a new cycle begins.

## Apply assumptions
* Simulate and calculate the ideal population size and distribution (suitable for sustainable development and survival)
* Take real-world data as input:
   * Simulate and calculate the ideal population size and distribution (suitable for sustainable development and survival)