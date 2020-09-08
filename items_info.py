# The code add items to a list and display it in an array

# adding another line of code working in the receipt branch

# adding a feature for greeting

def greeting():

    greet = "Good day, nice to add you come shopping"

    return greet

def add_item():
    list_of_items = []

    item = " "

    while True :
        item = input("put item into the list")

        list_of_items.append(item)

        response = input("do you want to add more item: yes/no")

        if response == "no":
            break
    print("the is the list of item in the basket : ", list_of_items)

add_items()
greeting()
