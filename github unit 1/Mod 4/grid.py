#Joy Flowers
#09/24/19
#This program prints a heart from the initial given grid
#It then prints an attempt at a horse using keyboard characters

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
for x in range(6):
    for y in range(9):
        print(grid[y][x],end='')
    print('')
face = [['.', '^', '.', '.', '^', '.'],
        ['.', '^', '.', '.', '^', '.'],
        ['.', '0', '.', '.', '0', '.'],
        ['.', '.', '|', '|', '.', '.'],
        ['.', '(', 'o', 'o', ')', '.'],
        ['.', '.', '-', '.', '.', '.'],
        ['.', '\\', '_', '_', '/', '.'],
        [' ', '.', '.', '.', '.', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ']]
print('')
for x in range(9):
    for y in range(6):
        print(face[x][y],end='')
    print('')
