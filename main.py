def search(a, c):
    risult = []

    for word in a:
        if word[0] == c:
            risult.append(word)

    return risult

if __name__ == '__main__':

    b = ["Hello", "World!"]
    print(search(b, "H"))
    print(search(b, "W"))