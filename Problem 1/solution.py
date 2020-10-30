
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

        distance[self.source] = 0

        for i in range(self.V_count - 1):
            for a,b,c in self.edges:
                if distance[a] != float('inf') and distance[a] + c < distance[b]:
                    distance[b] = distance[a] + c


        for a,b,c in self.edges:
            if distance[a] != float("inf") and distance[a] + c < distance[b]:
                print('NG Found')
                return False
            return True

# line1 = input().split()
# vertices = int(line1[0])  #number of vertices from input   
# edges = int(line1[1])     #number of edges python ./solution.py < input-x.txt > my-output-x.txtfrom input
# source = int(line1[2])    #source vertex from input

Main_graph = Graph(4,6,3)
# x = 1
# while x <= edges:
#     edge = input().split()
#     Main_graph.add_edge(int(edge[0]),int(edge[1]),int(edge[2]))
#     x+=1

Main_graph.add_edge(3 ,1 ,-2)
Main_graph.add_edge(1 ,4 ,8)
Main_graph.add_edge(1, 2, 0)
Main_graph.add_edge(3, 4, -9)
Main_graph.add_edge(3, 2, -10)
Main_graph.add_edge(4, 3, 4)

print(Main_graph.BelmanFord())