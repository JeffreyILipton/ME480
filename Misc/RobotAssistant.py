#!/usr/bin/env python3
import sys

if __name__ == '__main__':
	print("Booting")
	for line in sys.stdin:
		print(f' I will order {line}')
