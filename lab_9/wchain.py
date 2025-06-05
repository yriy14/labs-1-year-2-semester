def read_words(filename):
    f = open(filename, "r")
    n_line = f.readline()
    n = 0
    for ch in n_line:
        if ch >= '0' and ch <= '9':
            n = n * 10 + (ord(ch) - ord('0'))

    words = []
    count = 0
    while count < n:
        line = f.readline()
        word = ""
        for ch in line:
            if ch >= 'a' and ch <= 'z':
                word += ch
        words.append(word)
        count += 1
    f.close()
    return words

def radix_sort_by_length(words):
    max_len = 0
    i = 0
    while i < len(words):
        length = 0
        while True:
            try:
                _ = words[i][length]
                length += 1
            except IndexError:
                break
        if length > max_len:
            max_len = length
        i += 1

    count = [0] * (max_len + 1)
    i = 0
    while i < len(words):
        length = 0
        while True:
            try:
                _ = words[i][length]
                length += 1
            except IndexError:
                break
        count[length] += 1
        i += 1
    j = 1
    while j <= max_len:
        count[j] = count[j] + count[j - 1]
        j += 1

    output = [None] * len(words)
    i = len(words) - 1
    while i >= 0:
        length = 0
        while True:
            try:
                _ = words[i][length]
                length += 1
            except IndexError:
                break
        count[length] -= 1
        output[count[length]] = words[i]
        i -= 1

    i = 0
    while i < len(words):
        words[i] = output[i]
        i += 1

def build_chain(words):
    word_dict = {}
    i = 0
    while i < len(words):
        word_dict[words[i]] = 0
        i += 1

    radix_sort_by_length(words)

    max_chain = 1
    i = 0
    while i < len(words):
        current_word = words[i]
        best = 1
        j = 0
        length = 0
        while True:
            try:
                _ = current_word[length]
                length += 1
            except IndexError:
                break

        while j < length:
            smaller = ""
            k = 0
            while k < length:
                if k != j:
                    smaller += current_word[k]
                k += 1
            if smaller in word_dict:
                if word_dict[smaller] + 1 > best:
                    best = word_dict[smaller] + 1
            j += 1
        word_dict[current_word] = best
        if best > max_chain:
            max_chain = best
        i += 1
    return max_chain

def write_result(filename, result):
    f = open(filename, "w")
    f.write(str(result))
    f.close()

def main():
    words = read_words("lab_9/wchain.in.txt")
    result = build_chain(words)
    write_result("lab_9/wchain.out.txt", result)

if __name__ == "__main__":
    main()
