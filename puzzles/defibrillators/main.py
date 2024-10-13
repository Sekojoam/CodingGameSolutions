import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def debug(message, params=""):
    print(f"{params}:{message}", file=sys.stderr, flush=True)

def super_float(string:str):
    return float(string.replace(",", "."))

class Defribilator():

    def __init__(self, line):
        args = line.split(";")
        self.id = args[0]
        self.name = args[1]
        self.address = args[2]
        self.number = args[3]
        self.long = super_float(args[4])
        self.lat = super_float(args[5])

    def __str__(self):
        return self.name

    def calculate_distance(self, longA, latA):
        x = (self.long - longA) * math.cos ((latA+self.lat)/2)
        y = self.lat - latA
        return ((x**2 + y **2)**0.5) * 6371

    def calculate_distance_simple(self, longA, latA):
        return ((abs(longA - self.long)**2 + (self.lat - latA) **2))

lon = super_float(input())
lat = super_float(input())
n = int(input())
defibs = []
smallest = 10000
smallest_id = -10
for i in range(n):
    defib = Defribilator(input())
    debug(defib, "defib")
    distance = defib.calculate_distance_simple(lon, lat)
    if distance < smallest:
        smallest = distance
        smallest_id = i
    defibs.append(defib)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(defibs[smallest_id].name)
