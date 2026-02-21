# Lab-report-1
Iterative Deepening Depth-First Search (IDDFS).  
Name: Mahinul Islam Rabby
Id: 232002011
Section:232_D7
Course code : CSE316 
## OBJECTIVES/AIM   
The objective of this lab is to implement the Iterative Deepening Depth-First Search (IDDFS) algorithm to find a path in a grid from a given start position to a target position.:  
•	To understand the working principle of Iterative Deepening Depth-First Search (IDDFS) and its advantages over DFS and BFS.
•	To implement IDDFS to find a path from a given start position to a target position in a 2D grid.
•	To learn how to use stack-based DFS with a depth limit to traverse a graph efficiently.
•	To track and display the traversal path and analyze the depth at which the goal is found.
## How to Run
Lab report 1.py

You are given a 2D grid representing a maze, where each cell is either an empty space (0) or a wall (1). Your task is to implement a Python program that uses Iterative Deepening Depth-First Search (IDDFS) to determine whether a valid path exists from a given start cell to a specified target cell. You may move up, down, left, or right to adjacent empty cells, but you cannot pass through walls, and each cell may be visited only once during a single path exploration.

Case#1Input:
4 4
0 1 0 1
0 1 0 0
0 1 0 0
0 0 1 0
Start: 0 0
Target: 3 3

Case#1Output:
Path found at depth 6 using IDDFS
Traversal Order: [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2), (2, 3), (3, 3)]
