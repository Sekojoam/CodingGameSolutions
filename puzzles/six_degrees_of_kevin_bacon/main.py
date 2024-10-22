import sys
import math


def debug(message, params=""):
    print(f"{params}:{message}", file=sys.stderr, flush=True)

# 6 Degrees of Kevin Bacon!

class Node:

    def __init__(self, isFirst, linkedActors, name, movieName, previousNode:list):
        self.isFirst = isFirst
        self.linkedActors = linkedActors
        self.name = name
        self.movieName = movieName
        self.previousNode = previousNode

    def __str__(self):
        return f"name : {self.name}, isFirst {self.isFirst}, actors {[i.name for i in self.linkedActors]} previousNode {self.previousNode}"

class Movie:

    def __init__(self, title, actors):
        self.title = title
        self.actors = actors

actor_name = input()
debug(actor_name, "actor_name")
n = int(input())
movie_list = []
node = None

specialName = "Kevin Bacon"
solutionFound = False
finalNode = None
for i in range(n):
    movie_cast = input()
    title, actors = movie_cast.split(": ")
    actors = actors.split(", ")
    if actor_name in actors:
        node = Node(isFirst=True, linkedActors = [], name = actor_name, movieName = title, previousNode= [])
        for linkedActor in actors:
            if linkedActor == actor_name:
                continue
            node.linkedActors.append(Node(isFirst=False, linkedActors = [], name = linkedActor, movieName=None, previousNode=[title]))

            if linkedActor == specialName:
                solutionFound = True
                print("1")
        debug(node, "node")
    debug(title, "title")
    debug(actors, "actors")
    movie_list.append(Movie(title, actors))
if node is not None:
    for actor in node.linkedActors:
        for movie in movie_list:
            # don't forget 
            if movie.title in actor.previousNode:
                continue
            if actor.name in movie.actors:
                actor.movieName = movie.title
                for linkedActor in movie.actors:
                    if linkedActor == actor.name:
                        continue
                    previousNode = list(actor.previousNode)
                    previousNode.append(movie.title)
                    actor.linkedActors.append(Node(isFirst=False, linkedActors = [], name = linkedActor, movieName=None, previousNode=previousNode))
                    if linkedActor == specialName:
                        solutionFound = True
                        print(len(previousNode))
                # new_node = Node(isFirst=False, linkedActors = [], name = actor_name, movieName = title, previousNode=None)



# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# print(solutionFound)
