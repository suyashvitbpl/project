import csv
from datetime import date
import os

# Define the file where we will store the data
FILE_NAME = "routine_log.csv"

def setup_file():
    """Checks if the CSV file exists. If not, creates it and writes the header row."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Writing the column headers
            writer.writerow(["Date", "Water (L)", "Sleep (Hrs)", "Activity", "Diet Category"])

def log_day():
    """Handles user input, provides feedback, and saves the data."""
    print("=== Holistic Routine & Lifestyle Tracker ===")
    today = date.today().strftime("%Y-%m-%d")
    print(f"Date: {today}\n")

    try:
        # 1. Collect Data
        water = float(input("How many liters of water did you drink today? (e.g., 2.5): "))
        sleep = float(input("How many hours did you sleep last night? (e.g., 6.5): "))
        activity = input("What was your activity today? (e.g., 8000 steps, gym, none): ")
        
        print("\nDiet Categories:")
        print("1: Standard Mess/Thali Food")
        print("2: Heavy/Junk/Fast Food")
        print("3: Light & Healthy (Fruits, Salads, Home-style)")
        diet_choice = input("Enter the number that best describes your meals today (1/2/3): ")

        # 2. Provide Instant Feedback
        print("\n=== Your Daily Balance Feedback ===")
        
        if water < 2.0:
            print("💧 Hydration: A bit low. Keep a water bottle at your desk tomorrow!")
        else:
            print("💧 Hydration: Excellent job staying hydrated.")

        if sleep < 7.0:
            print("🛏️ Sleep: You are running a sleep deficit. Try to wind down earlier tonight.")
        else:
            print("🛏️ Sleep: Great resting hours. Your brain will thank you.")

        if diet_choice == '2':
            print("🍲 Diet: Heavy meals today. Consider adding cooling foods (like buttermilk or fruit) tomorrow to balance the heat.")
        elif diet_choice == '1':
            print("🍲 Diet: Standard meals logged. Ensure you are digesting well and staying active.")
        elif diet_choice == '3':
            print("🍲 Diet: Fantastic, light, and healthy choices today!")
        else:
            print("🍲 Diet: Unrecognized category, but logged anyway.")

        # 3. Save Data to CSV
        with open(FILE_NAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([today, water, sleep, activity, diet_choice])
            
        print(f"\n✅ All done! Your log for {today} has been securely saved to {FILE_NAME}.")

    except ValueError:
        # This prevents the program from crashing if the user types a letter instead of a number
        print("\n❌ Error: Please enter valid numbers for your water and sleep inputs. Try running the script again.")

if __name__ == "__main__":
    setup_file()
    log_day()