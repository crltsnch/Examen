# Examen
Mi dirección de  GitHub para estre repositorio es el siguiente: 
https://github.com/crltsnch/Examen.git
Hemos resuelto el juego de ajedrez de la UAX y el juego The Minion Game. Su código es:


' '
def miniongame(string):
  jugador1stuart = 0
  jugador2kevin = 0
  s=len(string)

  for i in (len(s)):
    if s[i] in "BCDFGHJKLMNÑPQRSTVWXYZ":
      jugador1stuart += (len(s)) - i
    elif s[i] in "AEIOU":
      jugador2kevin += (len(s)) - i

  while True:
    if jugador1stuart > jugador2kevin:
      print("¡Stuart ha ganado!")
    elif jugador1stuart < jugador2kevin:
      print("¡Kevin ha ganado!")
    elif jugador1stuart == jugador2kevin:
      print("Empate")

if __name__ == '__main__':
  s = input()
  miniongame(s)
  ' '
  
  
  
  ' '
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
    ' '
