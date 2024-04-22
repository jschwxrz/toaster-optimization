# Toaster Optimization

Welcome to the Toaster Optimization repository! This repository contains a series of optimization challenges, ranging from 'easy' to 'prepare to cry', all centered on the art of perfecting toaster settings. The various optimization tasks and the project outline are detailed in `toaster_optimization_task.py`.

## Repository Structure

Each difficulty level of the toaster optimization tasks has its own dedicated folder. The folder contains one or multiple python files where the filename indicates the type of algorithm that was used, as well as my implementation of that algorithm designed to maximize the utility function.

Notice that the folder 'hard' also contains following files:

- `plotted_function.py` (plot of the utility function)
- `calculation_partial_derivative.txt` (calculation of the partial derivative in respect to the power parameter)

## Prerequisites

Following libraries are required:

- mathplotlib
- numpy

## Running the Code

To run any of the optimization files:

1. Open your terminal or command prompt.
2. Change the directory to the folder of the desired difficulty level using `cd <foldername>`.
3. Execute the script with the following command:

`python <filename>.py`

The output will have following structure:

Optimum: ()

value:

## Algorithms

1. easy: brute force

   - Systematically examines every single possibility within the state space to identify optimum.

2. medium: hill climbing

   - Evaluates the utility of all adjacent parameters and selects the most advantageous one.

3. hard: hill climbing + gradient ascent

   - Integrates hill climbing for discrete parameters with gradient ascent to optimize continuous parameters.

4. very hard: hill climbing + gradient ascent + repeated search

   - Employs the strategy from 'hard' with an added repeated search to locate all optima.

5. prepare to cry: hill climbing + gradient ascent + repeated search

   - Executes a comprehensive search to determine all optima, while exclusively returning the supreme global optimum.
   - Notice: not optimal algorithm to solve this problem! A genetic algorithm would be more suited in this case!
