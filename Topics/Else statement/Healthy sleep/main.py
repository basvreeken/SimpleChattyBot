A = int(input())
B = int(input())
H = int(input())

sleep_health = "Normal"

if H < A:
    sleep_health = "Deficiency"
else:
    if H > B:
        sleep_health = "Excess"
print(sleep_health)
