def digit_value(ch):
    digits = '0123456789'
    i = 0
    while i < length(digits):
        if ch == digits[i]:
            return i
        i += 1
    return -1  

def digit_to_char(d):
    digits = '0123456789'
    i = 0
    while i < length(digits):
        if i == d:
            return digits[i]
        i += 1
    return '?' 

def to_int(s):
    num = 0
    i = 0
    negative = False
    if s[0] == '-':
        negative = True
        i = 1
    while i < length(s):
        num = num * 10 + digit_value(s[i])
        i += 1
    if negative:
        num = -num
    return num

def length(s):
    count = 0
    for _ in s:
        count += 1
    return count

def split_line(line, sep):
    result = []
    current = ''
    i = 0
    while i < length(line):
        if line[i] == sep:
            result.append(current)
            current = ''
        else:
            current += line[i]
        i += 1
    result.append(current)
    return result

def read_input(filename):
    f = open(filename, 'r')
    lines = []
    while True:
        line = f.readline()
        if line == '':
            break
        lines.append(line.strip())
    f.close()
    return lines

def write_output(filename, value):
    f = open(filename, 'w')
    f.write(str(value))
    f.close()

def build_graph(lines):
    graph = {}
    i = 1
    while i < length(lines):
        pair = split_line(lines[i], ',')
        u = to_int(pair[0])
        v = to_int(pair[1])
        if u not in graph:
            graph[u] = []
        graph[u].append(v)
        i += 1
    return graph

def bfs_min_depth(graph, root):
    queue = [(root, 1)]  # (node, depth)
    front = 0
    rear = 1
    while front < rear:
        node, depth = queue[front]
        front += 1
        if node not in graph:  # якщо лист
            return depth
        children = graph[node]
        j = 0
        while j < length(children):
            queue.append((children[j], depth + 1))
            rear += 1
            j += 1
    return 0

lines = read_input('C:/Users/User/Desktop/lab_5_main/input.txt')
root = to_int(lines[0])
graph = build_graph(lines)
min_depth = bfs_min_depth(graph, root)
write_output('C:/Users/User/Desktop/lab_5_main/output.txt', min_depth)