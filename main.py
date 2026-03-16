#grocery list program
#add, delete (as we pick), end exit out

def create_list():
    pass

def shop_list():
    pass

def main():
    choice = 0
    while choice != 3:
        print("+++ Grocery list Program +++")
        print("1. Create list")
        print("2. Shop with list")
        print("3. Exit")

        choice = int(input("What would you like to do? : "))
        while choice < 1 or choice > 3:
            print("Sorry, I didn't quite get that.")
            print()
            choice = int(input("What would you like to do again? : "))

        print() #break up console prints
        if choice == 1:
            create_list()
        elif choice == 2:
            shop_list()
        else:
            print("Ok, bye!")
        print() #spacing!!!

if __name__ == '__main__':
    main()
