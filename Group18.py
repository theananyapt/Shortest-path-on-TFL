#Below is the Dijkstra's algorithm for finding shortest path from the given rail network
def dijkstra(graph, origin, destination):
    #setting track of stations visited
    visited = set()
    #initializing an empty dictionary to store the shortest distance from origin to each station
    distance = {}
    #initializing an empty dictionary to store the predecessor station after every station visited on the shortest path
    predecessor = {}
    #Initializing current station with the origin
    current = origin
    #the predecessor of starting station is set to None
    predecessor[current] = None
    #the distance of starting station from predecessor is set to 0
    distance[current] = 0
    #loop for iterating all visiting stations
    if origin not in graph or destination not in graph:
    #If the station is not present in the network it will print error and provide the available stations
       print("Error: One or both stations are not present in the network.")
       print("Available stations:", ", ".join(graph.keys()))
       return
    while len(visited) != len(graph):
        #adding the current station to visited station set
        visited.add(current)
        #Updating the predecessor and distance for adjacent stations
        for adj_station in graph[current]:
            if adj_station not in visited:
                new_distance = distance[current] + graph[current][adj_station]
                #Checking if the current path is the shhortest path
                if adj_station in distance:
                    if new_distance < distance[adj_station]:
                        distance[adj_station] = new_distance
                        predecessor[adj_station] = current
                else:
                    distance[adj_station] = new_distance
                    predecessor[adj_station] = current
        #finding the next station to visit from the unvisited stations that has the minimum distance
        min_distance = float("inf")
        for station in distance:
            if station not in visited and distance[station] < min_distance:
                min_distance = distance[station]
                current = station
    #constructing the shortest path again from destination to origin using the predecessor dictionary
    path = []
    next_station = destination
    while next_station is not None:
        path.append(next_station)
        next_station = predecessor[next_station]
    #reversing the aboth path list to get the path from origin ot destination
    path.reverse()
    #printing the shortest possible route and the total time taken to cover it
    print(path)
    print("This journey takes", distance[destination], "minute(s).")

#creating a dictionary of model network
if __name__ == "__main__":
    graph = {"Aldgate East": {"Liverpool Street": 4,"Tower Hill": 2},
    "Baker Street": {"Bond Street": 2,"Paddington": 6,"Kings Cross": 7,"Oxford Circus": 4},
    "Bank": {"Blackfriars": 4,"Holborn": 5,"Liverpool Street": 2,"London Bridge": 2,"Moorgate": 3,"Tower Hill": 2},
    "Blackfriars": {"Bank": 4,"Embankment": 4},
    "Bond Street": {"Baker Street": 2,"Green Park": 2,"Notting Hill Gate": 7,"Oxford Circus": 1},
    "Charing Cross": {"Embankment": 1,"Leicester Square": 2,"Piccadilly Circus": 2},
    "Elephant & Castle": {"London Bridge": 3,"Waterloo": 4},
    "Embankment": {"Blackfriars": 4,"Charing Cross": 1,"Westminster": 2,"Waterloo": 2},
    "Green Park": {"Bond Street": 2,"Oxford Circus": 2,"Piccadilly Circus": 1,"South Kensington": 7,"Victoria": 2,"Westminster": 3},
    "Holborn": {"Bank": 5,"Kings Cross": 4,"Leicester Square": 2,"Tottenham Court Road": 2},
    "Kings Cross": {"Baker Street": 7,"Holborn": 4,"Moorgate": 6,"Old Street": 6,"Warren Street": 3},
    "Leicester Square": {"Charing Cross": 2,"Holborn": 2,"Piccadilly Circus": 2,"Tottenham Court Road": 1},
    "Liverpool Street": {"Aldgate East": 4,"Bank": 2,"Moorgate": 2,"Tower Hill": 6},
    "London Bridge": {"Bank": 2,"Elephant & Castle": 3,"Waterloo": 3},
    "Moorgate": {"Bank": 3,"Kings Cross": 6,"Liverpool Street": 2,"Old Street": 1},
    "Notting Hill Gate": {"Bond Street": 7,"Paddington": 4,"South Kensington": 7},
    "Old Street": {"Kings Cross": 6,"Moorgate": 1},
    "Oxford Circus": {"Baker Street": 4,"Bond Street": 1,"Green Park": 2,"Piccadilly Circus": 2,"Tottenham Court Road": 2,"Warren Street": 2},
    "Paddington": {"Baker Street": 6,"Notting Hill Gate": 4},
    "Piccadilly Circus": {"Charing Cross": 2,"Green Park": 1,"Leicester Square": 2,"Oxford Circus": 2},
    "South Kensington": {"Green Park": 7,"Notting Hill Gate": 7,"Victoria": 4},
    "Tottenham Court Road": {"Holborn": 2,"Leicester Square": 1,"Oxford Circus": 2,"Warren Street": 3},
    "Tower Hill": {"Aldgate East": 2,"Bank": 2,"Liverpool Street": 6},
    "Victoria": {"Green Park": 2,"South Kensington": 4,"Westminster": 4},
    "Warren Street": {"Kings Cross": 3,"Oxford Circus": 2,"Tottenham Court Road": 3},
    "Waterloo": {"Elephant & Castle": 4,"Embankment": 2,"London Bridge": 3,"Westminster": 2},
    "Westminster": {"Embankment": 2,"Green Park": 3,"Victoria": 4,"Waterloo": 2}}
    #asking user for inputs of start and end stops
    origin = input("Starting station: ")
    destination = input("Finishing station: ")
    #calling the Dijkshtra function defined above
    dijkstra(graph, origin, destination)

