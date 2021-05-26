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


## Second Iterations
def open_using_with_and_print(file):

    try:
        with open("Order.txt", "r") as file:
            for line in file.readlines():
                print(line.rstrip('\n'))

    except FileNotFoundError as errmsg:
        # creating an alias
        print("This file has not been found " + str(errmsg))

    finally:
        return "Thank you for visiting"

print(open_using_with_and_print('Order.txt'))