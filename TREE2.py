# problem can be found at
# https://codechef.com/problems/TREE2

import sys
answer = []
for i in range(int(input())):
    temp = int(input())
    sticks = set(map(int, input().split()))
    sticks = sticks.difference({0})
    answer.append(len(sticks))
print(*answer, sep='\n')
