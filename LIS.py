#
# Longest Increasing Subsequence
# A dynamic programming approach
#
# O(n^2) complexity
#

sequence = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

all_lis = [[sequence[0]]]
for idx, s in enumerate(sequence):
	endx = sequence[idx]
	for idy, l in enumerate(all_lis):
		endy = all_lis[idy][-1]
		if(s > endy):
			all_lis.append(all_lis[idy] + [s])

max_len = max(map(len, all_lis))
print [m for m in all_lis if len(m) == max_len]