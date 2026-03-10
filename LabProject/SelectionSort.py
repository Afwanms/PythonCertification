def selection_sort(array):
    if len(array) <= 1:
        return array
    
    for num in range(len(array)):
        min_index = num
        for j in range(num + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        if min_index != num:
            array[num], array[min_index] = array[min_index], array[num]
    return array