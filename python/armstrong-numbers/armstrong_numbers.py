def is_armstrong_number(number):
    num, sum = str(number), 0
    for digit in num:
        sum += int(digit)**len(num)
    return sum == number
