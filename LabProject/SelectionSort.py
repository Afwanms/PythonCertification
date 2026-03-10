def selection_sort(array):
    if len(array) <= 1:
        return array
    
    for num in range(len(array)):
        min_index = num
        for value in range(num + 1, len(array)):
            if array[value] < array[min_index]:
                min_index = value
        if min_index != num:
            array[num], array[min_index] = array[min_index], array[num]
    return array