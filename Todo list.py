import sys
import random
import tkinter
Choice=['']
rando=random.randint(1,13)
todolist=[]
root = tkinter.Tk()
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
    root.destroy()

def congrats():
    print('CONGRATS... YOU WIN NOTHING')

def show_list():
    listbox.delete(0,'end')
    load_data()
    print (todolist)
    for i in range(len(todolist)):
        listbox.insert(tkinter.END, str(i+1) + ": " + todolist[i][0] + "  Due: " + todolist[i][1])

def save_data():
    global todolist


    try:
        myfile = open("todolist.txt", "w")
        s=""
        for item in todolist:
            s = s + '' + ','.join(item)+';'
        s = s
        myfile.write(s)
        myfile.close()

    except:
        print("File Not Updated")
    #print(s)


def load_data():
    global todolist

    try:
        myfile = open("todolist.txt", "r")
        mytext = myfile.read()
        myfile.close()
        #print(mytext)
        firstlist=mytext.split(";")
        #print(firstlist)
        firstlist.pop()
        todolist= []
        for item in firstlist:
            todolist.append(item.split(","))
        print(todolist)


    except:
        print("File not read")
myfont= "Arial 20 bold"
title = tkinter.Label(root, text="STOP WATCHING YOUTUBE AND DO THIS NOW!!!", font="Arial 30 bold")            
addbtn = tkinter.Button(root, text="Add", font=myfont, padx=30)
delbtn = tkinter.Button(root, text="Delete", font=myfont, padx=30)
quitbtn = tkinter.Button(root, text="Quit", font=myfont,command=quit,padx=30)
itembox = tkinter.Entry(root, font=myfont, width=55)
datebox = tkinter.Entry(root, font=myfont, width=55)
item = tkinter.Label(root, text= "New Item", font=myfont)
date = tkinter.Label(root, text= "Due Date", font=myfont)
listbox = tkinter.Listbox(root, width=150, height=20)




title.grid(row=0, column =0, columnspan=3)
addbtn.grid(row=2, column=2, rowspan=2, columnspan=2)
delbtn.grid(row=4, column=1)
quitbtn.grid(row=4, column=2)
item.grid(row=2, column=0)
date.grid(row=3, column=0)
itembox.grid(row=2, column=1)
datebox.grid(row=3, column=1)
listbox.grid(row=1, column=0, columnspan=3)
show_list()        
root.mainloop()
