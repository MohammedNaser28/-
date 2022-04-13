# Declartion list
MyFavoriteSubjects = [
    "Math",
    "Arabic",
    "Science",
    "Chemistry",
    "English",
    "History"
]
# Declartion Dectionary
MyShortcut = {
    "tele":"Telegram",
    "wt":"Whatsapp",
    "num":"phone number",
    "chal":"challenge",
    "gol":"Google",
    "face":"FaceBook",
}

# Where you want to search
where = input("Enter Dic if you want to search in Dictionary or list if you want to search in list: ")



size = len(MyFavoriteSubjects)

if where.capitalize() == "Dic":

    short = input("Enter the shortcut do you want to know: ")

    print(MyShortcut[short],"\n")
elif where == "list":
    i = int(input("Enter the number of index you want to know: "))
    if i > size  :
        print("Please Enter number less than", i)
    
    else:
        print(MyFavoriteSubjects[i])
else:
    print("please input valid keyword")