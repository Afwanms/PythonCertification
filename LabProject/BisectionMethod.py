def square_root_bisection(value, tolerance=1e-6, max_num=100):
    if value < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    elif value == 0 or value == 1:
        print(f'The square root of {value} is {value}')
        return value
    else:
        if value < 1:
            left, right = value, 1
        else:
            left, right = 1, value
        
        for _ in range(max_num):
            mid = (left + right) / 2
            if (right - left) < tolerance:
                print(f'The square root of {value} is approximately {mid}')
                return mid
            elif mid * mid < value:
                left = mid
            else:
                right = mid
        
        print(f'Failed to converge within {max_num} iterations')
        return None
    
print(square_root_bisection(225, 1e-7, 10))