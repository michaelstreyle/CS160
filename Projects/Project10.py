'''

Kevin Bacon Project (10)

Michael Streyle
11/30/18

'''
import heapq
import sys

class Queue:
    '''Implementing Queue ADT as a list'''
    def __init__(self):
        '''Initialize an instance'''
        self.items = []
    def is_empty(self):
        '''is the Queue empty'''
        return self.items == []
    def enqueue(self, item):
        '''Add an item'''
        self.items.insert(0, item)
    def dequeue(self):
        '''Remove an item'''
        return self.items.pop()
    def size(self):
        '''How big is it?'''
        return len(self.items)
    def look(self):
        return self.items

class Vertex:
    """Graph vertex"""
    def __init__(self, key):
        """Graph constructor"""
        self._key = key
        self._neighbors = {}
        self._distance = sys.maxsize
        self._previous = None
        self._color = "white"
        self._discovered = 0
        self._colored = 0
    def get_key(self):
        """Get node key"""
        return self._key
    key = property(get_key)
    def get_neighbor(self, other: str):
        """Get one adjacent node (neighbor)"""
        return self._neighbors.get(other, None)
    def set_neighbor(self, other: str, weight: int = 0):
        """Add neighbor"""
        self._neighbors[other] = weight
    neighbor = property(get_neighbor, set_neighbor)
    def get_all_neighbors(self):
        """Get all adjacent nodes (neighbors)"""
        return self._neighbors.keys()
    all_neighbors = property(get_all_neighbors)
    def get_distance(self):
        """Get distance"""
        return self._distance
    def set_distance(self, distance: int):
        """Set distance"""
        self._distance = distance
    distance = property(get_distance, set_distance)
    def get_previous(self):
        """Get previous"""
        return self._previous
    def set_previous(self, previous):
        """Set previous"""
        self._previous = previous
    previous = property(get_previous, set_previous)
    def get_color(self):
        """Get color"""
        return self._color
    def set_color(self, color: str):
        """Get color"""
        self._color = color
    color = property(get_color, set_color)
    def get_discovery(self):
        """Get discovery time"""
        return self._discovered
    def set_discovery(self, t):
        """Set discovery time"""
        self._discovered = t
    discovered = property(get_discovery, set_discovery)
    def get_finish(self):
        """Get finish time"""
        return self._colored
    def set_finish(self, t):
        """Set finish time"""
        self._colored = t
    finished = property(get_finish, set_finish)
    def get_weight(self, other):
        """Get edge weight"""
        return self._neighbors[other]
    def __str__(self):
        """Print a vertex"""
        return (
            "Neighbors of "+ str(self._key)+ ": "+ str([x.key for x in self._neighbors]))
    def __lt__(self, other):
        return self._key < other.key

class Graph:
    """Graph class"""

    def __init__(self):
        """Create a new, empty graph"""
        self.vertices = {}
        self.time = 0
        self.num_edges = 0
    def add_vertex(self, key: str):
        """Add an instance of Vertex to the graph"""
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex
    def add_edge(self, from_vertex: str, to_vertex: str, weight=0):
        """Add a new, weighted, directed edge to the graph that connects two vertices"""
        if from_vertex not in self.vertices:
            self.add_vertex(from_vertex)
        if to_vertex not in self.vertices:
            self.add_vertex(to_vertex)
        self.vertices[from_vertex].set_neighbor(self.vertices[to_vertex], weight)
        self.num_edges +=1
    def get_vertex(self, key: str):
        """Find the vertex in the graph named vert_key"""
        return self.vertices.get(key, None)
    def get_vertices(self):
        """Return the list of all vertices in the graph"""
        return self.vertices.keys()
    def reset_distances(self):
        """Reset distances to test Dijkstra's"""
        for v in self:
            v.set_distance(sys.maxsize)
    def __contains__(self, key: str):
        """Return True for a statement of the form vertex in graph, if the given vertex is in the graph, False otherwise"""
        return key in self.vertices
    def __iter__(self):
        """Iterator"""
        return iter(self.vertices.values())
    def __len__(self):
        """Graph's size"""
        return len(self.get_vertices())
    def hub(self):
        """Find a Vertex with the most outgoing edges"""
        li = {}
        for x in self.__iter__():
            li[x] = len(x.all_neighbors)
        m = max(li, key=li.get)
        return str(m.get_key())
    def size(self):
        """Find the number of edges in a Graph"""
        return self.num_edges//2


def build(filename):
    g = Graph()
    infile = open(filename)
    movie_dict = {}
    for line in infile:
        line = line.rstrip()
        line_list = line.split('|')
        if line_list[0] != 'title':
            movie = line_list[0]
            actor = line_list[1]
            if movie not in movie_dict:
                movie_dict[movie] = []
                movie_dict[movie].append(actor)
            else:
                movie_dict[movie].append(actor)
    for movie in movie_dict.keys():
        for x in movie_dict[movie]:
            for y in movie_dict[movie]:
                if x!=y:
                    g.add_edge(x, y, movie)
    return g


def bfs(g,start):
    start.set_distance(0)
    start.set_previous(None)
    vertq = Queue()
    vertq.enqueue(start)
    while (vertq.size() > 0):
        cur_vert = vertq.dequeue()
        for n in cur_vert.get_all_neighbors():
            if (n.get_color() == 'white'):
                n.set_color('gray')
                n.set_distance(cur_vert.get_distance() + 1)
                n.set_previous(cur_vert)
                vertq.enqueue(n)
            cur_vert.set_color('black')
    return vertq


def traverse(y, info: list):
    levels = 0
    x = y
    while (x.get_previous()):
        info.append([x.get_key(), 'acted with', x.get_previous().get_key(), 'in', x.get_weight(x.get_previous())])
        x = x.get_previous()
        levels +=1
    info.append(x.get_key())
    info.append(levels)
    return info

    
    
def main():
    print('building the actor graph...')
    graph = build('movie_actors_full.txt')
    find = input('What actor would you like to trace? (type "exit" to quit) \n')
    print('---------------------------------------')
    
    while find != 'exit':
        try:
            bfs(graph, graph.get_vertex('Kevin Bacon'))
            info = [] 
            traverse(graph.get_vertex(find), info) 
            print('The Kevin Bacon Number for  {}  is {}'.format(find, info[-1]))
            for i in range(-2-info[-1], (-2-info[-1]) + info[-1]):
                print(*info[i])
            find = input('What actor would you like to trace? (type "exit" to quit) \n')
            print('---------------------------------------')
        except:        
            print(find + ' is not connected to Kevin Bacon.')
            find = input('What actor would you like to trace? (type "exit" to quit) \n')
            print('---------------------------------------')


main()
