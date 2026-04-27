import re
""" 
txt=input("Enter Text: ")
bpat=input("Enter beg pattern: ")
epat=input("Enter end pattern: ")
if re.search(pattern=bpat, string=txt):
    print("beg pattern available")
else:
    print("beg pat not avilable")
    """

mbno=input("Enter number: ")
pat=r"[0-9]"
if re.search(pattern=pat, string=mbno):
    print("all are numbers")
else:
    print("enter numbers only")


un=input("Enter user name: ")
pat