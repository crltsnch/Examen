def miniongame(string):
  palabra = "Banana"
  jugador1stuart = 0
  jugador2kevin = 0
  s=len(string)

  for i in (len(s)):
    if s[i] in "BCDFGHJKLMNÑPQRSTVWXYZ":
      jugador1stuart += (len(s)) - i
    elif palabra in "AEIOU":
      jugador2kevin += (len(s)) - i

  if jugador1stuart > jugador2kevin:
    print("¡Stuart ha ganado!")
  elif jugador1stuart < jugador2kevin:
    print("¡Kevin ha ganado!")
  elif jugador1stuart == jugador2kevin:
    print("Empate")