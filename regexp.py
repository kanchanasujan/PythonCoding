import re
text ="clouds are blue"
#text ="clouds are blue Roses are red lights are bright"
pattern = r"blue"
search = re.search(pattern, text)
if search:
    print("Pattern found : ",search.group())
else:
    print("Pattern not found")

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")
    
replace = "red"
new_text = re.sub(pattern, replace, text)
print("Modified text:", new_text)
        
pattern = r" "
split_result = re.split(pattern, text)
print("Split result:", split_result)