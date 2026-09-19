import requests,json

LINK = 'https://jsonplaceholder.typicode.com/todos'
FILE = "data.json"


response = requests.get(LINK)

response = response.json()


#View all the Todo's
def view_todo():
    print('These are all the tasks: ')
    print('////////////////////////////')
    for task in response:
        print(f"{task['id']}. {task['title']} : {task['completed']}")

#View Todo's by ID
def view_todo_by_id(id):
    response_id = requests.get(f'https://jsonplaceholder.typicode.com/todos/{id}')
    response_id = response_id.json()

    
    print(f'Todo #{response_id['id']}')
    print(f'Title: {response_id['title']}')
    print(f'User:{response_id['userId']}')
    print(f'Completed: {response_id['completed']}')

        

#View Todo by UserID
def post_todo(userId):
    response_id = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={userId}')
    response_id = response_id.json()

    print(f'Userid #{userId}')
    print("/////////////////////")

    for task in response_id:      
        print(f'Title: {task['title']}')
        print(f'Completed: {task['completed']}')


#Create a Todo & add to the List
def add_todo():
    pass
#Update a Todo in the List
def update_todo():
    pass
#Delete a todo from the List
def delete_todo():
    pass

