import json,os

#Add Job applications
def add():
    #Load the Json FIle first
    FILE = 'data_file.json'
    # Check if the Json Exists
    if os.path.exists(FILE):
        with open(FILE,'r') as file:
            applications = json.load(file)
    else:
        applications = []
    
  
    data = {}
    data['ID'] = len(applications) + 1
    data['Company'] = input('Company: ').lower()
    data['Position'] = input('Position: ').lower()
    data['Location'] = input('Location: ').lower()
    data['Status'] = input('Status: ').lower()

    applications.append(data)

    with open('data_file.json',"w") as file:
        json.dump(applications,file)



#View Job application by status
def view():
    with open('data_file.json', 'r') as file:
        data = json.load(file)
    while True:
        search_status = input('What job status are u looking for? (Applied,Interview,Rejected,Accepted) ')
        for application in data:
            if application['Status'] == search_status.lower():
                print(application)
        break

    

#Update Job application


#Delete a job application


#View all the Job applications
def show_application():
    with open('data_file.json', 'r') as file:
        data = json.load(file)
    while True:
        for applications in data:
            print(f"Application {applications['ID']} : {applications}")
        break





#Create Menu to display Option to Choose
def menu():
    
    while True:

        print("1. Add an Job Application")
        print("2. View all Job applications")
        print("3. View Job application by Status")
        print("4. Update Job Application")
        print("5. Delete Job application")
        print("6. Exit program")
        
        user_input = int(input("Choose a Option 1-7: "))
        

        if user_input == 1:
            add()
            print('Your application has been added!!!')
        elif user_input == 2:
            show_application()
            print('Here is all the applications!!!')
        elif user_input == 3:
            view()
            print("Here is the searched for application!!!")
        elif user_input == 4:
            print("Application updated!!!") 
        elif user_input == 5:
            print("Application is deleted!!!") 
        elif user_input == 6:
            print("Thank you for using my CLI program")
            exit
        else:
            print("You can only enter a number between 1 - 7")

menu()
