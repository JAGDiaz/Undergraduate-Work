#! /usr/bin/python3

import re

number = "619-594-1668"
p1 = re.compile(r"(-\d)")
p2 = re.compile(r"(\d{3}-){2}")

print(p1.match(number))
print(p2.match(number))
