import src.api_client.client as todo

def input_():
    user_choice = int(input('Choose a number: '))
    return user_choice

def menu():
    print("1. View all TODO's")
    print("2. View one todo")
    print("3. Find todos by user")
    print("4. Create todo")
    print("5. Update todo")
    print("6. Delete todo")
    print("7. Exit")

    while True:
       choice = int(input('Choose an option from (1-7): '))
       if choice == 1:
           todo.view_todo()
       elif choice == 2:
           todo.view_todo_by_id(input_())
       elif choice == 3:
           todo.post_todo(input_())
       elif choice == 4:
           todo.add_todo()
       elif choice == 5:
           todo.update_todo(input_())
       elif choice == 6:
           todo.delete_todo()
       elif choice == 7:
            print("Thank you for using my CLI TODO List!!!")
            break
       else:
           print("Only Enter Valid Numbers!!")
        

menu()