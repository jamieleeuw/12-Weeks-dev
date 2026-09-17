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
    data['ID'] = len(data) + 1
    data['Company'] = input('Company: ')
    data['Position'] = input('Position: ')
    data['Location'] = input('Location: ')
    data['Status'] = input('Status: ')

    applications.append(data)

    with open('data_file.json',"w") as file:
        json.dump(applications,file)



#View one Job application
def view():
    with open('data_file.json', 'r') as file:
        data = json.load(file)
    print(data)


#Search for Job applications



#Update Job application


#Delete a job application


#View all the Job applications






#Create Menu to display Option to Choose
def menu():
    
    while True:
        user_input = int(input("Choose a Option 1-7: "))
        if user_input == 1:
            add()
            print('Your application has been added')
        elif user_input == 2:
            view()
            print("View") 
        elif user_input == 3:
            print("Search")
        elif user_input == 4:
            print("Update") 
        elif user_input == 5:
            print("Delete") 
        elif user_input == 6:
            print("Show")
        elif user_input == 7:
            print("Thank you for using my CLI program")
            break
        else:
            print("You can only enter a number between 1 - 7")

menu()
