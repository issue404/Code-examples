x = 0
y = 0
while True:
    x = input("ENTER THE NUMBER FOR FIZZBUZZ: ")
    try:
        x = int(x)
        if x < 0:
            x = -x
        break
    except:
        print("THE INPUT WASN'T A NUMBER")
for i in range(x):
    y += 1
    if y % 3 == 0 and not y % 5 == 0:
        print(str(y) + ": FIZZ")
    if not y % 3 == 0 and y % 5 == 0:
        print(str(y) + ": BUZZ")
    if not y % 3 == 0 and not y % 5 == 0:
        print(str(y) + ": NONE")
    if y % 3 == 0 and y % 5 == 0:
        print(str(y) + ": FIZZBUZZ")
print("COMPLETED")
x = input("")
