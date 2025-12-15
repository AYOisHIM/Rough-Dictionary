idoma = idoma_dict = {
    "water": "mme",
    "fire": "onye",
    "sun": "anwu",
    "food": "ocho",
    "house": "ogba",
    "man": "enye",
    "woman": "onyo",
    "child": "omo",
    "tree": "ukpo",
    "road/path": "okpokwu",
    "chair": "ekwu",
    "table": "otoro",
    "clothes": "echo",
    "shoes": "ikolo",
    "book": "akpa",
    "pen": "okpe akpa",
    "plate": "ebe",
    "bed": "odu",
    "light": "enya",
    "cup": "iko",
}

key = input("Welcome to the idoma dictionary, what object would you like to translate to idoma")

if key in idoma_dict:
    print(f"The idoma tranlation for {key} is {idoma_dict[key]}")
else:
    print("Sorry, the object you are trying to translate does not exist")