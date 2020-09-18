ans = input("Answer: ")

ans = ans.strip()
ans = " ".join(ans.split()) # Remove duped spaces

regexAns = "" # Final regex-ed answer

lastChar = ""

for x in ans:
  if(x == "(" or x == ")"):
    cur = "[\s]*\\" + x + "[\s]*"
  else:
    cur = x
  
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
