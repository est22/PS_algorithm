# 버그왕
import re
import sys


bug_exist = True
p = sys.stdin.readline().rstrip()
while (bug_exist):
    m = re.sub(r'^BBUG*UBUG*G', '', str(m))
    # 다시 검사
    a = re.match("BUG", m)

    if a == None:
        bug_exist = False
        break



print(m)


