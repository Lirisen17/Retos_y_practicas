colection = []
num = 0


def solution(number):
    total = 0
    for n in range(number):
        if n % 3 == 0 or n % 5 == 0:
            colection.append(n)
    for c in colection:
        total = total + c
    colection.clear()
    return total


print(solution(5))
print(colection)
