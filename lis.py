#
# Longest Increasing Subsequence
# A dynamic programming approach
#
# O(n^2) complexity
#

def lis(sequence):
    all_lis = [[sequence[0]]]
    for idx, s in enumerate(sequence):
        endx = sequence[idx]
        for idy, l in enumerate(all_lis):
            endy = all_lis[idy][-1]
            if(s > endy):
                all_lis.append(all_lis[idy] + [s])

    max_len = max(map(len, all_lis))
    return [m for m in all_lis if len(m) == max_len]