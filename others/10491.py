# quite a problem
import sys

for line in sys.stdin:
    line = line.rstrip().lower()

    if 'problem' in line:
        print('yes')
    else:
        print('no')


