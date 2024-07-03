def binary_search(search_list, search_item):
    search_list.sort()

    if len(search_list) == 0:
        return False

    midpoint = len(search_list) // 2

    if search_list[midpoint] == search_item:
        return True
    elif search_item < search_list[midpoint]:
        return binary_search(search_list[:midpoint], search_item)
    else:
        return binary_search(search_list[midpoint + 1:], search_item)

if __name__ == '__main__':

    lst = [12, 64, 23, 3, 57, 19, 1, 17, 51, 62]

    print("12 e' nella lista: ", binary_search(lst, 12))
    print("5 e' nella lista: ", binary_search(lst, 5))
    print("64 e' nella lista: ", binary_search(lst, 64))
    print("3 e' nella lista: ", binary_search(lst, 3))
    print("7 e' nella lista: ", binary_search(lst, 7))