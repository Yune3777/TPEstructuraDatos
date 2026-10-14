from collections import deque  # Import deque for efficient queue operations

def bfs(arbol, start):
    visitado = [] 
    queue = deque([start])  # Initialize the queue with the starting node

    while queue:  # While there are still nodes to process
        node = queue.popleft()  # Dequeue a node from the front of the queue

        if node not in visitado:  # Check if the node has been visitado
            visitado.append(node)  # Mark the node as visitado
            print(node, end=" ")  # Output the visitado node

            # Enqueue all unvisitado neighbors (children) of the current node
            for neighbor in arbol[node]:
                if neighbor not in visitado:
                    queue.append(neighbor)  # Add unvisitado neighbors to the queue