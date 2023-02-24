# for loop with range function

total = 0
for number in range (1, 101):
    total += number
print(total)

#Write your code below this row 👇

 # range(start, stop, step)
total = 0
for number in range(2, 101, 2):   # step: Optional. An integer number specifying the incrementation. Default is 1
    total += number
print(total)

# Another way to do it
total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number
print(total2)