"""
This is Simple Guess Number Program
"""

# Approch 1 : Binary Search

import random

def random_guessing_game():
    print("Socho ek number 1 se 100 ke bich ka")
    input("Soch Liya? Taiyar hoo to Enter Dabado")

    low = 1
    high = 100

    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        attempts += 1

        print(f"Mera guess: {guess}")

        feedback = input("Tumhara Jawab ? (Too High / Too Low / Correct)").lower()

        if feedback == "too high":
            high = guess - 1
        elif feedback == "too low":
            low = guess + 1
        elif feedback == "correct":
            print(f"Yay! Maine {attempts} attempts mein guess kar liya randomly 🎉")
            break
        else:
            print("Galat input! Sirf 'Too High', 'Too Low', ya 'Correct' likho.")

    if low > high:
        print("Lagta hai number thoda confuse ho gaya 😅")

# Run the random version
random_guessing_game()