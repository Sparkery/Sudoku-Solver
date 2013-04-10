Sudoku-Solver
=============

Solves a given Sudoku puzzle entered in a single string.

A sample Sudoku string is as follows.

..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..

Where a "." is a blank square.

Algorithm
=========

This solver uses map coloring. According to the Four Color Theorem, any map can be colored distinctly with at most four colors. Sudoku is a map coloring problem, except with nine colors.

Efficiency
==========

April 9, 2013: Is able to solve all 3 Al Escargot problems in just over four seconds, including printing time. Solves one of the top 95 most difficult Sudoku puzzles in around 3 minutes. This is subject to improvement over some duration.
