# 🎯 Number Guessing Game (Python)

A beginner-friendly Python console game where the computer randomly selects a number and the player tries to guess it with helpful hints.

---

## 📌 Project Description

This is a simple number guessing game written in Python.  
The program randomly generates a number between **1 and 50**, and the user keeps guessing until the correct number is found.  
After every wrong guess, the program gives a hint to guess **higher** or **lower**.

---

## 🧠 How the Game Works

1. The computer selects a random number between **1 and 50**
2. The user enters a guess
3. The program responds:
   - **"Lower than this"** if the guess is too high
   - **"Higher than this"** if the guess is too low
4. The game continues until the correct number is guessed
5. The total number of attempts is displayed

---

## 🧪 Sample Output

Guess the number : 20
Higher than this
Guess the number : 35
Lower than this
Guess the number : 28
You have guessed the right number in 3 attempts

yaml
Copy code

---

## 🛠️ Technologies Used

- Python 3
- Built-in `random` module

---

## 📦 Requirements

- Python 3.x installed on your system

(No external libraries required)

---

## ▶️ How to Run the Program

1. Clone or download this repository
2. Open terminal / command prompt
3. Navigate to the project folder
4. Run the command:

```bash
python number_guessing_game.py
📂 Project Structure
typescript
Copy code
number-guessing-game/
│
├── number_guessing_game.py
└── README.md
🚀 Future Improvements
Add difficulty levels (Easy / Medium / Hard)

Set a maximum number of attempts

Handle invalid inputs (letters, symbols)

Store best scores

Add replay option

✨ Learning Outcomes
Working with loops

Using conditional statements

Handling user input

Using random number generation

Writing clean beginner-level Python code

👨‍💻 Author
Created with ❤️ while learning Python basics.
Perfect for beginners and first GitHub projects 🚀