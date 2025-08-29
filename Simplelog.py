# SimpleLog.py

from datetime import datetime

def write_to_log(activity):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("activity_log.txt", "a") as file:
        file.write(f"[{timestamp}] {activity}\n")

print("Welcome to Daily Activity Logger!")
print("Type 'exit' to stop logging.\n")

while True:
    activity = input("Enter your activity: ")
    if activity.lower() == "exit":
        print("Logging finished. Have a great day!")
        break
    write_to_log(activity)
    print("✔ Activity logged!\n")
