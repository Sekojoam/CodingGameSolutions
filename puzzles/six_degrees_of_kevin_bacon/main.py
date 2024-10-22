import sys
import math


def debug(message, params=""):
    print(f"{params}:{message}", file=sys.stderr, flush=True)


# 6 Degrees of Kevin Bacon!


class Node:

    def __init__(self, name):
        self.name = name
        self.parentsList = []


class Graph:

    def __init__(self, movies, actors):
        self.queue: list[Node] = []
        self.movies = movies
        self.actors = actors

    def bfs(self, actorName):
        kevin = "Kevin Bacon"
        if actor_name == kevin:
            print("0")
            return
        kevinFound = False
        node = Node(actorName)
        self.queue.append(node)
        movies = self.actors[node.name]
        while not kevinFound:
            for node in self.queue:
                movies = self.actors[node.name]
                for movie in movies:
                    movie_actors = self.movies[movie]
                    if kevin in movie_actors:
                        kevinFound = True
                        debug(movie, "kevin found in ")
                        debug(node.parentsList, "kevin found in ")
                        print(len(node.parentsList) + 1)
                        break
                    else:
                        if node.name in movie_actors:
                            movie_actors.remove(node.name)
                        for movie_actor in movie_actors:
                            newNode = Node(movie_actor)
                            debug(node.name, "node.name")
                            debug(node.parentsList, "node.parentsList")
                            newNode.parentsList = list(node.parentsList)
                            if node.name not in newNode.parentsList:
                                newNode.parentsList.append(node.name)
                            self.queue.append(newNode)
                if kevinFound:
                    break


actor_name = input()
debug(actor_name, "actor_name")
movies = {}
actors = {}
n = int(input())
for i in range(n):
    movie_cast = input()
    movie_title, movie_actors = movie_cast.split(": ")
    movie_actors = movie_actors.split(", ")
    movies[movie_title] = movie_actors
    for actor in movie_actors:
        if actor in actors:
            actors[actor].append(movie_title)
        else:
            actors[actor] = [movie_title]

debug(movies, "movies")
debug(actors, "actors")

graph = Graph(movies, actors)

graph.bfs(actor_name)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# print("N degrees to Kevin Bacon")
