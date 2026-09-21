import requests,json

LINK = 'https://jsonplaceholder.typicode.com/todos'
FILE = "data.json"


try:
    response = requests.get(LINK)
    response = response.json()
except requests.exceptions.RequestException as e:
    print(f"Could not load todos: {e}")
    response = []

#View all the Todo's
def view_todo():
    print('These are all the tasks: ')
    print('////////////////////////////')
    for task in response:
        print(f"{task['id']}. {task['title']} : {task['completed']}")

#View Todo's by ID
def view_todo_by_id(id):

    try:
        response_id = requests.get(f'{LINK}/{id}')
        response_id = response_id.json()
    except requests.exceptions.RequestException as e:
        print(f"Could not get Todo #{id}: {e}")
        return

    
    print(f'Todo #{response_id['id']}')
    print(f'Title: {response_id['title']}')
    print(f'User:{response_id['userId']}')
    print(f'Completed: {response_id['completed']}')

        

#View Todo by UserID
def post_todo(userId):
    try:

        response_id = requests.get(f'{LINK}?userId={userId}')
        response_id = response_id.json()
    except requests.exceptions.RequestException as e:
        print(f"Could not get todos for User #{userId}: {e}")
        return

    print(f'Userid #{userId}')
    print("/////////////////////")

    for task in response_id:      
        print(f'Title: {task['title']}')
        print(f'Completed: {task['completed']}')


#Create a Todo & add to the List
def add_todo():
    try:
        userid = int(input("What is your UserID?: "))
    except ValueError:
        print("UserID must be a number.")
        return
    
    title = input('What is the Todo title: ')
    complete = False

    todo = {
        "userId": userid,
        "title" : title,
        "completed": complete
    }
    try:
        
        create_response = requests.post(LINK, json=todo)
        if create_response.status_code == 201:
            response.append(create_response.json())
            print('Task Created!!!')
    except requests.exceptions.RequestException as e:
        print(f"Could not create task: {e}")

   


#Update a Todo in the List
def update_todo():
    bfound = False

    while not bfound:
        try:
            id = int(input('Provide me the ID: '))
        except ValueError:
            print('That is not a valid ID, try again')
            continue
        for task in response:
            if id == task['id']:
                title = input('What should the Todo be: ').lower()
                todo = {'title': title}
                try:
                    update_response = requests.put(f"{LINK}/{id}",json=todo)
                    if update_response.status_code == 200:
                        task['title'] = title
                        print('Task Updated!!!')
                except requests.exceptions.RequestException as e:
                     print(f"Could not update task: {e}")
                bfound = True
            
        if not bfound:
            print('That ID does not exist try again')

            

        
#Delete a todo from the List
def delete_todo():
    bfound = False

    while not bfound:
        try:
            id = int(input('Provide me the ID: '))
        except ValueError:
            print('That is not a valid ID, try again')
            continue
        for task in response:
            if id == task['id']:
                try:
                    delete_response = requests.delete(f"{LINK}/{id}")
                    if delete_response.status_code == 200:
                        response.remove(task)
                except requests.exceptions.RequestException as e:
                    print(f"Could not delete task: {e}")
                bfound = True
        if not bfound:
            print('That ID does not exist try again')

