#! /usr/bin/python3

import numpy as np

elements = [33, 10, 9, 13, 12, 45, 26, 17]
ra = np.full([12], np.nan)
def hash_code(k):
	return abs(3-(k%12))

for i in elements:
	index = hash_code(i)
	j = 0
	while(not np.isnan(ra[index])):
		index += 1
		index %= ra.shape[0]
		j += 1

	ra[index] = i

print(ra)



