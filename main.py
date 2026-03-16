#grocery list program
#add, delete (as we pick), end exit out
grocery_list = []

def view_list():
    if len(grocery_list) == 0:
        print("Sorry, you don't have a list yet.")
    else:
        print("Here is your list: ")
        #for item in grocery_list:
        #    print(item)
        for i in range(len(grocery_list)):
            print(str(i + 1) + "." + grocery_list[i])
        print()

def add_item():
    view_list()
    print("+ Add item to list +")
    get_item_input()

#prompts user for items to add to the list
def get_item_input():
    while True:
        item = input("Enter item (Or enter 'Q' to quit): ")

        if item.upper == "q":
            break

        grocery_list.append(item)

def create_list():
    grocery_list.clear()
    print("+ Create new list +")
    get_item_input()

def shop_list():
    print("+ Shop with list +")

    while len(grocery_list) > 0:
        view_list()

        item = int(input("Enter item you found: "))
        while item < 0 or item > len(grocery_list):
            print("I'm sorry, which item?")
            item = int(input("Enter item you found: "))
        del(grocery_list[item-1])
    print()
    print("The list is empty! Good Job!")
    print()

def main():
    choice = 0
    while choice != 5:
        print("+++ Grocery list Program +++")
        print("1. View Current list")
        print("2. Add item")
        print("3. Create New list")
        print("4. Shop with list")
        print("3. Exit")

        choice = int(input("What would you like to do? : "))
        while choice < 1 or choice > 5:
            print("Sorry, I didn't quite get that.")
            print()
            choice = int(input("What would you like to do again? : "))

        print() #break up console prints
        if choice == 1:
            view_list()
        elif choice == 2:
            add_item()
        elif choice == 3:
            create_list()
        elif choice == 4:
            shop_list()
        else:
            print("Ok, bye!")
        print() #spacing!!!

if __name__ == '__main__':
    main()
