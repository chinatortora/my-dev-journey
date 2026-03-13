import requests
import json
import sys


def display_table(records):
    """Visualizes the schedule in a clean table format."""
    header = "{:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format(
        'Activity', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri')
    print("\n" + header)
    print("-" * 75)
    for item in records:
        print("{:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format(
            item['Activity'], item['Monday'], item['Tuesday'],
            item['Wednesday'], item['Thursday'], item['Friday']
        ))


def run():
    print("=== Fitness Centre Booking System ===")

    # Step 1: Show Schedule
    if input("View next week's schedule? (y/n): ").lower() == 'y':
        response = requests.get('http://localhost:5001/activities')
        display_table(response.json())
    else:
        print("Goodbye!")
        sys.exit()

    # Step 2: Make a Booking
    if input("\nWould you like to book a class? (y/n): ").lower() == 'y':
        p_id = int(input("Enter your User ID: "))
        act = input("Enter activity (e.g. Yoga): ").lower()
        day = input("Enter day: ").lower()

        # Post the data to API
        booking_payload = {"person_id": p_id, "activity": act, "day": day}
        requests.post('http://localhost:5001/class_booking', json=booking_payload)

        # Step 3: Confirm Booking
        print("\n--- Confirmation Receipt ---")
        conf = requests.get('http://localhost:5001/reservation').json()
        for c in conf:
            print(f"ID: {c['ID']} | Activity: {c['Activity']} | Day: {c['Day']}")
        print("See you in class!")


if __name__ == '__main__':
    run()
