def merge_list (list1, list2):
    listWhole = list1 + list2

    length = len(listWhole)

    for i in range(1, length):
        key = listWhole[i]
        j = i - 1

        
        while j >= 0 and key < listWhole[j]:
            listWhole[j + 1] = listWhole[j]
            j -= 1

        listWhole[j + 1] = key

    return listWhole

