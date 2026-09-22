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
        response_id.raise_for_status()
        response_id = response_id.json()
    except requests.exceptions.RequestException as e:
        print(f"Could not get Todo #{id}: {e}")
        return

    
    return response_id

        

#View Todo by UserID
def view_todos_by_user(userId):
    try:

        response_id = requests.get(f'{LINK}?userId={userId}')
        response_id = response_id.json()
    except requests.exceptions.RequestException as e:
        print(f"Could not get todos for User #{userId}: {e}")
        return

    return response_id


#Create a Todo & add to the List
def add_todo(userid,title,complete):
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
def update_todo(id,title):
    bfound = False

    while not bfound:
        for task in response:
            if id == task['id']:
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
def delete_todo(id):
    bfound = False

    while not bfound:
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

