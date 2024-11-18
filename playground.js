const gridWidth = 6
const gridHeight = 8

const startingCoordinate = [1,2]
let [columnCoord, rowCoord] = startingCoordinate


function createGrid() {
    let grid = []
    for (i = 0; i < gridHeight; i++) {
        let row = []
        for (j = 0; j < gridWidth; j++) {
            row.push('X')
        }
        grid.push(row)
    }
    return grid
}





function snakeMoving() {
    let [columnCoord, rowCoord] = startingCoordinate
    for (i = 0; i < 5; i++) {
        console.log(i)
        let grid = createGrid()
        columnCoord++
        grid[columnCoord][rowCoord] = "S"
        console.log(grid)
    }
}

snakeMoving()