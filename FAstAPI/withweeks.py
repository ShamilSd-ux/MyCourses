from datetime import datetime

class BirthdayCalculator:
    def __init__(self, birthday_str):
        # Store the birthday string and parse it to a datetime object
        self.birthday = datetime.strptime(birthday_str, "%m-%d")
    
    def days_until_next_birthday(self):
        # Get the current date
        today = datetime.today()
        
        # Replace the year of the birthday with the current year
        next_birthday = self.birthday.replace(year=today.year)
        
        # Check if the next birthday is in the past for this year
        if next_birthday < today:
            # If it is, set the next birthday to the following year
            next_birthday = next_birthday.replace(year=today.year + 1)
        
        # Calculate the difference in days
        days_left = (next_birthday - today).days
        return days_left

    def months_until_next_birthday(self):
        # Get the current date
        today = datetime.today()
        
        # Replace the year of the birthday with the current year
        next_birthday = self.birthday.replace(year=today.year)
        
        # Check if the next birthday is in the past for this year
        if next_birthday < today:
            # If it is, set the next birthday to the following year
            next_birthday = next_birthday.replace(year=today.year + 1)
        
        # Calculate the difference in months and days
        months_left = (next_birthday.year - today.year) * 12 + (next_birthday.month - today.month)
        # Adjust for partial months
        if today.day > next_birthday.day:
            months_left -= 1

        return months_left

# Input: your birthday in "MM-DD" format
birthday_input = input("Enter your birthday (MM-DD): ")

# Create an instance of BirthdayCalculator
birthday_calculator = BirthdayCalculator(birthday_input)

# Calculate and display the results
days = birthday_calculator.days_until_next_birthday()
months = birthday_calculator.months_until_next_birthday()

print(f"Months until your next birthday: {months} month(s)")
print(f"Days until your next birthday: {days} day(s)")
