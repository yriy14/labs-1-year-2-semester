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


def build_chain(words):
    word_dict = {}
    for i in range(len(words)):
        word_dict[words[i]] = 0

    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) > len(words[j]):
                temp = words[i]
                words[i] = words[j]
                words[j] = temp

    max_chain = 1
    for i in range(len(words)):
        current_word = words[i]
        best = 1
        j = 0
        while j < len(current_word):
            smaller = ""
            k = 0
            while k < len(current_word):
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
    return max_chain

def write_result(filename, result):
    f = open(filename, "w")
    f.write(str(result))
    f.close()


def main():
    words = read_words("C:/Users/Admin/OneDrive/Desktop/lab_9/wchain.in.txt")
    result = build_chain(words)
    write_result("C:/Users/Admin/OneDrive/Desktop/lab_9/wchain.out.txt", result)


if __name__ == "__main__":
    main()
