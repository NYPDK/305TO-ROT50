import string

def rot(text):
    n_a = dict(enumerate(string.printable))
    a_n = {v: k for k, v in n_a.items()}
    new_word = []
    for x in text:
        if x in a_n:
            num = a_n[x] - len(n_a) // 2
            if num < 0:
                num += len(n_a)
            new_word.append(n_a[num])
        else:
            new_word.append(x)
    return "".join(new_word)

if __name__ == "__main__":
    while True:
        print("Output:", rot(input("Text: ")))
