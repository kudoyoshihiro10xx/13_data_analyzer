def calculation_total(numbers):
    total = 0

    for num in numbers:
        total += num

    return total


def calculation_maximum(numbers):
    maximum = 0

    for num in numbers:
        if num > maximum:
            maximum = num

    return maximum


def calculation_minimum(numbers):
    minimum = numbers[0]

    for num in numbers:
        if num <= minimum:
            minimum = num

    return minimum


def calculation_ave(numbers):
    ave = round((calculation_total(numbers) / len(numbers)), 3)
    # sum = 0
    #
    # for num in numbers:
    #     sum = sum + num
    #     print(sum)
    # ave = sum / len(numbers)

    return ave
