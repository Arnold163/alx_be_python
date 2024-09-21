# daily reminder
task = input("enter the task description: ")
priority = input("enter the priority level (high/medium/low): ").lower()
time_bound = input("is the task time bound (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"The task {task} is high priority."
    case "medium":
        reminder = f"The task {task} is medium priority."
    case "low":
        reminder = f"The task {task} is low priority."
    case _:
        reminder = "Invalid priority level entered."

if time_bound == "yes" and priority in ["high", "medium", "low"]:
    reminder = reminder + " It requires immidiate attention today."

print(reminder)