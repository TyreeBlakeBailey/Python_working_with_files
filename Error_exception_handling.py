#
# # name = "Devops"
# # year = 2021
# # print(name + year)
# try:
#     file = open("Order.txt")
# except FileNotFoundError as errmsg:
#     # creating an alias
#     print("This file has not been found " + str(errmsg))
#
# finally:
#     print("Thank you for visiting")
#


# Second Iterations
def open_using_with_and_print(file):
    try:
        with open("Order.txt", "r") as file:  # Will open the file in read only mode
            for line in file.readlines():
                print(line.rstrip('\n'))

    except FileNotFoundError as errmsg:
        # creating an alias
        print("This file has not been found " + str(errmsg))

    finally:
        return "Thank you for visiting"


# Create a function to called open_using_with_and_print write/add/append
# Display the data with the added time - item name - Pizza, cake, Avacado, Biryani, Pasta

def write_to_file(file, text):
    with open(str(file), "w") as file:
        # "w" allows you to only write to the file will delete all contents that is currently on the file
        file.write(str(text))
        file.close()


def add_to_file(file):
    with open(file, "a") as file:
        # "a" will allow you to add or remove items from the file and will create if it doesn't exists
        #file.write(f"\n{str(text)}")
        file.write(f"\nPizza")
        file.write(f"\nCake")
        file.write(f"\nAvocado")
        file.write(f"\nBiryani")
        file.write(f"\nPasta")
        file.close()


while True:
    print("1: Start new file and write text\n2: Append text add set menu\n3: Read file")
    choice = int(input())
    if choice == 1:
        write_to_file("Order.txt", input("Write new items"))
    elif choice == 2:
        add_to_file("Order.txt")
    elif choice == 3:
        open_using_with_and_print("Order.txt")
    else:
        print("Try again")