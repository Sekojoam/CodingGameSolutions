import sys
import math


def debug(message, params=""):
    print(f"{params}:{message}", file=sys.stderr, flush=True)


n = int(input())
smallest_input = 1000


list_input = []
for i in range(n):
    pi = int(input())
    list_input.append(pi)
list_input.sort()

for i in range(1, len(list_input)):
    diff = abs(list_input[i] - list_input[i - 1])
    if diff < smallest_input:
        smallest_input = diff

print(smallest_input)
