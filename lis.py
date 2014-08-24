def lis(sequence):
    """Longest Increasing Subsequence 'LIS'

    A dynamic programming approach - O(n^2) complexity

    Returns all the LISs of a sequence
    """

    # elements at the beginning of sequences that are bigger than all other
    # elements can be removed
    if(len(sequence) > 1):
        while(max(sequence) == sequence[0]):
            if(len(sequence) > 0):
                del(sequence[0])

    # empty sequences and single element sequences are single LISs
    if(len(sequence) <= 1):
        return [sequence]

    all_lis = [[sequence[0]]]

    # construct an array of subsequences
    for idx, s in enumerate(sequence):
        for idy, l in enumerate(all_lis):
            endy = all_lis[idy][-1]
            if(s > endy):
                all_lis.append(all_lis[idy] + [s])

    # what is the LIS of these subsequences e.g. 6
    max_len = max(map(len, all_lis))

    # out of all the subsequences, which ones are LISs
    # in other words, which subsequences have the length of the LIS
    return [m for m in all_lis if len(m) == max_len]