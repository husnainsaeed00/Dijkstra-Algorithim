import math

# Create a graph represented as a dictionary of dictionaries
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# Create a dictionary to store the costs from the start node to each node
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = math.inf

# Create a dictionary to store the parents of each node
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# Create a list to keep track of processed nodes
processed = []

# Function to find the node with the lowest cost in the costs dictionary
def find_lowest_cost_node(costs):
    lowest_cost = math.inf
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# Dijkstra's algorithm implementation
def dijkstra_algorithm():
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for neighbor in neighbors:
            new_cost = cost + neighbors[neighbor]
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)

# Call the Dijkstra's algorithm function to run the algorithm
dijkstra_algorithm()

# Function to get the shortest path from the start node to the given node
def get_shortest_path(node):
    path = []
    while node is not None:
        path.append(node)
        node = parents[node]
    return list(reversed(path))

# Print the shortest path from "start" to "fin"
shortest_path = get_shortest_path("fin")
print("Shortest Path:", shortest_path)
print("Cost:", costs["fin"])
