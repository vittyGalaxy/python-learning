if __name__ == '__main__':
    def merge_sort(lst):

        if len(lst) <= 1:
            return lst

        else:
            punto_medio = len(lst) // 2

            sinistra = merge_sort(lst[:punto_medio])
            destra = merge_sort(lst[punto_medio:])

            nuova_lista = []
            while len(sinistra) and len(destra) > 0:

                if sinistra[0] < destra[0]:
                    nuova_lista.append(sinistra[0])
                    del sinistra[0]

                else:
                    nuova_lista.append(destra[0])
                    del destra[0]

            nuova_lista.extend(sinistra)
            nuova_lista.extend(destra)

            return nuova_lista

    print(merge_sort([2, 5, 3, 8, 6, 9, 1, 4, 7]))