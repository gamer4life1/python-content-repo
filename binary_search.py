def binary_search_recursive(a_list, item, first, last):
    if first == last:
        if item == a_list[first]:
            return first
        else:
            return -1
    else:
        i = int((first + last) / 2)
        if item == a_list[i]:
            return i
        else:
            if a_list[i] < item:
                return binary_search_recursive(a_list, item, i+1, last)
            else:
                return binary_search_recursive(a_list, item, first, i)
