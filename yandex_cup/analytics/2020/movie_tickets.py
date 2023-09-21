import networkx as nx

FILE_PATH = 'data/logs.csv'

# edge weight - number of orders per (email, phone)
G = nx.Graph()
with open(FILE_PATH, 'r') as file:
    for line in file:
        email, phone = line.strip().split(',')
        email = email if email else phone
        phone = phone if phone else email
        if G.has_edge(email, phone):
            G[email][phone]['weight'] += 1
        else:
            G.add_edge(email, phone, weight=1)

connected_components = list(nx.connected_components(G))

# Find the component with the largest total weight of edges (maximum number of orders from 1 user)
largest_component = max(connected_components,
                        key=lambda comp: sum(weight for _, _, weight in G.subgraph(comp).edges(data='weight')))

largest_subgraph = G.subgraph(largest_component)

# Maximum number of orders
print(sum(weight for _, _, weight in largest_subgraph.edges(data='weight')))
