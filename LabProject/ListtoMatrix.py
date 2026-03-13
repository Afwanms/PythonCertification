def adjacency_list_to_matrix(dictionary):
    adj_matrix = []
    size = len(dictionary)
    for key in dictionary:
        row = [0] * size
        
        for neighbor in dictionary[key]:
            row[neighbor] = 1
        adj_matrix.append(row)
    
    for row in adj_matrix:
        print(row)
    
    return adj_matrix

print(adjacency_list_to_matrix({0: [1, 2], 1: [2], 2: [0, 3], 3: [2]}))
