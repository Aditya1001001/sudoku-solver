grid = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def print_puzzle(grid):
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("-----------------------  ")

        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")


def is_valid(grid, num, pos):

    x, y = pos

    # Checking row
    for i in range(len(grid[0])):
        if grid[x][i] == num and y != i:
        # ignoring the cell we just inserted he number into
            return False

    # Checking column
    for i in range(len(grid)):
        if grid[i][y] == num and x != i:
        # ignoring the cell we just inserted the number into
            return False

    # Cheking 3x3 box
    box_x = x // 3
    box_y = y // 3

    for i in range(box_y * 3, box_x * 3 + 3):
        for j in range(box_x * 3, box_y * 3 + 3):
            if grid[i][j] == num and i != x and j != y:
                return False
    
    return True


def find_empty_space(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i, j) #return row, column
    
    return False # No empty spaces


def solve(grid):

    #uncomment this if you want to see the progess
    # print_puzzle(grid)

    empty = find_empty_space(grid)
    if not empty:
        return True
    else:
        i, j = empty
    
    for num in range(1,10):
        if is_valid(grid, num, (i, j)):
            grid[i][j] = num

            if solve(grid):
                return True
            
            grid[i][j] = 0

    return False

print_puzzle(grid)
print("   ")
solve(grid)
print_puzzle(grid)