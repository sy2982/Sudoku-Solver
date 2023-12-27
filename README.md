# Sudoku Solver

The Sudoku Solver is a Python program designed to solve Sudoku puzzles using backtracking and constraint satisfaction techniques. This project aims to provide a simple and efficient solution to solving Sudoku puzzles, offering both interactive and batch processing modes.

## Introduction

Sudoku is a popular number-placement puzzle that requires filling a 9x9 grid with digits from 1 to 9, ensuring that each row, each column, and each of the nine 3x3 subgrids contain all of the digits from 1 to 9.

This Sudoku Solver provides an efficient and well-documented solution for solving Sudoku puzzles of varying difficulty levels.

## Features

- **Backtracking Algorithm:** The solver employs a backtracking algorithm to explore potential solutions, ensuring it finds the correct solution efficiently.
- **Customizable Constraints:** The solver uses constraint satisfaction to validate potential assignments, ensuring they adhere to Sudoku rules.
- **Interactive Input:** Users can input Sudoku puzzles interactively or provide a batch of puzzles through a text file.
- **Visualization:** The solver visually displays the initial and solved Sudoku boards, aiding users in understanding the solution process.

## Usage

To run you can type python3 sudoku.py follow by a valid problem.

- For example: python3 sudoku.py 003020600900305001001806400008102900700000008006708200002609500800203009005010300
- Should return: 483921657967345821251876493548132976729564138136798245372689514814253769695417382

## Algorithms

### Backtracking Algorithm

The backtracking algorithm explores potential assignments for each cell and backtracks when a conflict is detected, ensuring the correct solution is found.

### Constraint Satisfaction

The solver uses constraint satisfaction techniques to validate potential assignments, ensuring they adhere to Sudoku rules.
