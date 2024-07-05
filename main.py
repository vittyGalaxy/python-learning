def word_length(a):
    result = []

    for i in a:
        content = len(i)
        result.append(content)

    return result

if __name__ == '__main__':

    b = ["Hello", "World!"]
    print(word_length(b))