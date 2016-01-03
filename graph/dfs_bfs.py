import Queue 
class Graph(object):
    def __init__(self):
        self.adjacents = {}
        self.nedges = 0
    def add_edge(self,v,w):
        if v not in self.adjacents:
            self.adjacents[v] = []
        self.adjacents[v].append(w)


        self.nedges = self.nedges + 1

    def adjacent(self,v):
        return self.adjacents[v]

    def print_adjacents(self):
        print(self.adjacents)

    def num_vertices(self):
        return self.adjacents.keys()


def _dfs(node, adjacents, visited):
    if node not in visited:
        visited.append(node)
        if node in adjacents.keys():
            for child in adjacents[node]:
                _dfs(child, adjacents, visited)


def _bfs(start, adjacents):
    visited = set()
    visited.add(start)
    q = Queue.Queue()
    q.put(start)
    while not q.empty():
        current = q.get()
        for nodes in adjacents[current]:
            if nodes not in visited:
                q.put(nodes)
                visited.add(nodes)
    return visited            


def main():
    graph = Graph()
    visited = []
    graph.add_edge(0,1)
    graph.add_edge(0,2)
    graph.add_edge(1,2)
    graph.add_edge(2,0)
    graph.add_edge(2,3)
    graph.add_edge(3,3)
    

    print('------Graph Adjacency List--------')
    print(graph.adjacents)
    print('----------DFS-----------')
    _dfs(2,graph.adjacents, visited)
    print(visited)
    print('-----------BFS-----------')
    visited = _bfs(0, graph.adjacents)
    print(visited)




main()
