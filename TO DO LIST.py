import sys
import random
Choice=['']
rando=random.randint(1,13)
todolist={}
next_key=1
def menu():
    print('Choose a menu item')
    print("type 'a' to add a item")
    print("type 'b' to delete a item")
    print("type 'c' to quit")
    print("type ' a random number' to win a special prize:):)")
    
    Choice=input()
    if Choice=="a":
        add()
    elif Choice=="b":
        delete()
    elif Choice=="c":
        quit()
    elif str(rando)==Choice:
        congrats()
    else:
        print('thats not a option silly')
        print('TRY AGAIN!!!. YOU CANT FOLLOW THE SIMPLEST DIRECTION. YOU ARENT SMART ENOUGH TO USE MY TO_DO LIST')
        sys.exit()
    menu()


def add():
    global next_key
    todo_item = ""
    while todo_item =="":
        print('What is ur To-Do item')
        todo_item = input()
        
        x = todo_item.find("english")
        if x > -1:
            print('hahahaha you have english homework. Remember,user, dont forget your commas')
        else:
            print('HAHA YOU HAVE WORK... HAHAHAHAHAH. IM SITTING ON MY COUCH DOING NOTHING')
    
    print('When is it due')
    due_date = input()


    todolist[next_key] = [todo_item, due_date]
    next_key += 1
    show_list()
    
    menu()

def delete():
    show_list()
    print('what would you like to delete')
    delete_me = int(input())
    if delete_me in todolist:
        del todolist[int(delete_me)]
    else:
        print('YOU ARE SO DUMB... YOU ENTERED SOMETHING THAT ISNT AVAILABLE... I WANT TO DELETE YOU...')
        sys.exit
    menu()
def quit():
    sys.exit()

def congrats():
    print('CONGRATS... YOU WIN NOTHING')

def show_list():
    print(todolist)
menu()
