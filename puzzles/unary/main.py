import sys
import math


def debug(msg, param=""):
    print(f"{f'{param} ' if param != '' else ''}{msg}", file=sys.stderr, flush=True)

message = input()
debug(message, "message")

def make_seven_bits_from_message(message):
    dataOut = []
    for char in message:
        bin_bin = bin(ord(char))[2:]
        if len(bin_bin) == 7:
            dataOut.append(bin_bin)
        else:
            missingZeros = 7 - len(bin_bin)
            dataOut.append("".join(["0" for i in range(missingZeros)])+bin_bin)
    return "".join(dataOut)

binary = make_seven_bits_from_message(message)

dataOut = []
actualSerie = ""
for character in binary:
    if actualSerie == "":
        actualSerie= character
    elif character == actualSerie[-1]:
        actualSerie += character
    else:
        dataOut.append(actualSerie)
        actualSerie = character
dataOut.append(actualSerie)

convertedOut= []
for serie in dataOut:
    if bool(int(serie)):
        convertedOut.append(f"0 {serie.replace('1', '0')}")
    else:
        convertedOut.append(f"00 {serie}")
convertedOutLitteral = " ".join(convertedOut)

print(convertedOutLitteral)