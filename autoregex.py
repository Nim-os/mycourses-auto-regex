ans = input("Answer: \t")

antiRegexSquad = ["$","^","*","+","|",".","?","(",")","[","]","{","}"]
spaceIndependent = ["-","/","\"","\'","=","<",">"]



ans = ans.strip()
ans = " ".join(ans.split()) # Remove duped spaces

regexAns = "" # Final regex-ed answer

addSpaceFromRegex = False
addSpaceFromOther = False

for char in ans:    
    
    add = char
    
    # Prevent these characters from being used as REGEX or if they can have space around them
    addSpaceFromRegex = char in antiRegexSquad
    addSpaceFromOther = char in spaceIndependent
    
    if(addSpaceFromRegex):
        if(char == "."): # If it is a period, chances are we don't want to add space around it.
            cur = "\\" + char
        else:
            add = "[\s]*\\" + char
    elif(addSpaceFromOther):
        add = "[\s]*" + char
    
    regexAns += add
  
print("\nRegex Answer: \t", regexAns)

# -Double [\s]* when whitespace succeeds )
