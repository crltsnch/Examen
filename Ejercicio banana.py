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