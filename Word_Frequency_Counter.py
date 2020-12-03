# Count the words longer than 3 characters from a text file
# You may use your own text file while writing the code
# User should be able to change that while running
# Write your code in this cell

def updateDict(word,word_dict):
    if word not in list(word_dict.keys()):
        word_dict[word] = 0
    word_dict[word] += 1
    return word_dict

def wordCounter(word_dict,path, punc = ".!,:/\?#@%&-_+(){}[]`*^$"):
    # Reading Words from a File
    with open(path, "r", encoding = "utf8") as file:
        for line_count, line in enumerate(file):
            for word in line.split(" "):
                word = word.strip(punc) # remove punctions
                word = word.lower() # change all characters to lowercase
                if len(word) > 3:
                    word_dict = updateDict(word,word_dict)
    file.close()
    return word_dict
    
def sortDict(word_dict, desc = False):
    if desc:
        temp = {k:v for k,v in sorted(word_dict.items(),key=lambda i: i[1],reverse=True)}
    else:
        temp = {k:v for k,v in sorted(word_dict.items(),key=lambda i: i[1])}   
    return temp
    


# Change the path of the text file if necesssary
#path = r"C:\Users\vigne\Documents\NTUsem1\AI6120 Python Programming\text.txt"
path = input("Enter full file path, please : ")

# Initiate word dictonary with any common word
word_dict = {'only' : 0}

word_dict = wordCounter(word_dict,path, punc = ".!,:/\?")
word_dict = sortDict(word_dict, desc = True)