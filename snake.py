gridWidth = 16
gridHeight = 10

currentCoordinates = [1,5]
[columncoord, rowcoord] = currentCoordinates
def snakeMoving():
    for i in range(1):
        grid = []
        currentCoordinates = [columncoord + 1, rowcoord]

        for _ in range(gridHeight):
            row = []
            for _ in range(gridWidth):
                row.append("X")

        grid.append(row)




        grid[columncoord][rowcoord] = "S"

        value = grid[columncoord][rowcoord]

        printingGrid = ""
        for row in grid:
            printingGrid += "".join(row) + "\n"

        print(printingGrid)

        print(f"{columncoord} + {rowcoord}: {value}")




snakeMoving()