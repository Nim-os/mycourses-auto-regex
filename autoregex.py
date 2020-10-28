ans = input("Answer: ")

antiRegexSquad = ["$","^","*","+","|",".","?","(",")","[","]","{","}"]



ans = ans.strip()
ans = " ".join(ans.split()) # Remove duped spaces

regexAns = "" # Final regex-ed answer

lastChar = ""

for x in ans:
    
    cur = x
    
    # Prevent these characters from being used as REGEX
    if(x in antiRegexSquad):
        if(x == ".")
            cur = "\\" + x
        else:
            cur = "[\s]*\\" + x + "[\s]*"
  
    if(lastChar == " "):
        regexAns += "[\s]*"
        
    lastChar = x
    
    if(lastChar == " "):
        continue
    
    regexAns += cur
  
print("Regex Answer: ", regexAns)

## Issues ##
# -Double [\s]* when whitespace succeeds )
# -Doesn't account for " or ' (Split into groups maybe?)
