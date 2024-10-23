
Grapg = {
    'A' : ['B','D'],
    'B' : ['A','C','E'],
    'C' : ['B','E'],
    'D' : ['A','E'],
    'E' : ['C','D','F'],
    'F' : ['E']

}

visited = set()
queue = []

def BFRS(visited,graph,node):
    visited.add(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end="")

        for i in graph[m]:
            if i not in visited:
                visited.add(i)
                queue.append(i)

BFRS(visited,Grapg,'C')