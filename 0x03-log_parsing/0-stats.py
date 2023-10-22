#!/usr/bin/python3
"""Log parsing"""


import sys


def print_stats(status_codes, file_size):
    """Prints the stats"""
    print("File size: {}".format(file_size))
    for key in sorted(status_codes.keys()):
        if status_codes[key] > 0:
            print("{}: {}".format(key, status_codes[key]))


status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
file_size = 0
count = 0
try:
    for line in sys.stdin:
        count += 1
        data = line.split()
        try:
            file_size += int(data[-1])
        except ValueError:
            pass
        try:
            status_codes[data[-2]] += 1
        except KeyError:
            pass
        if count == 10:
            print_stats(status_codes, file_size)
            count = 0
    print_stats(status_codes, file_size)
except KeyboardInterrupt:
    print_stats(status_codes, file_size)
    raise
