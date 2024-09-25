#date and time 
from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()

    formmatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    print("current date and time:", formmatted_date)

def calculate_future_date():
    days = int(input("Enter the number of days to add: "))
    current_date = current_date + timedelta(days=days)
    formatted_future_date = current_date.strftime("%Y-%m-%d")

    print("future date after", days, "days :", formatted_future_date)
                                           
