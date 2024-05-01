import random
"""
2. Guess the Number Game:

Create a function that generates a random number within a range specified by the user.
Prompt the user to guess the number within a specified maximum number of attempts.
Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.
Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.
"""
def check_num() -> int:
    while True:
        try:
            num: int = int(input("Inserisci un numero da 1 a 10: "))
            if 1 <= num <= 10:
                return num
            elif num < 1:
                print("Il numero non può essere minore di 1, riprova")
            elif num > 10:
                print("Il numero non può essere maggiore di 10, riprova")
        except:
            print("Dovevi scrivere solo un numero intero")


def guess_number(num: int) -> str:
    num_rand: int = random.randint(1, 10)
    while True:
        if num == num_rand:
            return f"Hai vinto! Il numero è {num}"
        elif num < num_rand:
            num = int(input("Il numero che hai inserito è più piccolo del target, riprova: "))
        elif num > num_rand:
            num = int(input("Il numero che hai inserito è più grande del target, riprova: "))


print(guess_number(check_num()))