# 🎯 Number Guessing Game (Python)

A simple and interactive number guessing game built with Python. Challenge yourself to guess a randomly selected number between 1 and 100 within a limited number of attempts. Tracks your wins and losses across multiple rounds!

---

## 🚀 Features

- 🎲 **Random Number Generation**  
  Each round starts with a different number between `1` and `100` using `random.randint()`.

- 🔁 **Multiple Rounds**  
  Play as many rounds as you want. Your performance is tracked.

- 🔢 **Guessing Logic with Hints**  
  - "Too Low" if your guess is lower than the secret number  
  - "Too High" if your guess is higher

- ⏳ **Attempt Limit**  
  You get **10 attempts** per round to guess correctly.

- 🧠 **Win/Loss Tracking**  
  Win if you guess correctly within 10 tries. Lose otherwise. Final stats are displayed when you quit.

- ✅ **Input Validation**  
  Handles invalid (non-numeric) inputs gracefully.

---

## 📷 Game Preview

```bash
===== 🎯 Welcome to the Number Guessing Game =====

I'm thinking of a number between 1 and 100.
You have 10 attempts to guess it.

Enter your guess: 50
Too high!
Enter your guess: 25
Too low!
...
Correct! You guessed the number in 7 attempts.

Do you want to play again? (yes/no): no

Game Over! Your Score: 2 Wins, 1 Losses.
Thanks for playing!
