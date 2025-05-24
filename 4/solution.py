#classes
class Road:
    def __init__(self, id, name, start, destination):
        self.id = id
        self.name = name
        self.start = start
        self.destination = destination
class City:
    def __init__(self, id, name):
        self.id = id
        self.name = name
#data
Cities = {}
Roads = {}
#-------------- menu -----------------
#main menu
def menu():
    print("""Main Menu - Select an action:
1. Help
2. Add
3. Delete
4. Show
5. Exit""")
    mainOptions()
def mainOptions():
    choice = int(input())
    if choice == 1:
        Help()
        mainOptions()
    elif choice == 2:
        Add()
        mainOptions()
    elif choice == 3:
        Delete()
        mainOptions()
    elif choice == 4:
        Show()
        mainOptions()
    elif choice == 5:
        exit()
    else:
        print("Invalid input. Please enter 1 for more info.")
        menu()
#help menu
def Help():
    print("Select a number from shown menu and enter. For example 1 is for help.")
    menu()

#add menu
def Add():
    print("""Select model:
1. City
2. Road""")
    choice = int(input())
    if choice == 1:
        add_city()
        menu()
    elif choice == 2:
        add_road()
        menu()
    else:
        print("Invalid input")
        Add()

#   add city
def add_city():
    ct_id = int(input("id:\n"))
    ct_name = input("name:\n")
    Cities[ct_id] = City(ct_id, ct_name)
    print(f"City with id={ct_id} added!")
    ct_sub()
def ct_sub():
    print("""Select your next action
1. Add another City
2. Main Menu""")
    in_choice = int(input())
    if in_choice == 1:
        add_city()
    elif in_choice == 2:
        menu()

#   add road
def add_road():
    rd_id = int(input("id:\n"))
    rd_name = input("name:\n")
    rd_start = int(input("starting:\n"))
    if rd_start not in Cities:
        rd_sub()
    else:
        rd_dest = int(input("destination:\n"))
        if rd_dest not in Cities:
            rd_sub()
        else:
            Roads[rd_id] = Road(rd_id, rd_name, rd_start, rd_dest)
            print(f"Road with id={rd_id} added!")
            rd_success()

def rd_sub():
    print("""There is not any city with this id. Please enter valid id.
Select your next action
1. Add Road
2. Main Menu""")
    in_choice = int(input())
    if in_choice == 1:
        add_road()
    elif in_choice == 2:
        menu()

def rd_success():
    print("""Select your next action
1. Add another Road
2. Main Menu""")
    in_choice = int(input())
    if in_choice == 1:
        add_road()
    elif in_choice == 2:
        menu()

#delete menu
def Delete():
    print("""Select model:
1. City
2. Road""")
    choice = int(input())
    if choice == 1:
        del_ct()
        menu()
    elif choice == 2:
        del_rd()
        menu()
    else:
        print("Invalid input")
        Delete()

#   del city
def del_ct():
    ct_id = int(input("id:\n"))
    if ct_id in Cities:
        del Cities[ct_id]
        print(f"City:{ct_id} deleted!")
    else:
        print(f"City with id {ct_id} not found!")

#   del road
def del_rd():
    rd_id = int(input("id:\n"))
    if rd_id in Roads:
        del Roads[rd_id]
        print(f"Road:{rd_id} deleted!")
        
    else:
        print(f"Road with id {rd_id} not found!")

#show menu
def Show():
    print("""Select model:
1. City
2. Road""")
    choice = int(input())
    if choice == 1:
        for ct in Cities:
            print(f"{Cities[ct].id}\t{Cities[ct].name}")
        menu()
    elif choice == 2:
        for rd in Roads:
            print(f"{Roads[rd].id}\t{Roads[rd].name}\t{Cities[Roads[rd].start].name}\t{Cities[Roads[rd].destination].name}")
        menu()
    else:
        print("Invalid input")
        Show()

menu()
