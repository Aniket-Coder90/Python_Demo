"""
This is Simple Guess Number Program
"""

# Approch 1 : Binary Search

# import random

# def random_guessing_game():
#     print("Socho ek number 1 se 100 ke bich ka")
#     input("Soch Liya? Taiyar hoo to Enter Dabado")

#     low = 1
#     high = 100

#     attempts = 0

#     while low <= high:
#         guess = (low + high) // 2
#         attempts += 1

#         print(f"Mera guess: {guess}")

#         feedback = input("Tumhara Jawab ? (Too High / Too Low / Correct)").lower()

#         if feedback == "too high":
#             high = guess - 1
#         elif feedback == "too low":
#             low = guess + 1
#         elif feedback == "correct":
#             print(f"Yay! Maine {attempts} attempts mein guess kar liya randomly 🎉")
#             break
#         else:
#             print("Galat input! Sirf 'Too High', 'Too Low', ya 'Correct' likho.")

#     if low > high:
#         print("Lagta hai number thoda confuse ho gaya 😅")

# # Run the random version
# random_guessing_game()

# Approch 2: 🤖 AI Number Guessing Game with Pattern Learning

# import json
# import random
# import os

# DATA_FILE = "user_pattern.json"

# # Step 1: Load Previous user numbers

# def load_data():
#     if os.path.exists(DATA_FILE):
#         with open(DATA_FILE, "r") as f:
#             return json.load(f)
        
#     else:
#         return { "user_numbers": [] }
    

# # Step 2: Save new Number
# def save_number(user_number):
#     data = load_data()
#     data["user_numbers"].append(user_number)

#     with open(DATA_FILE, "w") as f:
#         json.dump(data, f)

# # Step 3: Analyze Pattern
# def analyze_pattern(data):
#     numbers = data["user_numbers"]

#     if not numbers:
#         return None
    
#     avg = sum(numbers) / len(numbers)

#     bias = "high" if avg > 60 else "low" if avg < 40 else "mid"

#     return bias

# # Step 4: AI Game Logic
# def ai_guess_game():
#     print("Socho ek number 1 se 100 ke beech.")

#     user_number = int(input("Tumhara number (AI ko batana hain training ke liye): "))

#     # Save User Number

#     save_number(user_number)

#     # Load + Analyze

#     data = load_data()

#     bias = analyze_pattern(data)

#     print(f"\n🤖 AI ne past data se predict kiya: '{bias}' number hone ka chance zyada hai.")

#     # Game Start
#     low = 1
#     high = 100

#     attempts = 0

#     while low <= high:
#         # Step 5: 