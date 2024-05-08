import service
from dto import UserRegisterDTO
from utils import ResponseData
from colorama import Fore


def print_response(response: ResponseData):
    color = Fore.GREEN if response.status else Fore.RED
    print(color + str(response.data) + Fore.RESET)


def print_error(error: Exception):
    print(Fore.RED + str(error) + Fore.RESET)


def menu():
    print('Login => 1')
    print('Register => 2')
    print('Logout => 3')
    print('Todo ADD => 4')
    print('Quit => q')
    return input('?: ')


def authentication():
    username = input('Username: ')
    password = input('Password: ')
    response: ResponseData = service.login(username, password)
    print_response(response)


def register():
    username = input('Username: ')
    password = input('Password: ')
    dto: UserRegisterDTO = UserRegisterDTO(username=username, password=password)
    response: ResponseData = service.register(dto)
    print_response(response)


def logout():
    response: ResponseData = service.logout()
    print_response(response)


def add_todo():
    try:
        title = input('Todo title: ')
        response: ResponseData = service.add_todo(title)
        print_response(response)
    except Exception as e:
        print_error(e)


def delete_todo():
    try:
        todo_id = input('Todo id to delete: ')
        response: ResponseData = service.delete_todo(todo_id)
        print_response(response)
    except Exception as e:
        print_error(e)


def edit_todo():
    try:
        todo_id = input('Todo id to edit: ')
        new_title = input('New title: ')
        response: ResponseData = service.add_todo(new_title, todo_id)
        print_response(response)
    except Exception as e:
        print_error(e)


def view_todo(todo_id=None, new_title=None):
    try:
        response:ResponseData = service.edit_todo(todo_id, new_title)
        print_response(response)
    except Exception as e:
        print_error(e)


if __name__ == '__main__':
    while True:
        choice = menu()
        if choice == '1':
            authentication()
        elif choice == '2':
            register()
        elif choice == '3':
            logout()

        elif choice == '4':
            add_todo()
        elif choice == 'q':
            break
