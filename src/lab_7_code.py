def naive_search_last(haystack, needle):
    hay_len = 0
    for _ in haystack:
        hay_len += 1

    needle_len = 0
    for _ in needle:
        needle_len += 1

    last_index = -1
    comparisons = 0

    for i in range(hay_len - needle_len + 1):
        match = True
        for j in range(needle_len):
            comparisons += 1
            if haystack[i + j] != needle[j]:
                match = False
                break
        if match:
            last_index = i

    return last_index, comparisons

def read_input(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = []
        for line in f:
            lines.append(line.strip())
    haystack = ""
    needle = ""

    for line in lines:
        if line.startswith("haystack:"):
            haystack = line[len("haystack:"):].strip()
        elif line.startswith("needle:"):
            needle = line[len("needle:"):].strip()

    return haystack, needle

def write_output(filename, index, comparisons):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("Останній індекс входження: " + str(index) + "\n")
        f.write("Кількість порівнянь: " + str(comparisons) + "\n")

haystack, needle = read_input("C:/Users/User/Desktop/work/input_lab7.txt")
index, comparisons = naive_search_last(haystack, needle)
write_output("C:/Users/User/Desktop/work/output_lab7.txt", index, comparisons)
