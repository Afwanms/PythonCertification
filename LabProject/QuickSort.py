def quick_sort(array):
    if len(array) <= 1:
        return array
    
    mid = array[len(array) // 2]
    left_part = []
    right_part = []
    middle_part = []
    for number in array:
        if number < mid:
            left_part.append(number)

    for number in array:
        if number == mid:
            middle_part.append(number)
            
    for number in array:
        if number > mid:
            right_part.append(number)

    return quick_sort(left_part) + middle_part + quick_sort(right_part)