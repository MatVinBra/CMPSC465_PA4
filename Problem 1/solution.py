#Matthew Brady (mvb5936), Arman Fatehi (aff5276), Matthew Balogh (mjb6723)
class Graph:
    def __init__(self,vertices,edge_num,source):
        self.V_count = vertices # number of vertices in graph
        self.E_count = edge_num # number of vertices in graph
        self.edges = [] #list of graph's edges
        self.source = source 

    def add_edge(self,a,b,c):
        #add edge
        self.edges.append([a,b,c])

    def BelmanFord(self):
        distance = [float('inf')] * self.V_count
        prev = [None]*self.V_count
        distance[self.source-1] = 0
    
        for x in range(self.V_count-1):
            for a,b,c in self.edges:
                if distance[a-1] != float("inf") and distance[a-1] + c < distance[b-1]:
                    distance[b-1] = distance[a-1] + c
                    prev[b-1] = a

        #Check negative cycles
        for a,b,c in self.edges:
            if distance[a-1] != float("inf") and distance[a-1] + c < distance[b-1]:
                return True
        return False

line1 = input().split()
vertices = int(line1[0])  #number of vertices from input   
edges = int(line1[1])     #number of edges python ./solution.py < input-x.txt > my-output-x.txtfrom input
source = int(line1[2])    #source vertex from input

Main_graph = Graph(vertices,edges,source)

x = 1
while x <= edges:
    edge = input().split()
    Main_graph.add_edge(int(edge[0]),int(edge[1]),int(edge[2]))
    x+=1

print(Main_graph.BelmanFord())