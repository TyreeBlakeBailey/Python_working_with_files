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