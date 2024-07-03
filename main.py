if __name__ == '__main__':
    def bubble_sort(lst):

        scambio_necessario = True

        while scambio_necessario:

            scambio_necessario = False

            for i in range(len(lst) - 1):

                if lst[i] > lst[i + 1]:

                    temp = lst[i]

                    lst[i] = lst[i + 1]

                    lst[i + 1] = temp

                    bubble_sort(lst)

        return lst

    print(bubble_sort([34, 16, 2, 78, 4, 6, 1]))