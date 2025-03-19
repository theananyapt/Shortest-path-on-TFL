# Dijkstra Algorithm for Shortest Path in a Railway Network (Transport for London - TFL)

A project demonstrating the implementation of Dijkstra’s algorithm in Python to calculate the shortest path between stations in a simplified rail network. This repository also includes documentation of tests, limitations, and proposals for future improvements.

---

## Project Overview

1. **Dijkstra’s Algorithm:**  
   - Core logic for finding the shortest travel time (or distance) between two railway stations.  
   - Maintains a dynamic dictionary for distances and predecessor nodes, updating them until all nodes are visited.

2. **Railway Network Model:**  
   - Represented in a directed graph where stations (nodes) connect to neighboring stations with travel times (weights).  
   - Users specify an origin and destination; the algorithm outputs the shortest route and total travel time.

3. **Testing & Validation:**  
   - Five different test cases explore various route scenarios.  
   - Includes error handling (e.g., unknown stations) and verifying consistency when swapping origin and destination.

4. **Limitations & Improvements:**  
   - Currently assumes a **directed** graph; real-world railway systems often require an **undirected** approach.  
   - Suggestion to integrate **error handling** for invalid user inputs and to handle **multiple shortest paths**.  
   - Potential for **real-time updates** or **unit tests** to enhance reliability and match real-world use cases.

---

## Key Features

- **Python Implementation:** A concise Python function demonstrates how to initialize data structures, track visited nodes, update shortest paths, and retrieve final route information.
- **Meeting Records:** Summaries of development progress, issues encountered, and solutions proposed at each stage.
- **Test Suite:** Multiple scenarios confirm that the algorithm correctly computes routes under various station combinations and edge cases.

---

## How to Use

1. **Setup:** Clone or download this repository and ensure you have a Python environment (3.x) installed.  
2. **Run the Algorithm:** Provide a list (or dictionary) representing the rail network (stations and travel times). Then call the Dijkstra function with your chosen origin and destination.  
3. **Results:** The console prints the shortest route and total travel time.  

---

## Future Directions

- **Undirected Graph Support:** Adjust data structures to treat every route bidirectionally if appropriate.  
- **Enhanced Error Handling:** Improve user prompts for unrecognized stations or format errors.  
- **Dynamic Routing:** Incorporate real-time data on travel delays or disruptions.  
- **Multiple Shortest Paths:** Extend the approach to return all equally optimal solutions, not just one.

---

