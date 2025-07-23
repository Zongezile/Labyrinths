import random
import pickle
from collections import deque

def generate_new_maze():
    size = int(input('Please, enter the size of a maze\n'))
    wall = '\u2588\u2588'
    road = '  '

    labyrinth = [[wall for x in range(size)] for x in range(size)]
    row, col = random.randint(1, size - 2), 0
    labyrinth[row][col] = road  # wejście
    neighbors = {}
    exit_ = False

    def add_neighbor(row, col, parent_r, parent_c):
        nonlocal exit_
        if col == size - 1 and exit_ == False and 0 < row < size - 1 and labyrinth[row][col] == wall:
            exit_ = True
            neighbors[(row, col)] = (parent_r, parent_c)
        elif 0 < row < size - 1 and 0 < col < size - 1 and labyrinth[row][col] == wall:
            neighbors[(row, col)] = (parent_r, parent_c)

    add_neighbor(row - 2, col, row, col)
    add_neighbor(row + 2, col, row, col)
    add_neighbor(row, col - 2, row, col)
    add_neighbor(row, col + 2, row, col)

    while neighbors:
        (row, col), (pr, pc) = random.choice(list(neighbors.items()))
        neighbors.pop((row, col))
        if labyrinth[row][col] == wall:
            mid_r = (row + pr) // 2
            mid_c = (col + pc) // 2
            labyrinth[mid_r][mid_c] = road
            labyrinth[row][col] = road
            add_neighbor(row - 2, col, row, col)
            add_neighbor(row + 2, col, row, col)
            add_neighbor(row, col - 2, row, col)
            add_neighbor(row, col + 2, row, col)

    for line in labyrinth:
        print(''.join(line))

    return labyrinth

def solve_maze(labyrinth):
    road = '  '
    path = '//'
    rows = len(labyrinth)
    cols = len(labyrinth[0])
    start = None
    end = None
    for r in range(rows):
        if labyrinth[r][0] == road:
            start = (r, 0)
        if labyrinth[r][cols - 1] == road:
            end = (r, cols - 1)

    # BFS
    queue = deque([start])
    paths = {}
    while queue:
        r, c = queue.popleft()
        if (r, c) == end:
            break
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and labyrinth[nr][nc] == road and (nr, nc) not in paths:
                queue.append((nr, nc))
                paths[(nr, nc)] = (r, c)

    # Odtwarzanie ścieżki
    right_path = end
    while right_path and right_path != start:
        r, c = right_path
        labyrinth[r][c] = path
        right_path = paths[right_path]
    r, c = start
    labyrinth[r][c] = path

    for line in labyrinth:
        print(''.join(line))

option = ''
labyrinth = []

while option != '0':
    if labyrinth:
        option = input('''=== Menu ===
                        1. Generate a new maze
                        2. Load a maze
                        3. Save the maze
                        4. Display the maze
                        5. Find the escape
                        0. Exit\n''')
    else:
        option = input('''=== Menu ===
                            1. Generate a new maze
                            2. Load a maze
                            0. Exit\n''')
    if option == '1':
        labyrinth = generate_new_maze()
    elif option == '2':
        file = input()
        try:
            with open(file, 'rb') as f:
                labyrinth = pickle.load(f)
        except FileNotFoundError:
            print(f'The file {file} does not exist')
        except pickle.UnpicklingError:
            print('Cannot load the maze. It has an invalid format')
    elif option == '3':
        file = input()
        with open(file, 'wb') as f:
            pickle.dump(labyrinth, f, pickle.HIGHEST_PROTOCOL)
    elif option == '4':
        for line in labyrinth:
            print(''.join(line))
    elif option == '5':
        solve_maze(labyrinth)
    elif option == '0':
        print('Bye!')
        break
    else:
        print('Incorrect option. Please try again')
