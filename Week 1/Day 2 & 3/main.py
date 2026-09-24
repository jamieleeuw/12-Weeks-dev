import service.todo_logic as logic
import database.db as db


def menu():

    while True:
        print("1. View all TODO's")
        print("2. View todo by todo ID")
        print("3. Find todos by userID")
        print("4. Create todo")
        print("5. Update todo")
        print("6. Delete todo")
        print("7. Exit")

        try:
            choice = int(input("Choose an option from (1-7): "))
        except ValueError:
            print("Only Enter Valid Numbers!!")
            continue

        if choice == 1:
            print("These are all the tasks: ")
            print("////////////////////////////")
            response = db.get_todos()

            for task in response:
                print(f"ID : {task[0]}")
                print(f"title : {task[1]}")
                print(f"Completed : {task[2]}")
                print("///////////////////////")
        elif choice == 2:
            user_choice = input("What ID are you looking for: ")
            task = db.get_todo_by_id(logic.input_(user_choice))
            if type(task) is tuple:
                print(f"Todo #{task[0]}")
                print(f"Title: {task[1]}")
                print(f"User:{task[3]}")
                print(f"Completed: {task[2]}")
            else:
                print(f'Todo #{user_choice} doesnt exist please create a todo first')
        elif choice == 3:
            user_choice = input("What userID are you looking for: ")
            task = db.get_user_todo(logic.user_id(user_choice))
            for todo in task:
                if type(todo) is tuple:
                    print(f"ID #{todo[0]}")
                    print(f"title: {todo[1]}")
                    print(f"complete: {todo[2]}")
                else:
                    print(f"UserID {user_choice} doesn't exist, let's create one")
                    name = input('Whats your name: ')
                    surname = input('Whats your surname: ')
                    new_id = db.create_user(name, surname)
                    print(f'User created with userId {new_id}!! add a TODO with that userID')
        elif choice == 4:
           title = input('What should the Todo be: ').lower()
           user_choice = input('What is your userID: ')
           user_id = logic.user_id(user_choice)
 
           if user_id is False:
               print("Only Enter Valid Numbers!!")
               continue
 
           existing_user = db.get_user_by_id(user_id)
           if not existing_user:
               print(f"UserID {user_id} doesn't exist, let's create one")
               name = input('Whats your name: ')
               surname = input('Whats your surname: ')
               new_id = db.create_user(name, surname)
               if not new_id:
                   continue
               user_id = new_id
 
           result = db.create_todo(title, user_id)
           if result:
               print(f'Todo created with TODOID {result}!!')
        elif choice == 5:
           id = (input('Provide me the TodoID: '))
           id  = logic.input_(id)
           if id is False:
               print("Only Enter Valid Numbers!!")
               continue
 
           existing = db.get_todo_by_id(id)
           if not existing:
               print(f'Todo #{id} doesnt exist create a todo first')
               continue
 
           title = input('What should the Todo be: ').lower()
           if db.update_todo(id, title, existing[2]):
                print('Task Updated!!!')
        elif choice == 6:
           id = (input('Provide me the ID: '))
           id  = logic.input_(id)
           if id is False:
               print("Only Enter Valid Numbers!!")
               continue
           existing = db.get_todo_by_id(id)
           if not existing:
               print(f'Todo #{id} doesnt exist create a todo first')
               continue
           
           if db.delete_todo(id):
               print("Todo deleted!!")
        elif choice == 7:
            print("Thank you for using my CLI TODO List!!!")
            break
        else:
            print("Only Enter Valid Numbers!!")


menu()
