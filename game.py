import random
from colorama import init, Fore, Style

# init colorama
init(autoreset=True)

# read all words from words.txt
with open('words.txt', 'r') as file:
    words = file.read().split(',')

# randomly select a target word
target_word = random.choice(words)
word_length = len(target_word)

# Welcome message and rules description
print("Welcome to the Word Guessing Game!")
print("Please select difficulty level:")
print("1 - Easy: Any correct letter will be revealed in correct position.")
print("2 - Normal: Wordle style (green = correct, yellow = misplaced, red = wrong)")
print("3 - Hard: Only exact matches (letter + position) are revealed.")

# choose difficulty
while True:
    try:
        difficulty = int(input("Enter difficulty level (1/2/3): "))
        if difficulty not in [1, 2, 3]:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter 1, 2, or 3.")

print(f"\nThe word has {word_length} letters.\n")
print(Fore.GREEN + "Letters in the correct position" + Style.RESET_ALL, "will be shown in green,")
if difficulty == 2:
    print(Fore.YELLOW + "Letters that are correct but in the wrong position" + Style.RESET_ALL, "will be shown in yellow,")
print(Fore.RED + "Incorrect letters" + Style.RESET_ALL, "will be shown in red.\n")

# Initialising the game state
current_display = ['_'] * word_length
# hint can only be used once
hint_used = False

# print(target_word)  # For testing

# The main game loop
while True:
    guess = input("Enter your guess (or '?' for a hint): ").lower()

    # Processing tips
    if guess == '?':
        if hint_used:
            print(Fore.MAGENTA + "You've already used your hint for this game.\n")
            continue
        # Find the positional index of the letters in the target_word that have not yet been correctly guessed.
        unrevealed = []
        for i in range(word_length):
            if current_display[i] != target_word[i]:
                unrevealed.append(i)
        if not unrevealed:
            print(Fore.MAGENTA + "All letters are already revealed!\n")
            continue
        # A randomly selected letter from the unguessed ones
        hint_index = random.choice(unrevealed)
        current_display[hint_index] = target_word[hint_index]
        print(Fore.BLUE + f"💡 Hint revealed: Letter {hint_index + 1} is '{target_word[hint_index].upper()}'\n")
        hint_used = True
        continue

    # Check the length of user input
    if len(guess) != word_length:
        print(f"Please enter a word with exactly {word_length} letters.\n")
        continue

    # Easy 
    if difficulty == 1:
        result = []
        for i in range(word_length):
            # Letters in the correct position
            if guess[i] == target_word[i]:
                current_display[i] = guess[i]
                result.append(Fore.GREEN + guess[i] + Style.RESET_ALL)
            # Letter exists in the target word, but position is ignored in Easy mode
            elif guess[i] in target_word:
                result.append(Fore.GREEN + guess[i] + Style.RESET_ALL)
            # Letter is not in the target word
            else:
                result.append(Fore.RED + guess[i] + Style.RESET_ALL)
        print("Progress: " + ' '.join(result))
        # Check if the entire word has been guessed
        if ''.join(current_display) == target_word:
            print(Fore.CYAN + f"\n🎉 Congratulations! You guessed the word: {target_word}")
            break

    # Normal 
    elif difficulty == 2:
        # Track which letters in target_word have been matched
        used = [False] * word_length
        # Store colored output for each guessed letter
        result = [None] * word_length

        # check for exact matches (correct letter and position)
        for i in range(word_length):
            if guess[i] == target_word[i]:
                result[i] = Fore.GREEN + guess[i] + Style.RESET_ALL
                used[i] = True
        # check for correct letters in the wrong position
        for i in range(word_length):
            # Already matched in the first check
            if result[i] is not None:
                continue
            found = False
            for j in range(word_length):
                if not used[j] and guess[i] == target_word[j]:
                    found = True
                    # Prevent reusing the same letter
                    used[j] = True
                    break
            if found:
                result[i] = Fore.YELLOW + guess[i] + Style.RESET_ALL
            else:
                result[i] = Fore.RED + guess[i] + Style.RESET_ALL

        print("Result: " + ' '.join(result))
        # Check if the guessed word is correct
        if guess == target_word:
            print(Fore.CYAN + f"\n🎉 Excellent! You've cracked the word: {target_word}")
            break

    # Hard 
    else:
        result = []
        for i in range(word_length):
            # Only exact matches are accepted
            if guess[i] == target_word[i]:
                current_display[i] = guess[i]
                result.append(Fore.GREEN + guess[i] + Style.RESET_ALL)
            # No hint for incorrect letters or misplaced correct letters
            else:
                result.append(Fore.RED + guess[i] + Style.RESET_ALL)

        print("Progress: " + ' '.join(result))
        # Check if the entire word has been guessed correctly
        if ''.join(current_display) == target_word:
            print(Fore.CYAN + f"\n🎉 Well done! The word was: {target_word}")
            break


"""
The Word Guessing Game is an engaging, text-based puzzle designed to challenge players' vocabulary and deduction skills. Players must guess a hidden word, with feedback provided based on their chosen difficulty: Easy (reveals all correct letters), Normal (Wordle-style color hints), or Hard (only exact matches shown). A one-time hint feature adds strategic depth. Ideal for language learners, puzzle lovers, and casual gamers, this game offers a fun way to improve spelling, logic, and word recognition through interactive gameplay.
"""

