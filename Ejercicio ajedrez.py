import math
import os
import random
import re
import sys

def torresverticales(t1, t2):
    xor= 0
    for v1,v2 in zip(t1,t2):
        xor ^= abs(v1-v2) - 1
    print ("player-2" if xor != 0 else "player-1")

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "ayuda.txt"
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
    r1 = []
    for _ in range(n):
        r1_item = int(input().strip())
        r1.append(r1_item)
    r2 = []
    for _ in range(n):
        r2_item = int(input().strip())
        r2.append(r2_item)
    result = torresverticales(r1, r2)
    fptr.write(result + '\n')
    fptr.close()