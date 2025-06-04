class DSU:
    def __init__(self):
        self.people = []
        self.parent = []

    def find_index(self, x):
        for i in range(len(self.people)):
            if self.people[i] == x:
                return i
        return -1

    def find(self, x):
        idx = self.find_index(x)
        if idx == -1:
            self.people.append(x)
            self.parent.append(x)
            return x
        if self.parent[idx] != x:
            self.parent[idx] = self.find(self.parent[idx])
        return self.parent[idx]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        idx_x = self.find_index(rx)
        if idx_x != -1:
            self.parent[idx_x] = ry

def process_pairs(input_lines):
    n = int(input_lines[0])
    dsu = DSU()
    people = []

    for line in input_lines[1:n+1]:
        i = 0
        while i < len(line) and line[i] == ' ':
            i += 1
        num1 = ''
        while i < len(line) and line[i] != ' ':
            num1 += line[i]
            i += 1
        while i < len(line) and line[i] == ' ':
            i += 1
        num2 = ''
        while i < len(line):
            num2 += line[i]
            i += 1

        a = int(num1)
        b = int(num2)

        dsu.union(a, b)

        if a not in people:
            people.append(a)
        if b not in people:
            people.append(b)

    roots = []
    boys = []
    girls = []

    for person in people:
        root = dsu.find(person)

        found = False
        for i in range(len(roots)):
            if roots[i] == root:
                if person % 2 == 0:
                    girls[i] += 1
                else:
                    boys[i] += 1
                found = True
                break

        if not found:
            roots.append(root)
            if person % 2 == 0:
                girls.append(1)
                boys.append(0)
            else:
                girls.append(0)
                boys.append(1)

    total_boys = 0
    total_girls = 0

    for b in boys:
        total_boys += b
    for g in girls:
        total_girls += g

    result = 0
    for i in range(len(roots)):
        result += boys[i] * (total_girls - girls[i])
        result += girls[i] * (total_boys - boys[i])

    return result // 2
