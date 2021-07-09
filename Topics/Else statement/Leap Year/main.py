# put your python code here
year = int(input())
leap = False
if year % 400 == 0:
    leap = True
else:
    if year % 4 == 0:
        leap = bool(year % 100 != 0)
print("Leap" if leap else "Ordinary")
