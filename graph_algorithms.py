
def bfs(graph, start_node, search_node=None):
    # graph: a dictionary representing the graph to be traversed.
    # start_node: a string representing the starting node of the traversal.
    # search_node: an optional string representing the node being searched for in the graph.
    # Note: If the given start_node belongs to one strongly connected component then the other nodes belong to that
           # particular component can only be traversed. But the nodes belonging to other components must not be traversed
           # if those nodes were not reachable from the given start_node.

    #The output depends on whether the search_node is provided or not:
        #1. If search_node is provided, the function returns 1 if the node is found during the search and 0 otherwise.
        #2. If search_node is not provided, the function returns a list containing the order in which the nodes were visited during the search.

    #Useful code snippets (not necessary but you can use if required)
    if search_node and start_node == search_node:
        return 1  # search node found

    visited = set()
    visited.add(start_node)
    queue = []
    queue.append(start_node)
    visited_nodes = []
    visited_nodes.append(start_node)
    while(len(queue)):
        c_node = queue.pop()
        if(c_node in graph.keys()):
            for node in graph[c_node].keys():
                if node == search_node:
                    return 1
                if node not in visited: 
                    visited.add(node)
                    visited_nodes.append(node)
                    queue.append(node)

    if search_node is not None:
        return 0  # search node not found

    return visited_nodes  # search node not provided, return entire path [list of nconst values of nodes visited]


def dfs(graph, start_node, visited=None, path=None, search_node=None):
    # graph: a dictionary representing the graph
    # start_node: the starting node for the search
    # visited: a set of visited nodes (optional, default is None)
    # path: a list of nodes in the current path (optional, default is None)
    # search_node: the node to search for (optional, default is None)

    # Note1: The optional parameters "visited" and "path" are initially not required to be passed as inputs but needs to be
            # updated recursively during the search implementation. If not required for your implementation purposes they can
            # be ignored and can be removed from the parameters.

    # Note2: If the given start_node belongs to one strongly connected component then the other nodes belong to that
           # particular component can only be traversed. But the nodes belonging to other components must not be traversed
           # if those nodes were not reachable from the given start_node.

    # The function returns:
        # 1. If search_node is provided, the function returns 1 if the node is found and 0 if it is not found.
        # 2. If search_node is not provided, the function returns a list containing the order in which the nodes were visited during the search.

    #Useful code snippets (not necessary but you can use if required)
    if start_node == search_node:
        return 1 # search node found
    
    if visited is None :
        visited = set()
    path = []
    def dfsHelper(c_node):
        visited.add(c_node)
        path.append(c_node)
        if(c_node == search_node):
            return 1
        if(c_node in graph.keys()):
            for node in graph[c_node].keys():
                if(node not in visited):
                    if dfsHelper(node) ==  1:
                        return 1

    if dfsHelper(start_node) ==  1:
        return 1
    
    if search_node is not None:
        return 0  # search node not found

    return path  # search node not provided, return entire path [list of nconst id's of nodes visited]



def dijkstra(graph, start_node, end_node):
    # graph: a dictionary representing the graph where the keys are the nodes and the values
            # are dictionaries representing the edges and their weights.
    # start_node: the starting node to begin the search.
    # end_node: the node that we want to reach.

    # Outputs:
        #1. If the end_node is not reachable from the start_node, the function returns 0.

        #2. If the end_node is reachable from the start_node, the function returns a list containing three elements:
                #2.1 The first element is a list representing the shortest path from start_node to end_node.
                     #[list of nconst values in the visited order]
                #2.2 The second element is the total distance of the shortest path.
                     #(summation of the distances or edge weights between minimum visited nodes)
                #2.3 The third element is Hop Count between start_node and end_node.
    
    def findMinNode(dist_map,visited):
        min = None
        min_node = None
        for node in dist_map:
            if min is None or (node not in visited and dist_map[node][1] <= min):
                min = dist_map[node][1]
                min_node = node
        return min_node

    if start_node == end_node:
        return [[start_node],0,0]
    # Return the shortest path and distances
    distance_map = {}
    for node in graph.keys():
        distance_map[node] = ([],float('inf'),0)
    distance_map[start_node] = ([start_node],0,0)
    visited = set()
    for i in range(0,len(graph.keys())-1):
        min_node = findMinNode(distance_map,visited)
        visited.add(min_node)
        if(min_node == end_node):
            break
        for node in graph[min_node].keys():
            weight = graph[min_node][node]
            if(distance_map[node][1] >= weight + distance_map[min_node][1]):
               distance_map[node] =  [distance_map[min_node][0] + [node],weight + distance_map[min_node][1],1 + distance_map[min_node][2]]

    return distance_map[end_node]




# (strongly connected components)
def kosaraju(graph):
    # graph: a dictionary representing the graph where the keys are the nodes and the values
            # are dictionaries representing the edges and their weights.
    #Note: Here you need to call dfs function multiple times so you can Implement seperate
         # kosaraju_dfs function if required.

    #The output:
        #list of strongly connected components in the graph,
          #where each component is a list of nodes. each component:[nconst2, nconst3, nconst8,...] -> list of nconst id's.

    def kosaraju_dfs(g,node,visited,stack):
        visited.add(node)
        for c_node in g[node].keys():
            if c_node not in visited:
                kosaraju_dfs(g,c_node,visited,stack)
        stack = stack.append(node)
    
    def transpose_graph():
        graph_t = {}
        for node in graph.keys():
            graph_t[node] = {}
        for node in graph.keys():
            for c_node in graph[node].keys():
                graph_t[c_node][node] = graph[node][c_node]
        return graph_t
    
    stack_g = []
    visited = set()
    for node in graph.keys():
        if node not in visited:
            kosaraju_dfs(graph,node,visited,stack_g)
    
    graph_t = transpose_graph()

    visited = set()
    components = []
    while len(stack_g) != 0:
        node = stack_g.pop()
        if node not in visited:
            component_arr = []
            kosaraju_dfs(graph_t,node,visited,component_arr)
            components.append(component_arr)
    
    return components
