#>90,"A",>80....
mark=int(input("Please Enter Grade "))
if mark>90:
    grade="A"
elif mark>80:
    grade="B"
elif mark>70:
    grade="C"
elif mark>60:
    grade="D"
else:
    grade="F"

print("your grade is " + grade)