# Find the sum of all the multiples of 3 or 5 below a given number:
def multilesOf3or5(number):
    if number % 3 == 0:
        return True
    if number % 5 == 0:
        return True
    else:
        return False


def sumOfMultiples(number):
    sum = 0
    for i in range(1, number):
        if multilesOf3or5(i):
            sum += i
    return sum

print(sumOfMultiples(1000))
