import sys
import math

def debug(message, param=""):
    print(f"{param}:{message}", file=sys.stderr, flush=True)
expression = input()


first = True
debug(expression)
operandes = []
for index, char in enumerate(expression):
    if index == 0:
        operandes.append(expression[0])
        continue
    last = operandes[-1]
    if char.isnumeric() and last.isnumeric():
        operandes[-1]= last+char
    else:
        operandes.append(char)
debug(operandes)

for index, operande in enumerate(operandes):
    if index != 0 and operandes[index-1].isnumeric():
        continue
    if operande == "-":
        last = operandes[index+1]
        operandes[index] = f"(-{last})"
        operandes.pop(index+1)
debug(operandes)

for operator in ["+", "/", "-", "*"]:
    while operator in operandes:
        index = operandes.index(operator)
        first = operandes[index-1]
        last = operandes[index+1]
        operandes.pop(index+1)
        operandes.pop(index)
        operandes[index-1] = f"({first}{operator}{last})"

debug(operandes)
result = round(eval("".join(operandes)))
print(result)
