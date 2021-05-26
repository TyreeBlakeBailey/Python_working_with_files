# Working with files
## Error and exception handling

## 'try ', ' except' and 'finally' block of codes 
- Can think of them as a if adn else block 
- Finally, works like elif, if and else will alwasy run no matter what  

```python
# name = "Devops"
# year = 2021
# print(name + year)
try:
    file = open("Order.txt")
except FileNotFoundError as errmsg:
    # creating an alias
    print("This file has not been found " + str(errmsg))

finally:
    print("Thank you for visiting")
```


### *open(file, mode)*
- We have already opened a file and we have begun to handle some of the errors that can come from it but there are many more options to be applied to the opening of a file. The key part is adding a mode to the file opening

```bash

| Mode |Description|
| :----: |:---- |
|'r' |This is the default mode. It Opens file for reading. |
|'w' |This Mode Opens file for writing. If file does not exist, it creates a new file. If file exists it truncates the file.|
|'x' |Creates a new file. If file already exists, the operation fails.|
|'a' |Open file in append mode. If file does not exist, it creates a new file.|
|'t' |This is the default mode. It opens in text mode.|
|'b' |This opens in binary mode.
|'+' |This will open a file for reading and writing (updating)|

```

### Error handing menu task
The task below uses the open() file method which allows us to edit external files
```python
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
```