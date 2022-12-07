import json
from difflib import get_close_matches
data=json.load(open("data.json"))
def dic():
    word=input("enter your word : ")
    word=word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
       yn = input(f"did you mean {get_close_matches(word,data.keys())[0]} instead ? enter y if yes or n if no : ")
       if yn == "y":
            return data[get_close_matches(word,data.keys())[0]]
       elif yn=="n":
            return "sorry ,i can't find your word"
       else:
            return "i don't understand your entry "
    else:
        return "the word doesn't exist. please double check it"

output=dic()
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
    