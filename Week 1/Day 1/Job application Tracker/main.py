import json, os

FILE = "data_file.json" #Set Json file Location to a variable to keep consistency


# Add Job applications
def add():
    # Load the Json FIle first

    # Check if the Json Exists
    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            applications = json.load(file)
    else:
        applications = []

    data = {}
    data["ID"] = len(applications) + 1
    data["Company"] = input("Company: ").lower()
    data["Position"] = input("Position: ").lower()
    data["Location"] = input("Location: ").lower()
    data["Status"] = input("Status: ").lower()

    applications.append(data)

    with open(FILE, "w") as file:
        json.dump(applications, file)


# View Job application by status
def view():
    with open(FILE, "r") as file:
        data = json.load(file)
    while True:
        search_status = input(
            "What job status are u looking for? (Applied,Interview,Rejected,Accepted) "
        )
        for application in data:
            if application["Status"] == search_status.lower():
                print(application)
        break


# Update Job application
def update_application():
    with open(FILE, "r") as file:
        data = json.load(file)
    valid_fields = ["company", "position", "location", "status"]
    while True:
        fields = input("What do you wanna update (Company/Position/Location/Status) : ")
        if fields not in valid_fields:
            print("These are the only options: (Company/Position/Location/Status)")
            continue
        id_input = input("ID of the application you want to update: ").strip()
        if not id_input.isdigit() or int(id_input) <= 0:
            print("ID's can't be less than or equal to 0")
            continue
        target_id = int(id_input)

        found = False
        for application in data:
            if application["ID"] == target_id:
                application[fields.capitalize()] = input(
                    "What do you want to change it to? : "
                )
                found = True
                break

        if found:
            with open(FILE, "w") as file:
                json.dump(data, file)
            print("Updated successfully.")
        else:
            print("ID doesn't exist.")
        break


# Delete a job application
def delete_application():
    with open(FILE, "r") as file:
        data = json.load(file)
    while True:
        id_input = input("ID of the application you want to delete: ").strip()
        if not id_input.isdigit() or int(id_input) <= 0:
            print("ID's can't be less than or equal to 0")
            continue
        target_id = int(id_input)

        found = False

        for application in data:
            if application["ID"] == target_id:
                data.remove(application)
                found = True
                break

        if found:
            for index, application in enumerate(data, start=1):
                application["ID"] = index
            with open(FILE, "w") as file:
                json.dump(data,file)
        else:
            print("ID doesnt exist")
        
        break


# View all the Job applications
def show_application():
    with open("data_file.json", "r") as file:
        data = json.load(file)
    while True:
        for applications in data:
            print(f"Application {applications['ID']} : {applications}")
        break


# Create Menu to display Options to Choose
def menu():

    while True:

        print("1. Add an Job Application")
        print("2. View all Job applications")
        print("3. View Job application by Status")
        print("4. Update Job Application")
        print("5. Delete Job application")
        print("6. Exit program")

        user_input = int(input("Choose a Option 1-6: "))

        if user_input == 1:
            add()
            print("Your application has been added!!!")
        elif user_input == 2:
            show_application()
            print("Here is all the applications!!!")
        elif user_input == 3:
            view()
            print("Here is the searched for application!!!")
        elif user_input == 4:
            update_application()
        elif user_input == 5:
            delete_application()
            print("Application is deleted!!!")
        elif user_input == 6:
            print("Thank you for using my CLI program")
            break
        else:
            print("You can only enter a number between 1 - 6")


menu()
