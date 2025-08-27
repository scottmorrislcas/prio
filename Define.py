# Import the modules required
import json
from difflib import get_close_matches

# Loading data from json file
# in python dictionary
data = json.load(open("dictionary.json"))


def translate(w):
    # converts to lower case
    w = w.lower()

    if w in data:
        return data[w]
    # for getting close matches of word
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean % s instead?: " %
                   get_close_matches(w, data.keys())[0])
        yn = yn.lower()
        if yn == "yes":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "no":
            return "The word doesn't exist in my database. Please double check it."
        else:
            return "I didn't understand your entry."
    else:
        return "The word doesn't exist in my datadbase. Please double check it."


# Driver code
word = input("What word?: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
