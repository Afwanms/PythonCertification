def dfs(matrix, node):
    visited = set()
    result = []
    
    def dfs_helper(current):
        visited.add(current)
        result.append(current)
        
        for node_val, neighbor in enumerate(matrix[current]):
            if neighbor == 1 and node_val not in visited:
                dfs_helper(node_val)
    
    dfs_helper(node)
    return result