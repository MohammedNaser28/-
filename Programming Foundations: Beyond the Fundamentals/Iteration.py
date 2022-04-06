Names = [
    "Ahmed",
    "Ali",
    "Youssed",
    "Faten",
    "Malek",
    "Zara",
    "Sara",
    "Shetos",
    "Sama"
] 

for Name in Names:
    print(Name)
print("The list complete Now we will print by while loop \n")








User = True
i = 0
l = 100
while User:
    print(i)
    i+=10
    
    if i == l:
        user = input("Enter true to contniue or false to stop : ")

        if user.capitalize() == "True":
            l += 100
            continue
        else:
            break

print("You outside the while loop.\n")