# GIS Garden Party Volunteer Management Program

while True:
    print("\nGIS Garden Party Volunteer Management")
    print("1. Add Volunteer")
    print("2. View Volunteers")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        # Adding a volunteer
        name = input("Enter volunteer's name: ")
        role = input("Enter the role (e.g., Food Stall, Ticket Sales): ")
        availability = input("Enter availability (All Day or Specific Hours): ")

        # Open the file in append mode and write the data
        file = open("volunteers.txt", "a")
        file.write(name + ", " + role + ", " + availability + "\n")
        file.close()

        print("Volunteer added successfully.")

    elif choice == "2":
        # Viewing volunteers
        try:
            file = open("volunteers.txt", "r")
            volunteers = file.readlines()
            file.close()

            print("\n--- List of Volunteers ---")
            for volunteer in volunteers:
                details = volunteer.strip().split(", ")
                print("Name: " + details[0] + ", Role: " + details[1] + ", Availability: " + details[2])

        except FileNotFoundError:
            print("No volunteer data found. Please add some volunteers first.")

    elif choice == "3":
        # Exiting the program
        print("Exiting program.")
        break

    else:
        print("Invalid option. Please try again.")
