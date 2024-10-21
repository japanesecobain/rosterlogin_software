'''Aoi Araki's Roster Login System'''

def main():
    import os

    # Ensure that roster.txt exists and read its contents
    if not os.path.isfile("roster.txt"):
        open("roster.txt", "w").close()

    roster = []

    # Read existing roster data
    with open("roster.txt", "r") as file:
        for line in file:
            student = line.strip().split(", ")
            if len(student) == 7:
                # Convert grad_year and meetings_attended to integers
                student[5] = int(student[5])  # Graduation year
                student[6] = int(student[6])  # Number of meetings attended
                roster.append(student)
            else:
                print("Warning: Incorrect data format in roster.txt.")

    print("Welcome to the Design and Development Club meeting!\n")

    action = input("Please enter an action (sign in, display, save): ").lower()

    while action != "save":
        if action == "sign in":
            first_name = input("Please enter your first name: ").strip()
            last_name = input("Please enter your last name: ").strip()
            position = -1

            # Check if student already exists in the roster
            for current in range(len(roster)):
                if roster[current][0].lower() == first_name.lower() and roster[current][1].lower() == last_name.lower():
                    position = current
                    break  # Exit loop once student is found

            if position > -1:  # Student is in the roster
                print(f"\nWelcome back, {roster[position][0]} {roster[position][1]}!")
                roster[position][6] += 1  # Increment meetings attended
            else:  # New student
                pronouns = input("Please enter your pronouns: ").strip()
                major = input("Please enter your major: ").strip()
                grad_year = int(input("Please enter your graduation year: ").strip())
                email = f"{first_name[0]}{last_name}@bowdoin.edu".lower()
                student = [first_name, last_name, pronouns, email, major, grad_year, 1]
                roster.append(student)
                print(f"\nWelcome to the club, {first_name} {last_name}!")

        elif action == "display":
            print("\nCurrent Roster:")
            for student in roster:
                print(f"{student[0]} {student[1]} ({student[2]}): {student[3]}")
                print(f"Major: {student[4]}")
                print(f"Graduation Year: {student[5]}")
                print(f"Number of meetings attended: {student[6]}\n")
            print(f"Number of members: {len(roster)}\n")
        else:
            print("That wasn't a valid action, please enter a valid action!")
        action = input("Would you like to sign in, display, or save? ").lower()
            
    # Save logic
    with open("roster.txt", "w") as file:
        for student in roster:
            # Convert all elements to strings
            student_data = [str(element) for element in student]
            file.write(", ".join(student_data))
            file.write("\n")
        
    print("Roster has been saved to roster.txt.")

main()
