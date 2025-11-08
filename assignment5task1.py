dictory = {"pradeep":"100","mohan":"100","manoj":"100"}
str = input("enter student marks:")
if str in dictory:
    print(str,"marks are:",dictory[str])
else:
    print("student not found")