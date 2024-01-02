import random

WALL = "▓"
OPEN_SPACE = "◌"
START = "S"
END = "E"
PATH = "◍"

def generate_maze(n, wall_percentage):
    maze = [[WALL if random.random() < wall_percentage else OPEN_SPACE for _ in range(n)] for _ in range(n)]
    maze[0][0] = START
    maze[n-1][n-1] = END
    return maze

def print_maze(maze):
    for row in maze:
        print(" ".join(row))

def dfs_pathfinding(maze, x, y, path):
    if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == OPEN_SPACE:
        maze[x][y] = PATH
        path.append((x, y))

        if (x, y) == (len(maze) - 1, len(maze[0]) - 1):
            return True

        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            if dfs_pathfinding(maze, x + dx, y + dy, path):
                return True

        maze[x][y] = OPEN_SPACE
        path.pop()

    return False

def main():
    n = 5  
    wall_percentage = 0.2 

    maze = generate_maze(n, wall_percentage)
    print("Generated Maze:")
    print_maze(maze)

    maze_clone = [row[:] for row in maze]

    path = []
    if dfs_pathfinding(maze_clone, 0, 0, path):
        print("\nPath Found:")
        print_maze(maze_clone)
        print("\nPath Coordinates:")
        print(path)
    else:
        print("\nNo Path Found. Try adjusting maze parameters.")

if __name__ == "__main__":
    main()
