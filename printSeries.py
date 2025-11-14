def printSeries(n):
    result = []
    value = 100
    diff = 1

    while value > n:
        result.append(str(value))
        value -= diff
        diff += 1

    return ",".join(result)
import sys
print(printSeries(int(sys.argv[1])), end="")
