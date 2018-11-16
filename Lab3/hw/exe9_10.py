def get_even_list(l):
    elt = []
    for i in l:
        if i % 2 == 0:
            elt.append(i)
    return elt
e_lt = get_even_list([1, 2, 5, 9, -10, 6])

if set(e_lt) == set([2, -10, 6]):
    print("correct")
else:
    print("bugggggg")