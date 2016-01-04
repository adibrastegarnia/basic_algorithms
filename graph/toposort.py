class Graph(object):
    def __init__(self):
        self.adjacents = {}
        self.nedges = 0

    def add_edge(self, v, w):
        if v not in self.adjacents:
            self.adjacents[v] = []
        if w not in self.adjacents:
            self.adjacents[w] = []
        self.adjacents[v].append(w)

        self.nedges = self.nedges + 1

    def print_adjacents(self):
        print(self.adjacents)

    def adjacent(self,v):
        return self.adjacents[v]
    def vertices(self):
        return self.adjacents.keys()


def _toposort(node, visited, adjacents,stack):
    if node not in visited:
        visited.add(node)
        if node in adjacents.keys():
            for child in adjacents[node]:  
                  _toposort(child, visited, adjacents, stack)
            stack.append(node)

    return stack






def main():
    graph = Graph()
    visited = set()
    stack = []
    """
    graph.add_edge(0,5)
    graph.add_edge(0,1)
    graph.add_edge(0,2)
    graph.add_edge(1,4)
    graph.add_edge(3,5)
    graph.add_edge(3,6)
    graph.add_edge(3,4)
    graph.add_edge(3,2)
    graph.add_edge(5,2)
    graph.add_edge(6,0)
    graph.add_edge(6,4)
    """
    """
    graph.add_edge(0,3)
    graph.add_edge(0,4)
    graph.add_edge(1,2)
    graph.add_edge(1,3)
    graph.add_edge(2,4)
    graph.add_edge(3,5)
    graph.add_edge(3,7)
    graph.add_edge(4,7)
    graph.add_edge(5,6)
    """
    """
     
    graph.add_edge(0,1)
    graph.add_edge(0,3)
    graph.add_edge(1,2)
    graph.add_edge(1,6)
    graph.add_edge(3,7)
    graph.add_edge(4,6)
    graph.add_edge(5,7)

    """
    ## 5 4 2 3 1 0
    """
    graph.add_edge(5,2)
    graph.add_edge(5,0)
    graph.add_edge(4,0)
    graph.add_edge(4,1)
    graph.add_edge(2,3)
    graph.add_edge(3,1)
    """
    graph.add_edge(1,2)
    graph.add_edge(2,3)
    graph.add_edge(3,4)
    graph.add_edge(4,5)
    vertices = graph.vertices()
    
    for v in vertices:
     if v not in visited:
        _toposort(v,visited, graph.adjacents,stack)
    print(stack[::-1])

main()
