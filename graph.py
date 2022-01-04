from collections import defaultdict
from copy import deepcopy

# Program to check if a graph is acyclic or cyclic. If acyclic then is it a tree. If tree what is its height

def parse_string(string):
    graph = defaultdict(set)
    nodes = set()
    if ';' in string:
        edges = string.split(";")
        for edge in edges:
            if ':' in edge:
                num_colons = edge.count(':')
                if num_colons > 1:
                    print(f"Syntax Error: More than one : found in edge {edge}")
                    exit()
                source = edge.split(':')[0]
                destinations = edge.split(':')[1]
                if ',' in destinations:
                    destinations = destinations.split(',')
                if len(source) == 0:
                    print(f"Syntax Error: No source for edge {edge}")
                    exit()
                if len(destinations) == 0:
                    print(f"Syntax Error: No destination for edge {edge}")
                    exit()
                source = int(source)
                nodes.add(source)
                if isinstance(destinations, list):
                    for des in destinations:
                        graph[source].add(int(des))
                        nodes.add(int(des))
                else:
                    graph[source].add(int(destinations))
                    nodes.add(int(destinations))
    elif ':' in string:
        num_colons = string.count(':')
        if num_colons > 1:
            print(f"Syntax Error: No ; in the string ({string}), yet multiple : found")
            exit()
        source = string.split(':')[0]
        dest = string.split(':')[1]
        if ',' in dest:
            destinations = dest.split(',')
        if len(source) == 0:
            print(f"Syntax Error: No source for edge")
            exit()
        if len(dest) == 0:
            print(f"Syntax Error: No destination for edge")
            exit()
        source = int(source)
        nodes.add(source)
        if isinstance(dest, list):
            for des in dest:
                graph[source].add(int(des))
                nodes.add(int(des))
        else:
            graph[source].add(int(dest))
            nodes.add(int(dest))
    else:
        print("Syntax Error: No ; or : in string")
        exit()

    return graph, nodes


def get_roots(graph, nodes):
    temp = deepcopy(nodes)
    for destinations in graph.values():
        for ver in destinations:
            if ver in temp:
                temp.remove(ver)
    return temp


def get_multipaths(graph):
    counts = defaultdict(int)
    multipaths = []
    for destinations in graph.values():
        for ver in destinations:
            counts[ver] += 1

    for node, count in counts.items():
        if count > 1:
            multipaths.append(node)

    return multipaths


def dfs(node, parent, graph, visited, stack):
    visited[node] = True
    stack.append(node)

    for child in graph[node]:
        if visited[child] is False:
            if dfs(child, node, graph=graph, visited=visited, stack=stack):
                return True
        else:
            if child in stack:
                stack.append(child)
                return True
    stack.pop()
    return False


def get_height(graph, root):
    if root is None:
        return 0
    h = 0
    for child in graph[root]:
        h = max(h, get_height(graph, child))
    return h+1


if __name__ == '__main__':
    graph_string_input = "5:11;7:11,8;3:8,10;11:2,9,10;8:9"         # src: dest1, dest2; src, dest
    graph, nodes = parse_string(graph_string_input)
    roots = get_roots(graph, nodes)
    multipaths = get_multipaths(graph)
    cyclic = False
    stack = []
    if len(roots):
        for node in roots:
            visited = dict.fromkeys(nodes, False)
            if dfs(node, -1, graph=graph, visited=visited, stack=stack):
                cyclic = True
                break
    else:
        visited = dict.fromkeys(nodes, False)
        sources = list(graph.keys())
        if dfs(sources[0], -1, graph=graph, visited=visited, stack=stack):
            cyclic = True
    if cyclic:
        stack = stack[::-1]
        index = -1
        for i in range(1, len(stack)):
            if stack[i] == stack[0]:
                index = i
                break
        stack = stack[:index]
        stack = stack[::-1]
        stack.append(stack[0])
        print(f"Cyclic graph with cycle: {stack} ")
    else:
        if len(roots) == 1 and len(multipaths) == 0:
            root = roots.pop()
            height = get_height(graph, root)
            print(f"Graph is Acyclic and has root at {root} and no multipaths. Therefore is a Tree with height: {height}")
        elif len(roots) > 1:
            print(f"Graph Acyclic and not tree as it has {len(roots)} roots: {roots}")
        else:
            print(f"Graph Acyclic and not tree as it has multipaths at: {multipaths}")
    print()