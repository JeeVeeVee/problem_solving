class node:
    def __init__(self, index):
        self.index = index
        self.reachable_nodes = [self]

    def add_new_reachable_node(self, node):
        self.reachable_nodes.append(node)

    def __repr__(self):
        return "node " + str(self.index)

    def __eq__(self, other):
        return other.index == self.index

    def __hash__(self):
        return self.index

def generate_nodes(n):
    output = []
    for i in range(0, n):
        output.append(node(i + 1))
    return output

def read_edge(raw_input):
    index_node_1 = int(raw_input[0]) - 1
    index_node_2 = int(raw_input[1]) - 1
    all_nodes[index_node_1].add_new_reachable_node(all_nodes[index_node_2])
    all_nodes[index_node_2].add_new_reachable_node(all_nodes[index_node_1])

def read_query():
    size = int(input())
    values = input().split(" ")
    for i in range(size):
        values[i] = int(values[i])
    return values

def shortest_path_length(a, b):
    node_a = all_nodes[a - 1]
    node_b =  all_nodes[b - 1]
    reached_nodes = [node_a]
    output = 0
    while node_b not in reached_nodes:
        new_reached_nodes = []
        for n in reached_nodes:
            for reached_node in n.reachable_nodes:
                new_reached_nodes.append(reached_node)
        output += 1
        reached_nodes = list(set(new_reached_nodes))
    return output

def handle_duo(a , b):
    return a * b * shortest_path_length(a, b)

def handle_querie(querie):
    if len(querie) < 2:
        print(0)
        return
    querys = [[querie[i], querie[j]] for i in range(len(querie)) for j in range(i + 1, len(querie))]
    output = 0
    for duo in querys:
        output += handle_duo(duo[0], duo[1])
    print(output % 1000000007)



n_and_q = input().split(" ")
n = int(n_and_q[0])
q = int(n_and_q[1])
all_queries = []
all_nodes = generate_nodes(n)
for i in range(n - 1):
    new_edge = input().split(" ")
    read_edge(new_edge)
for i in range(q):
    all_queries.append(read_query())

for querie in all_queries:
    handle_querie(querie)



