# Project: Expense Tracker - Installment 2
# Author: Bryan Kyle Dimpal
# Description: Interactively prompts for user input, processes expenses, and prints a formatted summary.

print("=" * 40)
print("\t" + " " * 5 + "EXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

print("\nMAIN MENU")
print("\t[1] Add an expense\t\t(coming soon)")
print("\t[2] View all expenses\t\t(coming soon)")
print("\t[3] Show total spent\t\t(coming soon)")
print("\t[4] Exit\t\t\t(coming soon)\n")

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.\n")

item1 = input("First expense? ")
amount1 = float(input("Amount? "))

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

print("")
print("-" * 40)
print("SUMMARY")
print(f" - {item1}:\t\t${amount1}")
print(f" - {item2}:\t\t${amount2}")
print(f"Total spent:\t\t${total}")
print(f"Average:\t\t${average}")
print("-" * 40)
print("Made by: Bryan Kyle Dimpal  |  Installment 2")