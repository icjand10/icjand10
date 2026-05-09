def wordprocessor(line, words):
    current_len = 0
    current_line = []

    for w in words:
        if current_len == 0:
            current_line.append(w)
            current_len = len(w)
        else:
            if current_len + len(w) <= line:
                current_line.append(w)
                current_len += len(w)
            else:
                print(" ".join(current_line))
                current_line = [w]
                current_len = len(w)

    print(" ".join(current_line))

print(wordprocessor(10,"Hello, this is bessie and this is my essay."))