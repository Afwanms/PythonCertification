def verify_card_number(card_num):
    card_num = str(card_num).replace('-', '').replace(' ', '')
    digits = []

    for char in card_num[::-1]:
        digits.append(int(char))

    for num in range(1, len(digits), 2):
        digits[num] *= 2
        if digits[num] > 9:
            digits[num] -= 9

    total = sum(digits)
    
    if total % 10 == 0:
        return 'VALID!'
    else:
        return 'INVALID!'

print(verify_card_number(4539148803436467))