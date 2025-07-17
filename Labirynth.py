import tkinter as tk
wall = '\u2588\u2588'
road = '  '
labirynth = [[wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall],
             [road, road, wall, road, wall, road, wall, road, wall, road, wall],
             [wall, road, wall, road, wall, road, wall, road, wall, road, wall],
             [wall, road, road, road, wall, road, wall, road, wall, road, wall],
             [wall, road, wall, road, wall, road, wall, road, wall, road, wall],
             [wall, road, wall, road, wall, road, wall, road, wall, road, wall],
             [wall, road, wall, road, road, road, road, road, road, road, wall],
             [wall, road, wall, road, wall, road, wall, road, wall, road, wall],
             [wall, road, wall, road, wall, road, wall, road, wall, road, road],
             [wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall]]
for line in labirynth:
    print(*line)