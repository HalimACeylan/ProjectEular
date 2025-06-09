
def spiral_from_center(n, m):
    grid = [[0 for _ in range(m)] for _ in range(n)]

    # Starting point: center of grid
    x, y = n // 2, m // 2

    # For even dimensions, start slightly left/up of center
    if n % 2 == 0: x -= 1
    if m % 2 == 0: y -= 1

    # Directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    steps = 1
    num = 1
    dir_index = 0

    grid[x][y] = num
    num += 1

    while num <= n * m:
        for _ in range(2):  # two directions per step size
            dx, dy = directions[dir_index % 4]
            for _ in range(steps):
                x += dx
                y += dy
                if 0 <= x < n and 0 <= y < m:
                    grid[x][y] = num
                    num += 1
                if num > n * m:
                    break
            dir_index += 1
        steps += 1

    return grid

matrix = spiral_from_center(1001, 1001)
def sum_diagonals(grid):
    n = len(grid)
    total = 0
    for i in range(n):
        total += grid[i][i]                  # primary diagonal
        total += grid[i][n - 1 - i]          # secondary diagonal

    if n % 2 == 1:
        center = grid[n // 2][n // 2]
        total -= center  # subtract one duplicate center
    return total

print(sum_diagonals(matrix))