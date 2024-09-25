#date and time 
from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format date
    print("Current date and time:", formatted_date)

def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date: "))  # Prompt for input

    current_date = datetime.now()  # Get current date

    future_date = current_date + timedelta(days=days)  # Calculate future date

    formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format future date

    print("Future date after", days, "days:", formatted_future_date)  # Print future date

                                           
display_current_datetime()
calculate_future_date()