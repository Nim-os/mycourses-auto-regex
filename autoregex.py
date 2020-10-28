ans = input("Answer: \t")

antiRegexSquad = ["$","^","*","+","|",".","?","(",")","[","]","{","}"]
spaceIndependent = ["-","/","\"","\'","=","<",">"]



ans = ans.strip()
ans = " ".join(ans.split()) # Remove duped spaces

regexAns = "" # Final regex-ed answer

# Edgy edgecase is edgy
addedSpace = False

for char in ans:
    
    
    # Prevent double space regex in case of 
    if(char == " " and addedSpace):
        continue
    
    add = char
    
    # Character is mistaken REGEX or can have space around it
    if(char in antiRegexSquad):
        if(char == "."): # If it is a period, chances are we don't want to add space around it.
            add = "\\" + char
        else:
            add = "\\" + char + "[\s]*"
            if(not addedSpace):
                add = "[\s]*" + add
            addedSpace = True
    elif(char in spaceIndependent):
        add = char + "[\s]*"
        if(not addedSpace):
                add = "[\s]*" + add
        addedSpace = True
    else:
        addedSpace = False
    
    regexAns += add

# Extra spicy edgecase
if(regexAns[-5:] == "[\s]*"):
    regexAns = regexAns[:-5]

print("\nREGEX Answer: \t", regexAns)
