def miniongame(i):
  palabra = "banana"
  piramide = " "
  jugador1stuart = 0
  jugador2kevin = 0
  palabra = []

  for item in palabra:
    piramide += item
  
  for i in range(palabra):
    if palabra in "BCDFGHJKLMNÑPQRSTVWXYZ":
      jugador1stuart += palabra - i
    elif palabra in "AEIOU":
      jugador2kevin += palabra - i

  if jugador1stuart > jugador2kevin:
    print("¡Stuart ha ganado!")
  elif jugador1stuart < jugador2kevin:
    print("¡Kevin ha ganado!")
  elif jugador1stuart == jugador2kevin:
    print("Empate")

