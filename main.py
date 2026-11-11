import json
import time

COMPANY_NAME = "Enqluid"
type = ""
total_price = 0

with open("data.json", "r")as f:
    data = json.load(f)


def save_data():
    with open("data.json", "w")as f:
        json.dump(data, f, indent=4)

def class_type():

    print("Please select your travel class: [1] Economy  [2] Business")

    type_choice = int(input("-> "))

    if type_choice == 1:
        type = "Economy"

        print("Thank you! Your Economy seat has been booked.")

    elif type_choice == 2:
        type = "Business"

        print("Thank you! Your Business seat has been booked.")

def information_register():
    
    name_register = input("Please enter your first name -> ")

    data['person_information']['Name'] = name_register

    print(f"Nice to meet you, {data['person_information']['Name']}!")
    
    surname_register = input("Please enter your last name -> ")
    data['person_information']['Surname'] = surname_register

    age_register = int(input("Please enter your age -> "))

    if age_register >= 18:
        print("Thank you! Your details have been saved.")
        save_data()

    else:
        print("Sorry, bookings are only available to passengers aged 18 and over.")
        exit()


while True: 
    print(f"Welcome to {COMPANY_NAME}! How can we help you today?")
    print("[1] Enter passenger details")