def hanoi_solver(disks):
    rod_1 = []
    rod_2 = []
    rod_3 = []

    numbers = list(range(disks, 0, -1))
    for num in numbers:
        rod_1.append(num)

    def move(num, start, mid, end):
        nonlocal string

        if num == 1:
            end.append(start.pop())
            string += f"{rod_1} {rod_2} {rod_3}\n"
        else:
            move(num - 1, start, end, mid)
            end.append(start.pop())
            string += f"{rod_1} {rod_2} {rod_3}\n"
            move(num - 1, mid, start, end)

    string = f"{rod_1} {rod_2} {rod_3}\n"
    move(disks, rod_1, rod_2, rod_3)
    return string.strip()


test = 3
print(hanoi_solver(test))