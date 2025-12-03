Snake Water Gun Game 🐍💧🔫
A Python implementation of the classic hand game (similar to Rock-Paper-Scissors) where you compete against the computer.
Game Rules

Snake drinks Water → Snake wins
Water douses Gun → Water wins
Gun shoots Snake → Gun wins

How It Works
The game uses a numerical system for comparisons:

1 = Snake (s)
-1 = Water (w)
0 = Gun (g)

Computer randomly selects one option, you input your choice, and the winner is determined based on the rules above.
Usage
bashpython snake_water_gun.py
Input Options

Type s for Snake
Type w for Water
Type g for Gun

Example Output
enter your choice : s
Computer choosed Gun
You choosed Snake
You Lose
Code Structure

Random Selection: Computer choice generated using random.choice()
Input Mapping: User input converted via dictionary (youDict)
Reverse Mapping: Numbers converted back to readable names for display
Win Logic: Nested conditionals check all possible outcomes

Skills Demonstrated

Basic Python syntax and control flow
Dictionary usage for mapping
Random module for unpredictability
Conditional logic for game rules
User input handling

Future Improvements

Add score tracking across multiple rounds
Implement best-of-N gameplay
Add input validation and error handling
Create a game loop for continuous play
Track win/loss statistics


Author: Aadii
Level: Beginner Python Project
Purpose: Learning fundamentals through game development