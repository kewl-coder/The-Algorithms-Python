from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, node, visited):
        visited[node] = True
        print(node, end=' ')

        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

    def dfs_traversal(self, start_node):
        visited = [False] * (max(self.graph) + 1)
        self.dfs(start_node, visited)

# Example usage:
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("DFS traversal starting from node 0:")
    g.dfs_traversal(0)
