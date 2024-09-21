# daily reminder
task = input("enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"Reminder: The task '{task}' is high priority."
    case "medium":
        reminder = f"Reminder: The task '{task}' is medium priority."
    case "low":
        reminder = f"Reminder: The task '{task}' is low priority."
    case _:
        reminder = "Reminder: Invalid priority level entered."

if time_bound == "yes" and priority in ["high", "medium", "low"]:
    reminder = reminder + " It requires immidiate attention today."

print(reminder)