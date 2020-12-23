def merge_sorted_arrays(a1, a2):  # a1 - array1, a2 - array2

    if type(a1) and type(a2) not in (tuple, list):
        raise TypeError('Only tuples and lists are allowed')
    if type(a1) is not type(a2):
        raise TypeError('Input collections must be same type')
    if len(a1) is 0 or len(a2) is 0:
        raise ValueError('Input collections cannot be empty')

    try:
        if (min(a1) is a1[0]) and (max(a1) is a1[len(a1) - 1]):  # a1 ordered by asc
            pass
        else:  # a1 ordered by desc
            a1.reverse()
        if (min(a2) is a2[0]) and (max(a2) is a2[len(a2) - 1]):  # a2 ordered by asc
            pass
        else:  # a2 ordered by desc
            a2.reverse()
    except TypeError as e:
        raise ValueError('Only integer and float values are allowed') from e

    if a1[-1] > a2[-1]:  # comparing last element's values
        if a2[-1] < a1[0]:  # no sort needed, a1 complements a2
            return a2 + a1
    else:
        if a1[-1] < a2[0]:  # no sort needed, a2 complements a1
            return a1 + a2

    res = []
    a1_iterator = 0
    a2_iterator = 0

    while (a1_iterator != len(a1)) and (a2_iterator != len(a2)):

        if a1[a1_iterator] < a2[a2_iterator]:
            res.append(a1[a1_iterator])
            a1_iterator = a1_iterator + 1
        else:
            res.append(a2[a2_iterator])
            a2_iterator = a2_iterator + 1

    if len(res) < len(a1 + a2):  # part of elements are not in resulting array (one given array is larger than other)

        if len(a1) > a1_iterator:  # a1 is larger than a2
            [res.append(element) for element in a1[a1_iterator:]]  # appending a1's remainder to resulting array
            '''list comprehension used to append elements 
            one by one as single elements (not as list of elements)'''
        elif len(a2) > a2_iterator:  # a2 is larger than a1
            [res.append(element) for element in a2[a2_iterator:]]  # appending a2's remainder to resulting array

        if len(res) == len(a1 + a2):  # all elements on its own place
            if type(a1) is tuple and type(a2) is tuple:
                return tuple(res)
            return res

    else:  # all elements are on their own place
        if type(a1) is tuple and type(a1) is tuple:
            return tuple(res)
        return res
