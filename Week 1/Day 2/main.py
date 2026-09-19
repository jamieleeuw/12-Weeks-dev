import src.api_client.client as todo


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
           todo.view_todo_by_id(input('What ID are you Looking For?: '))
       elif choice == 3:
           todo.post_todo(input('What UserID are you Looking For?: '))
       elif choice == 4:
           print("4")
       elif choice == 5:
           print("5")
       elif choice == 6:
           print("6")
       elif choice == 7:
            print("Thank you for using my CLI TODO List!!!")
            break
       else:
           print("Only Enter Valid Numbers!!")
        

menu()