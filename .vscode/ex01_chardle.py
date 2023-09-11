"""EX01 - Chardle - A cute step toward Wordle."""
_author_ = "730661577"
word: str = input("Enter a 5-character word: ")
len_word: int = len(word)
if len_word!=5:
    print("Error: Word must contain 5 characters")
    exit()
character: str = input("Enter a single character: ")
len_char: int = len(character)
if len_char!=1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for e in hello")
num: int = 0
if(word[0]) == character:
    print(character+" found at index 0")
    num+=1
if(word[1]) == character:
    print(character+" found at index 1")
    num+=1
if(word[2]) == character:
    print(character+" found at index 2")
    num+=1
if(word[3]) == character:
    print(character+" found at index 3")
    num+=1
if(word[4]) == character:
    print(character+" found at index 4")
    num+=1
if num==0:
    print("No instances of "+character+" found in "+word)
else:
    if num==1:
        print(str(num)+" instance of "+character+" found in "+word)
    if num>1:
        print(str(num)+" instances of "+character+" found in "+word)