from collections import defaultdict

dd = defaultdict(int)

for i in range(29):
    dd[input()] += 1

for key, val in print(sorted(dd.items())):
    print(key, val/ 29 * 100)