fun main() {
    val grid = Array(12) {
        readln().toCharArray()
    }

    fun drop() {
        for (col in 0 until 6) {
            for (row in 10 downTo 0) {
                if (grid[row][col] != '.' && grid[row + 1][col] == '.') {
                    var r = row
                    while (r + 1 < 12 && grid[r + 1][col] == '.') {
                        grid[r + 1][col] = grid[r][col]
                        grid[r][col] = '.'
                        r++
                    }
                }
            }
        }
    }

    fun boom(): Boolean {
        val toBoom = Array(12) { BooleanArray(6) { false } }
        var hasBoom = false

        for (row in 0 until 12) {
            for (col in 0 until 6) {
                if (grid[row][col] == '.') continue
                val color = grid[row][col]
                val queue = ArrayDeque<Pair<Int, Int>>()
                val connected = mutableListOf<Pair<Int, Int>>()
                queue.add(Pair(row, col))
                connected.add(Pair(row, col))
                toBoom[row][col] = true

                while (queue.isNotEmpty()) {
                    val (r, c) = queue.removeFirst()
                    val directions = listOf(Pair(1, 0), Pair(-1, 0), Pair(0, 1), Pair(0, -1))
                    for ((dr, dc) in directions) {
                        val nr = r + dr
                        val nc = c + dc
                        if (nr in 0 until 12 && nc in 0 until 6 && !toBoom[nr][nc] && grid[nr][nc] == color) {
                            toBoom[nr][nc] = true
                            queue.add(Pair(nr, nc))
                            connected.add(Pair(nr, nc))
                        }
                    }
                }

                if (connected.size >= 4) {
                    hasBoom = true
                    for ((r, c) in connected) {
                        grid[r][c] = '.'
                    }
                } else {
                    for ((r, c) in connected) {
                        toBoom[r][c] = false
                    }
                }
            }
        }
        
        return hasBoom
    }

    var chainCount = 0

    while (boom()) {
        chainCount++
        drop()
    }

    println(chainCount)
}