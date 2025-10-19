def reverse_sort_dictionary(input):
    returnList = []
    for key, value in input.items():
        tupleValue = (key, value[0])
        returnList.append(tupleValue)
    returnList.sort(reverse=True)
    return returnList

