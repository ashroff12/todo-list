import sys
import random
Choice=['']
rando=random.randint(1,13)
todolist=[]

def menu():
    show_list()
    
    print('Choose a menu item')
    print("type 'a' to add a item")
    print("type 'b' to delete a item")
    print("type 'c' to quit")
    print("type  'a random number' to win a special prize:):)")
    
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
        print('TRY AGAIN!!!. YOU CANT FOLLOW THE SIMPLEST DIRECTION. YOU ARENT SMART ENOUGH TO USE MY TO_DO LIST, GOODBYE, I AM ALSO DELETING YOUR ENTIRE LIST')
        todolist=[]
        sys.exit()
    menu()


def add():
    
    todo_item = ""
    while todo_item =="":
        print('What is ur To-Do item')
        todo_item = input()
        
        x = todo_item.find("english")
        if x > -1:
            print('hahahaha you have english homework. Remember,user, dont forget your commas')
        else:
            print('HAHA YOU HAVE WORK... HAHAHAHAHAH. IM SITTING ON MY COUCH DOING NOTHING')
            print('Good excutive functioning skills')
    print('When is it due')
    due_date = input()


    todolist.append([todo_item, due_date])
    
    
    save_data()
    menu()

def delete():
    show_list()
    print('what would you like to delete')
    delete_me = int(input()) -1
    if delete_me < len(todolist):
        todolist.pop(delete_me)
    else:
        print('YOU ARE SO DUMB... YOU ENTERED SOMETHING THAT ISNT AVAILABLE... I WANT TO DELETE YOU...')
        sys.exit
    menu()
def quit():
    sys.exit()

def congrats():
    print('CONGRATS... YOU WIN NOTHING')

def show_list():
    for i in range(len(todolist)):
        print(str(i+1) + ": " + todolist[i][0] + "  Due: " + todolist[i][1])

def save_data():
    global todolist


    
    myfile = open("todolist.txt", "w")
    s=""
    for item in todolist:
        s = s + '[' + ','.join(item)
    s = s 
    print(s)


def load_data():
    global todolist

    try:
        myfile = open("todolist.txt", "r")
        mytext = myfile.read()
        myfile.close()
        print(mytext)
        firstlist.(mytext.split(";"))
        print(firstlist)
        firstlist.pop()
        todolist= []
        for item in firstlist:
            todolist.append(item.split(","))
        print(firstlist)


    except:
        print("File not read")

            
        
load_data()        
menu()
