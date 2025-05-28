def parse_line(line):
    parts = []
    part = ''
    for ch in line:
        if ch == ',' or ch == '\n':
            parts.append(part)
            part = ''
        else:
            part += ch
    if part != '':
        parts.append(part)
    return parts

def to_int(s):
    result = 0
    for ch in s:
        result = result * 10 + (ord(ch) - ord('0'))
    return result

def read_graph_from_txt(filename):
    file = open(filename, "r")
    lines = []
    while True:
        line = file.readline()
        if line == '':
            break
        lines.append(line)
    file.close()

    farms = parse_line(lines[0])
    shops = parse_line(lines[1])

    capacity = {}
    for i in range(2, len(lines)):
        parts = parse_line(lines[i])
        u, v, c = parts[0], parts[1], to_int(parts[2])
        if u not in capacity:
            capacity[u] = {}
        if v not in capacity[u]:
            capacity[u][v] = 0
        capacity[u][v] += c

    return farms, shops, capacity


def bfs(capacity, flow, source, sink, parent):
    visited = {}
    queue = [source]
    visited[source] = True

    found = False
    while len(queue) > 0:
        u = queue[0]
        queue = queue[1:]

        if u in capacity:
            for v in capacity[u]:
                residual = capacity[u][v] - (flow[u][v] if u in flow and v in flow[u] else 0)
                if v not in visited and residual > 0:
                    parent[v] = u
                    visited[v] = True
                    if v == sink:
                        found = True
                        break
                    queue.append(v)
        if found:
            break
    return found

def min_val(a, b):
    if a < b:
        return a
    return b

def max_flow(farms, shops, capacity):
    flow = {}
    source = "SRC"
    sink = "SNK"

    # Додаємо штучне джерело
    for f in farms:
        if source not in capacity:
            capacity[source] = {}
        capacity[source][f] = 1000000000  # псевдо-безкінечність

    # Додаємо штучний стік
    for s in shops:
        if s not in capacity:
            capacity[s] = {}
        capacity[s][sink] = 1000000000

    total_flow = 0

    while True:
        parent = {}
        if not bfs(capacity, flow, source, sink, parent):
            break

        # Знаходимо мінімальний шляховий потік
        path_flow = 1000000000
        cur = sink
        while cur != source:
            prev = parent[cur]
            available = capacity[prev][cur] - (flow[prev][cur] if prev in flow and cur in flow[prev] else 0)
            path_flow = min_val(path_flow, available)
            cur = prev

        # Оновлюємо потоки
        cur = sink
        while cur != source:
            prev = parent[cur]
            if prev not in flow:
                flow[prev] = {}
            if cur not in flow[prev]:
                flow[prev][cur] = 0
            flow[prev][cur] += path_flow

            if cur not in flow:
                flow[cur] = {}
            if prev not in flow[cur]:
                flow[cur][prev] = 0
            flow[cur][prev] -= path_flow
            cur = prev

        total_flow += path_flow

    return total_flow
