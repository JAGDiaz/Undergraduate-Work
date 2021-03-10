#! /usr/bin/python3

import numpy as np

def minAVLtree(h):
	if h == 0:
		return 1
	elif h == 1:
		return 2
	return 1 + minAVLtree(h - 1) + minAVLtree(h-2)

def maxAVLtree(h):
	if h == 0:
		return 1
	return 1 + 2*maxAVLtree(h - 1)

def minFulltree(h):
	if h == 0:
		return 1
	return 2 + minFulltree(h - 1)


print(minAVLtree(5))
print(maxAVLtree(5))


print(minFulltree(6))
