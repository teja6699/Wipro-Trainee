"""
counting a in a string
"""
text = "Teja Sai Manikanta"
count = 0
for i, char in enumerate(text):
    if char == 'a' :
        count += 1
print(count)