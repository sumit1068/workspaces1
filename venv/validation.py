def chkAge(age):
    if age>=23 and age <=40:
        return age
    else:
        raise ValueError("Invalid age")