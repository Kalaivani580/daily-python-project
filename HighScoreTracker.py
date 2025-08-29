# HighScoreTracker.py

import os
from datetime import datetime

HIGH_SCORE_FILE = "high_scores.txt"

def save_score(name, score):
    with open(HIGH_SCORE_FILE, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{name},{score},{timestamp}\n")
    print(f"🎉 Score saved for {name}!")

def load_scores():
    if not os.path.exists(HIGH_SCORE_FILE):
        print("📂 No high scores yet.")
        return

    print("\n🏆 High Scores:\n-------------------")
    with open(HIGH_SCORE_FILE, "r") as file:
        for line in file:
            name, score, timestamp = line.strip().split(",")
            print(f"{name} scored {score} on {timestamp}")

# Example usage
if __name__ == "__main__":
    print("🎮 Welcome to the High Score Tracker!")
    name = input("Enter your name: ")
    try:
        score = int(input("Enter your score: "))
        save_score(name, score)
        load_scores()
    except ValueError:
        print("❌ Invalid score. Please enter a number.")
