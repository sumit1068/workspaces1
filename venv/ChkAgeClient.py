import validation as va
age=int(input("Enter age:"))
try:
    result=va.chkAge(age)
    print(result)
except ValueError as e:
    print(e)
