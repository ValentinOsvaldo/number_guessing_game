# Guess the number
import random

def play_number_guessing_game():
  print("Bienvenido a el juego de adivinar el número")
  print("Tienes 5 intentos para adivinar un número del 1 a 10")
  
  scores = []

  while True:
    number_to_guess = random.randint(1, 10)
    attempts = 5
    
    print("Nueva ronda!, intenta adivinar el número")
    
    for attempt in range(1, attempts + 1):
      # if the user enters a non-integer
      while True:
        try:
          guess = int(input(f"Intento {attempt}/{attempts}: Pon un número: "))
          break;
        except ValueError:
          print("Valor invalido, debe ser un número entero")
      
      if (guess == number_to_guess):
        print(f"Felicidades! adivinaste el número {number_to_guess} correctamente")
        scores.append(attempt)
        break
      elif guess > number_to_guess:
        print("Muy arriba, intenta de nuevo")
      else:
        print("Muy abajo, intenta de nuevo")
    else:
      print(f"Lo sentimos, has perdido todos tus intentos, el número era {number_to_guess}")
      
    play_again = input("Deseas jugar nuevamente? (si/no): ").lower()
    if (play_again != "si"):
      break
    
  print("\nGame Over!")
  print("Tú puntuación en cada ronda: ")
  
  for round_number, score in enumerate(scores, start = 1):
    print(f"Ronda {round_number}: {score} intentos")

if __name__ == "__main__":
  play_number_guessing_game()
