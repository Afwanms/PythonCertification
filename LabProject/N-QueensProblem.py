def dfs_n_queens(n):
    solutions = []
    visited = []
    if n < 1:
        return []

    def dfs_helper(board_size, row):
        if row >= board_size:
            solutions.append(visited.copy())
            return
        for col in range(board_size):
            if col not in visited and all(abs(col - c) != row - r for r, c in enumerate(visited)):
                visited.append(col)
                dfs_helper(board_size, row + 1)
                visited.pop()

    dfs_helper(n, 0)
    return solutions

print(dfs_n_queens(4))
print(len(dfs_n_queens(8)))