import src.api_client.client as todo
import service.todo_logic as logic
    

def menu():

    while True:
       print("1. View all TODO's")
       print('2. View todo by todo ID')
       print("3. Find todos by userID")
       print("4. Create todo")
       print("5. Update todo")
       print("6. Delete todo")
       print("7. Exit")

       try:
        choice = int(input('Choose an option from (1-7): '))
       except ValueError:
           print("Only Enter Valid Numbers!!")
           continue
       
       if choice == 1:
           print('These are all the tasks: ')
           print('////////////////////////////')
           response = todo.view_todo()

           for task in response:
                print(f"{task['id']}. {task['title']} : {task['completed']}")
       elif choice == 2:
           user_choice = input('What ID are you looking for: ')
           task = todo.view_todo_by_id(logic.input_(user_choice))
           if type(task) is dict: 
            print(f'Todo #{task['id']}')
            print(f'Title: {task['title']}')
            print(f'User:{task['userId']}')
            print(f'Completed: {task['completed']}')
       elif choice == 3:
           user_choice = input('What userID are you looking for: ')
           response = todo.view_todos_by_user(logic.user_id(user_choice))
           if response:
                print(f'Userid #{user_choice}')
                print("/////////////////////")
                for task in response:
                    print(f'Title: {task['title']}')
                    print(f'Completed: {task['completed']}')
           else:
               print(f'UserID: {user_choice} doesnt exist')
               
           
       elif choice == 4:
           userID = ('What is the UserID: ')
           title = input('What is the Todo title: ')
           complete = False
           approved = logic.user_id(userID)
           if todo.add_todo(approved,title,complete):
               print("Task created!!!")
    
       elif choice == 5:
           id = (input('Provide me the ID: '))
           id  = logic.input_(id)
           title = input('What should the Todo be: ').lower()

           if todo.update_todo(id,title):
                print('Task Updated!!!')
       elif choice == 6:
           id = (input('Provide me the ID: '))
           id  = logic.input_(id)
           if todo.delete_todo(id):
               print("Todo deleted!!")
       elif choice == 7:
            print("Thank you for using my CLI TODO List!!!")
            break
       else:
           print("Only Enter Valid Numbers!!")
        

menu()