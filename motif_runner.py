from addax.data_structures.graph import Graph
from addax.kavosh.enumerate import EnumerateSubgraphsSequentially
from addax.kavosh.classify import ClassifySubgraph, ParseCertificate
import json

def main():
    
    #-----Import edgelist and convert-----#
    
    # TODO changed when we get API change
    print("Importing edgelist and converting")

    with open("./edge_list.json","r") as f:
        edge_list = json.load(f)
    
    int_edge_list = [[int(a), int(b)] for [a,b,c] in edge_list]
    nodes = set()
    
    # getting rid of self loops 
    for index, i in enumerate(int_edge_list):
        if i[0] == i[1]:
            int_edge_list.pop(index)

    for edge in int_edge_list:
        nodes.add(edge[0])
        nodes.add(edge[1])
    

    #-----Instantiate Graph-----#

    print("Instantiate graph")

    g = Graph("connectome", True)

    for node in nodes:
        g.AddVertex(node)

    for edge in int_edge_list:
        g.AddEdge(edge[0], edge[1])


    #-----Generate Subgraphs-----#
    
    # TODO change when we get API change
    print("Generate Subgraphs")

    motif_generator = EnumerateSubgraphsSequentially(g,3)
    
    subgraph_stuctures = []
    for subgraph in motif_generator:
        certificate = ClassifySubgraph(g, subgraph, 3)
        subgraph_type = ParseCertificate(3, certificate, True)
        subgraph_stuctures.append((subgraph_type, subgraph))
    
    subgraphs_edge_list = [(i[0].edge_set, i[1]) for i in subgraph_stuctures]

    print("Subgraphs: \n")


    #-----Find frequency of subgraphs-----#    

    key_subgraph_tuple = tuple([tuple(i[0]) for i in subgraphs_edge_list])

    motif_freq = {}

    for i in key_subgraph_tuple:

        if i in motif_freq:
            motif_freq[i] += 1
        else:
            motif_freq[i] = 1

    for i in motif_freq.items():
        print(i[0])
        print(i[1])
        print("\n")

if __name__ == "__main__":
    main()
    
